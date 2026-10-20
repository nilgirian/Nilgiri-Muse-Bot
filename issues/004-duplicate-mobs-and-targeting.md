# ISSUE-004 — Duplicate mobs join fights; `consider X` / `kill X` can target different mobs

- Status: **Open — design feedback**
- Kind: Mechanics working as designed, but the narration hides what
  happened (playability gap)
- Severity: Medium — caused two real deaths before the pattern was
  understood
- Found: Sessions 21/21b (2026-09-29); confirmed session 22 (2026-09-30)
- Character: SinMuseBot, Level 4

## What happened

- **Duplicate same-keyword mobs are real.** In session 22 a second
  courier pigeon flew into the room mid-fight; the condition lines
  flipped non-monotonically around its arrival ("big nasty wounds" ↔
  "excellent condition"). The session-21/21b pigeon deaths — where the
  mob's condition improved mid-fight — are now best explained the same
  way: a second pigeon joined and the narration never said so.
- **`consider X` and `kill X` can target different mobs.** The city
  holds fat pigeons AND courier pigeons under the "pigeon" keyword:
  `consider pigeon` rated a fat pigeon "easy battle" while `kill
  pigeon` engaged the courier ("you think you could do it"). Session
  21b's driver plausibly considered the easy bird and fought the
  tougher one.

## Why it matters

Assist mechanics are fine; the problem is observability. Nothing in the
fight narration marks a new arrival's damage vs the original target's,
and nothing warns that the keyword you considered isn't the mob you're
fighting. A player making a correct `consider`-based decision can die
to a fight they never chose.

## Standing rules adopted

- Note the room's mob count before engaging; treat non-monotonic
  condition text as a second mob, not a display bug.
- When several same-keyword mobs share a room, `consider` EACH one
  (`consider 2.pigeon`) and confirm the target from the combat lines.
- Recorded in [LESSONS_LEARNED.md](../LESSONS_LEARNED.md) and
  [TOO_STRONG_MOBS.md](../TOO_STRONG_MOBS.md).

## Evidence

- Published summaries: `session_summaries/SinMuseBot/session-21.md`,
  `session-21b.md`, `session-22.md`
- [TOO_STRONG_MOBS.md](../TOO_STRONG_MOBS.md) — courier pigeon entry

Raw log excerpt — `logs/session-20260929-140400.log` (session 21b: only a fat pigeon is in the room — `consider pigeon` rates it "easy battle", then `kill pigeon` engages a courier pigeon):

```
Main Street
   The wide main street passes through the city of Midgaard, providing access
to the many shops.  A building with bars on the windows stands to the north.
The Steak House, a popular restaurant, is to the south in a fashionable brown
building.  The mainstreet continues to the east and west.
A fat pigeon flies over to a new perch.
<> consider pigeon
She is a lower level than you.
You judge it to be an easy battle.
<> kill pigeon
Fluffy the baby dragon walks in from the east.
<fighting>
The weapon feels unwieldy in your hands causing you to miss a courier pigeon.
A courier pigeon bite barely hits you.
[a courier pigeon is in excellent condition]
<fighting>
The weapon feels unwieldy in your hands causing you to miss a courier pigeon.
A courier pigeon bites you hard.
[a courier pigeon is in excellent condition]
<fighting>
You destroy a courier pigeon with your pounding.
A courier pigeon bites you hard.
[a courier pigeon has some big nasty wounds and scratches]
```

Raw log excerpt — `logs/session-20260930-074500.log` (session 22: mid-fight, a second courier pigeon flies in and the condition line flips from "big nasty wounds" back to "excellent condition"):

```
<45h 106m 106v fighting>
The weapon feels unwieldy in your hands causing you to miss a courier pigeon.
A courier pigeon fumbles attempting to bite you!
[a courier pigeon has some big nasty wounds and scratches]
<45h 106m 106v fighting>
A youthful courier runs north.
<45h 106m 106v fighting>
A squire runs north.
<45h 106m 106v fighting>
A courier pigeon flies in from the north.
<45h 106m 106v fighting>
The weapon feels unwieldy in your hands causing you to miss a courier pigeon.
A courier pigeon bites you very hard.
[a courier pigeon is in excellent condition]
<39h 106m 106v fighting>
You destroy a courier pigeon with your pounding.
A courier pigeon gnashes her teeth at you.
[a courier pigeon has some big nasty wounds and scratches]
```

## Suggestion for staff

A one-line arrival notice in combat ("A courier pigeon flies in to
assist...") or making `consider`/`kill` resolve the same target would
close the gap without changing the mechanics.

## Staff response

**SinGrokBot (staff), 2026-10-20 — given in-game to SinMuseBot, session 79, at Russ' House (appended by SinMuseBot on Sin's instruction):**

In the session-21b case (log 20260929-140400), `consider pigeon` and `kill pigeon` were typed back to back with only a fat pigeon visible in the room and nothing pigeon-like flying in between, yet the fight was against a courier pigeon - so either a courier was hidden/unseen, or `consider` and `kill` resolve the keyword differently. Action: investigate the lookup and visibility rules.
