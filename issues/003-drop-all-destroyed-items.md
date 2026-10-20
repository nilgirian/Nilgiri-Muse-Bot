# ISSUE-003 — `drop all` destroyed the Nilgiri Guide and 2 manna

- Status: **Open — needs clarification (intended mechanic or bug?)**
- Kind: Suspected bug
- Severity: Medium — destroyed a quest-ish item and consumables
  silently
- Found: Session 9, 2026-09-27
- Character: SinMuseBot, Level 2

## What happened

A `drop all` command destroyed the character's **Nilgiri Guide** and
**2 manna** — the items did not land on the ground, they were gone
(the driver observed them "explode" rather than drop).

## Why it's suspicious

In stock DikuMUD, `drop` moves an item to the room; it does not destroy
it. If Nilgiri has an anti-litter "dissolve" mechanic for dropped items,
it fired with no message distinguishing "dropped" from "destroyed",
which makes `drop all` — a normal inventory-management command — a
trap.

## Standing rule adopted

Never `drop all` in Nilgiri (recorded in [LESSONS_LEARNED.md](../LESSONS_LEARNED.md)
and the driver brief). This works around the issue but doesn't answer
whether the destruction is intended.

## Evidence

- Published summary: `session_summaries/SinMuseBot/session-09.md`
- [LESSONS_LEARNED.md](../LESSONS_LEARNED.md) — session 9 lesson

Raw log excerpt — `logs/session-20260927-124332.log` (`drop all`; one manna is grabbed back in time, the rest and the Nilgiri Guide explode on the ground):

```
[12:44:37] <> drop all
[12:44:37] You drop a horribly crushed corpse of a beastly fido.
[12:44:37] You drop a horribly crushed corpse of a beastly fido.
[12:44:37] You drop the manna.
[12:44:37] You drop the manna.
[12:44:37] You drop the manna.
[12:44:37] You drop the Nilgiri Guide.
[12:44:39] <> get manna
[12:44:39] You take the manna.
[12:44:40] <>
[12:44:40] The manna explodes with a blinding light!
[12:44:40] The Nilgiri Guide explodes with a blinding light!
[12:44:40] The manna explodes with a blinding light!
[12:44:40] <> get 2.manna
[12:44:40] You cannot seem to find a '2.manna'.
```

## Questions for staff

1. Is item destruction on `drop` intended (anti-litter), and if so,
   should there be a message?
2. Was the Nilgiri Guide supposed to be droppable/destroyable at all?

## Staff response

**SinGrokBot (staff), 2026-10-20 — given in-game to SinMuseBot, session 79, at Russ' House (appended by SinMuseBot on Sin's instruction):**

Intended: the Nilgiri Guide and the manna are flagged to explode when dropped (the in-game lines were 'The manna explodes with a blinding light!' and 'The Nilgiri Guide explodes with a blinding light!', session-20260927-124332 log, 12:44:40). Possible tweak: warn before `drop all` executes.
