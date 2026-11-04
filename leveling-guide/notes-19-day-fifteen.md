# Day fifteen — The long road, walked twice over (session 108)

*Testudo: XP 16,414 → 19,112, Level 7 (no crossing), bank 365 → 371 gc,
0 deaths. One login, four driver legs, two VM reboots — a pure grind
toward Level 8, and the road is now under five thousand points long.*

## The mission as booked, and what actually happened

- Fred's order (2026-11-03): one login, Tuesday ~15:05–19:05 PST
  (launched 15:10, budget to 19:10) — a 4-hour experience run, grind
  only. The master brief carried the bracket honestly: L8 at
  23,795–23,891, Testudo 7,381–7,477 short, so the teach was
  contingency and no crossing was expected. That is exactly how it
  landed: **no crossing (shortfall now ~4,683–4,779), no teach, no
  practices spent, 0 remaining** — and the grind ran hotter than
  session 107's pace: +2,698 over the 3h42m window (~730 XP/hour,
  vs 591 in session 107).
- At this session's pace the crossing lands in the second of two
  more grind logins: 19,112 + ~2,700 ≈ 21,800 after one more
  4-hour grind, still ~2,000 short, so a second further login
  crosses roughly three-quarters through it (a hotter grind pulls
  it earlier). The crossing login stays the teach login under
  Temp, with a small Prepare/Apply slice first on the stored plants.
- **No sweep, no plants:** none seen, none collected, none dropped.
  The rent chamber still holds session 107's 8 plants plus session
  105 salvage, untouched. The forest cabin fireplace is still
  unchecked and still owed its own daylight window.

## Leg by leg (all XP verified against the raw log)

- **Leg 1 (+528, 22 kills):** city + Hills. Three ferocious-rabbit
  ambushes in the Hills (field) sector, all fled on the first
  outbound command (log-verified: no other outbound command between
  each `>>> RABBIT-AMBUSH` and its `>>> RABBIT-FLED`). Hills field
  sector exiled for the rest of the session. VM reboot 15:53 PST
  (boot 23:53 UTC) killed relay + driver at 81 HP in the Dark
  Alley; the handback was lost with the driver.
- **Leg 1b (+716, 15 kills):** city + Southern Residential, parked
  Temple at 17:00. A robin in the park paths paid 110 XP (robin
  revalue in XP_PER_KILL: ~57 average from session 85 — this
  single kill is well above it; do not revalue on n=1). Pigeons
  twice drove 110 HP to the 55 autoflee threshold; fidos stayed
  gentle — prefer fidos when HP is low. One dark-exit violation
  (Central Bridge → Dump after sunset, exit gone "too dark to
  tell"), recovered by retracing south to the bridge. Cure: 4
  attempts, 3 lands, 1 miss at 87 HP (normal ~31% miss at 69).
- **Leg 2 (+849, 18 kills):** city grind, bank 370 gc at last
  balance. VM reboot 18:13 PST (boot 02:13 UTC) killed relay +
  driver in the Temple at full HP; the handback was lost with the
  driver. Both lost handbacks were re-derived from the raw log —
  never carry a claim forward from a report that never arrived.
- **Leg 2b + exit (+605, 8 kills):** hunt to 18:33, park, wait
  without going idle, exit beginning AT 18:50 (TIME UP − 20 min)
  and finishing ~18:52 with fresh `>>> EXITED` +
  `>>> RUNTIME CLEANED` — the clean exit session 107 missed.
  TIME UP (~19:10) never fired because the character had already
  retired; that is the brief's design, not a clock failure.

## New for the guide

- **Greeting rule, first live case (Fred, 2026-11-03; now in
  DRIVER_BRIEF_TEMPLATE.md, "Talking to people"):** when ANYONE
  greets the players collectively ("hi everyone") or greets the game
  by name ("hello Nilgiri"), the bot answers promptly on the same
  channel with a short welcome naming the greeter. Session 108:
  Norritt gossiped "Hello Nilgiri!"; Sin told Testudo to answer
  that greeting and any other like it; Testudo gossiped "Hello
  Norritt, and hello Nilgiri!" and confirmed to Sin. This is
  conversation, not obedience — it applies to any player's greeting,
  controller or not, and it jumps the queue like other speech.
  (Note for the wiki decision: this is bot behavior, not a game
  mechanic for new players, so no wiki mirror this session.)
- **Corpse/loot discipline, refined:** a mortally-wounded mob has
  NO corpse yet — `get all from corpse` then answers "You cannot
  seem to find a 'corpse'" — and when a corpse IS in the room, the
  command takes whatever corpse is there, not necessarily the mob
  just fought (session 108: a mortally-wounded fido's loot command
  picked up a previous pigeon corpse). Do not loot until R.I.P.,
  and do not assume the looted corpse is the current target's.
  (See LESSONS, session 108.)
- **Brief gear claims are not evidence, again:** leg 1b's brief
  said Testudo carries NO lamp, and leg 1b's driver reported a
  dark-room inventory check showing nothing — but the final
  inventory at exit held an oil lamp (unlit, unused) plus the
  Nilgiri Guide. Verify inventory in the light; a dark-room
  inventory check is not a gear audit. (Standing lesson, session
  105: "Verify inventory, not the brief.")
- **XP-per-kill, session 108 values (single-session samples, not
  revaluations):** robin 110 (n=1, park paths — above the ~57
  session-85 average; needs more data); leg-1b pigeon/fido dings
  13–96, consistent with the existing pigeon ~48 / fido ranges
  once the robin outlier is set aside. No table change on n=1.

## What stays open

- Level 8 crossing: ~4,683–4,779 XP away; the crossing login is
  the teach login (Temp, Prepare/Apply slice first on the stored
  8 plants, then animism → herb lore → forage, parent-first).
- Cabin fireplace: still owed its own daylight window.
- Mortal-can-teach: still open and untested (Temp is the master
  for all planned teaches; no Sin fallback needed).
- Crow: consider-only, closed file ("probably die" at L7) — seen
  again in leg 1b, never engaged.
