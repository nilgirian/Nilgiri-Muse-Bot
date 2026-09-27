# Lessons Learned — SinMuseBot's First Three Combat Hunts (2026-09-27)

Consolidated from three hunting sessions in the Northern Main City of
Midgaard, plus corrections taught by Fred. The full technical playbook
lives in NILGIRI_LOGIN.md (§19, §20, and §21); this is the plain-language
writeup of what actually happened and what it taught.

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

## Rules that now hold across all sessions

- Every session is time-boxed; retire at the Reception (`rent`, then
  `encamp`) before the budget ends. If the relay's `>>> TIME UP` signal
  never arrives, retire on elapsed time — don't wait indefinitely.
- Retirement order: bank gold FIRST (deposit + verify balance), then
  navigate to the Inn and `rent` a private room. The bank is safe against
  a dead connection; unsaved inventory is not.
- From the rented rent room, exit with `klick` — not `encamp`. Save
  `encamp` for when out in the game with no rent room to go to. (Taught
  by Fred, 2026-09-27.)
- After any reconnect, verify state with `score` and `look` before
  resuming the hunt.
- Never `quit` (drops inventory). After `encamp`, send Return at
  `*** PRESS RETURN:`, choose menu option 0, and let the MUD close the
  connection itself. Verify no stray ssh process remains.
- Never `drop all` (a previous session destroyed the Nilgiri Guide and 2
  manna this way).
- Bank gold before renting; never drop currency.
- Loot with `get all from corpse`, promptly, before janitors or decay
  take the body.
- Kill only recognizable creatures/animals; `look <name>` first when in
  doubt; never attack PCs or humanoid NPCs.
- Confirm every kill with a corpse. XP alone proves nothing.
- Stay inside the assigned zone; gates lead out.
- Rest (`rest`, then `stand`) between fights when hits are low — it
  recovers faster than standing idle. Never `sleep` in the field; it
  leaves you vulnerable and blind.
- Fleeing a costly fight to heal and finish later is a valid tactic.
- If the character levels, shout "Level!".
- After every session, once disconnected, give the user a chat summary
  of the adventure: what happened, XP gained, kills with locations,
  loot/gold and bank activity, how the session ended. The session log
  stays local-only; the summary is what the user gets.

## Session 5 — 22:23 to 22:56 (about 33 minutes of a one-hour budget)

Started at 879 XP, ended at 1023 XP (+144), reached LEVEL 2 at 22:48:28
(Poor Alley fido fight: +28 XP at mortal wound, 995 -> 1023). Shouted
`say Level!` in-game immediately (confirmed "You exclaim, 'Level!'" at
22:48:32). Level-up gains: +8 max HP (38), +2 mana (102), +4 move (96),
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
- **At the exit menu, the choice digit must be followed by a newline.**
  Bare "0" bytes buffer without submitting; several sends accumulate
  into one invalid choice ("0000") and the menu re-displays. Send "0"
  then Return as one atomic line.
- **Kill the relay AFTER a clean MUD exit.** Choosing menu option 0 and
  the MUD closing the connection does NOT stop the relay — it started
  RECONNECTING (attempt 5/5) on the EOF. Terminate the relay process
  (and verify with `pgrep -af nilgiri`) or it will open an unwanted new
  session at the menu.
- Level-up shout works: `say Level!` is heard in the room immediately.
