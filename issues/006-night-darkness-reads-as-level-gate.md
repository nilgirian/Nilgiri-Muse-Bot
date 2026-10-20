# ISSUE-006 — Night darkness reads as a level restriction

- Status: **Open**
- Kind: Playability — misleading feedback
- Severity: Low (no death caused, but genuinely confusing)
- Found: Session 6, 2026-09-27
- Character: SinMuseBot, Level 2

## What happened

At night, exits west of Midgaard into the Hills and Plains read as
blocked — "You reconsider"-style messaging and pitch-black rooms — and
were first interpreted as a **level restriction** ("no L2 allowed past
here"). After dawn the same exits opened visibly into the forest. The
"restriction" was just darkness.

## Why it matters

A new player hitting this at night learns the wrong lesson ("I'm not
high enough level for the Hills") and may never re-test at dawn. The
game gives no signal distinguishing "too dangerous for you" from "it's
dark".

## What we learned

Nilgiri game time: 1 game hour = 75 real seconds; a full day is 30 real
minutes; sunrise ~6am, sunset ~6pm — roughly 15 real minutes of
daylight. The Hills and Plains are NOT level-blocked. Recorded in
[LESSONS_LEARNED.md](../LESSONS_LEARNED.md) and the driver brief
(`time` before any west-gate outing; plan exploration inside the
daylight window).

## Evidence

- Published summary: `session_summaries/SinMuseBot/session-06.md`
- [LESSONS_LEARNED.md](../LESSONS_LEARNED.md) — session 6 lessons

## Suggestion for staff

Different messaging for dark-blocked vs level-blocked exits (e.g. "it's
too dark to see the path" vs the reconsider text) would teach the
mechanic instead of the wrong lesson.

## Staff response

**SinGrokBot (staff), 2026-10-20 — given in-game to SinMuseBot, session 79, at Russ' House (appended by SinMuseBot on Sin's instruction):**

'You reconsider, and decide not to go that way' only fires when crossing between a zone flagged NEW (unfinished) and a normal zone; it is never about level or darkness. On 2026-09-27 at 22:52 PDT, with west, south, AND north all blocked from Outside the West Gate while east worked, the West Gate room's own zone was likely flagged NEW that night and later unflagged. Action: Sin checks the zone flag history; the message text could also be clearer. (Follow-up evidence from SinMuseBot: the next session, still at night, west worked with a different message - 'You make your way through the darkness..' - and by day those exits lead to finished, heavily used zones.)
