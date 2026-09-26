#!/usr/bin/env python3
"""Interactive MUD relay for Nilgiri.

Logs in (SSH + character passwords from env), then relays:
  agent stdin  -> MUD
  MUD stdout   -> agent stdout (passwords redacted, ANSI stripped)

Speech from Sin/Motorola/Russ is flagged with >>> SPEECH lines so the agent
can spot it while polling. Send ">>>QUIT" on stdin to end the relay.

Reliability (added 2026-09-25 after a session went deaf: writes reached the
game but zero bytes came back for 3+ minutes while the process stayed alive):
  - ssh uses ServerAliveInterval/CountMax (see ssh_via_proxy.sh), so a
    one-way stall makes ssh abort instead of hanging silently.
  - Watchdog: in game, if no MUD output arrives for 75s we probe with "look";
    if still nothing after 150s we kill ssh and reconnect.
  - On EOF the relay automatically re-logs in (the MUD takes the session back
    with "Reconnecting..."). Max 5 reconnect attempts, then it gives up.

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

ANSI = re.compile(r"\x1b\[[0-9;]*m")
SPEECH = re.compile(
    r"^(Sin|Motorola|Russ)\s+(says|asks|exclaims|tells you|shouts|whispers|murmurs),\s+\"(.*)\"\s*$"
)

LOGIN_TIMEOUT = 120      # give up the login attempt after this long
PROBE_AFTER = 75         # no output for this long -> send "look" probe
STALL_AFTER = 150        # no output for this long -> kill ssh, reconnect
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


def run_session():
    """Run one login + relay loop. Returns 'eof' or 'quit'."""
    pid, fd = pty.fork()
    if pid == 0:
        os.execv(
            "/home/hatch/workspace/nilgiri/ssh_via_proxy.sh",
            ["ssh_via_proxy.sh", "player@nilgiri.net"],
        )

    buf = ""
    linebuf = ""
    stdin_buf = ""
    state = "ssh_pass"
    last_read = time.time()
    login_start = time.time()
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

    while True:
        r, _, _ = select.select([fd, sys.stdin], [], [], 15)
        now = time.time()

        if fd in r:
            try:
                chunk = os.read(fd, 65536).decode("utf-8", errors="replace")
            except OSError:
                emit(">>> MUD EOF")
                return "eof"
            if not chunk:
                emit(">>> MUD EOF")
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
                m = SPEECH.match(line.strip().strip("\r"))
                if m:
                    emit('>>> SPEECH name=%s verb=%s text=%s' % (m.group(1), m.group(2), m.group(3)))

            if state != "game":
                if now - login_start > LOGIN_TIMEOUT:
                    emit(">>> LOGIN TIMEOUT")
                    return "eof"
                advanced = True
                while advanced:
                    advanced = False
                    if state == "pressreturn" and "<>" in buf:
                        state = "game"
                        emit(">>> IN GAME (reconnected, skipped menu)")
                        advanced = True
                    elif state == "pressreturn" and "PRESS RETURN" in buf:
                        send("")
                        state = "menu"
                        advanced = True
                    elif state == "menu" and "<>" in buf:
                        state = "game"
                        emit(">>> IN GAME")
                        advanced = True
                    elif state == "menu" and "Make your choice:" in buf:
                        send("1")
                        state = "await_game"
                        advanced = True
                    elif state == "await_game" and "<>" in buf:
                        state = "game"
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

        # watchdog: only meaningful once in game
        if state == "game":
            idle = now - last_read
            if idle > STALL_AFTER:
                emit(">>> STALL: no MUD output for %ds, killing ssh to reconnect" % int(idle))
                try:
                    os.kill(pid, signal.SIGKILL)
                except OSError:
                    pass
                try:
                    os.waitpid(pid, os.WNOHANG)
                except (OSError, ChildProcessError):
                    pass
                return "eof"
            if idle > PROBE_AFTER and not probed:
                emit(">>> PROBE: no MUD output for %ds, sending look" % int(idle))
                try:
                    send("look")
                except OSError:
                    return "eof"
                probed = True


def main():
    for var, val in (("MUD_PASS", MUD_PASS), ("CHAR_PASS", CHAR_PASS)):
        if not val:
            emit(">>> LOGIN FAILED: %s not set" % var)
            return 1

    emit(">>> RELAY START (login as %s)" % CHAR_NAME)
    attempts = 0
    while True:
        try:
            result = run_session()
        except QuitRequested:
            return 0
        if result == "quit":
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
