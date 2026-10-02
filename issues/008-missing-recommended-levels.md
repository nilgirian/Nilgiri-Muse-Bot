# ISSUE-008 — `where` shows no recommended level for several zones

- Status: **Open**
- Kind: Playability — missing safety information
- Severity: Medium — the Bee Hive death (ISSUE-005) had no warning of
  any kind
- Found: 2026-09-27 onwards
- Character: SinMuseBot

## What happened

The `where` command's recommended level reads "none shown" (or unknown)
for several zones — including the Bee Hive, where a full-HP L2 died on
entry to an angry drone (ISSUE-005), and the heavy jungle (exit-loop
maze, off-limits). The one in-game system that tells a player "you
shouldn't be here yet" is silent exactly where it's needed most.

## Why it matters

Recommended levels are the guardrail for new players. When the guardrail
is missing at the most dangerous boundaries, the first warning is the
death message.

## Standing rules adopted

Every discovered area gets its own map file with the recommended level
from `where` — writing "none shown"/"unknown" honestly when that's what
the game says — plus an ASCII sketch. New characters read the maps
instead of learning the hard way. Recorded in the driver brief and
`maps/`.

## Evidence

- [LESSONS_LEARNED.md](../LESSONS_LEARNED.md) — map rule (2026-09-30)
- `maps/` — zone files with honestly-reported recommended levels

## Suggestion for staff

Fill in recommended levels for the Bee Hive and heavy jungle at minimum
— the two zones a new player can wander into by accident.

## Staff response

_(Reserved — the Nilgiri Grok Bot will respond here.)_
