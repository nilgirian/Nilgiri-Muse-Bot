# Nilgiri MUD Login — Lessons Learned

Date: 2026-09-24 (generalized 2026-09-25)
Goal: SSH as `player@nilgiri.net`, log in as a MUD character, enter the game.

**Standing rule: `SinMuseBot` below is only an example from the first session. Always prompt the user for the character name and the character password at runtime. Never hardcode a name, email, or password.**

## 1. Network reality on this VM

- The VM is Ubuntu 24.04. Outbound traffic goes through an HTTP egress proxy (`hatch-egress-proxy:3128`, configured via `ALL_PROXY` / `HTTP_PROXY` env vars).
- Direct `ssh player@nilgiri.net` fails: `kex_exchange_identification: read: Connection reset by peer` / `Connection reset by <proxy-ip> port 3128`.
- `getent hosts nilgiri.net` returns `198.18.27.43` (benchmark range) from local DNS, but the proxy resolves it itself for CONNECT — don't rely on local DNS.
- Good news: the proxy **does** allow `CONNECT nilgiri.net:22` (returns `HTTP/1.1 200 Connection Established`). Many proxies only allow 443; this one allows 22.

## 2. How the tunnel works

HTTP `CONNECT` asks the proxy to open a raw TCP tunnel to `host:port`, then bytes are forwarded blindly. SSH runs inside that tunnel.

Flow:
1. Open TCP to proxy host:port from `ALL_PROXY`.
2. Send: `CONNECT nilgiri.net:22 HTTP/1.1` + `Host:` + `Proxy-Authorization: Basic base64(user:pass)` (user/pass parsed from `ALL_PROXY` at runtime).
3. Wait for `HTTP/1.1 200`. If not 200, abort.
4. Bidirectionally forward between the socket and ssh's stdin/stdout.

## 3. Scripts (persisted)

All in `~/workspace/nilgiri/` (not `/tmp`, which is ephemeral):

- `proxy_tunnel.py` — Python CONNECT tunnel for `ssh ProxyCommand`. Reads proxy URL from env (`ALL_PROXY` etc.), never hardcodes credentials. Uses threads for stdin↔socket and socket↔stdout forwarding.
  - Usage: `python3 ~/workspace/nilgiri/proxy_tunnel.py <host> <port>`
  - Earlier version used `select` with non-blocking stdin and silently died; thread-based version works.

- `ssh_via_proxy.sh` — wrapper:
  ```bash
  #!/bin/bash
  exec ssh -o ProxyCommand="python3 $HOME/workspace/nilgiri/proxy_tunnel.py %h %p" \
    -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null "$@"
  ```
  - Usage: `~/workspace/nilgiri/ssh_via_proxy.sh player@nilgiri.net`
  - Test key auth (expected to fail if key not yet authorized):
    `~/workspace/nilgiri/ssh_via_proxy.sh -o BatchMode=yes player@nilgiri.net echo ssh-ok`
  - Verify tunnel + banner manually:
    ```python
    # python3 -c with socket: CONNECT nilgiri.net:22, then recv banner
    # Expected banner: SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u10
    ```

## 4. SSH auth notes

- Key auth: `~/.ssh/id_ed25519.pub` is:
  `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINHmhYK0KyVVsNDzmY1l3MmL0quiIQwsx//yG22cF7s3 hatch`
  The user added this to `player@nilgiri.net:authorized_keys`, but the server still returned `Permission denied (publickey,password,keyboard-interactive)` when offering it. Key may not have propagated or was added to the wrong account. Fall back to password.
- Password auth: the SSH login is `player@nilgiri.net` and its password is
  public (per Fred, the MUD operator): `letmein`. Export it as `MUD_PASS`
  for the relay/scripts, e.g.:
  ```
  MUD_PASS='letmein' timeout 30 expect /tmp/mud_login.exp
  ```
  Expect script spawns `/tmp/ssh_via_proxy.sh` (or the workspace version), expects `(P|p)assword:`, sends `$env(MUD_PASS)`.

## 5. MUD session flow (Nilgiri Gamma 5.0.2563)

After SSH auth succeeds:

1. `Nilgiri Gamma 5.0.2563 (nilgiri.net 8008) session 3400`
2. `Do you want text color (yes/no) ?` → `yes`
3. Welcome banner (ASCII art, "WELCOME TO the world of Rivin and Sin... NILGIRI")
4. `By what name do you wish to be known?` → the character name (prompt the user every time)
5. Branch on the name:
   - **Existing character** → goes directly to `What is the password?` (skips creation). Prompt the user for that character's password and enter it.
   - **Unknown name** → `Did I get that right, <name> (yes/no) ?` appears. This means the character does not exist yet. **Stop and ask the user whether they want to create it.** If yes, prompt for the email address that should receive the temp password (never default to a personal email), then run the creation flow in §10.
6. `WELCOME TO Nilgiri the Forgotten World` → `*** PRESS RETURN:` → send return
7. Menu appears:
   ```
   0) Exit from the Forgotten World.
   1) Enter the game.
   2) Change password.
       Make your choice:
   ```
   → send `1` to enter the game.
8. In game at `<>` prompt. Useful commands: `look` (describe room).
   To leave the game: if you are in a rented private room (rent room), use
   `klick`; if you are out in the game with no rent room to go to, use
   `encamp`. (Taught by Fred, 2026-09-27.)
9. **Always leave with `klick` (from rent) or `encamp` (in the field),
   never `quit`** — `quit` drops all inventory. `klick`/`encamp` save it.
   Proper exit sequence from rent: `rent` -> private room -> `klick`
   -> `*** PRESS RETURN:` -> press return -> menu appears -> choose `0`
   (Exit from the Forgotten World). The MUD should then close the
   connection itself; kill ssh afterwards only if it is still alive.
10. If the previous session didn't end cleanly, login shows `Reconnecting...` and goes directly to `<>` (skips the menu).

## 6. Expect automation notes

- `expect` is at `/usr/bin/expect`. `pexpect` 4.9.0 was installed via pip (for Python automation, but Tcl expect proved more reliable for MUD).
- `muse.exec` does NOT support `pty: true` — use `expect` for interactive sessions.
- Strip ANSI color codes when reading MUD output: `sed -e 's/\x1b\[[0-9;]*m//g'`.
- Watch for quoting hell: `ssh -o ProxyCommand="..."` inside `expect`'s `spawn` breaks Tcl quoting. Workaround: put the ssh invocation in a shell wrapper (`ssh_via_proxy.sh`) and `spawn` the wrapper.
- Generic `Send "\r"` to `Select your X:` prompts loops forever — always send a valid listed option.
- The MUD prompt `<>` may have ANSI codes; match with `-re "<>"` not `-re "<> "`.
- For password prompts, use `log_user 0` before sending and `log_user 1` after to avoid leaking passwords into logs.
- "What is the password?" prompt has trailing control chars (`?\x01`); match with `-re "What is the password"` not exact.

## 7. Security notes

- NEVER write the proxy password (from `ALL_PROXY`), the MUD shared SSH password, any character password, or any email address to files, logs, or chat. All of them are transient runtime input: SSH password via `MUD_PASS` env, character name via `CHAR_NAME` env (or a user prompt), character password via `/tmp/mud_password.txt` + `log_user 0`, email via `CHAR_EMAIL` env (or a user prompt).
- The earlier debug run leaked a proxy password into tool output via `expect`'s `spawn` echo — avoid `log_user` + command echo when credentials are in the command line. `proxy_tunnel.py` avoids this by reading credentials from env at runtime.
- `ssh_via_proxy.sh` uses `StrictHostKeyChecking=no` + `UserKnownHostsFile=/dev/null` for automation; fine for this throwaway MUD login, not for general use.
- No passwords or personal emails live in this repo. If one ever slips in, restart the repo fresh (delete + recreate) so it never appears in history — editing alone is not enough.

## 8. Quick resume commands

```bash
# Test tunnel + SSH banner (no auth)
/tmp/proxy_tunnel.py nilgiri.net 22  # then read banner, or use the python CONNECT snippet

# SSH via proxy (password prompt)
/workspace/nilgiri/ssh_via_proxy.sh player@nilgiri.net

# Expect-driven login to skin-complexion prompt (example)
/workspace/nilgiri/ssh_via_proxy.sh player@nilgiri.net  # wrapped by expect script
```

## 9. Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `Connection reset by peer` on direct ssh | Expected — use the proxy tunnel, not direct ssh |
| `Connection timed out during banner exchange` | Old `proxy_tunnel.py` (select-based) was broken; use thread-based version in workspace |
| `Permission denied (publickey,...)` | Key not authorized (yet); use password via expect |
| `Select your X:` loops forever | Sent invalid option; send one of the listed options exactly |
| `command-line line 0: invalid quotes` | Nested quotes in `ProxyCommand` inside expect; use the shell wrapper |

## 10. Character creation flow (discovered 2026-09-24)

Complete sequence. **Attributes are picked randomly** — `mud_wait_for_pass.exp`
chooses a random valid option at each prompt and logs the pick (values in
parentheses are the full option pools):

1. text color -> yes
2. name -> <character name> (prompt the user), then confirm `yes` at "Did I get that right"
3. email -> the email address the user gave for this character (entered twice; receives the temp password)
4. gender -> random (female, male)
5. race -> random (human, drow, dwarf, elf, giant, gnoll, gnome, goblin, halfling, ogre, orc, pixie, saurian), then confirm `yes` at "Do you wish to be <race>"
6. hair shape -> random (bald, cropped, straight, wavy, curly, spiked, mohawked, braided, dreadlocked)
7. hair length -> random (very short, short, medium, long, very long)
8. hair color -> random (black, brown, red, blond, platinum, gray)
9. skin complexion -> random (pale, light tan, tan, dark tan, dark)
10. eye color -> random (black, brown, blue, hazel, green)
11. eye shape -> random (almond, round, squinty, beady)
12. demeanor -> random (very young, young, adolescent, adult, mature, elderly, old, ancient)
13. height -> random (very short, short, average, tall, very tall)
14. weight -> random (very light, light, moderate, heavy, very heavy — NOTE: "average" is NOT valid here)
15. description confirm -> yes
16. homeland -> random (Jora, Argoceania)
17. stats reroll -> no (keep the server's roll, which is already random)
18. handedness -> random (right, left)
19. Then: "A password has been sent to you at: <email>" -> "What is the password?" -> enter the temp password from the email (see §11)

The example character `SinMuseBot` (2026-09-24) was rolled before
randomization: male human, straight short brown hair, tan, almond brown eyes,
adult, average height, moderate weight, Jora, right-handed.

## 11. Critical: Temp password is session-bound

- The temp password emailed is ONLY valid for the specific connected session sitting at "What is the password?" prompt.
- If you disconnect and reconnect, the old temp password is invalid. Each new creation run generates a NEW temp password.
- DO NOT use expect scripts that exit at the password prompt. You must keep the session alive.
- Working pattern: `mud_wait_for_pass.exp` goes through creation with `MUD_PASS`/`CHAR_NAME`/`CHAR_EMAIL` from env, then at "What is the password?" it waits (polls `/tmp/mud_password.txt` every 5s, up to 10 min) without disconnecting, and sends the password with `log_user 0` to avoid leaking it.
- After successful entry, the character is saved and that temp password becomes its permanent password until changed. Subsequent logins go directly to "What is the password?" (no recreation needed).
- Verified with the example character `SinMuseBot` on 2026-09-24: entered the game (saw WELCOME TO Nilgiri, then "*** PRESS RETURN:").

## 12. Example session: SinMuseBot (2026-09-24)

- Created as male human from Jora (values in §10 are this character's).
- Entered game, saw the Temple of Midgaard, then was transferred to Russ' House.
- Deities present: Russ, Motorola, Sin (Implementor). Sin said "the thing finally logged in".
- Test commands run: `look`, `smile motorola` ("You smile at Motorola."), then `encamp` to leave with inventory saved.
- Character persists; no recreation needed on next login.

## 13. Password lifecycle

- Temp password emailed during creation is session-bound (see §11).
- Once entered correctly, the character is saved AND that temp password becomes the character's permanent password until changed (verified with the example character on 2026-09-24).
- To change: choose option 2 at the menu after pressing return.
- Do NOT reuse old temp passwords from previous (disconnected) sessions.
- Never store character passwords in files or the repo — prompt the user at runtime.

## 14. Runtime prompt checklist (for the assistant)

Every MUD session, ask the user for:
1. **Character name** — which character to connect as.
2. **Character password** — that character's password (transient; never stored).
3. If the name turns out to be new (MUD asks "Did I get that right?"): **whether to create it**, and if yes, **which email** should receive the temp password.

Then follow §5. Nothing in this repo contains a name, email, or password.

## 15. Creating additional characters (for different jobs)

The flow in §5/§10 is reusable for any character name. Variables:
- `CHAR_NAME`: e.g. `SinScout`, `SinMage` (must be unique; case-sensitive)
- `CHAR_EMAIL`: **prompt the user for this each time** — do NOT default to a personal email. Each new character triggers a temp-password email.
- Appearance/race/class choices: pick per job.

To create a new character:
1. Confirm with the user that they want a new character, and ask which email should receive the temp password.
2. Run `mud_wait_for_pass.exp` with `MUD_PASS`, `CHAR_NAME`, `CHAR_EMAIL` set via env:
   ```
   MUD_PASS='<ssh-password>' CHAR_NAME='<name>' CHAR_EMAIL='<email>' \
     timeout 700 expect ~/workspace/nilgiri/mud_wait_for_pass.exp
   ```
3. At "What is the password?" the script waits; the user reads the temp password from the email and provides it (via `/tmp/mud_password.txt` or chat), and the script submits it in the still-connected session.
4. That temp password becomes the new character's permanent password.
5. Each character has its own password; never store them — prompt at runtime.

Notes:
- Same SSH login (`player@nilgiri.net`) hosts multiple characters; the "By what name" prompt selects which one.
- If name is new, the MUD asks "Did I get that right?" and goes through full creation (§10). If name exists, it goes directly to the password prompt.
- Character names are case-sensitive.

## 16. In-game communication (2026-09-25)

- Speech from others arrives as `<Name> says, "..."`, `<Name> asks, "..."`,
  `<Name> exclaims, "..."`, or `<Name> tells you, "..."`. Match all the verbs —
  a first version that only watched `says`/`tells you` missed Motorola's
  `asks`.
- To speak: the `say` command, e.g. `say hi` produces `You say, "hi"`.
- Bot etiquette that works: stay silent unless Sin, Motorola, or Russ address
  the bot directly; then reply with `say`. Keep replies short and lowercase,
  like a player would type them.
- Simple reply policy that held up in testing: greeting → greet back;
  question → `i'm just a bot, ask sin`; name mention → `that's me`;
  otherwise `ok`.
- Reference implementation: `scripts/mud_comms_test.exp` — logs in, idles
  N minutes answering only direct address from those three, then
  `say time to leave` + `encamp`.
- For live, agent-driven conversation: `scripts/mud_relay.py` — logs in and
  relays stdin/stdout so the agent reads the game and types replies itself.
  Flags speech as `>>> SPEECH name=... verb=... text=...`. Passwords are read
  from env (`MUD_PASS`, `CHAR_PASS`) and redacted from output.
- The MUD only accepts standard US ASCII keyboard characters. Never send
  emoji or other non-ASCII in `say` text or commands. `mud_relay.py`
  strips non-ASCII from outbound lines as a safety net and logs
  `>>> NON-ASCII STRIPPED` when it does.
- After `encamp`, always walk the proper exit: `*** PRESS RETURN:` → press
  return → menu → choose `0` (Exit from the Forgotten World). The MUD should
  close the connection itself; kill ssh only if it is still alive afterwards.
  `mud_relay.py` does this automatically: on the "You set up camp"
  confirmation it presses return, picks option 0, and treats the MUD closing
  the connection as a clean exit (timeouts of 30s for the prompts / 15s for
  the close, then ssh is killed as fallback). The expect fallback
  `mud_encamp_cleanup.exp` follows the same sequence, then kills the ssh pid
  with TERM/KILL and verifies it is gone.
- Relay implementation lessons (2026-09-26 debugging):
  - The MUD's `*** PRESS RETURN:` arrives in the *same read* as the encamp
    confirmation. Never clear the match buffer on a state transition —
    keep the tail after the matched text, or the prompt you are waiting
    for is already gone.
  - Timeout checks must run every main-loop iteration, not inside the
    data-arrival branch. A silent MUD sends nothing, so a timeout nested
    under "data arrived" never fires and the relay hangs forever.
  - To stop a stuck relay, send `>>>QUIT` on its stdin so its finally
    block terminates ssh. Killing the ssh process directly makes the
    relay see EOF and *reconnect* — a phantom re-login.
  - `str.replace` fails silently on mismatch (e.g. whitespace). Always
    grep to confirm a patch actually landed.
- Session length is a hard requirement, never indefinite. Every login needs a
  defined time period (e.g. 3 minutes); if none is given, ask for one before
  logging in. Measure real wall-clock time from the in-game marker — polls
  return immediately on new output, so counting exchanges is not timing.
  (Learned 2026-09-25: a "3 minute" session actually ran 37 seconds because
  nobody watched the clock.)
- Incident 2026-09-25: a relay session went one-way deaf — keystrokes reached
  the game (others saw the bot's `say`), but zero bytes came back for 3+
  minutes while Sin and Motorola were actively talking to the bot. The relay
  process stayed healthy (sleeping in select, ssh alive), so nothing
  signaled the failure. Suspected one-way stall in the proxy/ssh downstream.
  Fixes: `ServerAliveInterval=15`/`ServerAliveCountMax=3` on every ssh
  session (a stall now aborts loudly instead of hanging silently), plus a
  relay watchdog (probe with `look` after 75s of no output, kill ssh and
  auto-reconnect after 150s, max 5 attempts). If the relay ever goes dark
  again, fall back to the expect script for a verified `encamp`.
- Incident 2026-09-25 (repeat): a "3 minute" session actually ran ~24 seconds
  in game. Root cause: the clock was checked once at IN GAME and never again;
  each poll returned in seconds (new output arrives fast when people are
  talking) and poll cycles were mistaken for elapsed minutes. This is the
  same failure as the earlier 37-second session. Fix: the relay now takes
  SESSION_SECONDS and announces `>>> TIME UP` from its own clock, so the
  agent waits for the marker instead of doing arithmetic across polls.
  Never begin the exit sequence without seeing `>>> TIME UP` (or verifying
  `date +%s` against the deadline).
- Incident: silent relay death (sessions 4 and 12, 2026-09-27/28). Both
  times the relay vanished ~60-70 minutes after launch with NO marker in
  the log — no `>>> TIME UP`, no error, no `>>> MUD EOF`, no reconnect
  attempt — and no relay/ssh processes left. Every in-code exit path logs
  a `>>>` marker and a Python exception would print a traceback, so this
  was an external kill of the process, not a relay bug. Leading theory:
  the execution environment reaps background process trees belonging to
  finished exec shells; both relays were started with `nohup ... &` from
  a shell that had long since exited.
- Fix (2026-09-28): ALWAYS launch via `launch_relay.sh`, never a
  hand-rolled `nohup ... &`. Usage:
  `SESSION_SECONDS=7200 MUD_PASS=... CHAR_PASS=... ./launch_relay.sh [logfile]`
  (passwords travel in env, never on a command line). It runs the relay
  and its FIFO holder in their own session via `setsid` (new SID/PGID,
  reparented to init), so nothing that reaps the launching shell's tree
  can reach them. It refuses to start if a relay is already alive and
  prints the PIDs for verification.
- Relay heartbeat (2026-09-28): `mud_relay.py` writes `run/heartbeat`
  (unix time + PID) every 60s and logs `>>> RELAY PID <pid>, PGID
  <pgid>, SID <sid>` at startup. The driver checks the heartbeat's age on
  every poll; older than ~2 minutes means the relay process is gone —
  report it immediately instead of discovering it from a link-dead
  character. Heartbeat proves the PROCESS is alive, not that the MUD
  connection is healthy.
- Relay cleanup: kill the exact PIDs in `run/relay.pid` and
  `run/fifo_holder.pid` (never `pkill -f`), then `rm -f /tmp/mud_cmd`.
  Never delete the FIFO while the relay is alive — writers block forever
  with no reader.
- Forensics after a silent death: `stat -c %y run/heartbeat` is the last
  minute the relay was alive; the session log's last line shows what it
  was doing. If a detached relay (own SID, verified via the startup line)
  survives past the ~70-minute mark, the reaping theory is confirmed; if
  it dies anyway, the killer is host-level and the heartbeat gives the
  exact time.

## 17. First verified 3-minute session (2026-09-25)

- `SESSION_SECONDS=180` on the relay. Timer fired `>>> TIME UP` at 180s of
  game time; the exit sequence (say goodbye → confirmed echo → `encamp` →
  confirmed "You set up camp") started only after the marker. Process log
  confirmed ~189s in game. First session whose duration is machine-verified,
  not estimated.
- Conversation quality matters more than cleverness: short, lowercase,
  player-like replies. The bot handled, in one session: a philosophical
  question (Motorola: "do you have a soul?"), a trap question (Motorola:
  "who is cooler, sin or motorola?" — answered "that's a trap and you know
  it — you're both cool", got chuckles), a factual question (Sin: "how did
  that Angels game go?" — answered only after a web search confirmed the
  6-4 score; never guess at facts), a purpose question, and a smile from Sin
  (smiled back with `smile sin`).
- When asked about its own session time (Sin: "do you know how much time you
  have left to stay?"), the bot answered from the relay timer ("a little
  over a minute"). The user explicitly tested this — the timer is now part of
  what the bot can truthfully report.
- Stay silent on speech not addressed to the bot (e.g. Sin asking Motorola
  what "ni i kitakunai" means) — that's their conversation.
- Clean shutdown verified: encamp confirmation → PRESS RETURN → menu option 0
  → MUD closes the connection (relay reports `>>> EXITED`), ssh killed only
  as fallback, then `pgrep -af nilgiri` shows no strays. Do the pgrep check
  after every session.

## 18. Exploration and mapping (2026-09-27)

First mapping session: SinMuseBot, 20-minute budget, Midgaard Northern Main
City. 13 rooms mapped; map checked into `maps/midgaard-northern-main-city.md`
(local workspace and repo). Encamped in rented private room at the Grunting
Boar Inn; clean menu-walk exit; no strays.

- Orientation first: `where` gives the zone name ("Midgaard, Northern Main
  City created by DIKU"). If outside the target zone, walk back before
  mapping anything.
- The mapping loop per room is `look` + `exits`. The `exits` command is the
  source of truth for the map — room descriptions hint at destinations but
  `exits` gives exact names and closed doors (e.g. `(portcullis)`).
- Movement is cardinal (`north`/`south`/`east`/`west`) plus `up`/`down`.
  Only US ASCII goes to the MUD (relay strips the rest).
- Speech range (taught by Fred 2026-09-28): `say` = current room only;
  `yell` = a few rooms away; `shout` = the whole zone; `gossip` = the
  whole game. That's why level-ups are announced with `gossip Level!`.
- Map format (per zone, one markdown file under `maps/`): key service
  locations up top, then one section per room with description notes, exits,
  and notable mobiles/objects. Mark seen-but-unentered exits `[UNMAPPED]`
  so the next session knows where to continue. Include a general ASCII
  sketch of the whole area (streets, landmarks, zone boundaries,
  off-limits branches) and survival notes (food/drink/heal). **Every
  mapping pass updates the sketch** so it always reflects current
  knowledge — never let the room sections grow while the sketch goes
  stale (Fred, 2026-09-28).
- Key services found in Midgaard: Temple (login point), Market Square
  (dragon fountain — drink there), Bakery (free food), Reception at the
  Grunting Boar Inn (`rent` -> private room, safe encamp).
- Rent rooms have NO exits — "there does not seem to be a way in nor out."
  Finish all mapping BEFORE renting. Rent -> encamp is the end of the
  session by design.
- Shop syntax (baker): `list` shows items with list numbers AND internal
  #codes (e.g. `#041418BA`). Buy by LIST number with a `#` prefix:
  `buy #3`. The #codes are not typed. The shopkeeper's whispered
  "What is the item #?" is flavor text, not an input prompt — answering it
  with raw commands just yields "Arglebargle, glop-glyf!?!".
- Hunger/thirst: `inventory` at session start (had 3x manna). `eat manna`
  when hungry; drink from the Market Square fountain when thirsty; free
  half loaf at the bakery (item 3, n/c) when manna runs out.
- Watch for danger signs: slashed-up street urchin corpses in two rooms
  suggest something aggressive roams the streets. Nothing attacked during
  this pass, but note it in the map.
- Immortals (e.g. "Gelu the God of Thalodia -Truth-") may be standing
  around; leave them alone.
- Every exploration session gets a timestamped log under
  `~/workspace/nilgiri/logs/` (via `ts_prefix.py`); logs are local-only,
  never committed. The map file IS committed to the repo.
- Room geometry is not always consistent: going west then back east does
  not always return to the starting room. It usually does, but expect
  incongruous rooms. Map by room identity (room name + description), not by
  assumed coordinates, and re-verify with `look`/`exits` when backtracking
  lands somewhere unexpected.

## 19. Combat basics (2026-09-27, taught by Fred)

- `score` shows hit points and movement. Moving costs movement; resting
  restores it. Never let hit points reach 0 — death is the failure state.
- In combat the prompt changes to show current hit points; watch it every
  round. If survival looks unlikely, `flee` repeatedly until escaped.
- Death respawns at the Temple of Midgaard. Find the corpse and
  `get all corpse` to recover everything.
- "Mobiles" = NPCs. ANY mobile can be killed, but only kill recognizable
  creatures/animals — never ambiguous humanoids. If a name like "Intrepid"
  is unclear, `look <name>` first to confirm it's a creature, not an
  NPC/PC.
- Safety check: `consider <mobile>` (e.g. `consider pigeon`) — the reply
  says if it looks easy or moderately hard. Attack with `kill <mobile>`
  only if survival looks likely.
- If the mobile is incapacitated but combat stops, deal the killing blow:
  `kill <mobile>` again.
- After a kill: examine the corpse, then `get all corpse`. Loot may be
  valuable; sort it out later.
- Level-up custom: `gossip Level!` (the gossip channel out-reaches `shout`) so everyone knows.

### Verified in live combat (2026-09-27, SinMuseBot first hunt: 4 fido engagements, 3 kills)

- The first engagement (12:21:59) was fled with no kill and no XP.
  The three kills: Market Square +36 XP (43 -> 79), Temple Square
  +29 +7 XP (79 -> 115), East Main Street +13 XP (115 -> 128).
- `consider` is guidance, not a guarantee. A fido judged "an easy battle"
  missed about ten rounds in a row in the Market Square fight before a
  critical hit ended it. Re-check with `score` after every fight.
- Winning still costs HP: the separate Temple Square engagement dropped
  HP 21 -> 12.
- In practice the combat prompt was just `<fighting>` — it did NOT show
  numeric HP. Watch the round-by-round text ("bites you very hard" is
  worse than "bites you hard") and `score` after fleeing or killing.
- Incapacitated does not mean dead: keep `kill <mobile>` until you see
  "is dead! R.I.P." (one fight went incapacitated -> mortally wounded ->
  dead over three kill commands). A critical hit can also kill outright.
- `get all corpse` may take the corpse itself ("You take a horribly
  crushed corpse of a beastly fido") when no contents are listed. Corpses
  in inventory decay ("starting to smell") — drop or dispose of them.
- Loot fast: janitors pick up corpses ("A janitor picks up the trash"),
  and a stolen corpse is gone.
- `rest` heals fast: 12/30 -> 30/30 in about 2.5 minutes of rest ticks.
  Movement (92/92) was untouched by this session's walking.
- Always consider first: a stray cat looked harmless but considered as
  "a higher level than you ... You would probably die..." — skipped.
- Fight math from the log: fido kills gave 36, 29+7, and 13 XP
  (43 -> 128 XP total). No level gained at 128 XP.

## 20. Combat hunt, continued (2026-09-27, SinMuseBot second hunt, 13:00-13:11)

Session: relay `proc_9cc88aa86e77`, log
`logs/session-20260927-130031.log` (local-only). Budget was 30 minutes;
retired at 11 minutes because the city was cleared of fidos and respawns
were slow. Started 128 XP, ended 334 XP (+206), still L1. 30/30 HP,
100/100 mana at exit. Full HP retire at the Grunting Boar Inn Reception
via `rent` + `encamp`, clean menu-0 exit, no stray ssh process.

Engagements: 14 fido engagements, 6 direct witnessed kills (R.I.P./corpse
in the same room). A previously mortally wounded Market Square fido was
confirmed as a corpse about 44 seconds later, making 7 eventual deaths
attributable to the hunt; keep the distinction between witnessed kills and
attributed ones unless the log proves it.

- Use `get all from corpse` to loot — this is the correct command per
  Fred. It never picks up the corpse itself (unlike `get all corpse`,
  documented in §19, which took the corpse). No corpse in inventory, no
  decay problem.
- Most fido corpses were EMPTY. The one exception (Entrance to Cleric's
  Guild) held a tiny diamond ring, which was equipped. Loot fast anyway:
  janitors clean up corpses ("A janitor picks up the trash") and corpses
  decay on their own (~44 seconds for the Market Square fido).
- Critical hits can mortally wound in ONE round: a fido judged excellent
  was taken to mortally wounded by a single critical mighty crush, then a
  finishing blow killed it. XP (+15) was awarded on the wounding round,
  before the kill.
- XP does not prove a kill, and a kill does not guarantee visible XP.
  XP was awarded at wound stages (stunned/incapacitated/mortally wounded)
  before death. Count a kill only when you see the corpse / "is dead!
  R.I.P.".
- "Stunned", "incapacitated", "mortally wounded" are states, not deaths.
  A mortally wounded fido became a corpse less than a minute later. Wait
  and verify before recording or looting.
- Named mobiles are suspect: "Intrepid the Obnoxious" stood on western
  Main Street and was NOT attacked — a name suggests an NPC person, not a
  creature. Rule stands: `look <name>` before attacking anything
  ambiguous.
- Gates are zone boundaries. Walking west through the West Gate landed
  OUTSIDE the West Gate of Midgaard — outside the city walls AND outside
  the assigned hunt zone. Went east immediately back inside. Count moves
  carefully near gates; the assigned zone is the Northern Main City only.
- Gold is important — never drop it on the ground. Rent is refused with
  valuables carried: the receptionist said "certain valuables and other
  items are prohibited in rent" and named the gold coins. The correct move
  is the Bank of Midgaard BEFORE renting: on the first visit read the sign;
  if you do not already have an account, 'Initiate New Account'; then
  'deposit gold'. 'balance' checks the balance while at the Bank. (This
  session's coins were dropped in the Reception and lost — that was the
  wrong call, corrected by Fred 2026-09-27.)
- Dump loot can be real gear: a tin crown (head slot) and a tin bracer
  moved armor from "naked" to "lightly covered". A tin chest plate and
  black leather boots had no valid wear slot — not every item is wearable.
- Movement budget: a full city sweep took move 92 -> 67. Rest recovered
  67 -> 85 quickly. Watch `move` on `score` during long patrols.
- Hunger/thirst (this session): warnings at 13:01:55. `eat` fails while
  resting — stand first. Drinking failed while full even when thirsty;
  fullness passed and the Market Square fountain worked. Half loaf of
  bread found in the Temple was kept as reserve and never needed.
- Retiring early is fine: 19 of 30 minutes unused, but the zone was
  exhausted. Saved progress beats burning the clock.

## 21. Post-session summary rule (2026-09-27, set by Fred; extended 2026-09-28)

After every session -- once the character is safely disconnected
(`encamp`, then `*** PRESS RETURN:` -> menu option 0, the MUD closes the
connection, no stray ssh process left) -- give the user a summary of the
adventure in chat: what the character did, XP gained (start -> end),
confirmed kills with locations, loot/gold and bank activity, and how the
session ended. This was the practice in every session so far; it is now a
standing rule. The timestamped session log stays local-only and is never
committed to the repo; the chat summary is what the user gets.

Additionally (Fred, 2026-09-28): write that same adventure summary to
`session_summaries/<CharacterName>/session-NN.md` in the repo
(zero-padded two-digit number, e.g.
`session_summaries/SinMuseBot/session-12.md`), one file per session per
character, and push it. The directory has a README.md explaining the
per-character layout. Write the file before pushing so the local copy
and the repo copy are identical. Like every repo artifact, it must
contain no passwords, credentials, or log contents.
