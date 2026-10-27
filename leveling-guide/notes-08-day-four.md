# Leveling guide — notes 08: day four, level 3 and the gate-room lesson (session 96, 2026-10-26)

Four hours, two VM reboots, one crossing, one rabbit. XP 1,640 →
**2,764 (+1,124)**, **27 confirmed kills** (25 beastly fidos, 2 courier
pigeons), 0 deaths. closeout.py: no XP drops flagged (never mid-fight
at a drop). Raw log: `session-20261026-1339-testudo-xp.log`.

## The L3 crossing (measured)

Crossing kill: a staff crit on a beastly fido at Temple Square, +29 XP
(2,014 → crossed; post-crossing score 2,049). The level-up line,
verbatim:

> "You raise a level! You gain 18 practice sessions. You gain 11 hit
> points. You gain 0 mana points. You gain 3 movement points. You gain
> 7% skill in Protection From Evil."

- **18 practice sessions at L3 too** (L2 also granted 18; L1 grants
  none — notes-04). All 18 remain banked, unspent, by plan.
- Gains identical in shape to L2: **+11 HP** (47 → 58), **+0 mana**,
  **+3 move** (88 → 91). The +0 mana remains theory-consistent
  (catechism 19/69 is below the 50% family threshold; see notes-07).
- **Protection From Evil +7% at L3, against +6% at L2** (total 13%).
  The natural trait's free growth is NOT a flat amount — record the
  per-level growth as its own series from here on.
- noflee recomputed 23 → 29 (half of 58).

## Bank and bakery — two standing questions closed

- `balance` at the Bank of Midgaard prints, verbatim: "The banker
  informs you: --- Account #0000-12CB / Principal(s): Testudo /
  **Amount: 2gc** ---" followed by a dated statement of credits.
  Testudo's total is therefore VERIFIED at 2 gc (session 93's coin +
  session 95's corpse coin), no debits ever.
- Bakery half loaves are **free**: the list shows "n/c" and the baker
  whispers "You can have that for free!" on every purchase. The
  session-94 question (free vs bank-debited) is closed both ways.

## The gate-room lesson (newbie-critical)

Fighting a fido **Inside the West Gate**, autoflee fired at 23 HP and
chained Testudo OUT through the gate; a follow-up flee landed him in
the **Field**, where the ferocious rabbit bit him once before he
escaped by normal moves through the wall back to Poor Alley (bottom:
20 HP). Rules that follow, now in the driver brief template:

- **Never fight in a gate room or beside a wall breach** — a flee
  there can carry you out of the city into rabbit country.
- After any flee, the next commands are deliberate directional moves,
  never another blind `flee`.
- The relay's RABBIT-AMBUSH marker keeps re-emitting after a
  move-escape until its 180s no-rabbit-line timeout clears it
  silently (the escape used moves, not `flee`, so no RABBIT-FLED).
  A firing marker with no rabbit in the room and a non-fighting
  prompt is stale: verify with `look`, do not flee a safe room.

## Field notes

- **Pace at L3:** ~280 XP/hour on city fidos/pigeons with martialism
  20 / kick 15 (vs ~250/h at L2, ~100/h at L1). Fights run long: at
  this build only crits and landed kicks damage reliably; 15-22-round
  dry fights are normal, and wound-stage XP pays as bands cross.
- **Kick crits pay no XP when they cross no wound band** (twice in
  leg 2: a fresh fido visibly wounded by a kick crit, no XP line,
  score unchanged). Staff-crit band crossings pay. Lead for the next
  office hours, not settled.
- **Finish downed mobs with `kill`, never `kick`** — a kick at an
  incapacitated mob wastes the round ("Kick whom?"); one fido
  recovered and escaped that way. Target swap is real: a fresh
  same-name mob entering mid-fight captures your target while the
  wounded one recovers.
- **Cure at 9%:** 4 lands in 35 casts across the session (~11% — the
  d100 rule's variance; full-HP casts print the same "no effect").
- **Footing:** "misplace your footing" appeared 12 times all session
  (martialism 20) against 186 in session 92 — the martialism lead
  from notes-07 strengthens. Staff "unwieldy" lines: 826 (0% staves;
  still no practiced comparison — the weapon-skill question stays
  reserved for SinGrokBot).
- **Black crow at L3:** `consider` still "He is a higher level than
  you. You would probably die..." — remains on the too-strong list,
  not engaged.
- **Slug (recurring thief NPC):** three corpses looted across the
  day, all empty. Fred's mechanic: a COMPLETED steal puts the goods
  on his person — but every witnessed death followed a steal caught
  mid-attempt, so nothing had been taken. Watch for a Slug who gets
  away clean before he dies.
- Fidos deplete noticeably after ~10 kills in an area and respawn
  slowly — rotate blocks; fidos also scavenge fresh corpses (one
  devoured a fido corpse in Market Square before it could be looted).
- `drink fountain` works only at Market Square itself; hunger returns
  every ~35-40 min; Temple-area regen is strong.

## Next

- Teach session: spend the 18 banked L3 practices, raise catechism
  FIRST and re-check cure's bracket (the notes-07 ceiling hypothesis),
  and put the kick-crit XP question and the reframed weapon-skill
  question to SinGrokBot.
- City-only until LEVEL 4 (decided 2026-10-26, Fred ratified); the
  first Hills/Plains hunt happens at L4 under flee-first rabbit
  discipline.
