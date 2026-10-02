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

## Suggestion for staff

A one-line arrival notice in combat ("A courier pigeon flies in to
assist...") or making `consider`/`kill` resolve the same target would
close the gap without changing the mechanics.

## Staff response

_(Reserved — the Nilgiri Grok Bot will respond here.)_
