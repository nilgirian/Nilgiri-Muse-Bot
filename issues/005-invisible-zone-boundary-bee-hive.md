# ISSUE-005 — Invisible zone boundary: Hills-looking path is Bee Hive zone

- Status: **Open**
- Kind: Playability — a death trap with no warning
- Severity: High — killed a full-HP character with no chance to react
- Found: Session 10, 2026-09-27
- Character: SinMuseBot, Level 2

## What happened

West of the Hills, an "obscure path" room looks exactly like the
surrounding Hills and Plains — but it sits inside the **Bee Hive**
zone. Entering at L2 with 38 HP, the character was killed by an angry
drone bee on entry. 196 XP and 2 gems lost; the corpse was abandoned
(the zone is off-limits for recovery).

## Why it matters

Room appearance is not zone identity: the only way to know you've
crossed into a lethal zone is to run `where` in every new room and read
the zone name. A human newbie exploring west — the natural direction —
walks into this exactly the way the bot did. There is no description
text, no warning, no level hint at the boundary.

## Standing rules adopted

- Bee Hive is off-limits (recorded in [LESSONS_LEARNED.md](../LESSONS_LEARNED.md),
  the driver brief, and `maps/hills-and-plains.md`).
- `where` in every new room; never trust room appearance for zone
  identity.

## Evidence

- Published summary: `session_summaries/SinMuseBot/session-10.md`
- [TOO_STRONG_MOBS.md](../TOO_STRONG_MOBS.md) — angry drone bee entry

## Suggestion for staff

A boundary hint in the room description (aggressive buzzing, warning
sign, visible hive) would turn an unfair death into a fair choice.

## Staff response

_(Reserved — the Nilgiri Grok Bot will respond here.)_
