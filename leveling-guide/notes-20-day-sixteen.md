# Day sixteen — The road, interrupted twice (session 109)

*Testudo: XP 19,112 → 22,056, Level 7 (no crossing), bank 371 → 375 gc,
0 deaths. One login, six driver legs (one killed before it started,
one killed with its handback), two VM reboots — a pure grind toward
Level 8, and the road is now under two thousand points long.*

## The mission as booked, and what actually happened

- Fred's order (2026-11-04): one login, Wednesday 13:00–17:00 PST
  (240 min) — a 4-hour experience run, grind only. The master brief
  carried the bracket honestly: L8 at 23,795–23,891, Testudo
  4,683–4,779 short, so the teach was contingency and no crossing
  was expected. That is exactly how it landed: **no crossing
  (shortfall now ~1,739–1,835), no teach, no practices spent, 0
  remaining** — and the grind ran hotter than session 108's pace:
  +2,944 over the session (~750–800 XP/hour of driving time, vs
  ~730 in session 108).
- At this session's pace the crossing lands in the NEXT grind
  login: 22,056 + ~2,700 ≈ 24,750, past the top of the bracket, so
  a single further 4-hour login crosses roughly two-thirds through
  it — sooner if the grind runs hotter, later if reboots eat legs
  again. The crossing login stays the teach login under Temp, with
  a small Prepare/Apply slice first on the stored plants.
- **No sweep, no plants:** none seen, none collected, none dropped.
  The rent chamber still holds session 107's 8 plants plus session
  105 salvage, untouched. The forest cabin fireplace is still
  unchecked and still owed its own daylight window.

## Leg by leg (all XP verified against the raw log)

- **Leg 1 (killed at launch, +0):** VM reboot 13:01 PST (boot
  21:01 UTC) killed the just-launched relay (pid 10523) and the
  driver before ANY command was sent. Nothing happened in game:
  no greeting, no noflee, no feed, no kills. Recovery: relay
  relaunch on the remaining budget to the original 17:00 PST end
  (relay pid 1939, 14,126s), same log, verify PASS.
- **Leg 1b (+668, 11 kills):** city + Hills, parked Temple at
  13:51. Six ferocious-rabbit contacts in rabbit country, all
  fled, rabbit country exiled for the rest of the session. One
  inadvertent step south on a slimy path into Newtonia (unapproved)
  — turned straight back north immediately. Night darkened the
  outdoor exits despite a lit lamp; the driver waited it out to
  dawn. Crow consider-only, vulture skipped, white mountain goat
  fled wounded (60 XP on departure, NO R.I.P. — not a kill).
  Slug's crumpled corpse at Temple Square was passed, not looted.
  Handover was hungry + thirsty — the next leg fed first.
- **Leg 2 (+1,368, 30 kills):** city + park, parked Temple at
  15:04. Sixteen fidos, eight pigeons, three ducks, three robins.
  Sparrows fled at the first solid hit and were not chased into
  dark exits. One pigeon corpse swept by a janitor before looting,
  one devoured by a fido. A four-fido tangle in the Common Square
  resolved with no downed mob left behind. MUD EOF + auto-reconnect
  ~14:46, recovered in place at full HP, no rollback. Temp seen
  silent at the Inn Entrance; no speech, no teach (no crossing).
  Rabbit country never entered; Vineyard and Bee Hive skipped
  because both route through it.
- **Leg 3 (partial, +361, 5 kills — handback LOST):** VM reboot
  15:28 PST (boot 23:28 UTC) killed relay + driver ~20 min in.
  The handback never arrived, so this leg is re-derived from the
  log alone: 5 R.I.P.s (fido, pigeon, pigeon, fido, duck), XP
  21,148 → 21,509, last fight a swan in the park fled at 59 HP,
  hungry, not in combat — the swan is NOT a kill. Recovery: relay
  relaunch on the remaining budget to 17:00 PST (relay pid 1818,
  5,430s), same log, verify PASS.
- **Leg 3b (+501, 9 kills, plus +46 unattributed):** recovery leg,
  parked Temple at 16:03. First score after reconnect: XP 21,555
  — +46 above the pre-reboot snapshot, with no R.I.P. in between
  and no score-to-score drop. The +46 reads as wound XP paid when
  a wounded victim left the room, not as a kill and not as
  corruption. Seven pigeons, two fidos, all corpses empty; two
  gold coins banked one per command (see below). One redundant
  manual `flee` sent after autoflee had already fled the driver
  walked him south into the Armory — the session-69 bug, owned in
  the handback, no harm. Temp seen silent again; no speech.
- **Exit leg (16:40–16:43, +0):** began AT 16:40, not before, after
  a pre-window idle gap in the Temple (checked before the window,
  not inside it). Fed/drank first, bank check (nothing bankable:
  lamp + Guide only, balance 375 gc unchanged), rent first try,
  farewell gossiped in the chamber ("Testudo rests at Level 7 -
  the road is shorter than it was this morning."), klick, menu
  exit, fresh >>> EXITED + >>> RUNTIME CLEANED, verified clean
  before 17:00 TIME UP (which never fired). Slug lay mortally
  wounded at the Inn Entrance with Temp standing silent beside
  him; both were left alone, correctly — mortally wounded is not
  dead, and the exit leg is exit only.

## New for the guide

- **Link-loss penalty is not automatic (session 109):** two
  VM-reboot reconnects this session produced NO score-to-score
  drop at all — the first post-reboot score was a gain (+46
  wound payment), and closeout flagged zero drops across the
  whole log. Session 80's ~5% penalty is a thing that CAN happen
  on link loss, not a thing that DOES happen on every reconnect.
  Test every apparent dip against the ~5% figure, but do not
  assume a dip is coming, and do not write one off before seeing
  the first post-reconnect score.
- **Closeout script totals are not evidence (session 109):**
  `closeout.py` counted 54 kills (24 fido); the raw log holds 55
  R.I.P. lines (25 fido). The tale and this note use the raw log.
  Always grep the R.I.P. lines before publishing a kill total —
  the script's count is a starting point, not a verdict.
- **Deposit, confirmed again (session 109):** a carried stack
  reading "a shiny gold coin (x2)" deposited ONE coin per
  `deposit gold` command — balance 373 → 374 → 375 across two
  deposits with a balance read between them. This matches the
  standing rule (loose piles whole at once, stack items one per
  command) and the wiki's one-coin-per-command wording. No wiki
  change needed; the wiki already says it right.
- **Handback drift, again (session 109 leg 1b):** the handback
  said five rabbit contacts; the log shows six initial markers.
  It described autoflee-triggered flees as first-command flees.
  The operator spot-check caught both, and the corrections rode
  in the leg-2 brief (manual flee first command, never flee after
  autoflee). A handback that arrives is still not evidence until
  the log agrees with it — the s87/s108 rule, re-proven.
- **Swan cost (session 109, provisional):** the park swan fought
  long on unwieldy staff misses, cost ~50 HP, and ended in
  autoflee with the swan only "pretty hurt." It is not a priority
  target at L7 with a staff; the existing provisional swan value
  (~38 XP) does not justify the HP. No table change — the swan
  was never killed this session.
- **XP-per-kill, session 109:** no clean isolated values. Scores
  were multi-kill intervals throughout, and the +46 wound payment
  is unattributed by design. No table change.

## What stays open

- Level 8 crossing: ~1,739–1,835 XP away; the crossing login is
  the teach login (Temp, Prepare/Apply slice first on the stored
  8 plants, then animism → herb lore → forage, parent-first).
- Cabin fireplace: still owed its own daylight window.
- Mortal-can-teach: still open and untested (Temp is the master
  for all planned teaches; no Sin fallback needed).
- Crow: consider-only, closed file ("probably die" at L7) — seen
  again in leg 1b, never engaged.
- Swan: never killed, never a priority — re-consider only after
  Level 8, or with a better weapon than a staff.
