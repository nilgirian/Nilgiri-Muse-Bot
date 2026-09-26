#!/usr/bin/env python3
"""Interactive MUD relay for Nilgiri.

Logs in (SSH + character passwords from env), then relays:
  agent stdin  -> MUD
  MUD stdout   -> agent stdout (passwords redacted, ANSI stripped)

Speech from Sin/Motorola/Russ is flagged with >>> SPEECH lines so the agent
can spot it while polling. Send ">>>QUIT" on stdin to end the relay.

Reliability:
  - ssh uses ServerAliveInterval/CountMax (see ssh_via_proxy.sh), so a
    one-way stall makes ssh abort instead of hanging silently.
  - Watchdog: in game, if no MUD output arrives for 75s we probe with "look";
    if still nothing after 150s we kill ssh and reconnect.
  - On EOF the relay automatically re-logs in (the MUD takes the session back
    with "Reconnecting..."). Max 5 reconnect attempts, then it gives up.
  - The ssh session is ALWAYS terminated when the relay exits for any reason
    except reconnect (quit, stdin closed, encamp confirmed): no orphaned
    connections left sitting at the menu.

Env: MUD_PASS (ssh password), CHAR_PASS (character password),
     CHAR_NAME (default SinMuseBot)
"""
import os
import pty
import re
import select
import signal
import sys
import time

MUD_PASS = os.environ.get("MUD_PASS", "")
CHAR_PASS = os.environ.get("CHAR_PASS", "")
CHAR_NAME = os.environ.get("CHAR_NAME", "SinMuseBot")
try:
    SESSION_SECONDS = int(os.environ.get("SESSION_SECONDS", "0") or 0)
except ValueError:
    SESSION_SECONDS = 0

ANSI = re.compile(r"\x1b\[[0-9;]*m")
SPEECH = re.compile(
    r"^(Sin|Motorola|Russ)\s+(says|asks|exclaims|tells you|shouts|whispers|murmurs),\s+\"(.*)\"\s*$"
)
ENCAMPED = re.compile(r"you set up camp", re.IGNORECASE)

LOGIN_TIMEOUT = 120      # give up the login attempt after this long
PROBE_AFTER = 75         # no output for this long -> send "look" probe
STALL_AFTER = 150        # no output for this long -> kill ssh, reconnect
EXIT_TIMEOUT = 15        # give the MUD this long to close after menu option 0
EXIT_MENU_TIMEOUT = 30   # give the MUD this long to show PRESS RETURN / the menu
MAX_RECONNECTS = 5


def clean(s):
    s = ANSI.sub("", s)
    for secret in (MUD_PASS, CHAR_PASS):
        if secret:
            s = s.replace(secret, "***")
    return s


def emit(msg):
    sys.stdout.write(msg + "\n")
    sys.stdout.flush()


class QuitRequested(Exception):
    pass


def terminate_ssh(pid):
    """Make sure the ssh child is dead and reaped. Never raises."""
    for sig in (signal.SIGTERM, signal.SIGKILL):
        try:
            os.kill(pid, sig)
        except OSError:
            break
        time.sleep(1)
        try:
            wpid, _ = os.waitpid(pid, os.WNOHANG)
            if wpid == pid:
                break
        except (OSError, ChildProcessError):
            break
    try:
        os.waitpid(pid, os.WNOHANG)
    except (OSError, ChildProcessError):
        pass


def run_session():
    """Run one login + relay loop. Returns 'eof', 'quit', or 'encamped'."""
    pid, fd = pty.fork()
    if pid == 0:
        os.execv(
            "/home/hatch/workspace/nilgiri/ssh_via_proxy.sh",
            ["ssh_via_proxy.sh", "player@nilgiri.net"],
        )

    ssh_dead = False   # set True once we know the child is gone
    buf = ""
    linebuf = ""
    stdin_buf = ""
    state = "ssh_pass"
    last_read = time.time()
    login_start = time.time()
    exit_start = 0.0
    game_start = None          # wall-clock moment we entered the game
    time_up_announced = False
    probed = False

    def send(text):
        os.write(fd, (text + "\r").encode())

    # (state, prompt-substring, text-to-send, next-state)
    steps = [
        ("ssh_pass", "password:", MUD_PASS, "color"),
        ("color", "text color", "yes", "name"),
        ("name", "By what name", CHAR_NAME, "charpass"),
        ("charpass", "What is the password", CHAR_PASS, "pressreturn"),
    ]

    try:
        while True:
            r, _, _ = select.select([fd, sys.stdin], [], [], 15)
            now = time.time()

            if fd in r:
                try:
                    chunk = os.read(fd, 65536).decode("utf-8", errors="replace")
                except OSError:
                    if state == "exit_wait":
                        emit(">>> EXITED: MUD closed the connection after menu exit")
                        ssh_dead = True
                        return "encamped"
                    emit(">>> MUD EOF")
                    ssh_dead = True
                    return "eof"
                if not chunk:
                    emit(">>> MUD EOF")
                    ssh_dead = True
                    return "eof"
                last_read = now
                probed = False
                chunk = clean(chunk)
                sys.stdout.write(chunk)
                sys.stdout.flush()
                buf += chunk

                linebuf += chunk
                while "\n" in linebuf:
                    line, linebuf = linebuf.split("\n", 1)
                    stripped = line.strip().strip("\r")
                    m = SPEECH.match(stripped)
                    if m:
                        emit('>>> SPEECH name=%s verb=%s text=%s' % (m.group(1), m.group(2), m.group(3)))
                    if ENCAMPED.search(stripped) and state == "game":
                        emit(">>> ENCAMPED: pressing return for the exit menu")
                        state = "encamp_return"
                        exit_start = time.time()
                        # Keep only data after the encamp line: the MUD's
                        # PRESS RETURN prompt typically arrives in the same
                        # chunk, and clearing buf would wipe it.
                        buf = linebuf

                if state != "game":
                    if state not in ("encamp_return", "exit_menu", "exit_wait") and now - login_start > LOGIN_TIMEOUT:
                        emit(">>> LOGIN TIMEOUT")
                        return "eof"
                    if state == "exit_wait":
                        if now - exit_start > EXIT_TIMEOUT:
                            emit(">>> EXIT TIMEOUT: MUD did not close, ssh will be killed")
                            return "encamped"
                    if state in ("encamp_return", "exit_menu"):
                        if now - exit_start > EXIT_MENU_TIMEOUT:
                            emit(">>> EXIT MENU TIMEOUT: no prompt from MUD, ssh will be killed")
                            return "encamped"
                    advanced = True
                    while advanced:
                        advanced = False
                        if state == "encamp_return" and "PRESS RETURN" in buf:
                            send("")
                            state = "exit_menu"
                            # Keep the tail after the matched prompt: the menu
                            # may already have arrived in the same chunk.
                            i = buf.find("PRESS RETURN")
                            buf = buf[i + len("PRESS RETURN"):] if i >= 0 else ""
                            advanced = True
                        elif state == "exit_menu" and "Make your choice:" in buf:
                            send("0")
                            state = "exit_wait"
                            exit_start = time.time()
                            i = buf.find("Make your choice:")
                            buf = buf[i + len("Make your choice:"):] if i >= 0 else ""
                            advanced = True
                        elif state == "pressreturn" and "<>" in buf:
                            state = "game"
                            game_start = time.time()
                            emit(">>> IN GAME (reconnected, skipped menu)")
                            advanced = True
                        elif state == "pressreturn" and "PRESS RETURN" in buf:
                            send("")
                            state = "menu"
                            advanced = True
                        elif state == "menu" and "<>" in buf:
                            state = "game"
                            game_start = time.time()
                            emit(">>> IN GAME")
                            advanced = True
                        elif state == "menu" and "Make your choice:" in buf:
                            send("1")
                            state = "await_game"
                            advanced = True
                        elif state == "await_game" and "<>" in buf:
                            state = "game"
                            game_start = time.time()
                            emit(">>> IN GAME")
                            advanced = True
                        else:
                            for sname, prompt, text, nxt in steps:
                                if state == sname and prompt.lower() in buf.lower():
                                    send(text)
                                    state = nxt
                                    advanced = True
                                    break
                    if len(buf) > 20000:
                        buf = buf[-20000:]

            if sys.stdin in r:
                data = os.read(sys.stdin.fileno(), 65536).decode("utf-8", errors="replace")
                if not data:
                    emit(">>> STDIN CLOSED")
                    raise QuitRequested()
                stdin_buf += data
                while "\n" in stdin_buf:
                    line, stdin_buf = stdin_buf.split("\n", 1)
                    line = line.rstrip("\r")
                    if line == ">>>QUIT":
                        emit(">>> QUIT requested")
                        raise QuitRequested()
                    os.write(fd, (line + "\r").encode())
                    # NOTE: deliberately NOT resetting last_read here. Only bytes
                    # coming back from the MUD prove the connection is alive.

            # session timer: announce the deadline from the relay's own clock,
            # so the agent never has to do clock arithmetic across polls
            if state == "game":
                if (SESSION_SECONDS > 0 and game_start
                        and not time_up_announced
                        and now - game_start >= SESSION_SECONDS):
                    emit(">>> TIME UP: %d seconds in game, say goodbye and encamp"
                         % SESSION_SECONDS)
                    time_up_announced = True
            # watchdog: only meaningful once in game
            if state == "game":
                idle = now - last_read
                if idle > STALL_AFTER:
                    emit(">>> STALL: no MUD output for %ds, killing ssh to reconnect" % int(idle))
                    terminate_ssh(pid)
                    ssh_dead = True
                    return "eof"
                if idle > PROBE_AFTER and not probed:
                    emit(">>> PROBE: no MUD output for %ds, sending look" % int(idle))
                    try:
                        send("look")
                    except OSError:
                        ssh_dead = True
                        return "eof"
                    probed = True
    finally:
        # Never leave an orphaned ssh behind (quit / stdin closed / encamped).
        # On the reconnect path the child is already dead, so this is a no-op.
        if not ssh_dead:
            emit(">>> TERMINATING SSH")
            terminate_ssh(pid)
            emit(">>> SSH TERMINATED")


def main():
    for var, val in (("MUD_PASS", MUD_PASS), ("CHAR_PASS", CHAR_PASS)):
        if not val:
            emit(">>> LOGIN FAILED: %s not set" % var)
            return 1

    emit(">>> RELAY START (login as %s)" % CHAR_NAME)
    if SESSION_SECONDS > 0:
        emit(">>> SESSION LENGTH: %d seconds (timer starts at IN GAME)" % SESSION_SECONDS)
    attempts = 0
    while True:
        try:
            result = run_session()
        except QuitRequested:
            return 0
        if result in ("quit", "encamped"):
            return 0
        # eof -> reconnect
        attempts += 1
        if attempts > MAX_RECONNECTS:
            emit(">>> RECONNECT FAILED after %d attempts, giving up" % MAX_RECONNECTS)
            return 1
        emit(">>> RECONNECTING (attempt %d/%d)" % (attempts, MAX_RECONNECTS))
        time.sleep(3)


if __name__ == "__main__":
    sys.exit(main())
