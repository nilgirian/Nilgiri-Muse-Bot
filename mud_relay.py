#!/usr/bin/env python3
"""Interactive MUD relay for Nilgiri.

Logs in (SSH + character passwords from env), then relays:
  agent stdin  -> MUD
  MUD stdout   -> agent stdout (passwords redacted, ANSI stripped)

Speech from the bot controllers (Sin, Motorola, Russ, Mandessa) is flagged with >>> SPEECH lines so the agent
can spot it while polling. Unacknowledged SPEECH is re-emitted as >>> SPEECH-PENDING at 15s/30s (cleared by
any outbound speech from the driver) so combat spam can't bury it. A ferocious-rabbit ambush fires
>>> RABBIT-AMBUSH (re-emitted while the fight continues, cleared by outbound `flee`) so the driver's
only legal command while marked is `flee`. Entry into an off-limits zone fires >>> ZONE-VIOLATION
(re-emitted while the bot stays, cleared on approved ground) so the driver's only legal command while
marked is a move that exits the zone. Send ">>>QUIT" on stdin to end the relay.

Reliability:
  - ssh uses ServerAliveInterval/CountMax (see ssh_via_proxy.sh), so a
    one-way stall makes ssh abort instead of hanging silently.
  - Watchdog: in game, if no MUD output arrives for 75s we probe with "look";
    if still nothing after 150s we kill ssh and reconnect.
  - On EOF the relay automatically re-logs in (the MUD takes the session back
    with "Reconnecting..."). Max 5 reconnect attempts, then it gives up.
  - The ssh session is ALWAYS terminated when the relay exits for any reason
    except reconnect (quit, encamp confirmed): no orphaned connections left
    sitting at the menu.
  - If the driver's stdin pipe closes, the relay does NOT quit: it detaches
    (stops watching stdin) and keeps the session alive. At TIME UP it
    auto-retires with encamp plus the normal menu walk, so the character is
    stored safely even with no driver. Send ">>>QUIT" on stdin to end the
    relay deliberately; a bare stdin EOF never quits.

Env: MUD_PASS (ssh password), CHAR_PASS (character password),
     CHAR_NAME (default SinMuseBot)
"""
import base64
import os
import pty
import re
import select
import signal
import socket
import stat
import sys
import time
from urllib.parse import urlparse

MUD_PASS = os.environ.get("MUD_PASS", "")
CHAR_PASS = os.environ.get("CHAR_PASS", "")
CHAR_NAME = os.environ.get("CHAR_NAME", "SinMuseBot")
try:
    SESSION_SECONDS = int(os.environ.get("SESSION_SECONDS", "0") or 0)
except ValueError:
    SESSION_SECONDS = 0

ANSI = re.compile(r"\x1b\[[0-9;]*m")
# Bot controllers, hardcoded by design. Sin is the Implementor and the
# ultimate authority over every bot; Motorola, Russ, and Mandessa are
# the authorized immortals whose orders a bot also obeys. Other
# immortals and players cannot order bots around. Forks: edit this
# list deliberately.
SPEECH = re.compile(
    r"^(Sin|Motorola|Russ|Mandessa)\s+(says|asks|exclaims|tells you|shouts|whispers|murmurs|gossips|yells),\s+\"(.*)\"\s*$"
)
ENCAMPED = re.compile(r"you set up camp", re.IGNORECASE)
KLICKED = re.compile(r"you klick your heals", re.IGNORECASE)
# Ferocious-rabbit ambush detector (mechanical reflex; the prose RABBIT REFLEX
# rule was understood but never complied with, sessions 39-41). While any
# un-cleared marker exists, the driver's ONLY legal command is `flee`. The
# marker clears when the driver sends `flee`, or silently 180s after the last
# rabbit line (the rabbit wandered off). No deliberate-fight false positives:
# the rabbit is never fair game, so any rabbit combat line is an ambush.
RABBIT_ARRIVAL = re.compile(r"ferocious rabbit (is here|hops in from)", re.I)
RABBIT_COMBAT = re.compile(r"ferocious rabbit (bites|bite|gnashes|deftly|is in|has )", re.I)
RABBIT_NAG_EVERY = 10    # re-emit (still fighting) at most this often
RABBIT_TIMEOUT = 180     # clear silently after this long with no rabbit line
# Zone-violation guard (mechanical; Fred 2026-10-09, session 61 death).
# The brief marked Sleeping Forest D/E off-limits but the driver walked in
# through a dark exit anyway (third wording-based compliance miss: session
# 58 rabbit-flee, session 60 D-section, session 61 fatal D-section). While
# any un-cleared marker exists, the driver's ONLY legal command is a move
# that exits the zone. Fires on `where` zone output or room titles matching
# the off-limits list; re-emits while the bot stays; clears on approved
# ground. A controller's direct in-session order (e.g. a corpse run)
# overrides the guard — the marker still fires as information.
WHERE_ZONE = re.compile(r"the depths of (.+?) created by", re.I)
OFFLIMIT_ZONES = re.compile(r"heavy jungle|haon-dor.*dark|storm drain", re.I)
OFFLIMIT_ROOMS = re.compile(r"^the heavy forest( \(|$)", re.I)
ZONE_NAG_EVERY = 15      # re-emit (still in violation) at most this often
ZONE_TIMEOUT = 300       # clear silently after this long with no zone line

LOGIN_TIMEOUT = 120      # give up the login attempt after this long
PROBE_AFTER = 75         # no output for this long -> send "look" probe
STALL_AFTER = 150        # no output for this long -> kill ssh, reconnect
EXIT_TIMEOUT = 15        # give the MUD this long to close after menu option 0
EXIT_MENU_TIMEOUT = 30   # give the MUD this long to show PRESS RETURN / the menu
MAX_RECONNECTS = 5

_HERE = os.path.dirname(os.path.abspath(__file__))
# Repo layout: scripts/mud_relay.py with run/ at the repo root.
# Flattened layout: mud_relay.py at the repo root with run/ alongside.
REPO_ROOT = (os.path.dirname(_HERE) if os.path.basename(_HERE) == "scripts"
             else _HERE)
RUN_DIR = os.path.join(REPO_ROOT, "run")
HEARTBEAT_FILE = os.path.join(RUN_DIR, "heartbeat")
HOLDER_PID_FILE = os.path.join(RUN_DIR, "fifo_holder.pid")
RELAY_PID_FILE = os.path.join(RUN_DIR, "relay.pid")
FIFO_PATH = "/tmp/mud_cmd"
HEARTBEAT_EVERY = 60  # seconds between heartbeat writes


def cleanup_runtime():
    """Kill the FIFO holder and remove the FIFO on final exit.

    The launcher exits right after spawning the relay, so the holder
    (sleep 43200 > /tmp/mud_cmd) would otherwise survive a clean
    menu-0 exit and leave a stale FIFO behind. Never called on the
    reconnect path — the same FIFO stays open across reconnects.
    """
    try:
        with open(HOLDER_PID_FILE) as f:
            os.kill(int(f.read().strip()), 15)
    except (OSError, ValueError):
        pass
    try:
        if stat.S_ISFIFO(os.stat(FIFO_PATH).st_mode):
            os.unlink(FIFO_PATH)
    except OSError:
        pass
    for pf in (HOLDER_PID_FILE, RELAY_PID_FILE):
        try:
            os.unlink(pf)
        except OSError:
            pass
    emit(">>> RUNTIME CLEANED: holder killed, FIFO and PID files removed")


def write_heartbeat():
    """Prove the relay process is alive, independent of MUD health.

    A stale heartbeat (older than ~2x HEARTBEAT_EVERY) means the relay
    process itself is gone — killed from outside, since every in-code
    exit path logs a >>> marker first. Never raises.
    """
    try:
        with open(HEARTBEAT_FILE, "w") as f:
            f.write("%d %d\n" % (int(time.time()), os.getpid()))
    except OSError:
        pass


def clean(s):
    s = ANSI.sub("", s)
    for secret in (MUD_PASS, CHAR_PASS):
        if secret:
            s = s.replace(secret, "***")
    return s


# The MUD's game prompt, e.g. "<54h 106m 106v>" or "<54h 106m 106v fighting>".
# This is the definitive "we are in the game" signal: unlike the login
# banners/menus, it appears on every login path, including linkdead
# reconnects where the MUD skips straight to the prompt.
GAME_PROMPT_RE = re.compile(r"<\d+h \d+m \d+v[ >]")


def diagnose_path(timeout=10):
    """Independently check whether the VM -> proxy -> nilgiri.net path is alive.

    Opens a fresh TCP connection through the configured HTTP CONNECT proxy
    and requests a tunnel to nilgiri.net:22 — the same path ssh uses, but a
    separate connection, so it tells us whether a MUD silence is the
    transport or the game. Returns (ok, detail). Never logs credentials:
    only the proxy host:port and the outcome are reported. Never raises.
    """
    try:
        proxy_url = None
        for k in ("ALL_PROXY", "all_proxy", "HTTPS_PROXY", "https_proxy",
                  "HTTP_PROXY", "http_proxy"):
            v = os.environ.get(k)
            if v:
                proxy_url = v
                break
        if not proxy_url:
            return False, "no proxy env configured"
        p = urlparse(proxy_url)
        host, port = p.hostname, p.port or 8080
        if not host:
            return False, "proxy URL has no host"
        t0 = time.time()
        s = socket.create_connection((host, port), timeout=timeout)
        try:
            req = "CONNECT nilgiri.net:22 HTTP/1.1\r\nHost: nilgiri.net:22\r\n"
            if p.username:
                token = base64.b64encode(
                    ("%s:%s" % (p.username, p.password or "")).encode()
                ).decode()
                req += "Proxy-Authorization: Basic %s\r\n" % token
            req += "\r\n"
            s.settimeout(timeout)
            s.sendall(req.encode())
            resp = b""
            while b"\r\n\r\n" not in resp:
                chunk = s.recv(4096)
                if not chunk:
                    break
                resp += chunk
                if len(resp) > 8192:
                    break
        finally:
            s.close()
        dt = time.time() - t0
        status = resp.split(b"\r\n", 1)[0].decode(errors="replace") if resp else "<empty>"
        if " 200 " in status:
            return True, "proxy %s:%d CONNECT nilgiri.net:22 -> 200 in %.1fs" % (
                host, port, dt)
        return False, "proxy %s:%d CONNECT -> %s" % (host, port, status[:80])
    except Exception as e:
        return False, "path check failed: %s: %s" % (
            type(e).__name__, str(e)[:100])


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
    time_left_marks = set()    # countdown checkpoints already emitted
    probed = False
    pending_speech = []      # unacknowledged controller SPEECH: [ts, name,
                             # verb, text, stage]; the relay re-emits
                             # reminders until the driver answers with
                             # outbound speech (see SPEECH_NAG below)
    rabbit_nag = []          # ferocious-rabbit ambush marker: [[last_seen_ts,
                             # last_emit_ts]]; while non-empty the driver's
                             # only legal command is `flee` (see RABBIT_*)
    zone_nag = []            # zone-violation marker: [[last_seen_ts,
                             # last_emit_ts, zone_desc]]; while non-empty the
                             # driver's only legal command is a move that
                             # exits the zone (see WHERE_ZONE/OFFLIMIT_*)
    stdin_open = True          # driver command pipe; EOF detaches, never quits
    retire_start = 0.0         # detached auto-retire: when the encamp attempt began
    retire_stage = 0           # detached auto-retire: 0 encamp sent, 1 fled, 2 retried
    last_heartbeat = 0.0       # relay-process heartbeat (see write_heartbeat)

    def send(text):
        os.write(fd, (text + "\r").encode())

    def ssh_child_alive():
        """Is the ssh child process still there? Never raises."""
        try:
            os.kill(pid, 0)
            return True
        except OSError:
            return False

    # (state, prompt-substring, text-to-send, next-state)
    steps = [
        ("ssh_pass", "password:", MUD_PASS, "color"),
        ("color", "text color", "yes", "name"),
        ("name", "By what name", CHAR_NAME, "charpass"),
        ("charpass", "What is the password", CHAR_PASS, "pressreturn"),
    ]

    try:
        while True:
            r, _, _ = select.select([fd] + ([sys.stdin] if stdin_open else []),
                                    [], [], 15)
            now = time.time()

            # Heartbeat every minute: proves the relay process is alive even
            # when the MUD is silent. Checked by the driver each poll.
            if now - last_heartbeat >= HEARTBEAT_EVERY:
                write_heartbeat()
                last_heartbeat = now

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
                        # Nag list: if the driver never answers with outbound
                        # speech, reminders re-emit this below so combat spam
                        # can't bury it (session 20: Sin's "how you doing?"
                        # gossip went unanswered mid-fight).
                        pending_speech.append([now, m.group(1), m.group(2),
                                               m.group(3), 0])
                    # Rabbit ambush: arrival or combat lines (re)mark the
                    # ambush. Fires on arrival, refreshes on combat, and
                    # re-marks if a flee failed (marker cleared but the
                    # rabbit is still biting).
                    if (RABBIT_ARRIVAL.search(stripped)
                            or RABBIT_COMBAT.search(stripped)):
                        if not rabbit_nag:
                            emit(">>> RABBIT-AMBUSH: ferocious rabbit present - "
                                 "next command must be flee")
                            rabbit_nag.append([now, now])
                        else:
                            rabbit_nag[0][0] = now
                    # Zone-violation guard. Fires on `where` zone output or
                    # room titles matching the off-limits list. Re-marks
                    # while the bot stays; clears on approved ground or
                    # silently after ZONE_TIMEOUT.
                    zm = WHERE_ZONE.search(stripped)
                    if zm and OFFLIMIT_ZONES.search(zm.group(1)):
                        zone_desc = zm.group(1).strip()
                        if not zone_nag:
                            emit(">>> ZONE-VIOLATION: off-limits zone "
                                 f"({zone_desc}) - next command must be a "
                                 "move that exits the zone")
                            zone_nag.append([now, now, zone_desc])
                        else:
                            zone_nag[0][0] = now
                            zone_nag[0][2] = zone_desc
                    elif OFFLIMIT_ROOMS.search(stripped):
                        zone_desc = "Sleeping Forest D-section (heavy forest)"
                        if not zone_nag:
                            emit(">>> ZONE-VIOLATION: off-limits zone "
                                 f"({zone_desc}) - next command must be a "
                                 "move that exits the zone")
                            zone_nag.append([now, now, zone_desc])
                        else:
                            zone_nag[0][0] = now
                    elif zm and not OFFLIMIT_ZONES.search(zm.group(1)):
                        # Approved zone seen via `where` — clear the marker.
                        if zone_nag:
                            emit(">>> ZONE-CLEAR: back on approved ground")
                        zone_nag.clear()
                    if ENCAMPED.search(stripped) and state == "game":
                        emit(">>> ENCAMPED: pressing return for the exit menu")
                        state = "encamp_return"
                        exit_start = time.time()
                        # Keep only data after the encamp line: the MUD's
                        # PRESS RETURN prompt typically arrives in the same
                        # chunk, and clearing buf would wipe it.
                        buf = linebuf
                    if KLICKED.search(stripped) and state == "game":
                        # Rent-room exit (Fred's rule: klick, not encamp, in
                        # rent). The MUD's PRESS RETURN prompt and exit menu
                        # follow exactly as after encamp, so the same
                        # automatic exit flow applies.
                        emit(">>> KLICKED: pressing return for the exit menu")
                        state = "encamp_return"
                        exit_start = time.time()
                        buf = linebuf

                if state != "game":
                    if state not in ("encamp_return", "exit_menu", "exit_wait") and now - login_start > LOGIN_TIMEOUT:
                        emit(">>> LOGIN TIMEOUT")
                        return "eof"
                    # Global fallback: if the MUD is showing the game prompt,
                    # we are in the game regardless of which login path got us
                    # here. The banner/menu state machine misses linkdead
                    # reconnects where the MUD skips straight to the prompt,
                    # which used to LOGIN TIMEOUT-loop until the relay gave up
                    # (session 23, 2026-09-30: 13 drops, 5-fail give-up).
                    if state not in ("encamp_return", "exit_menu", "exit_wait") and GAME_PROMPT_RE.search(buf):
                        state = "game"
                        if game_start is None:
                            game_start = time.time()
                        emit(">>> IN GAME (game prompt detected)")
                        buf = ""
                    else:
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
                                if game_start is None:
                                    game_start = time.time()
                                emit(">>> IN GAME (reconnected, skipped menu)")
                                advanced = True
                            elif state == "pressreturn" and "PRESS RETURN" in buf:
                                send("")
                                state = "menu"
                                advanced = True
                            elif state == "menu" and "<>" in buf:
                                state = "game"
                                if game_start is None:
                                    game_start = time.time()
                                emit(">>> IN GAME")
                                advanced = True
                            elif state == "menu" and "Make your choice:" in buf:
                                send("1")
                                state = "await_game"
                                advanced = True
                            elif state == "await_game" and ("<>" in buf or "Welcome to the land of Nilgiri" in buf):
                                # "<>" is legacy (old relay versions echoed it);
                                # the banner is the live signal the MUD prints on
                                # entering the game. Without this, IN GAME never
                                # fires and LOGIN TIMEOUT kills the session in a
                                # reconnect loop (session 23, 2026-09-30).
                                state = "game"
                                if game_start is None:
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

            if stdin_open and sys.stdin in r:
                data = os.read(sys.stdin.fileno(), 65536).decode("utf-8", errors="replace")
                if not data:
                    # The command pipe closed. This is NOT a quit request: the
                    # driver may be gone, but the MUD session is healthy, so
                    # detach and keep it alive. select() would report EOF
                    # forever, so stop watching stdin entirely. At TIME UP the
                    # detached auto-retire below stores the character safely.
                    emit(">>> STDIN DETACHED: command pipe closed, continuing "
                         "unattended; will auto-encamp at TIME UP")
                    stdin_open = False
                else:
                    stdin_buf += data
                    while "\n" in stdin_buf:
                        line, stdin_buf = stdin_buf.split("\n", 1)
                        line = line.rstrip("\r")
                        if line == ">>>QUIT":
                            emit(">>> QUIT requested")
                            raise QuitRequested()
                        # The MUD only accepts US ASCII keyboard characters.
                        # Strip anything else rather than sending bytes it
                        # can't handle.
                        ascii_line = line.encode("ascii", "ignore").decode("ascii")
                        if ascii_line != line:
                            emit(">>> NON-ASCII STRIPPED from outbound line")
                        os.write(fd, (ascii_line + "\r").encode())
                        # NOTE: deliberately NOT resetting last_read here. Only bytes
                        # coming back from the MUD prove the connection is alive.
                        # Any outbound speech counts as acknowledging pending
                        # controller SPEECH: the driver is alive and reading.
                        first = ascii_line.strip().split(" ", 1)[0].lower() if ascii_line.strip() else ""
                        if first in ("say", "gossip", "tell", "yell",
                                     "shout", "whisper", "murmur", "ask",
                                     "exclaim"):
                            pending_speech.clear()
                        # Outbound flee clears the rabbit-ambush marker: the
                        # reflex fired. If the flee PANIC-fails, the next
                        # rabbit combat line re-marks (see RABBIT_* above).
                        if first == "flee" and rabbit_nag:
                            rabbit_nag.clear()
                            emit(">>> RABBIT-FLED: ambush marker cleared")

            # session timer: announce the deadline from the relay's own clock,
            # so the agent never has to do clock arithmetic across polls
            if state == "game":
                if SESSION_SECONDS > 0 and game_start:
                    elapsed = now - game_start
                    # Countdown checkpoints: keep the driver off its own
                    # time estimates. Skipped for sessions shorter than the mark.
                    for mark_min in (15, 10, 5):
                        if (mark_min not in time_left_marks
                                and SESSION_SECONDS > mark_min * 60
                                and elapsed >= SESSION_SECONDS - mark_min * 60):
                            emit(">>> TIME LEFT: %d minutes — do NOT retire "
                                 "before >>> TIME UP" % mark_min)
                            time_left_marks.add(mark_min)
                    if (not time_up_announced
                            and elapsed >= SESSION_SECONDS):
                        emit(">>> TIME UP: %d seconds in game, say goodbye and encamp"
                             % SESSION_SECONDS)
                        time_up_announced = True
            # speech nag: re-emit unacknowledged controller SPEECH so
            # combat spam can't bury it. Reminders at 15s/30s, then give up
            # with UNANSWERED at 60s (three nudges is enough; more is spam).
            for entry in pending_speech[:]:
                ts, name, verb, text, stage = entry
                age = now - ts
                if age >= 60 and stage < 3:
                    emit(">>> SPEECH-UNANSWERED (60s): %s %s: %s"
                         % (name, verb, text))
                    pending_speech.remove(entry)
                elif age >= 30 and stage < 2:
                    emit(">>> SPEECH-PENDING (30s unanswered): %s %s: %s"
                         % (name, verb, text))
                    entry[4] = 2
                elif age >= 15 and stage < 1:
                    emit(">>> SPEECH-PENDING (15s unanswered): %s %s: %s"
                         % (name, verb, text))
                    entry[4] = 1
            # rabbit nag: while a ferocious-rabbit ambush marker is active,
            # re-emit it so combat spam can't bury it. Clears when the
            # driver sends `flee`, or silently after RABBIT_TIMEOUT with no
            # rabbit line (the rabbit wandered off).
            if rabbit_nag:
                last_seen, last_emit = rabbit_nag[0]
                if now - last_seen >= RABBIT_TIMEOUT:
                    rabbit_nag.clear()
                elif now - last_emit >= RABBIT_NAG_EVERY:
                    emit(">>> RABBIT-AMBUSH (still fighting): flee now")
                    rabbit_nag[0][1] = now
            # Zone-violation re-emit: keep the marker visible while the bot
            # stays in the off-limits zone. Clears silently after
            # ZONE_TIMEOUT with no zone line.
            if zone_nag:
                last_seen, last_emit, zone_desc = zone_nag[0]
                if now - last_seen >= ZONE_TIMEOUT:
                    zone_nag.clear()
                elif now - last_emit >= ZONE_NAG_EVERY:
                    emit(">>> ZONE-VIOLATION (still in off-limits zone): "
                         "move out now")
                    zone_nag[0][1] = now
            # detached auto-retire: the driver is gone, so nobody will walk
            # to rent and klick. Encamp in place when the budget expires and
            # let the normal exit-menu flow store the character. Nudge with
            # flee + a second encamp if the MUD doesn't confirm (e.g. was
            # fighting); give up to link-dead only as a last resort.
            if (not stdin_open and SESSION_SECONDS > 0 and time_up_announced
                    and retire_start == 0.0 and state == "game"):
                emit(">>> DETACHED: budget expired with no driver; auto-encamping")
                try:
                    send("encamp")
                except OSError:
                    pass
                retire_start = now
                retire_stage = 0
            if not stdin_open and retire_start > 0.0 and state == "game":
                wait = now - retire_start
                if wait > 75:
                    emit(">>> DETACHED AUTO-RETIRE FAILED: giving up, "
                         "character will be link-dead")
                    return "encamped"
                elif wait > 40 and retire_stage == 1:
                    emit(">>> DETACHED: retrying encamp")
                    try:
                        send("encamp")
                    except OSError:
                        pass
                    retire_stage = 2
                elif wait > 25 and retire_stage == 0:
                    emit(">>> DETACHED: encamp unconfirmed, fleeing first")
                    try:
                        send("flee")
                    except OSError:
                        pass
                    retire_stage = 1
            # watchdog: only meaningful once in game
            if state == "game":
                idle = now - last_read
                if idle > STALL_AFTER:
                    # Layer attribution before killing anything: is the ssh
                    # child dead, is the transport dead, or is it the MUD?
                    path_ok, path_detail = diagnose_path()
                    ssh_ok = ssh_child_alive()
                    if not ssh_ok:
                        why = "SSH PROCESS DEAD"
                    elif path_ok:
                        why = ("PATH ALIVE (%s) — silence is the MUD or the "
                               "SSH session" % path_detail)
                    else:
                        why = "TRANSPORT FAILURE (%s)" % path_detail
                    emit(">>> STALL: no MUD output for %ds; %s; killing ssh "
                         "to reconnect" % (int(idle), why))
                    terminate_ssh(pid)
                    ssh_dead = True
                    return "eof"
                if idle > PROBE_AFTER and not probed:
                    # Early layer attribution (~75s before the stall kill),
                    # so the log shows which layer went quiet first.
                    path_ok, path_detail = diagnose_path()
                    ssh_ok = ssh_child_alive()
                    if not ssh_ok:
                        emit(">>> PROBE: no MUD output for %ds; SSH PROCESS "
                             "DEAD already" % int(idle))
                    elif path_ok:
                        emit(">>> PROBE: no MUD output for %ds; path alive "
                             "(%s) — probing MUD with look"
                             % (int(idle), path_detail))
                    else:
                        emit(">>> PROBE: no MUD output for %ds; TRANSPORT "
                             "FAILURE (%s) — probing anyway"
                             % (int(idle), path_detail))
                    try:
                        send("look")
                    except OSError:
                        ssh_dead = True
                        return "eof"
                    probed = True
            # exit-menu timeouts: run every loop iteration, not just when
            # data arrives, because the MUD is silent while waiting for us
            if state == "exit_wait":
                if now - exit_start > EXIT_TIMEOUT:
                    emit(">>> EXIT TIMEOUT: MUD did not close, ssh will be killed")
                    return "encamped"
            if state in ("encamp_return", "exit_menu"):
                if now - exit_start > EXIT_MENU_TIMEOUT:
                    emit(">>> EXIT MENU TIMEOUT: no prompt from MUD, ssh will be killed")
                    return "encamped"
    finally:
        # Never leave an orphaned ssh behind (quit / detached give-up /
        # encamped). On the reconnect path the child is already dead, so this
        # is a no-op.
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
    emit(">>> RELAY PID %d, PGID %d, SID %d"
         % (os.getpid(), os.getpgrp(), os.getsid(0)))
    try:
        os.makedirs(os.path.dirname(HEARTBEAT_FILE), exist_ok=True)
    except OSError:
        pass
    write_heartbeat()
    if SESSION_SECONDS > 0:
        emit(">>> SESSION LENGTH: %d seconds (timer starts at IN GAME)" % SESSION_SECONDS)
    attempts = 0
    last_drop = 0.0
    while True:
        try:
            result = run_session()
        except QuitRequested:
            cleanup_runtime()
            return 0
        if result in ("quit", "encamped"):
            cleanup_runtime()
            return 0
        # eof -> reconnect. The budget counts *consecutive* failures: drops
        # spaced far apart are fresh incidents on a flaky network, not a
        # cascade, so a drop more than 5 minutes after the previous one
        # restarts the budget. (Before this, 6 recoverable drops in one
        # session exhausted the budget and left the character link-dead —
        # session 19b, 2026-09-29.) A genuine hard-down still accumulates:
        # failed logins return in ~2 min, well inside the window.
        now = time.time()
        if now - last_drop > 300:
            attempts = 0
        last_drop = now
        attempts += 1
        if attempts > MAX_RECONNECTS:
            emit(">>> RECONNECT FAILED after %d consecutive attempts, giving up"
                 % MAX_RECONNECTS)
            cleanup_runtime()
            return 1
        emit(">>> RECONNECTING (attempt %d/%d)" % (attempts, MAX_RECONNECTS))
        time.sleep(3)


if __name__ == "__main__":
    sys.exit(main())
