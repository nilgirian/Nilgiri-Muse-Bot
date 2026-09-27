# Lessons Learned — SinMuseBot's First Two Combat Hunts (2026-09-27)

Consolidated from two hunting sessions in the Northern Main City of
Midgaard, plus corrections taught by Fred. The full technical playbook
lives in NILGIRI_LOGIN.md (§19 and §20); this is the plain-language
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

## The Bank of Midgaard (taught by Fred, 2026-09-27)

When carrying gold and preparing to rent:

1. Before renting, find the Bank of Midgaard.
2. On the first visit, read the sign.
3. If you do not already have an account, 'Initiate New Account'.
4. Then 'deposit gold'.
5. Check the balance with 'balance' while at the Bank.

## Rules that now hold across both sessions

- Every session is time-boxed; retire at the Reception (`rent`, then
  `encamp`) before the budget ends.
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
- If the character levels, shout "Level!".
