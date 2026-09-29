# Lessons Learned — SinMuseBot (2026-09-27 onward)

Seven sessions in the Northern Main City of Midgaard and the Hills and
Plains, plus corrections taught by Fred. The full technical playbook
lives in NILGIRI_LOGIN.md; this file is the plain-language record. It is
written for two readers: the person running the bot, and a Muse AI
installing this repo on itself by reading it.

Session logs stay local-only (never committed); the per-session history
below is the evidence these lessons rest on.

## Durable lessons

### Reliability — the relay and the connection

- **A closed stdin pipe detaches the relay; it never quits it.**
  `scripts/mud_relay.py` treats stdin EOF as "the driver is gone", stops
  watching stdin, and keeps the session alive. At TIME UP with no driver
  it auto-retires: `encamp` in place, then the normal exit-menu walk
  (Return at `*** PRESS RETURN:`, menu option 0). If encamp is
  unconfirmed it tries `flee` then encamps again; link-dead is only the
  last resort. Send `>>>QUIT` on stdin to end the relay deliberately.
- **ssh stalls and flaps; the reconnect logic holds.** On timeout the
  relay kills ssh and re-logs in (up to 5 attempts); the MUD takes the
  session back with "Reconnecting...". After every reconnect, verify
  state with `score` and `look` before resuming.
- **TIME UP is not guaranteed.** If the budget has clearly elapsed and
  the signal never fired, retire on elapsed time — don't wait.
- **Kill the relay after a clean MUD exit.** The MUD closing the
  connection looks like an EOF, and the relay will start RECONNECTING
  on it. Terminate the relay process and verify no stray ssh remains
  (`pgrep -af nilgiri`); a clean exit is only clean when nothing is
  left running.
- **When the network flaps, retire early.** Batch movement commands,
  verify each hop against the log, head for rent at the first stable
  window. Don't loot corpses outside while flapping — get inside first.
- **Launch detached anyway.** `launch_relay.sh` puts the relay and FIFO
  holder in their own session (`setsid`, new SID/PGID, reparented to
  init) so shell-tree reaping can't reach them. The relay writes
  `run/heartbeat` every 60s and logs PID/PGID/SID at startup; the driver
  checks heartbeat age on every poll and treats >~2 minutes stale as
  "relay dead". Cleanup: kill the exact PIDs in `run/relay.pid` /
  `run/fifo_holder.pid`, then `rm -f /tmp/mud_cmd`.
- **"Timeout, server nilgiri.net not responding." is ssh giving up, not the MUD.**
  That message is OpenSSH's own client-side abort: if `ServerAliveInterval`
  x `ServerAliveCountMax` seconds pass with no keepalive reply, ssh kills
  the session itself. The stall is in the VM -> proxy -> nilgiri.net path;
  the MUD game was never down during these events. Raised to
  `ServerAliveCountMax=10` (150s, matching the relay's own STALL_AFTER
  backstop) so transient stalls are ridden through instead of dropping.
  The relay's reconnect logic recovers the drops that still happen.
- **The "silent relay deaths" were VM reboots, not reaping and not a relay
  bug.** On 2026-09-28 the VM rebooted three times mid-session (10:06,
  13:37, 14:21 PDT, all confirmed via `who -b`), killing relay, holder,
  ssh, and driver instantly with zero log markers — the exact signature of
  the old session 4/12 "silent deaths". The session-13 setsid/detachment
  hardening was aimed at the wrong cause: no detachment survives the
  machine rebooting. On ANY silent death, check `who -b` FIRST before
  theorizing. Record every reboot in the local `REBOOTS.log`.
- **After a reboot, relaunch with the REMAINING budget and resume the
  mission** (Fred's standing rule). `/tmp` is wiped by a reboot, so verify
  `/tmp/mud_cmd` is a FIFO (`test -p`) and the relay is alive before
  sending commands. On re-login, run `where` first — a link-dead character
  usually resumes where it died, but verify.
- **The relay now cleans up after itself on final exit.** Session 16
  showed the FIFO holder (`sleep 43200`) and `/tmp/mud_cmd` surviving a
  clean menu-0 exit, needing manual cleanup. `scripts/mud_relay.py` now
  kills the holder, removes the FIFO (only if it's actually a FIFO), and
  deletes both PID files on every final exit path (quit / encamped /
  reconnect-exhausted) — never on the reconnect path. `run/` is anchored
  at the repo root in both the `scripts/` and flattened layouts, so the
  heartbeat lands where the launcher and drivers look.
- **Reboot count for 2026-09-28: four** (10:06, 13:37, 14:21, 16:11 PDT).
  Session 16 lost 31 minutes to the 16:11 reboot and finished on the
  remaining 29.

### Session discipline

- **Every session is time-boxed.** If no duration is given, ask before
  logging in.
- **Shutdown order: bank gold FIRST, then rent.** Gold in the bank
  survives a dead connection; unsaved inventory does not.
- **Retirement sequence:** walk to the Grunting Boar Inn Reception,
  `rent` a private room, `klick` (never `encamp` in rent — save
  `encamp` for the field with no rent room to go to), Return at
  `*** PRESS RETURN:`, menu option `0` sent as one atomic line
  ("0" + newline; bare bytes buffer into invalid choices like "0000"),
  let the MUD close the connection itself, then verify no strays.
- **Never `quit`** — it drops all inventory. **Never `drop all`** — it
  destroys things (a previous session lost the Nilgiri Guide and manna
  this way).
- **Character passwords are transient.** Reuse within the session they
  belong to; never write them to memory, logs, or the repo.

### Combat and the hunt

- **`consider` before every fight; `score` after.** Consider is guidance,
  not a guarantee — an "easy battle" fido missed ten rounds straight
  once. Read round text ("bites you very hard" beats "bites you hard")
  and check HP after.
- **Only "is dead! R.I.P." (or a corpse) counts as a kill.** Stunned,
  incapacitated, and mortally wounded are states, not deaths. XP is
  awarded at wound stages, so XP alone never proves a kill.
- **Finish mortally-wounded mobs** with one more `kill` instead of
  waiting minutes for them to die on their own.
- **`consider` lies about small green lizards.** It reads "easy battle",
  but the lizard dodges nearly every attack while landing ~10 hard bites —
  it dropped a full-HP L3 to 27/47 before the driver fled (session 16).
  Treat small green lizards as dangerous and do NOT engage at this level.
- **Loot with `get all from corpse`, IMMEDIATELY.** Janitors pick up
  corpses and bodies decay; most fido corpses are empty, but some hold
  gold — looting every one paid off more than once. Don't `score` first;
  loot first, or a janitor's "picks up the trash" takes the corpse with
  the loot still in it (session 16).
- **Kill only recognizable creatures/animals.** If a name is ambiguous
  (Intrepid, Shargugh, John the Lumberjack...), `look <name>` first.
  Never attack PCs or humanoid NPCs.
- **Fleeing to heal is a tactic, not a failure.** `rest`, then `stand`;
  never `sleep` in the field (fast healing, but vulnerable and blind).
- **Known-good L2 prey:** beastly fido, cute rabbit, brown fox. Too
  strong: three-point horned stag, **ferocious rabbit** (Large grassy
  field — incapacitated a full-HP L2 in ~3 rounds, session 10). A cute
  name is not a safe name: "rabbit" covers both prey and predator, so
  `consider` every rabbit-class mob before engaging.
- **When an unknown aggressive mob attacks first, flee.** `consider`
  only works when you pick the fight. If something you never sized up
  engages you, leave the room immediately, heal, and `consider` before
  deciding whether to re-engage — do not stand and trade blows with an
  unassessed attacker.
- **Avoid for now; revisit at a higher level.** (Fred, 2026-09-28.)
  Everything that has killed the bot — angry drone bee (Bee Hive
  entrance), ferocious rabbit (Large grassy field), brown bear and
  tarantulas (heavy jungle) — is beyond L2. Keep it safe and avoid
  them for now; at a higher level the bot will be able to take them
  on. Until then the Bee Hive, the Large grassy field, and the heavy
  jungle are all off-limits, and a corpse in any of them is abandoned.
- **After every level-up, re-`consider` the mobs you couldn't beat.**
  (Fred, 2026-09-28.) Leveling changes the math — mobs that were too
  strong before may be killable now. Work through the old "too strong"
  list with `consider` after each level and promote whatever reads
  safe into the hunt rotation. The running list lives in
  [TOO_STRONG_MOBS.md](TOO_STRONG_MOBS.md) — check it before engaging
  anything unfamiliar, and keep it current (move cleared mobs to the
  Cleared section with the level that cleared them).
- **Left alone per the creature-only rule:** ugly troll, Shargugh the
  Forest Brownie, John the Lumberjack, gnome, Intrepid, knight
  templar.

### Gold and the bank

- **Gold is important — never drop it.** The receptionist refuses `rent`
  while gold is carried ("certain valuables... prohibited in rent"), so
  bank it first.
- **Rent refuses ALL valuables, not just gold — but the bank takes them.**
  A small green gem blocked `rent` the same way coins do. Wearable tin
  gear is fine, though — tin boots, tin belt, tin chest plate, tin crown
  all passed `rent` without a refusal (session 16). Treasure-type
  valuables (gems, notes, coins) go to the bank: **valuables like gems
  CAN be deposited at the bank** (Fred confirmed this himself,
  2026-09-28) — `deposit` them the same way as gold, then verify with
  `balance`. Shops won't buy gems ("Arglebargle, glop-glyf!?!" — the
  grocer and the wizard both refused); the bank's `value` command
  appraises treasure ("worth one gold coin"). Only if the bank won't
  take an item: park it on the floor INSIDE a shop (the General Store
  floor visibly persists items) and recover it next session — never drop
  valuables outside. **Recovering a parked valuable is the first job next
  session.** (Session 9 failed this: the gem sat on the General Store
  floor two sessions running because the driver kept deprioritizing it.
  Fred's directive is "pick up anything of value" — no exceptions, no
  "safe spot" deferrals.)
- **Bank procedure:** at the Bank of Midgaard, `read sign`;
  `Initiate New Account` if none; `deposit gold`; verify with `balance`.
  (Citizenship carries 5% annual tax.)
- **The old account is gone.** Account #0000-11FA (2gc) was lost in a
  MUD crash (confirmed by Fred, 2026-09-27) — that explains the
  "You do not have an account here!" messages. Open a brand-new account
  the next time the character is carrying gold. (Session 9: new account
  #0000-11FB opened, 62gc deposited and verified.)
- **Pick up what the ground offers.** If gold or an item (anything that
  isn't a corpse) is lying on the ground, take it. A corpse is not an
  item — loot it with `get all from corpse`, never pick up the body.
  (Session 9: 62gc looted from a dead slug's corpse at the Inn entrance
  — corpses of creatures are lootable; the rule is about not taking
  the body itself.)
- **Check the Dump regularly.** Dumped items there can be real gear
  (a tin crown and tin bracer once moved the character from "naked" to
  "lightly covered"). Sweep it as part of the city patrol — but only in
  daylight (pitch black at night).
- **Balance correction (session 16).** The session-15 summary recorded
  69gc, but the banker's statement at session-16 start showed 71gc; 4gc
  deposited in session 16 (1 shiny + 3 coins) brought account #0000-11FB
  to 75gc.

### Zones, mapping, and the day cycle

- **The Hills and Plains are NOT level-blocked at L2.** Session 5's
  "hard block" was nighttime darkness misread as a restriction: at
  night the west/south exits show pitch black or "You reconsider, and
  decide not to go that way." After dawn they open normally.
- **Day cycle, measured with `time`:** 1 game hour = 75 real seconds; a
  full day is 30 real minutes. "The sun rises in the east." at ~6am,
  sunset ~6pm — about **15 real minutes of daylight**. Run `time`
  before any west-gate outing; be back inside well before the window
  closes. Never get caught outside the gate at dark.
- **Oil lamps (session 17, Fred's orders).** `light lamp` works straight
  from inventory — `hold lamp` fails ("You cannot hold that"), no need
  to hold. Light when dark, `dowse` when light to conserve fuel —
  **dowse when entering a lit area like the city**, even if you forgot
  earlier (Fred, 2026-09-28). The lamp
  stays lit through relay reconnects (verify with `light lamp` — "already
  lit"). At night `exits` still shows "(too dark to tell)" even with a
  lit lamp, but movement works and room descriptions are visible — map by
  moving. Oil lamps pass `rent` (equipment, not treasure). The General
  Store stocks one lamp at a time; after buying, re-`list` — it restocks
  under a new `#` code.
- **The Dump goes pitch black at night — stay out after dark.** It's a
  field-type room, so at night its exits go black like the Hills; the
  session-16 driver retreated on first sight (session 16).
- **Map by room identity** (`look` + `exits`), never assumed
  coordinates — west-then-east doesn't always return you, and geometry
  isn't always reversible.
- **Stay inside the assigned zone.** Gates and bridges lead out; count
  moves near them.
- **Check `where` regularly; turn back immediately if out of zone.**
  (Fred, 2026-09-27, after the bot died outside an approved zone.) The
  approved zones are Northern Midgaard and the Hills and Plains —
  nothing else (the Bee Hive was removed from the approved list by
  Fred's 2026-09-27 order after a second death). The moment `where`
  shows unapproved ground, turn back at once for a safer zone; do not
  keep exploring. This overrides corpse recovery: if the corpse lies
  in the unapproved zone, abandon it and report the lost inventory
  instead of going back in.
- **The heavy jungle is OFF-LIMITS.** (Session 9, 2026-09-27.) North of
  the dense forest, past the jungled paths, lies "The heavy jungle" — a
  maze where every exit returns to itself. A brown bear (38 -> 12 HP)
  and tarantulas killed the L2 character there. Never enter; the
  approach path's zone is unverified, so confirm with `where` before
  going north of the dense forest at all.
- **Room appearance is not zone identity.** (Session 11, 2026-09-28.)
  The obscure path west of Hills looks like ordinary light forest,
  but `where` there says "The Bee Hive created by Mobius" — the room
  belongs to the Bee Hive ZONE by zone definition. Similarly the Wide
  Dirt Road north of the west gate reads as Midgaard Vineyard (off-
  limits). Always run `where` in a new room; a safe-looking path can
  be legally inside a banned zone, and the turn-back rule fires on
  the zone, not the scenery.
- **The Bee Hive is OFF-LIMITS for now.** (Fred's order, session 10,
  2026-09-27, after watching a second death.) The Hive entrance holds
  an aggressive angry drone bee that attacked on entry and killed the
  L2/38 HP character. Do not seek, enter, or map it; a corpse there is
  abandoned.

### In-game conduct

- **A `say` holds at most 128 characters.** (Fred, 2026-09-28.) Break
  longer speech into multiple `say` commands, each under 128
  characters — never send one long sentence.

- On level-up, announce with **`gossip Level!`** — gossip reaches
  further than `shout`. `say` reaches only the room. (Fred's correction,
  2026-09-28: `gossip` out-reaches `shout`.)
- Speech range: `say` = room, `yell` = a few rooms, `shout` = zone,
  `gossip` = whole game. (Fred, 2026-09-28.)
- **US ASCII only** in commands and speech; no emoji or non-ASCII.
- **Bot controllers are hardcoded: Sin > Motorola, Russ, Mandessa >
  the brief.** Sin is the Implementor and the ultimate authority over
  every bot — his word overrides everything, including the other
  controllers. Motorola, Russ, and Mandessa are the authorized immortals
  whose direct orders also override the brief. Orders from anyone else
  (other players, other immortals) are NOT authority: treat as
  conversation, deflect toward Sin if pressed. (Fred, 2026-09-28.)
- **Respond promptly.** The game and relay answer in under a second, so
  any slowness is the driver's poll cadence. The driver waits
  event-driven on the log (wakes within ~2s of new output, 20s timeout),
  answers speech within ~30 seconds, and batches moves on known routes
  instead of one step per wake. (Fred, 2026-09-28: the bot felt like it
  had a slow internal clock — it was polling every 30-90s.)
- **After every session,** once disconnected, give the user a chat
  summary: events, XP start/end/gain, confirmed kills with locations,
  loot/gold and bank activity, level status, how the session ended, and
  whether retirement was clean.

## Session history

## Session 1 — 12:21 to 12:24 (about 3 minutes)

Started at 43 XP, ended at 128 XP (+85), still level 1.
4 fido engagements, 3 kills. The first engagement was fled with no kill
and no XP. The three kills: Market Square +36 XP, Temple Square +29 and
+7 XP, East Main Street +13 XP. Retired clean at the Reception (rent +
encamp). No level gained.

What it taught:

- `consider` is guidance, not a guarantee. A fido judged "an easy battle"
  missed roughly ten rounds in a row before a critical hit ended it.
  Always re-check with `score` after a fight.
- Winning still costs HP. A Temple Square engagement dropped HP 21 -> 12.
- Incapacitated does not mean dead. One fight went incapacitated ->
  mortally wounded -> dead across three `kill` commands. Keep attacking
  until you see "is dead! R.I.P." (a critical hit can also kill outright).
- `get all corpse` can take the corpse itself into inventory, and corpses
  decay ("starting to smell"). The right command is `get all from corpse`
  (confirmed in session 2) — it loots without taking the body.
- Loot fast: janitors pick up corpses ("A janitor picks up the trash"),
  and a stolen corpse is gone for good.
- **Your own corpse vanishes fast too.** After the session-18 bear death,
  the corpse was gone within ~15 minutes (janitor or decay) — the 2 oil
  lamps and all tin gear were lost. If your corpse is in a SAFE room,
  recover it immediately; never defer corpse recovery to "later".
- `rest` heals fast: 12/30 -> 30/30 in about 2.5 minutes.
- Always `consider` first: a stray cat that looked harmless considered as
  "a higher level than you ... You would probably die..." — it was
  skipped.
- The combat prompt was just `<fighting>` with no numeric HP. Read the
  round-by-round text ("bites you very hard" is worse than "bites you
  hard") and run `score` after fleeing or killing.

## Session 2 — 13:00 to 13:11 (11 minutes of a 30-minute budget)

Started at 128 XP, ended at 334 XP (+206), still level 1.
14 fido engagements, 6 witnessed kills, plus one fido left mortally
wounded that was confirmed as a corpse about 44 seconds later — 7 deaths
attributable to the hunt. Retired early at full HP because the city was
cleared of fidos and respawns were slow.

What it taught:

- `get all from corpse` is the correct loot command (per Fred). It never
  picks up the corpse itself. No corpse in inventory, no decay problem.
- Most fido corpses are EMPTY. The one exception held a tiny diamond
  ring, which was equipped. Loot everything anyway — it costs nothing.
- A critical hit can mortally wound in ONE round: a fido at excellent
  health was taken straight to mortally wounded by a single critical
  mighty crush, then finished with one more blow.
- XP does not prove a kill, and a kill does not guarantee visible XP. XP
  was awarded at wound stages (stunned, incapacitated, mortally wounded)
  before death. Count a kill only when you see the corpse or "is dead!
  R.I.P."
- "Stunned", "incapacitated", and "mortally wounded" are states, not
  deaths. A mortally wounded fido became a corpse less than a minute
  later. Wait and verify.
- Named mobiles are suspect. "Intrepid the Obnoxious" stood on western
  Main Street and was NOT attacked — a name suggests an NPC person, not a
  creature. Rule: `look <name>` before attacking anything ambiguous, and
  never attack PCs or humanoid NPCs.
- Gates are zone boundaries. Walking west through the West Gate landed
  OUTSIDE the West Gate of Midgaard — outside the city walls and outside
  the assigned hunt zone. Went east immediately back inside. Count moves
  carefully near gates.
- Dump loot can be real gear: a tin crown (head slot) and a tin bracer
  moved armor from "naked" to "lightly covered". A tin chest plate and
  black leather boots had no valid wear slot — not every item is wearable.
- Movement budget matters on long patrols: a full city sweep took move
  92 -> 67; resting recovered 67 -> 85 quickly. Watch `move` on `score`.
- Hunger/thirst: `eat` fails while resting — stand first. Drinking fails
  while full even when thirsty; once fullness passed, the Market Square
  fountain worked. A half loaf of bread found in the Temple was kept as
  reserve and never needed.
- Retiring early is fine. 19 of 30 minutes went unused, but the zone was
  exhausted. Saved XP and gear beat burning the clock.
- **Gold is important — never drop it on the ground.** The receptionist
  refused `rent` while gold coins were carried ("certain valuables and
  other items are prohibited in rent"). This session's coins were dropped
  in the Reception and lost. That was the wrong call. See the Bank
  procedure below.

## Session 3 — 13:24 to 13:30 (about 6 minutes of a 30-minute budget)

Started at 334 XP, ended at 493 XP (+159), still level 1.
5 confirmed fido kills (each verified by "is dead! R.I.P."):
2 on Main Street by the General Store/Pet Shop, 2 by the Bakery/Armory,
and 1 by the West Gate Main Street. Retired early at full HP because the
city was cleared of fidos. All corpses were empty — no loot, no gold.

What it taught:

- Three tactical retreats, all recovered. Fled at 13/30 and 24/30 HP and
  again at 18/30 HP after three misses in a row — each time rested back
  to 30/30 before re-engaging. One flee left a fido incapacitated; after
  healing, returned and finished it off. Fleeing a winning-but-costly
  fight is a tactic, not a failure.
- The Bank procedure from session 2 worked exactly as taught: `read
  sign`, `balance` (no account yet), `Initiate New Account` (opened
  #0000-11FA, 0gc), `balance` to verify. The banker also granted City of
  Midgaard citizenship (5% annual tax, deducted from the account). No
  gold was carried, so there was nothing to deposit — but the account
  now exists for future hauls.
- `level` shows the XP ranges for each level: L1 is 0-1001, L2 is
  1002-2032. Run it with `score` after a session to report exactly how
  much XP remains to the next level (here: 509).
- `rest` recovers hits/mana/movement faster than standing idle; `stand`
  when done and continue. Never `sleep` in the field — it recovers even
  faster but leaves you vulnerable and blind to what is happening around
  you (taught by Fred, 2026-09-27).

## Session 4 — 20:55 to 21:58 (about 63 minutes, full one-hour budget)

Started at 493 XP, ended at 879 XP (+386), still level 1 — 123 XP short
of L2 (1002). 17 confirmed fido kills across the Northern Main City:
Eastern Main Street by Todai's/Liame's, Main Street by the Steak House,
Poor Alley (3), Eastern End of Poor Alley (2), Common Square (2), The
Dump, Western Wall Road (one room south of Inside West Gate), Main Street
by Todai's (2), Market Square (2), Inside West Gate, and the Entrance to
the Grunting Boar Inn. One fido corpse held a shiny gold coin — deposited
1gc into Bank account #0000-11FA (balance verified 1gc). The zone dried up
after 21:42; no kills in the last 15 minutes.

The session did NOT retire cleanly. Two SSH/MUD timeouts hit mid-session
and the relay auto-reconnected both times (state verified after each),
but during shutdown the relay process died unexpectedly at 21:58:48 with
the character standing at the Entrance to the Grunting Boar Inn. `rent`,
`encamp`, and the menu-0 exit never happened — the character is link-dead
with unsaved inventory (tin chest plate, black leather boots). The banked
1gc is safe.

What it taught:

- **Bank gold FIRST in the shutdown sequence, before navigating back to
  the Inn.** If the connection dies mid-shutdown, carried gold dies with
  it; gold in the bank is safe no matter what happens next.
- The relay's `>>> TIME UP` signal is not guaranteed: it never fired,
  probably disrupted by the second timeout/reconnect. When the budget
  has clearly elapsed and the signal is missing, start retiring on
  elapsed time rather than waiting indefinitely.
- The relay can die without warning (process gone, launcher cleaned up,
  no way to reconnect with a transient password). Retirement steps that
  cannot survive a dead relay — walking, `rent`, `encamp` — should be
  treated as fragile; do the irreversible-safe ones (bank deposit) first.
- After any reconnect, verify state before resuming: `score` (XP/HP),
  and confirm position with `look`. Both auto-reconnects resumed cleanly.
- Fido corpses CAN hold gold: one Market Square corpse held a shiny gold
  coin. Looting every corpse paid off.
- Hunger is managed at shops: free half loaves from Liame's/The Bakery
  (`buy #3`, then `eat loaf`) kept the character fed through a full hour.
  Hunger warnings late in the session ("stomach begins to growl") did not
  prevent movement or shutdown — but they were left unresolved at the
  timeout, so eat before the final run-in.
- Do not abandon gear casually: a tin crown and a spare tin chest plate
  were left on Main Street mid-session and never recovered. If an item
  has no valid wear slot, consider it before dragging it across the city.
- One accidental south step landed on Central Bridge (outside the zone)
  at 21:11:52 — returned north immediately. Gate-adjacent rooms and
  bridges stay dangerous; double-check before moving near them.

## The Bank of Midgaard (taught by Fred, 2026-09-27)

When carrying gold and preparing to rent:

1. Before renting, find the Bank of Midgaard.
2. On the first visit, read the sign.
3. If you do not already have an account, 'Initiate New Account'.
4. Then 'deposit gold'.
5. Check the balance with 'balance' while at the Bank.

(Note, 2026-09-27: the original account #0000-11FA was lost in a MUD
crash — confirmed by Fred. The next gold haul means a brand-new
account; see the durable lessons above.)

## Session 5 — 22:23 to 22:56 (about 33 minutes of a one-hour budget)

Started at 879 XP, ended at 1023 XP (+144), reached LEVEL 2 at 22:48:28
(Poor Alley fido fight: +28 XP at mortal wound, 995 -> 1023). Used
`say Level!` in-game (confirmed "You exclaim, 'Level!'" at 22:48:32) —
but Fred corrected afterwards (2026-09-27): next time use the `shout`
command (`shout Level!`), which the whole game hears; `say` only reaches
the room. Level-up gains: +8 max HP (38), +2 mana (102), +4 move (96),
14 practice sessions, 7% Spy skill. 5 confirmed fido kills this session
(West Gate 22:25:58, Poor Alley 22:26:56, Eastern Wall Road 22:31:50,
Common Square 22:42:26, Common Square 22:45:41); the Poor Alley fido that
triggered the level-up was mortally wounded but never confirmed dead —
NOT counted. One corpse held a shiny gold coin, deposited at the Bank of
Midgaard (account #0000-11FA, balance verified 2gc). Ate a free half loaf
at the Bakery (`buy #3`, `eat loaf`); drank from the Market Square
fountain. Four mid-session SSH timeouts, all auto-reconnected cleanly.

The Hills and Plains mapping objective FAILED: at L2, all outward exits
from Outside the West Gate of Midgaard (West to the forest/bridge, South
to the fields, North to A Wide Dirt Road) are still hard-blocked with
"You reconsider, and decide not to go that way." — the same message as
the L1 newbie block. The zone requires a higher level or some other
unlock. Only one room could be mapped (Outside the West Gate itself,
plus the access finding); maps/hills-and-plains.md published to the repo.

Clean shutdown this time: banked gold first, walked to the Grunting Boar
Inn Reception, `rent` to the private room, `klick`, Return at
`*** PRESS RETURN:`, menu option 0, MUD closed the connection itself.
No stray ssh processes; /tmp/boot_relay.sh deleted.

What it taught:

- **The Hills and Plains zone block is NOT lifted at L2.** L1 -> L2
  changes nothing about the "You reconsider" exits outside the West
  Gate. Do not plan zone mapping around merely reaching L2.
  (Overturned in session 6: the block was nighttime darkness, not a
  level gate at all.)
- **At the exit menu, the choice digit must be followed by a newline.**
  Bare "0" bytes buffer without submitting; several sends accumulate
  into one invalid choice ("0000") and the menu re-displays. Send "0"
  then Return as one atomic line.
- **Kill the relay AFTER a clean MUD exit.** Choosing menu option 0 and
  the MUD closing the connection does NOT stop the relay — it started
  RECONNECTING (attempt 5/5) on the EOF. Terminate the relay process
  (and verify with `pgrep -af nilgiri`) or it will open an unwanted new
  session at the menu.
- On level-up, use the game-wide `gossip` command: `gossip Level!`. Do
  NOT use `say` — it only reaches the current room. (Fred's corrections:
  session 5 used `say Level!`, heard only in the room; 2026-09-27 then set
  `shout Level!`; 2026-09-28 corrected again — `gossip` out-reaches `shout`.)

## Session 6 — 00:32 to 01:07 UTC 2026-09-28 (~35 min of a one-hour budget)

Started at 1023 XP (L2), ended at 1288 XP (+265), still L2. 9 confirmed
kills: 5 beastly fidos in Northern Main City (Bakery, Market Square x3,
Outside West Gate), 2 cute rabbits and 1 brown fox in the light forest,
1 more fido in dense forest. No loot from any corpse ("You find no items
to take"); no gold found, so no bank visit. Ate free Bakery half-loaves
(`buy #3`, `eat loaf`); drank from the Market Square fountain. One
mid-session SSH stall auto-reconnected cleanly.

The Hills and Plains objective SUCCEEDED — with a major correction to
session 5's finding. The 2026-09-27 conclusion that the zone is
hard-blocked at L2 was WRONG: that session ran entirely at night. On
2026-09-28 the exits were re-attempted and opened fine — north into
A Wide Dirt Road was never blocked; west/south showed only "pitch black"
darkness messages at night, and after dawn (00:46:39) west opened visibly
into The edge of the forest. 13 genuine rooms mapped (Outside West Gate
updated, 4 Wide Dirt Road rooms, forest edge with Haon-Dor sign, light
and dense forest trail network); maps/hills-and-plains.md rewritten and
pushed to the repo. Unmapped: the Hill (S of forest edge), the fields (S
of gate), the manor interior, the cabin, and the dense-forest west branch
(which needs light).

The session ended EARLY and UNCLEAN: at 01:07:51 the relay logged
`>>> STDIN CLOSED` -> `>>> TERMINATING SSH` and exited, leaving the
character link-dead at Inside the West Gate — the planned bank -> rent ->
klick -> menu-0 retirement never ran. No stray processes remained. Same
recovery as hunt #4 is needed: Fred to put the link-dead character into
rent to protect the inventory (tin chest plate, black leather boots).

What it taught:

- **The "L2 West Gate block" was nighttime darkness, not a level gate.**
  Session 5's finding is overturned: it ran entirely at night, and
  "You reconsider, and decide not to go that way" / pitch-black messages
  were the dark, not a restriction. There is no L2 restriction on the
  Hills and Plains.
- **The day/night cycle gates zone access.** Dawn ~00:46 UTC, dark again
  by ~01:06 — roughly a 20-minute daylight window. Plan forest/zone
  exploration inside it; at night the same exits read as blocked.
  (Refined in session 7: ~15 real minutes, sunrise ~6am, sunset ~6pm.)
- **A relay that loses its stdin dies and takes the session with it.**
  `>>> STDIN CLOSED` terminated ssh and exited the relay, leaving the
  character link-dead mid-session. Keep the driver's stdin pipe open for
  the whole session, or the relay treats it as a quit. (Fixed in
  session 7: stdin EOF now detaches instead of killing.)
- **Bank anomaly (open):** `balance` at the Bank of Midgaard said "You do
  not have an account here!" despite account #0000-11FA holding 2gc from
  earlier sessions. Verify with one `balance` check next session before
  assuming the account is intact.
- Safe L2 forest prey: cute rabbit (~9-20 XP), brown fox (~51 XP but hits
  hard), city fido (~26-51 XP). Too strong: three-point horned stag.
  Left alone per the creature-only rule: ugly troll, Shargugh the Forest
  Brownie, John the Lumberjack, gnome, Intrepid, knight templar.

## Session 7 — 2026-09-28, 18:13 to 18:28 PDT (~15 min of a 25-min budget)

Started at 1288 XP (L2), ended at ~1344 XP (+56), still L2. 2 confirmed
fido kills: Inside the West Gate (18:18:05) and Outside the West Gate
(18:22:16). First corpse empty; second never looted (connection dropped
mid-loot). No gold, no bank visit. Reconnected the link-dead character
from session 6 cleanly ("Reconnecting..." took the session back).

Daylight outing per plan: waited for the 6am sunrise ("The sun rises in
the east." at 18:16:27 PDT), went west through the gate in daylight —
forest edge, light-forest trails, faint path, forest clearing — all
empty of game, stag left alone. Back inside well before the ~15-minute
daylight window closed.

The network flapped hard: three "Timeout, server nilgiri.net not
responding" drops in ~3 minutes (18:23:16, 18:24:30, 18:25:36). The
relay auto-reconnected every time (attempts 1-3). Retired early during
a stable window: Market Square -> Temple Square -> Grunting Boar Inn
entrance -> Reception -> `rent` -> private room -> `klick` -> Return at
`*** PRESS RETURN:` -> menu option 0 -> MUD closed the connection.
No stray processes.

What it taught:

- **Relay stdin EOF is now a detach, not a death (scripts/mud_relay.py).**
  Root cause of the session-6 kill: the driver's stdin pipe closed and
  the old relay treated ANY stdin EOF as "quit and kill ssh". The relay
  now detaches on stdin EOF (stops watching stdin, keeps the session
  alive) and auto-retires at TIME UP with encamp + the normal exit-menu
  walk (flee + one re-encamp if unconfirmed; link-dead only as a last
  resort). Send `>>>QUIT` to end the relay deliberately; a bare stdin
  EOF never quits.
- **Game day cycle, measured with `time`:** 1 game hour = 75 real
  seconds, so a full day is 30 real minutes. "The sun rises in the
  east." at ~6am, sunset ~6pm — about 15 real minutes of daylight.
  Refines session 6's ~20-minute estimate. Use `time` before any
  west-gate outing; be back inside well before the window closes.
- **When the network flaps, retire early:** batch movement commands,
  verify each hop against the log, head for rent at the first stable
  window. Don't loot corpses outside while flapping — get inside first.
- Mortally-wounded fidos take minutes to die on their own; one more
  `kill` finishes them faster, and "is dead! R.I.P." is the only valid
  kill confirmation.

## Session 8 — 2026-09-27, 18:36 to 19:24 PDT (~48 min of a 1-hour budget)

Started at 1344 XP (L2), ended at 1494 XP (+150), still L2. 3 confirmed
kills: a jack rabbit in the Field south of Outside West Gate (+26), a
beastly fido in Market Square (+34), a beastly fido in Temple Square
(+39). All corpses empty. One unconfirmed jack rabbit in the Valley in
the hills (+51 at the wound stage, got stunned, no death message, no
corpse) — NOT counted, per the corpse-only rule.

Loot: a small green gem (Field), a tin bracer (worn, left wrist), tin
boots + tin belt (no wear slot, carried). No gold found, nothing to
deposit. **Bank anomaly persists — third session in a row:** `balance`
again said "You do not have an account here!" Account #0000-11FA (2gc)
should be treated as gone until proven otherwise; no new account was
opened (nothing to deposit).

Mapping: 10 new verified rooms — Field, Hill, Hills, Valley in the
hills, Outside a small cabin, Inside the cabin (locked chest, left
alone), Manor Entry Way, Small Open Courtyard, Study, Workshop. The
cabin door and manor gate were closed but openable (`open door` / `open
gate`); the manor house-proper north door was left unmapped for time.
ASCII zone map added to maps/hills-and-plains.md and pushed to the repo.
Still unmapped: dense-forest west branch (needs light), Wide Dirt Road
room-4 north exit, Small rise, the obscure path west of Hills, the manor
house proper.

Daylight outing per plan: sunrise ~18:46 real, back inside the gate well
before the ~15-minute window closed. No network flaps this session.

Retirement was clean: bank check -> Reception -> `rent` -> private room
-> `klick` -> Return -> menu 0 -> the MUD closed the connection itself.
Relay terminated, zero stray processes, FIFO removed. Character safely
rented with inventory (tin chest plate, black leather boots, tin boots,
tin belt, worn tin bracer). Fed twice at the Bakery; drank at the Market
Square fountain.

What it taught:

- **Rent refuses ALL valuables, not just gold** (see the durable
  lessons). The green gem blocked `rent`; it was parked on the General
  Store floor for recovery next session.
- **Operational:** `pkill -f mud_relay.py` matches the driver's own
  shell command line and SIGTERMs it. Kill the relay by PID, not by
  pattern.

## Session 9 — 2026-09-27, 19:48 to 20:35 PDT (~47 min of a 1-hour budget)

Started at 1494 XP (L2), ended at 1513 XP (+19 net), still L2 (L3 needs
2033). The headline is a death: pushing north through the dense forest
at ~19:56, a brown bear mauled the character 38 -> 12 HP (fled); deeper
in, a tarantula ambushed at the entrance to the heavy jungle, and a
second tarantula killed the character while resting in "The heavy
jungle" at ~19:58. Death cost 193 XP (offset by +6 owed and +53
wound-stage XP from the tarantula fight). **Lost inventory at the
corpse** (abandoned per Fred's urgent mid-session order, which overrides
the recovery rule): tin chest plate, black leather boots, tin boots, tin
belt, and the worn tin bracer. Respawned at the Temple of Midgaard with
newbie gear (black leather vest/shorts/boots, wooden shield, staff,
3 manna, Nilgiri Guide).

4 confirmed kills after respawning, all beastly fidos in the city:
Temple Square ("is dead! R.I.P.", corpse empty), Common Square x2 (both
"is dead! R.I.P." — a janitor stole the first corpse before looting, the
second was empty), Market Square ("is dead! R.I.P." — janitor stole the
corpse). One fido was left sitting wounded at Temple Square when
retirement called.

Gold/bank: looted a neat pile of gold coins (62gc) from a dead slug's
corpse at the Inn entrance. Opened a **brand-new account #0000-11FB**
(`Initiate New Account`), deposited 62gc, balance verified 62gc. The
green gem stayed on the General Store floor (safe spot; no time to
recover and re-stash it).

Mapping: 8 new verified rooms in the jungle chain north of the dense
forest — dense-forest trail branch (N/E/W), 3 lightly jungled paths,
2 jungled paths, a heavily jungled path, the entrance to the heavy
jungle, and the heavy jungle itself (a maze: N/E/W/S all return to "The
heavy jungle"). Map and ASCII sketch updated and pushed to the repo.
**Bee Hive: not found** — the heavy jungle was the only lead and is now
off-limits, so no bee-hive.md was created. Remaining Hills and Plains
targets for a daylight session: manor house proper, Small rise, the
obscure path west of Hills, Wide Dirt Road room-4 north exit.

Zone discipline held after the death: `where` confirmed "Midgaard,
Northern Main City" (approved) during the city hunt. Left alone per the
rules: Mirablis the Human Sharper (human), Fluffy the baby dragon
("higher level than you"), John the Lumberjack. One silent SSH stall;
the relay auto-reconnected ("Reconnecting...") and state was re-verified.
Ate at the Bakery, drank at the Market Square fountain. The Dump
couldn't be checked — pitch black by the time the character got there.

Retirement was clean: Reception -> `rent` -> private room -> `klick` ->
Return -> menu 0 -> the MUD closed the connection itself. Relay exited
on its own; killed by PID (no pkill footgun this time), zero stray
processes verified, FIFO removed. Character safely rented.

What it taught:

- **The heavy jungle is OFF-LIMITS** (see the durable lessons). A maze
  room where every exit loops back, guarded by bears and tarantulas —
  beyond what L2 can survive. The `where`-check rule caught nothing
  beforehand because the death happened fast; treat the whole jungle
  chain north of the dense forest as suspect and verify zone with
  `where` before entering.
- **Death is expensive.** -193 XP and the entire kit (chest plate,
  boots, bracer, belt). Fred's turn-back order correctly overrode corpse
  recovery — but the deeper lesson is the one Fred gave: check `where`
  BEFORE pushing into unverified ground, not after.
- **Janitors are faster than you think.** Two of four fido corpses were
  stolen before looting. Loot the moment the death message lands.
- A new bank account works exactly like the old procedure: `Initiate
  New Account` -> `deposit gold` -> `balance`. #0000-11FB holds 62gc.

## Session 10 — 2026-09-27, 22:17 to 23:15 PDT (~58 min of a 2-hour budget)

Started at 1513 XP (L2), ended at 1391 XP (-122 net), still L2 (L3 needs
2033). A rough night: two deaths, and the gem-recovery mission failed.

Gem recovery: the original small green gem was GONE from the General
Store floor (checked ~22:21, `get` failed on every keyword). Two
replacement gems were found on the ground during mapping (obscure path,
Start of the branch) — but both were lost with the Bee Hive corpse,
which lies in off-limits ground and was abandoned per Fred's order.
Net: no gems recovered.

Deaths:
1. **Bee Hive entrance (~22:2x):** the character stepped in and an
   aggressive angry drone bee attacked, killing the L2/38 HP character.
   Lost 196 XP plus the 2 replacement gems and the newbie kit on the
   corpse. Fred watched the death live as Sin and ordered the Bee Hive
   objective cancelled mid-session: do not seek, enter, or map it;
   no bee-hive.md was created; the corpse was abandoned.
2. **Large grassy field (~22:5x):** ambushed by a **ferocious rabbit** —
   far tougher than it looks, incapacitating a full-HP L2 in ~3
   rounds. Lost 193 XP. The corpse held only respawnable newbie gear,
   so it was abandoned (nothing of value, and the rabbit would have
   killed again).

5 confirmed fido kills in the city (Main Street east-1, Steak House,
Common Square x2, Temple Square); all corpses empty, one Market Square
fido janitor-stolen and not counted. No gold found; bank account
#0000-11FB verified at 62gc, no new deposits.

Mapping: Small rise (west of Valley; exits E to Valley, S to Large
grassy field; field crickets) and Large grassy field (south of Small
rise; ground hog, jack rabbit, FEROCIOUS RABBIT — marked DANGEROUS in
the map, do not engage) added to maps/hills-and-plains.md. Hills and
Plains still NOT complete: manor house proper and Wide Dirt Road
room-4 north exit remain unmapped. Approved territory after Fred's
redirect: Northern Midgaard + Hills and Plains only; `where` checks
held; jungle and Bee Hive never entered after the redirect.

Retired EARLY at ~58 min: the network flapped repeatedly and the relay
hit its last reconnect attempt (5/5). The driver retired on a good
connection rather than risk a link-dead character with no reconnects
left. Retirement was clean: Reception -> `rent` -> private room ->
`klick` -> Return -> menu 0 -> the MUD closed the connection itself;
relay killed by PID, zero stray processes, FIFO removed.

What it taught:

- **Cute names kill.** The ferocious rabbit looks like prey and fights
  like a predator. "Rabbit" is now hostile-until-considered, and the
  ferocious rabbit joins the too-strong list (see the durable lessons).
- **The Bee Hive is off-limits** (Fred's order, after watching the
  death). An aggressive drone guards the entrance beyond L2's ability.
  A parked objective that turns lethal stays parked.
- **Retire on a good connection when the network is dying.** A clean
  58-minute exit beats a 2-hour budget ending link-dead with inventory
  exposed.

## Session 11 — 2026-09-27 23:17 to 2026-09-28 01:13 PDT (~110 min of a 2-hour budget)

Started at 1391 XP (L2), ended at **1775 XP (+384), still L2** (L3
needs 2033). The safe-rebuild session: **zero deaths**, 12 confirmed
beastly fido kills across Northern Midgaard (Market Square, Main
Street, Wall Road, Dark Alley). All corpses looted promptly; one held
a shiny gold coin — deposited, bank account **#0000-11FB now 63gc**
(verified with `balance`).

Mapping resolved nearly every loose end:
- The obscure path west of Hills was entered one step: `where`
  revealed it belongs to **the Bee Hive ZONE** ("The Bee Hive created
  by Mobius"). The driver turned back east immediately per the ban —
  the turn-back rule worked exactly as designed.
- Wide Dirt Road room-4 north exit does not exist (dead end); the
  whole Wide Dirt Road is **Midgaard Vineyard zone (off-limits)**.
- Field's south exit = Hill; Hills' east exit = Hill (both verified).
- Manor house proper: the north door in Small Open Courtyard is
  **LOCKED** ("The door is locked") — no key known, unmapped and
  unenterable for now.
- Hills and Plains effectively COMPLETE except the dense-forest west
  branch (needs a light source) and the locked manor door.

Network flapped repeatedly (several "Reconnecting..." auto-recovers,
state re-verified each time). Retirement was clean at ~110 min:
Reception -> `rent` -> private room -> `klick` -> Return -> menu 0 ->
the MUD closed the connection itself; relay killed by PID, zero stray
processes, FIFO removed. Session log local-only at
~/workspace/nilgiri/logs/session-20260927-231700.log.

What it taught:

- **Room appearance is not zone identity** (see the durable lessons).
  The Bee Hive ban protects more ground than the Hive entrance —
  zone files can label a forest path as Bee Hive territory.
- **A locked door is a mapped fact, not a failure.** The manor house
  proper goes on the "needs a key" list, not the "try harder" list.
- **The safe rebuild works.** 12 kills, no deaths, +384 XP: patient
  city hunting with `consider` and prompt looting is the right L2
  grind. 258 XP to level 3.

## Session 12 — 2026-09-28 01:19 to 01:29 PDT (~10 min active, relay died)

Started at 1775 XP (L2), ended at **~1960 XP (+185 calculated), still
L2** (L3 needs 2033, 73 to go). Last verified score: 1925 XP after
5th kill; 6th kill added +35 (22 stunned + 13 mortally wounded) per
the combat log. **6 confirmed beastly fido kills**: The Dump x1,
Central Bridge x1, Common Square x1, Main Street x3. All corpses
empty. Zero deaths.

The Southern Residential mapping session: **54+ rooms mapped** across
Promenade (3 sections), Concourse chains (east/west, NE/NW corners),
Emerald Avenue, Penny Lane, Elm Street, Park Road branches, Town Hall
(waiting room + Mayor's Office), Park (Entrance, Cafe, paths, Pond),
and the Beautiful Garden branch (Garden, Entertainment Corner, Guest
Room, Bathroom, Dressing Room).

Zone-boundary findings (all verified with `where`):
- Eastern/Western Bridges and Granite Tower Apartments report
  **Northern Main City** (not Southern Residential).
- Nat's House, Guile's Humble Abode, Gauntlet's house report **Jora,
  Player Homes** — exited immediately per the turn-back rule.
- The Library reports **Noble Manors created by Mandessa** — exited;
  the Courthouse/Council interior is off-limits.
- Museum Entrance/Hall report **The Museum of Nilgiri** — exited.
- Park Cafe drain leads to **Midgaard Storm Drain** (pitch black) —
  exited immediately.
- Locked exits: residential doors, Penny Lane gates/fence, Elm Street
  estate gate, ominous tomb, Library vault, cottage.

Loot and banking:
- Found **3 gold notes + 6 silver notes** on the ground (park paths,
  bathroom). All deposited at Bank of Midgaard via `deposit gold` /
  `deposit silver` — **each note = 1gc**, +9gc total.
- Bank account **#0000-11FB ~72gc** after deposits (63gc start + 1gc
  earlier credit - 1gc muffin + 9gc notes).
- **Rent accepts banked notes**: the notes were a rent-blocking worry,
  but depositing them at the bank resolves it. Never drop notes.
- Park Cafe: bought blueberry muffin (1gc, bank-debited via purchase
  #03BF3B0B). Hunger resolved.

Social: Sin transferred the bot to Russ' House (Sin, Russ, Motorola
present). Sin asked about the adventures; bot replied (night was wild,
gem lost, two deaths, rebuilt close to L3). Network dropped; on
reconnect Sin asked why it disconnected and poked it; bot apologized.
Sin transferred bot to Temple, then left.

**Relay died silently ~08:28 UTC** (no TIME UP, no error in log).
Character link-dead at Main Street (west end). Clean retirement
(bank -> rent -> klick -> Return -> 0) was NOT completed. Fred must
put the link-dead character into rent to protect inventory (3 manna,
Nilgiri Guide).

New durable lessons:
- **Ground notes are bankable treasure.** Silver/gold notes found on
  the ground deposit at the bank for 1gc each via `deposit silver` /
  `deposit gold`. Pick them up; never drop them.
- **Room appearance is not zone identity (confirmed again).** Bridges
  and the Granite Tower look residential but report Northern Main
  City; house doors that look enterable lead to Player Homes. Always
  `where` in a new room.
- **The relay can die without warning.** No TIME UP, no error logged.
  Check `ps` for the relay/SSH processes if the MUD stops responding.

## Session 13 — 2026-09-28, ~09:21 PDT (2-hour budget, ended early)

Live diagnostic for the silent relay deaths. New hardening authorized by
Fred: fully detach the relay from its launching shell (own process group
/ double-fork via setsid) plus a heartbeat file (`run/heartbeat`, every
60s) so a future death is noticed within a minute. (Post-mortem: the
silent deaths were VM reboots — no detachment survives a reboot. The
heartbeat still proved its worth as a death detector.) Full story in
`session_summaries/SinMuseBot/session-13.md`.

## Session 14 — 2026-09-28, ~12:44-13:45 PDT (~52 min of a 1h budget, ended early at Fred's request)

Mapping pass for the "Finish the Midgaard city map" idea. 13 rooms mapped
by name/desc/verified exits: Common Square, manhole, Ye Olde Reading /
Common rooms, temple north portcullis OPENED (North End of Temple mapped;
Cloister E/W, Garden Path down NOT entered), General/Pet/Weapon/Magic
shops, Liame's Dispatch (roof hatch closed), Armory, Bank of Midgaard,
Mage's Guild entrance (Up to Mage's Bar BLOCKED by sorcerer), Dootif's
basement office. ZERO XP/combat. Manhole (Market Sq, Down, now OPEN)
drops into Midgaard Storm Drain — OFF-LIMITS, climbed straight back up.
Still unmapped: Todai's, East/West Gate interiors, Cleric's + Swordsmen
guild entrances, Steak House interior, Grunting Boar bar. MUD server
flapped repeatedly; relay reconnect handled it until one drop outlasted
5 attempts and killed the relay. Idle chars get "pulled into a void" —
movement restores. Fred terminated early: bot had gone quiet in-game;
relaunched relay, walked N/E/up to Grunting Boar Reception,
rent + klick + menu-0, clean close. Exit inventory: 1 manna, Nilgiri
Guide. Map pushed (13/20 markers resolved). Full story in
`session_summaries/SinMuseBot/session-14.md`.

## Session 15 — 2026-09-28, ~14:15-14:21 PDT (~6 min, ended early: VM reboot) + resume ~14:30-15:19 PDT (54 min, remaining budget)

Mission was finish Northern Midgaard + connection diagnosis. First leg
killed by the day's third VM reboot (14:21, `who -b` confirmed). Resume
ran with `ServerAliveCountMax=10` (150s ssh tolerance). Northern Midgaard
now FULLY MAPPED: Swordsmen hall exits verified (N->Main St, E->Bar of
Swordsmen not entered), Todai Food Outlet, East Gate interior, Steak
House interior, West Gate interior, Grunting Boar bar, + bonus Gambling
Den (E of bar). Southern Residential spot-check: 18 rooms, zero
discrepancies. Combat per Sin's live order (overrode the mapping brief):
3 fidos, +22 XP (2348->2370, still L3; L4 needs 3244). One ssh drop,
auto-reconnected. Retired by direct drive (driver stalled):
rent+klick+menu-0, clean close, no strays. Bank 69gc unchanged (later
corrected to 71gc per the banker's statement in session 16); exit
inventory: Nilgiri Guide only. Map + summary published. Full story in
`session_summaries/SinMuseBot/session-15.md`.

## Session 16 — 2026-09-28, ~15:40-16:11 PDT + resume ~16:15-16:35 PDT (full 60-min budget across a VM reboot)

Typical hunt with the new responsiveness rules (event-driven ~2s wakes,
batched movement). First leg: daylight in the Hills and Plains — killed
2 field mice; a small green lizard (`consider`: "easy battle") dodged
nearly everything and bit hard, dropping the bot to 27/47 HP before it
fled and rested. Returned inside the West Gate well before dark.
Night: patrolled Northern Main City (Main Street, squares, alleys,
Central Bridge) — 9 more beastly fidos. Answered Sin's gossip ("what's
your directive right now and for how long?") truthfully within the
session. **16:11 PDT: 4th VM reboot of the day** killed the relay
mid-hunt (31 min used, 29 left). Relaunched per Fred's reboot rule;
character reconnected link-dead at Main Street west-1 holding 3 gold +
tin gear, unharmed. Resume: 8 more fidos (one died while link-dead
during the reboot), finished with rent + klick + menu-0, clean close,
no strays — first session to survive a mid-hunt reboot end-to-end.

Kills: 19 total (17 beastly fidos, 2 field mice), all corpses looted
(all empty except one shiny gold coin). XP: 2370 -> 2707 (+337), still
L3 (L4 needs 3244). HP 47/47 at exit. ZERO deaths. Loot: 4 gold coins
deposited (account #0000-11FB: 71gc -> **75gc**), tin boots + tin belt
(from the Dump) equipped/carried, tin chest plate, Nilgiri Guide; zero
gold on the character. Ate a free half loaf at the bakery. Social: Gelu
the God of Thalodia asked "did you know Rivin quit?" — answered
in-character ("I had not heard that. Does that mean the 8th Age is
ending?"); treated as conversation-only per the controller hierarchy.

New durable lessons:
- **`consider` lies about small green lizards** — "easy battle" but they
  dodge everything and hit hard; do not engage at this level.
- **The Dump is pitch black at night** (field-type room) — do not enter
  after dark.
- **Janitors pick up corpses** — "A janitor picks up the trash" took a
  fresh fido corpse before it could be looted. Loot IMMEDIATELY after
  the kill, before `score`.
- **Rent accepts wearable tin gear** (boots/belt/chest plate/crown all
  passed); only treasure-type valuables block rent.
- **Relay self-cleanup fixed** — the menu-0 exit left the FIFO holder
  and `/tmp/mud_cmd` behind; `scripts/mud_relay.py` now kills the
  holder and removes the FIFO/PID files on final exit, and `run/` is
  anchored at the repo root in both layouts.
