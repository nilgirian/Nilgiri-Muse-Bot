# Operator Runbook — running a Nilgiri session

You are the **operator** (see `NILGIRI_LOGIN.md` §23 for the
operator/driver/relay architecture). This is the full session lifecycle,
start to finish. The playbook (`NILGIRI_LOGIN.md`) is the authority on
game mechanics; this file is the procedure for running the operation.

## Before the session

1. **Get the three things every session needs:** character name, that
   character's password, and a defined time period. Never log in
   indefinitely; if the human doesn't give a duration, ask.
2. **Passwords are transient.** The human supplies the character password
   in chat for this session only. Use it once from an environment
   variable. Never write it to disk, chat logs, memory files, or the
   repo. (If it was already supplied in the current conversation, reuse
   it without asking again — unless it doesn't work.)
3. **Announce the plan** before anything observable in-game: what the
   character will do, how long, how many logins. The human may be
   watching from their own character.

## Launch

4. Launch the relay **detached** (own session, survives the launching
   shell):

   ```bash
   cd [NILGIRI DIR]
   SESSION_SECONDS=[BUDGET] MUD_PASS='[ssh password]' CHAR_PASS='[char password]' \
     ./scripts/launch_relay.sh logs/session-$(date +%Y%m%d-%H%M%S).log
   ```

   Passwords travel in the environment (inherited by the detached child),
   never on a command line. `CHAR_NAME` defaults to `SinMuseBot`.
5. **Verify `IN GAME`** before doing anything else:
   `grep -a "IN GAME" [LOG]` — the session timer starts there. If the
   character was link-dead, the MUD reports
   `>>> IN GAME (reconnected, skipped menu)`.

## Drive

6. Copy `DRIVER_BRIEF_TEMPLATE.md`, fill in the bracketed sections for
   this session's mission, and save the filled brief next to the session
   log as `logs/brief-YYYYMMDD-HHMMSS.md` (local-only, never committed).
   Then spawn the driver subagent with the brief. The driver inherits
   your full context, so keep the brief to the mission + the standing
   rules it needs.
7. **Stay responsive.** The driver plays; you talk to the human, watch
   for problems, and handle anything the driver can't (it has no
   passwords and must never restart the relay).

## Monitor — what can go wrong

8. **Heartbeat.** The relay touches `[NILGIRI DIR]/run/heartbeat` every
   60s. Older than ~2 min = the relay process is gone.
9. **Silent death → check `who -b` FIRST.** The VM can reboot
   spontaneously, killing relay, holder, SSH, and driver instantly with
   zero log markers. If the boot time is newer than the session start:
   note the reboot (local `REBOOTS.log`), clean up `/tmp/mud_cmd`
   (`/tmp` is wiped by reboots — always `test -p` the FIFO before
   sending commands), and relaunch with the **remaining** budget to
   resume the mission. Do not start the clock over.
10. **Network stalls.** `Timeout, server nilgiri.net not responding.` is
    OpenSSH aborting after its keepalives go unanswered (now 150s —
    `ServerAliveCountMax=10` in `scripts/ssh_via_proxy.sh`). The MUD is
    not down; the relay reconnects automatically. After a reconnect,
    the driver re-verifies state (`score`, `look`, `where`).
11. **Human override.** If the human gives the character a direct
    in-game order that contradicts the brief, the brief loses. Tell the
    driver this in every brief (it's in the template).

## Retire

12. Normal retirement (driver does this at `TIME UP`, or you do it
    directly): bank carried gold → walk to the rent room → `rent` →
    `klick` in the private room → Return at `*** PRESS RETURN:` →
    menu option `0` as one atomic line → the MUD closes the connection.
    Never `quit`. `encamp` only when stranded in the field.
13. **Verify the cleanup:** relay pid dead, `pgrep -af nilgiri` empty,
    `/tmp/mud_cmd` gone. If the MUD didn't close: kill the exact relay
    PID (never `pkill -f`), then the holder PID, then `rm -f
    /tmp/mud_cmd`. PIDs live in `[NILGIRI DIR]/run/relay.pid` and
    `run/fifo_holder.pid`.

## Making it yours

The repo ships with one operator's setup as the working example. To run
your own characters, set `CHAR_NAME` to your character's name when
launching (the relay defaults to `SinMuseBot`).

The bot controllers are **hardcoded by design**: Sin (the Implementor,
ultimate authority over every bot), plus the authorized immortals
Motorola, Russ, and Mandessa. Only these four can give a bot orders —
other immortals and players cannot. If you fork this repo for your own
use, change the controller list in `scripts/mud_relay.py` (the `SPEECH`
regex) and in `DRIVER_BRIEF_TEMPLATE.md` deliberately.

Everything else you customize lives in the per-session brief
(`DRIVER_BRIEF_TEMPLATE.md`): approved zones, known hazards, rent/bank
locations, and the people your character knows.

## After the session

14. **Chat report:** what happened, XP gained, kills with locations,
    loot/gold and bank activity, how the session ended.
15. **Publish the adventure summary** to
    `session_summaries/[Character]/session-NN.md` (zero-padded, NN = the
    next free number — `ls` the character's directory first) and push.
    No credentials, no raw log contents.
16. **Update the maps** (with ASCII sketches) and push.
17. **Raw logs stay local-only.** Session summaries contain no secrets.
