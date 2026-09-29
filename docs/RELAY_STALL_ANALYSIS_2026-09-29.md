# Relay drop / stall analysis — 2026-09-29

> Written by Nilgiri Muse Bot at Frederick's (nilgirian) request.
> Static, read-only analysis of repo HEAD `209a4a3` ("Document stall layer attribution markers").
> Nothing was run against the MUD, nilgiri.net or the proxy. The repo's code was **NOT modified**;
> the only executed code was an offline localhost re-creation of the tunnel's socket logic in a
> scratch directory (since deleted). Suggested fixes below are **suggestions only** for the owner /
> Muse AI. No secret values appear in this document.
>
> Labels: **VERIFIED** = confirmed by reading the code or by the offline simulation.
> **INFERENCE** = plausible, consistent with the notes, not proven.

## Ranked hypotheses

### 1. `proxy_tunnel.py` leaves a 15s socket timeout on the live tunnel; the download half dies silently

- **Code** (`scripts/proxy_tunnel.py:48`, `:83-91`, `:95`):
  - `socket.create_connection(..., timeout=15)` sets a 15s timeout that is never cleared, so it
    stays on the socket for the whole tunnel.
  - `sock_to_stdout` does a plain `s.recv()`. After 15s with no bytes from the MUD it raises
    `TimeoutError`, and the bare `except Exception: pass` swallows it and the thread exits.
  - `stdin_to_sock` keeps running and `main` blocks in `t1.join()`. The process stays alive, ssh's
    stdin still reaches the game, and nothing ever comes back. ssh sees a healthy pipe.
- **VERIFIED offline.** A localhost re-creation of the same structure: the download thread died
  silently on the first quiet spell longer than the timeout; the upload thread stayed alive and a
  later "look" still reached the server; the banner sent before the quiet spell was delivered.
- **Why it fires often (INFERENCE).** ssh's `ServerAliveInterval=15` only sends its keepalive after
  15s of inbound silence and the reply arrives one round trip later, so the gap between inbound
  bytes on a quiet game is about 15s + RTT, longer than 15.0s. Any quiet game stretch of ~15s kills
  the download half.
- **Evidence in the notes:**
  - NILGIRI_LOGIN incident 2026-09-25: "keystrokes reached the game (others saw the bot's `say`),
    but zero bytes came back for 3+ minutes… relay process stayed healthy (sleeping in select, ssh
    alive)". Exactly the signature of a one-way-dead tunnel.
  - Session 7 (LESSONS_LEARNED): drops at 18:23:16, 18:24:30, 18:25:36 — gaps of 74s and 66s.
    `ServerAliveCountMax` was 3 then, so ssh gives up after 15x(3+1)=60s; add the relay's 3s sleep
    and login time and you get ~68s. Every reconnect worked, meaning logins were fine — each fresh
    connection went deaf shortly after login, which fits this better than a network outage.
  - Session 15: a background probe found the proxy path healthy (0.2-0.4s) right up to the reboot.
  - Fred confirms the game never went down during stalls.
  - Session 17: a corpse was taken by a janitor during a ~5 minute freeze — the character was
    probably still active in game while the driver was blind.
  - Raising `ServerAliveCountMax` 3->10 (commit `a8f5407`, 2026-09-28) did not stop stalls
    (sessions 17, 18b, 19b — about 6 cycles in 19b).
- **Remains INFERENCE:** how often 15s+ quiet gaps occur vs. the observed drop rate. The raw session
  logs are local-only and carry no timestamps.
- **Consequence:** riding through stalls for 150s is pointless when the tunnel is one-way dead; it
  stretches each blind period from ~60s to ~150s. The character keeps acting in game, and driver
  commands sent during a stall are delivered but unseen. The session-18b conclusion that commands
  "vanish into a dead pipe" is probably wrong — they likely executed.

### 2. The reconnect budget is cumulative, so 6 recoverable drops kill the relay (VERIFIED)

- `scripts/mud_relay.py:526-541`: `attempts` is incremented on every EOF and never reset, even after
  a reconnect reaches "IN GAME". The sixth drop of the whole session prints
  "RECONNECT FAILED… giving up", runs cleanup, and leaves the character link-dead.
- The notes call this "5 failed reconnects" (sessions 10, 14, 19b). It is really 5 successful
  reconnects plus one more drop. Session 19b had "~6 stall/reconnect cycles".

### 3. Kill and reconnect hygiene (VERIFIED in code; minor to moderate impact)

- `terminate_ssh` (`mud_relay.py:195`) signals only the ssh pid. The `proxy_tunnel.py` child and its
  TCP socket to the proxy survive (for up to 15s if the tunnel is healthy; in the half-dead case
  only the 15s timeout ends the download thread and the process can linger).
- The relay sleeps only 3s (`:543`) before relogging; the MUD may still see the old connection
  (the "Reconnecting…" takeover path).
- When ssh exits by itself (`ssh_dead=True`, `:279-285`) nothing calls `waitpid`, so a zombie ssh is
  left each time; the pty master `fd` is never `os.close`d, so one fd leaks per reconnect.
- INFERENCE: no handler exists for an "already playing / overwrite? (Y/N)" style prompt, if the MUD
  ever shows one.
- `os.write(fd, ...)` is unguarded at `:326`, `:347`, `:357`, `:369`, `:401`. If ssh dies between
  `select` and the write, `OSError` propagates; `main()` catches only `QuitRequested`, so the relay
  would crash with a traceback and leave the FIFO holder and PID files stale.
- `LOGIN_TIMEOUT` is only checked inside the "data arrived" branch (`:319`), so a silent login never
  times out — the exact mistake NILGIRI_LOGIN already warns about ("timeout checks must run every
  main-loop iteration"). ssh's own timeout is the only backstop.

### 4. Watchdog timing and the new probe

- ssh gives up after 15x(10+1)=165s, not 150s, so the relay's 150s `STALL_AFTER` always fires first.
  "Timeout, server nilgiri.net not responding" should no longer appear; the docs' claim of exact
  alignment is slightly off.
- `diagnose_path()` (`mud_relay.py:130`) blocks the main loop for up to ~20s and runs at PROBE and
  again at STALL; during that time the relay is not reading the pty or the FIFO.
- The probe opens a fresh CONNECT to nilgiri.net:22 and closes without reading the SSH banner. It
  proves only that the proxy can open a TCP connection to the host; it says nothing about data flow
  on the existing tunnel. The extra pre-auth connections also show up in sshd logs and could trip
  rate limits (INFERENCE).
- Killing ssh at 150s does little damage (a false positive costs a relogin). The `look` probe also
  keeps the game's idle timer alive.

### 5. Environment and host (INFERENCE unless noted)

- **VM reboots (documented):** four on 2026-09-28 (10:06, 13:37, 14:21, 16:11 PT, via `who -b`).
  None are recorded since, yet stalls continued — reboots do not explain the stalls.
- **Unconfirmed attribution:** the "silent deaths" of session 4 (21:58:48, ~63 min after launch)
  and session 12 (~01:29, ~70 min in) predate `REBOOTS.log`; calling them reboots is a guess. Both
  fall in a 60-70 min window, which could also be a sandbox lifetime limit.
- **Session 14** (12:44-13:45) contains the 13:37 reboot but its summary blames reconnect
  exhaustion and does not mention a reboot.
- **Proxy:** idle/lifetime limits and MTU/PMTU issues are unknown. ssh keepalives every 15s would
  defeat a plain idle timer.
- **MUD side:** idle characters get "pulled into a void" (session 14); the relay's `look` at 75s
  should defeat that. The MUD has crashed before (bank account lost 2026-09-27).
- **ssh/pty options:** the local pty makes ssh request a remote tty automatically, so `-t` vs `-tt`
  is irrelevant. ControlMaster is not used. DNS is not involved (the proxy resolves the name).

### 6. Connection-setup edge (VERIFIED code; low likelihood)

- `proxy_tunnel.py:56-64` discards any bytes that arrive in the same read as the `\r\n\r\n` ending
  the proxy's 200 response. If the SSH banner is coalesced with it, it is lost and ssh fails with a
  banner-exchange error (a symptom listed in NILGIRI_LOGIN's troubleshooting table).

### 7. Driver-side FIFO hang (VERIFIED by POSIX semantics)

- If the relay dies without cleanup, `sleep 43200 > /tmp/mud_cmd` remains as the only opener. The
  driver's `printf ... > /tmp/mud_cmd` then blocks forever (opening a FIFO for write blocks with no
  reader), which looks like a total seize-up.
- `DRIVER_BRIEF_TEMPLATE.md:23` says the write "blocks until the relay reads it" — not accurate.

## Can the new debug markers discriminate layers?

No. The most likely fault (hypothesis 1) reads as "ssh alive, path alive -> silence is the MUD or
the SSH session", which sends the investigation to the wrong layer.

- No timestamps: `emit()` writes none, so nothing correlates with server logs.
- `os.kill(pid, 0)` succeeds on a zombie ssh (blind spot).
- Nothing inspects the local tunnel process or its threads.
- `diagnose_path` tests a different, fresh connection, not the stalled one.

## What to log next

1. **Tunnel diagnostics** in `proxy_tunnel.py`: timestamped file log of each thread's exit reason and
   exception type, bytes in/out, time of last receive. This alone confirms or kills hypothesis 1.
2. **Live checks at PROBE/STALL:** thread count from `/proc/<proxy pid>/task` (healthy 3, dead
   download half 2); `ss -tin` for the tunnel socket (large Recv-Q on the proxy socket = local
   threads; large Send-Q with retransmits = network); ssh state from `/proc/<pid>/stat` (zombie?).
3. **Timestamps + a 60s `>>> STATS` line:** bytes in/out, `last_read` age, last chunk size (tests
   the "heavy output" idea), reconnect count.
4. **ssh debug log:** run ssh with `-E <file> -vv` so keepalive/rekey timing goes to a file, not the pty.
5. **Better path probe:** non-blocking, and read the SSH banner with a timing.
6. **Gap check on existing logs:** was each recorded stall preceded by 15s+ of quiet game output?

## Suggested fixes (suggestions only — not applied)

1. `proxy_tunnel.py`: call `s.settimeout(None)` after the 200 response; use TCP keepalive on the
   socket instead; keep bytes that follow the header terminator; end the whole process
   (`os._exit`) when either direction ends; log exceptions instead of swallowing them.
2. Reset `attempts` after a session has been in game for a few minutes (or count only consecutive
   failed logins); back off; never give up while budget remains.
3. Kill the process group (`os.killpg`), always `waitpid`, close the pty fd, and confirm the old
   proxy process is gone before relogging.
4. Wrap `os.write(fd, ...)` in `try/except OSError` and treat failure as EOF; add a top-level
   `try/finally` in `main()` that logs the traceback and cleans up.
5. Run the login timeout every loop iteration; handle "already playing / overwrite" prompts.
6. Once the tunnel is fixed, tighten ssh (e.g. `ServerAliveInterval=10`, `CountMax=3`) and probe at
   ~45s / kill at ~90s; riding through 150s rested on a wrong premise.
7. Make driver FIFO writes non-blocking or wrapped in `timeout 5`, and check the relay pid first.
8. Tell drivers that commands sent during a stall probably did execute; verify with `score`,
   `look`, `where`.

## Server-side checks for Frederick

Repo timestamps are coarse, so correlation needs new timestamped logs; still:

- **sshd `auth.log`** for `player` sessions from the egress IP: did the sshd session persist through
  a "stall" until the relay killed ssh, or did the server close it first?
- **Commands during stalls:** did the MUD execute commands issued while the driver saw silence?
  (Supports hypothesis 1.)
- **MUD connect / link-dead / reconnect log** for SinMuseBot around: 2026-09-27 21:58:48 (session 4);
  2026-09-28 18:23:16, 18:24:30, 18:25:36 (session 7); and the session 17, 18b and 19b windows
  (2026-09-28 evening through 2026-09-29 ~00:42-02:18 PT).
- **Probe fingerprints:** the relay's new probes look like bare TCP connects to port 22 with no
  banner exchange, at PROBE (75s) and STALL (150s) times.
- **Server settings:** sshd `ClientAliveInterval`, `MaxStartups`, `RekeyLimit`; whether the
  `player` shell wraps telnet; any MUD idle-disconnect timer.

## Timezone note

Session summaries mix PDT and UTC and disagree on some dates: session 7 is dated 2026-09-27 in its
own file and 2026-09-28 in LESSONS_LEARNED, and session 6 is labelled UTC in one place and PDT in
another. Confirm the timezone before matching times against server logs.
