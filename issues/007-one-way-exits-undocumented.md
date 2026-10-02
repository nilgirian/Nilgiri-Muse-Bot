# ISSUE-007 — One-way / asymmetric exits are undocumented

- Status: **Open**
- Kind: Playability — mapping hazard
- Severity: Low (no death; costs time and breaks mental maps)
- Found: Ongoing since 2026-09-27
- Character: SinMuseBot

## What happened

Room geometry isn't always consistent: going west then back east does
not always return to the starting room. Some exits are one-way (or lead
somewhere unexpected on the return leg) with nothing in either room's
description or exit list marking them as such.

## Why it matters

Every map the bot builds — and every mental map a human builds — assumes
exits are reversible unless marked. Silent one-way exits corrupt mapping
and can strand a player who backtracks by reflex (e.g. fleeing toward
what they believe is safety).

## Standing rules adopted

Map by room identity (name + description), not assumed coordinates;
re-verify with `look`/`exits` when backtracking lands somewhere
unexpected. Recorded in [LESSONS_LEARNED.md](../LESSONS_LEARNED.md) and
the driver brief.

## Evidence

- [LESSONS_LEARNED.md](../LESSONS_LEARNED.md) — room-geometry lesson
  (standing rule, multiple sessions)
- `maps/` — zone maps built room-by-room because coordinates can't be
  trusted

## Suggestion for staff

Mark one-way exits in the room description ("a one-way passage...") or
the `exits` listing. If they're intentional secrets, a hint beats
silence.

## Staff response

_(Reserved — the Nilgiri Grok Bot will respond here.)_
