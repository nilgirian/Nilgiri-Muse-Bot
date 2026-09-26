#!/usr/bin/env python3
"""Interactive MUD relay for Nilgiri.

Logs in (SSH + character passwords from env), then relays:
  agent stdin  -> MUD
  MUD stdout   -> agent stdout (passwords redacted, ANSI stripped)

Speech from Sin/Motorola/Russ is flagged with >>> SPEECH lines so the agent
can spot it while polling. Send ">>>QUIT" on stdin to end the relay.

Env: MUD_PASS (ssh password), CHAR_PASS (character password),
     CHAR_NAME (default SinMuseBot)
"""
import os
import pty
import re
import select
import sys

MUD_PASS = os.environ.get("MUD_PASS", "")
CHAR_PASS = os.environ.get("CHAR_PASS", "")
CHAR_NAME = os.environ.get("CHAR_NAME", "SinMuseBot")

ANSI = re.compile(r"\x1b\[[0-9;]*m")
SPEECH = re.compile(
    r"^(Sin|Motorola|Russ)\s+(says|asks|exclaims|tells you|shouts|whispers|murmurs),\s+\"(.*)\"\s*$"
)


def clean(s):
    s = ANSI.sub("", s)
    for secret in (MUD_PASS, CHAR_PASS):
        if secret:
            s = s.replace(secret, "***")
    return s


def emit(msg):
    sys.stdout.write(msg + "\n")
    sys.stdout.flush()


def main():
    for var, val in (("MUD_PASS", MUD_PASS), ("CHAR_PASS", CHAR_PASS)):
        if not val:
            emit(">>> LOGIN FAILED: %s not set" % var)
            return 1

    pid, fd = pty.fork()
    if pid == 0:
        os.execv(
            "/home/hatch/workspace/nilgiri/ssh_via_proxy.sh",
            ["ssh_via_proxy.sh", "player@nilgiri.net"],
        )

    buf = ""
    linebuf = ""
    state = "ssh_pass"
    stdin_buf = ""

    def send(text):
        os.write(fd, (text + "\r").encode())

    # (state, prompt-substring, text-to-send, next-state)
    steps = [
        ("ssh_pass", "password:", MUD_PASS, "color"),
        ("color", "text color", "yes", "name"),
        ("name", "By what name", CHAR_NAME, "charpass"),
        ("charpass", "What is the password", CHAR_PASS, "pressreturn"),
    ]

    emit(">>> RELAY START (login as %s)" % CHAR_NAME)
    while True:
        r, _, _ = select.select([fd, sys.stdin], [], [], 120)
        if fd in r:
            try:
                chunk = os.read(fd, 65536).decode("utf-8", errors="replace")
            except OSError:
                emit(">>> MUD EOF")
                return 0
            if not chunk:
                emit(">>> MUD EOF")
                return 0
            chunk = clean(chunk)
            sys.stdout.write(chunk)
            sys.stdout.flush()
            buf += chunk

            # speech detection, line by line
            linebuf += chunk
            while "\n" in linebuf:
                line, linebuf = linebuf.split("\n", 1)
                m = SPEECH.match(line.strip().strip("\r"))
                if m:
                    emit('>>> SPEECH name=%s verb=%s text=%s' % (m.group(1), m.group(2), m.group(3)))

            if state != "game":
                # advance the login state machine
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
                # keep buffer bounded
                if len(buf) > 20000:
                    buf = buf[-20000:]

        if sys.stdin in r:
            data = os.read(sys.stdin.fileno(), 65536).decode("utf-8", errors="replace")
            if not data:
                emit(">>> STDIN CLOSED")
                return 0
            stdin_buf += data
            while "\n" in stdin_buf:
                line, stdin_buf = stdin_buf.split("\n", 1)
                line = line.rstrip("\r")
                if line == ">>>QUIT":
                    emit(">>> QUIT requested")
                    return 0
                os.write(fd, (line + "\r").encode())


if __name__ == "__main__":
    sys.exit(main())
