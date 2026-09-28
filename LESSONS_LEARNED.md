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
- **Loot with `get all from corpse`, promptly.** Janitors pick up
  corpses and bodies decay; most fido corpses are empty, but some hold
  gold — looting every one paid off more than once.
- **Kill only recognizable creatures/animals.** If a name is ambiguous
  (Intrepid, Shargugh, John the Lumberjack...), `look <name>` first.
  Never attack PCs or humanoid NPCs.
- **Fleeing to heal is a tactic, not a failure.** `rest`, then `stand`;
  never `sleep` in the field (fast healing, but vulnerable and blind).
- **Known-good L2 prey:** beastly fido, cute rabbit, brown fox. Too
  strong: three-point horned stag. Left alone per the creature-only
  rule: ugly troll, Shargugh the Forest Brownie, John the Lumberjack,
  gnome, Intrepid, knight templar.

### Gold and the bank

- **Gold is important — never drop it.** The receptionist refuses `rent`
  while gold is carried ("certain valuables... prohibited in rent"), so
  bank it first.
- **Rent refuses ALL valuables, not just gold.** A small green gem
  blocked `rent` the same way coins do. If you're carrying treasure at
  shutdown: shops won't buy gems ("Arglebargle, glop-glyf!?!" — the
  grocer and the wizard both refused); the bank's `value` command
  appraises treasure ("worth one gold coin") but doesn't buy it. Park
  the item on the floor INSIDE a shop (the General Store floor visibly
  persists items) and recover it next session — never drop valuables
  outside. **Recovering a parked valuable is the first job next session.**
  (Session 9 failed this: the gem sat on the General Store floor two
  sessions running because the driver kept deprioritizing it. Fred's
  directive is "pick up anything of value" — no exceptions, no "safe
  spot" deferrals.)
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
  "lightly covered"). Sweep it as part of the city patrol.

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
- **Map by room identity** (`look` + `exits`), never assumed
  coordinates — west-then-east doesn't always return you, and geometry
  isn't always reversible.
- **Stay inside the assigned zone.** Gates and bridges lead out; count
  moves near them.
- **Check `where` regularly; turn back immediately if out of zone.**
  (Fred, 2026-09-27, after the bot died outside an approved zone.) The
  approved zones are Northern Midgaard, the Hills and Plains, and the
  Bee Hive — nothing else. The moment `where` shows unapproved ground,
  turn back at once for a safer zone; do not keep exploring. This
  overrides corpse recovery: if the corpse lies in the unapproved zone,
  abandon it and report the lost inventory instead of going back in.
- **The heavy jungle is OFF-LIMITS.** (Session 9, 2026-09-27.) North of
  the dense forest, past the jungled paths, lies "The heavy jungle" — a
  maze where every exit returns to itself. A brown bear (38 -> 12 HP)
  and tarantulas killed the L2 character there. Never enter; the
  approach path's zone is unverified, so confirm with `where` before
  going north of the dense forest at all.

### In-game conduct

- On level-up, announce with **`shout Level!`** — game-wide. `say`
  reaches only the room.
- **US ASCII only** in commands and speech; no emoji or non-ASCII.
- If Sin, Motorola, or Russ speak to the bot, respond to what they
  actually say as it happens — never from anticipated speech.
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
- On level-up, use the game-wide `shout` command: `shout Level!`. Do
  NOT use `say` — it only reaches the current room. (Fred's correction,
  2026-09-27: session 5 used `say Level!`, which the room heard but the
  game at large did not.)

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
