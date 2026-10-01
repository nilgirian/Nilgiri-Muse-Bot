# Operator Runbook — running a Nilgiri session

You are the **operator** (see `NILGIRI_LOGIN.md` §23 for the
operator/driver/relay architecture). This is the full session lifecycle,
start to finish. The playbook (`NILGIRI_LOGIN.md`) is the authority on
game mechanics; this file is the procedure for running the operation.

**Who can push:** the "push to GitHub" steps below apply ONLY when you
are Fred's own Muse operating on his canonical repo
(`nilgirian/Nilgiri-Muse-Bot`) with his credentials. If you are any
other user's Muse working from a clone, do everything else in this
runbook but keep all changes local — never attempt to push to Fred's
repo. (GitHub enforces this anyway: `nilgirian` is the sole
collaborator.) Fork the repo if you want to publish your own version.

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
4. **Record the subscription meter** (`subscription-status status` — the
   "Usage: N% of free weekly limit" line and the reset time). You need
   the before/after pair to state the session's token cost as a percent
   of the weekly allowance in the published summary.

## Launch

4. Launch the relay **detached** (own session, survives the launching
   shell):

   ```bash
   cd [NILGIRI DIR]
   SESSION_SECONDS=[BUDGET] MUD_PASS='[ssh password]' CHAR_PASS='[char password]' \
     ./scripts/launch_relay.sh logs/session-$(date +%Y%m%d-%H%M%S).log
   ```

   `MUD_PASS` is the MUD's publicly-published `player@nilgiri.net`
   password — find it on the connect page at
   https://nilgiri.net/doku.php?id=nilgiri:connect. It is the only
   credential in this setup that isn't per-session. Passwords travel in
   the environment (inherited by the detached child), never on a command
   line. `CHAR_NAME` defaults to `SinMuseBot`.
5. **Verify `IN GAME`** before doing anything else:
   `grep -a "IN GAME" [LOG]` — the session timer starts there. If the
   character was link-dead, the MUD reports
   `>>> IN GAME (reconnected, skipped menu)`.
6. **Register the session with the watchdog.** Write
   `[NILGIRI DIR]/run/session_active.json` (home persists across VM
   reboots; `/tmp` does not — never put it there):
   ```json
   {
     "character": "SinMuseBot",
     "mission": "[e.g. treasure hunt]",
     "session_start": "[ISO 8601 with offset, e.g. 2026-09-29T08:42:05-07:00]",
     "budget_end": "[ISO 8601 with offset]",
     "log": "logs/session-YYYYMMDD-HHMMSS.log",
     "status": "active",
     "notified": false
   }
   ```
   The `nilgiri-session-watchdog` cron (every 5 min, goal-owned) reads
   this file: if the relay's heartbeat goes stale mid-session it pages
   Fred in the main chat with the remaining budget so a relaunch can be
   authorized. On clean retirement, delete this file (or set
   `status: "complete"`) so the watchdog stands down.

## Drive

6. Copy `DRIVER_BRIEF_TEMPLATE.md`, fill in the bracketed sections for
   this session's mission, and save the filled brief next to the session
   log as `logs/brief-YYYYMMDD-HHMMSS.md` (local-only, never committed).
   Then start the driver — see "Driver execution methods" below for the
   two ways (workflow driver is the current default; subagent driver is
   the fallback).
7. **Stay responsive.** The driver plays; you talk to the human, watch
   for problems, and handle anything the driver can't (it has no
   passwords and must never restart the relay).

## The driver model — why not drive directly

A session is one to two hours of polling the game every few seconds.
If the operator drove directly, it would be locked in for the whole
session — unresponsive to the human, who messages mid-session (live
in-game orders as Sin, questions, corrections). So the work splits:
the driver subagent plays the session in the background while the
operator stays available, holds the credentials, keeps the repo
current, and supervises.

**Known gap, stated plainly:** the driver is worse at playing than the
operator. It doesn't get the operator's judgment — it gets a written
brief, which is a compressed copy of what the operator knows, and
compression drops the *why* behind the rules. Every driver also starts
fresh with zero lived experience; the operator learns across sessions,
the driver doesn't. The result: it follows the letter and misses the
spirit. Real examples: a driver read "XP doesn't prove a kill" and
claimed the ferocious rabbit on a mortal-wound plus flee (reverted);
three drivers read "track real time" and retired early on estimated
time.

**How we improve it together** (Fred, 2026-09-29 — standing agreement):

- The repository is the shared brain. Every driver mistake becomes a
  hard structural rule in `DRIVER_BRIEF_TEMPLATE.md` the same session —
  not advice, mechanics (e.g. "the relay's `>>> TIME UP` is the only
  retirement trigger; check `date` every 15 minutes").
- The operator spot-checks the session log mid-session, not just in the
  end-of-session audit. Catching a misread kill or a missed gossip
  during the session is worth more than any post-mortem.
- The driver never sees passwords (they are transient, operator-only)
  and never restarts the relay — those stay with the operator, along
  with every repo write.

## Driver execution methods — subagent vs workflow (2026-09-29)

Two ways to run the driver. The briefs work for both; only the launch,
steering, and monitoring differ. Method B is the current default
(Fred, 2026-09-29); Method A is the fallback if B's tradeoffs aren't
worth it.

### Method A — subagent driver (original, fallback)

The operator spawns the driver with `subagent.spawn` and the session
brief. The driver inherits the operator's FULL chat transcript as its
starting context — every session report, every tool output, everything
discussed that day. After a full day of sessions that is hundreds of
thousands of tokens before the driver sends its first command.
(Measured 2026-09-29: one 2-hour block burned ~10% of the weekly token
allowance; the inherited transcript is the largest per-driver cost.)

- Steering: `subagent.send` — corrections delivered async, applied on
  the driver's next turn.
- Monitoring: `subagent.list` plus the runtime's activity summaries.
- To switch back to A: spawn with `subagent.spawn`, steer with
  `subagent.send`, monitor with `subagent.list`. Nothing else changes.

### Method B — workflow driver (current default, experiment 2026-09-29)

**Setup (do once):** the workflow script lives in this repo at
`workflows/nilgiri-driver.js`. Install it as a saved workflow named
`nilgiri-driver` (via `workflow.create` with the file's contents).
Without this step, Method B cannot launch — the name alone is not
enough.

The driver runs as a child agent of the saved workflow
`nilgiri-driver`, launched with `workflow.launch_async` and args
(`brief_path`, `log_path`, `inbox_path`, `session_seconds`,
`character`). A probe on 2026-09-29 verified: workflow children get the
~30K-token standing context (system prompt, MEMORY.md, people index —
i.e. the durable instruction set) but NONE of the operator's
conversation. Spawn cost drops from "the whole day" to ~30K + the
brief. Zero-context spawn is not possible — the standing context is
baked in for every agent.

Differences from A:

- Steering: no `subagent.send`. The driver reads
  `run/driver_inbox.md` on EVERY wake; the operator steers by appending
  timestamped notes to that file. Operator notes override the brief the
  same way controller speech does. (Create the inbox file at session
  launch; it is local-only, never committed.)
- Monitoring: `workflow.view_run` instead of `subagent.list`. There are
  no automatic activity summaries — the operator spot-checks the
  session log directly, which matters more anyway.
- Failure modes: the workflow daemon is VM-local, so a VM reboot kills
  the workflow driver exactly like it kills the relay. Recovery is
  unchanged: the watchdog pages, the operator relaunches the relay and
  starts a new workflow run for the remaining budget.
- Unchanged: relay launch, watchdog, retirement procedure, repo writes,
  and the brief format. The driver still never sees passwords.

### What Method B does NOT fix

The in-session accumulation problem: a driver waking every 20 seconds
still piles up log reads and tool outputs over a 2-hour session.
Method B fixes the spawn cost, not the session cost. Lean-driver
discipline (small `tail` windows, no redundant reads, short runs)
applies under both methods — and is the next thing to tighten.

### How to compare

After a Method B session, compare against the Method A baseline
(session 21b, 2026-09-29): spawn context (~30K + brief vs full
transcript), steering latency (inbox poll vs `subagent.send`),
missed-controller-speech count, and whether the operator felt blind
without activity summaries. If B is worse at playing or harder to
supervise, switch back to A per above.

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
9b. **Session watchdog (2026-09-29, Fred's request).** The
   `nilgiri-session-watchdog` cron runs every 5 min, above the VM, so it
   survives reboots. While `run/session_active.json` says `active` and
   the budget window hasn't closed, it checks the relay heartbeat: if
   stale, it compares `who -b` against `session_start` to tell a reboot
   from a plain relay death, then pages Fred ONCE in the main chat
   (`notified: true` in the session file stops repeats) with the
   remaining budget and an ask for the character password to relaunch.
   It cannot relaunch by itself — passwords are never stored — so the
   page is the recovery path. Watchdog event log:
   `~/workspace/goals/nilgiri-mud-bot-gameplay/hidden_files/watchdog.log`.
   A reboot is a platform deployment replacing the VM (documented
   behavior, ~5 logged so far), not something our load causes: our
   footprint is tens of MB on an 8GB VM.
10. **Network stalls.** `Timeout, server nilgiri.net not responding.` is
    OpenSSH aborting after its keepalives go unanswered (now 150s —
    `ServerAliveCountMax=10` in `scripts/ssh_via_proxy.sh`). The MUD is
    not down; the relay reconnects automatically. After a reconnect,
    the driver re-verifies state (`score`, `look`, `where`). Stalls now
    carry layer attribution: `>>> PROBE` / `>>> STALL` lines say
    `SSH PROCESS DEAD`, `TRANSPORT FAILURE (...)`, or `PATH ALIVE (...)
    — silence is the MUD or the SSH session`, from an independent TCP
    check through the proxy to nilgiri.net:22.
11. **Human override.** If the human gives the character a direct
    in-game order that contradicts the brief, the brief loses. Tell the
    driver this in every brief (it's in the template).

## Retire

12. Normal retirement (driver does this at `TIME UP`, or you do it
    directly): bank carried gold AND valuables (gems, notes, treasure —
    the bank accepts deposits of valuables, not just coins) → walk to the
    rent room → `rent` →
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

**This checklist fires EVERY time the bot is stood down for any reason**
— TIME UP retirement, manual park, reboot-shortened session, Fred calling
it early. "Parked" is "session ended." Do not report a park/exit as a
mere status update and stop; run the full checklist every time.

14. **Chat report — tell it as a story, in first person.** MUD is
    about storytelling: the debrief should read like an imaginative
    adventure tale told BY the character ("I woke in the Newtonia rent
    room", "I put my shoulder into the boulder") — never third-person
    ("SinMuseBot woke...", "The bot put..."). The character tells it as
    an adventure, not a technical report: fleeing is framed as panic
    ("I panicked and fled"), never as noflee mechanics ("noflee fired
    at 27"). TIME UP is never named in the story — it is the session's
    natural end ("my game session came to its end in the rent room").
    Health is described in plain words ("I took a massive beatdown",
    "barely clinging on"), never as HP ("my HP cratered"). Draw every
    beat from what
    actually happened — the hunts, the close calls, the finds — with the
    hard numbers woven in: XP gained, kills with locations, loot/gold
    and bank activity, token cost (with percent of weekly allowance),
    how the session ended. Never invent events; every story beat must
    come from the log. End the debrief with a link to the published
    session summary page
    (`https://github.com/nilgirian/Nilgiri-Muse-Bot/blob/main/session_summaries/[Character]/session-NN.md`).
15. **Publish the adventure summary** to
    `session_summaries/[Character]/session-NN.md` (zero-padded, NN = the
    next free number — `ls` the character's directory first) and push.
    No credentials, no raw log contents. Write it as a story too —
    first-person as the character ("I", never "SinMuseBot"/"the bot"),
    narrative first, then a compact stat block at the end (XP, kills,
    loot, bank, and the `## Token cost` section with raw tokens AND
    percent of weekly allowance). The stat block's bank line shows the
    account's movement: `+Xgc deposited, -Ygc spent → Zgc total
    (#0000-11FB)` — growth, spending, and ending total, not just
    "deposited".
16. **Update the maps** (with ASCII sketches) and push. **Every newly
    discovered zone gets its own `maps/<zone>.md` file** — never just a
    section inside another area's map (session 27's fishing village was
    folded into `newtonia.md` with a "layout TBD" lump instead of a
    real map; Fred caught it). **Every map file starts with the zone's
    recommended level** from `where` (quoted; "none shown" or "unknown —
    `where` never run" where that's the case). The area it connects
    from links to it by name and with the `{{Zone}}` marker. Verify the sketch against the
    room list before pushing: every mapped room must appear on the
    sketch, and no sketch note may contradict the room list (stale
    "NOT FOUND" / difficulty notes are dangerous). A map whose sketch
    and room list disagree is not done. Every sketch marks
    its connections to other mapped areas with `{{Area Name}}` at the
    edge where the areas meet (e.g. `{{Hills and Plains}}` outside the
    West Gate, `{{Midgaard Southern Residential}}` across the Central
    Bridge) — each map shows where the others attach.
17. **Raw logs stay local-only.** Session summaries contain no secrets.
