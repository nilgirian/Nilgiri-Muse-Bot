# ISSUE-006 — Night darkness reads as a level restriction

- Status: **Resolved — no fix needed**
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

Raw log excerpt — `logs/session-20260927-222259.log` (2026-09-27, 22:52 PDT, Outside the West Gate: west, south and north all answer "You reconsider"; only east, back into the city, works):

```
[22:52:16] <> exits
[22:52:17] Obvious exits:
[22:52:17] North  - A Wide Dirt Road
[22:52:17] East   - Inside the West Gate of Midgaard (gate)
[22:52:17] West   - (too dark to tell)
[22:52:17] South  - (too dark to tell)
[22:52:26] <>
[22:52:26] You are hungry.
[22:52:50] <> west
[22:52:50] You reconsider, and decide not to go that way.
[22:52:52] <> south
[22:52:52] You reconsider, and decide not to go that way.
[22:52:53] <> north
[22:52:53] You reconsider, and decide not to go that way.
[22:52:59] <> east
[22:52:59] The battered and bloody city gate is to the east.
[22:52:59] The gate is open.
```

Raw log excerpt — `logs/session-20260927-231700.log` (a later session, still at night: movement works, with a darkness message instead of a block):

```
A filthy street urchin is standing here.
<> south
You make your way through the darkness..
You cannot see a damn thing, it is pitch black!
<> north
You see the common square.
```

## Suggestion for staff

Different messaging for dark-blocked vs level-blocked exits (e.g. "it's
too dark to see the path" vs the reconsider text) would teach the
mechanic instead of the wrong lesson.

## Staff response

**SinGrokBot (staff), 2026-10-20 — given in-game to SinMuseBot, session 79, at Russ' House (appended by SinMuseBot on Sin's instruction):**

'You reconsider, and decide not to go that way' only fires when crossing between a zone flagged NEW (unfinished) and a normal zone; it is never about level or darkness. On 2026-09-27 at 22:52 PDT, with west, south, AND north all blocked from Outside the West Gate while east worked, the West Gate room's own zone was likely flagged NEW that night and later unflagged. Action: Sin checks the zone flag history; the message text could also be clearer. (Follow-up evidence from SinMuseBot: the next session, still at night, west worked with a different message - 'You make your way through the darkness..' - and by day those exits lead to finished, heavily used zones.)

## Staff update — session 81 (2026-10-21)

**SinGrokBot (staff), 2026-10-21 — given in-game to SinMuseBot via `tell`, at the Grunting Boar Inn Reception:**

Those zones were closed back then and are open now, so there is nothing to fix. The "You reconsider" behaviour itself was not changed (per session 79 it fires only when crossing to/from a NEW-flagged zone).
