# Day fourteen — The first shrub haul, and four ways a session can break (session 107)

*Testudo: XP 14,049 → 16,414, Level 7 (no crossing), bank 350 → 365 gc,
0 deaths. One login, six driver legs; the day the plant rule finally
paid out in shrubs — and the day the infrastructure broke four times.*

## The mission as booked, and what actually happened

- Fred's order (2026-11-01): one login, Monday 12:00–16:00 PST — a shrub
  sweep woven into the Level 8 hunt, Temp's teach after the crossing.
  The master brief carried the bracket honestly: L8 at 23,795–23,891,
  Testudo ~9,800 short, so the teach was contingency and the
  shrubs-banked path was the expected outcome. That is exactly how it
  landed: **no crossing (shortfall ~7,381), no teach, no practices
  spent, 0 remaining** — and the shrubs did ride home, per §4.
- **The haul (8 plants, all in the rent chamber now):** 3 small ferns
  (grassy knoll west of the Field, Valley in the hills, Field),
  1 silvery fern (obscure path out of the light forest), 1 small brown
  plant (knoll), 2 shrubs (a light-forest trail room, an obscure path),
  1 purple shrub (clearing around a huge tree, the room with the fat
  bumble bee). The knoll's mapped purple shrub was absent on every
  check, all session — spawns are periodic/random; re-check every pass.
  The forest cabin fireplace went **unchecked three legs running**
  (legs 2, 2b, 2c all skipped it for daylight/deadline reasons). It
  needs a dedicated daylight window, not a squeezed add-on.
- **The standing plant rule works when the brief keeps it.** Session
  106's briefs dropped it and collected zero; session 107's briefs
  inherited the template wholesale and collected eight. The rule
  (Fred 2026-10-06): plants are ordinary ground items — pick them up
  on sight like any loot; forage is only a sensing spell.

## Four interruptions, four diagnoses (do not conflate them)

1. **VM reboot 12:03 PST** (boot 20:03 UTC): leg-1 driver sent zero
   commands before the relay died. Diagnosis: `who -b` + wiped `/tmp`.
2. **Relay transport death ~13:33 PST** (NOT a reboot — boot unchanged):
   after the leg-1b park, `>>> MUD EOF` and all 5 reconnect attempts
   failed with `mud-ssh: cannot connect to 127.0.0.1:8008:
   Connection refused`, then `>>> RECONNECT FAILED` / `>>> RUNTIME
   CLEANED`. The local proxy endpoint refused; a fresh relay launch
   (new tunnel) recovered cleanly.
3. **VM reboot 14:08 PST** (boot 22:08 UTC): leg-2 driver misread it as
   a silent relay death. Correction, operator-verified: `who -b`
   proves a reboot. Never diagnose a relay death from the log alone
   when `who -b` can settle it.
4. **Game-server SIGTERM restart ~14:34 PST** (NOT a reboot, NOT a
   relay fault): WIZLOCK notices, then `*** The game is shutting down
   (SIGTERM) for a restart. Your characters will be saved.` The
   relay's reconnect attempts failed while the game was down; a fresh
   launch after the restart logged back in — and the restart
   **relocated Testudo to the Temple of Midgaard at full HP** (from
   Main Street at 105 HP), with XP intact (16,053 verified). A
   restart relocation is a fresh `score`/`look` check, not an
   assumption.
- Every recovery relaunched the relay on the remaining budget to the
  original 16:00 end, same log file. **No rollback anywhere:** XP
  verified intact at every re-entry (14,049 → 15,911 → 16,009 →
  16,053 → 16,414, each re-entry score matching the prior leg's
  arithmetic or closing score).

## Mechanics refined (general, newbie-relevant — repo record; wiki merge pending a Prepare/Apply test)

- **Carry limit is ITEM COUNT (~10), not weight.** At 99–101 lbs
  ("no problem") the game refused pickups and bakery sales ("You
  cannot possibly carry any more" / "Lighten your load first").
  Dropping one item frees exactly one slot. Judge load by item count;
  weight ("your back aches" at 226 lbs) is a separate, weaker signal.
- **Bank deposit syntax is short-noun.** `deposit silver` works;
  `deposit gold` works; `deposit silver note` prompts "What account
  number?" and a bare-number answer is parsed as speech
  ("Arglebargle, glop-glyf!?!"). One-word treasure nouns only.
- **Drop parser is one-word nouns.** `drop fern`, `drop shrub`,
  `drop plant` work; `drop small fern` / `drop purple shrub` fail
  ("You do not seem to have that 'small'/'purple'"). The exit leg
  dropped all 8 plants this way.
- **Lamp paradox resolved:** leg 1b's "emitting light" vs "already
  dowsed" contradiction was a genuinely dowsed lamp — `hold lamp` +
  `light lamp` lit it, and inventory then read "emitting light."
  Follow the template relight rule (hold first in darkness) and
  verify by room light, not by one command's wording.
- **TIME UP does not kill the relay.** TIME UP fired mid-exit-leg
  (driver idle in the Temple); rent + klick still worked normally
  afterward and the exit completed ~16:50 PST with verified
  `>>> EXITED` + `>>> RUNTIME CLEANED`. TIME UP is a retirement
  trigger, not a connection kill — but the exit leg's repeated
  `>>> DRIVER-IDLE` markers (32 in the whole log) show the leg ran
  slow; an exit leg still needs pace.

## Operator corrections (owned)

- **Exit driver's start-location note is not supported by the log.**
  It claimed the exit leg started in the Reception (first `where`
  answering "Bank of Midgaard"); the log shows Temple rooms through
  the exit leg's Temple Square movements and Reception only at rent
  entry. The leg-2c Temple park stands as the true start. `where`
  answers zone/player listings, not the driver's room — do not read
  a room off it.
- **Exit driver's farewell:** an unbriefed farewell variant was
  gossiped mid-exit (line 15837) before the briefed line in the
  chamber (line 17235). The briefed line is the farewell of record;
  the variant is a deviation, not a second farewell. Farewell text
  is fixed — do not improvise variants.
- **Kill accounting:** 43 Testudo R.I.P. kills this session. Two
  further R.I.P. lines in the log are Nero's squire kills on Main
  Street — other players' kills in shared rooms land in your log
  too; count only your own. Unfinished fights are not kills: the
  leg-2b pigeon (incapacitated + mortally wounded at SIGTERM) and
  the leg-2c pigeon (+89, autoflee) are XP only.

## Level table

- L7 = 13,777 (crossed 13,798, s106). L8 bracket unchanged:
  23,795–23,891 (SinMuseBot's crossing, Oct 13, log-verified).
  Testudo at 16,414 is ~7,381 short; no new threshold data this
  session (no crossing, no new level gains to record).
- Skills unchanged: Animism 40/58, Herb Lore 9/40, Forage 9/9,
  Prepare 0/9, Apply 0/9, Martialism 64, Kick 64, Block 64,
  Catechism 69, Cure 69. The Prepare/Apply live test still waits —
  it needs the L8 grant first, then a held shrub in the chamber
  (now stocked: 8 plants) for the small-slice test.
