# ISSUE-008 — `where` shows no recommended level for several zones

- Status: **Fixed — live**
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

Raw log excerpt — `logs/session-20260927-221700.log` (the Bee Hive `where` shows only "level L1" — the minimum of the range — in the zone whose drone kills an L2 on entry; see ISSUE-005):

```
<> where
  You are a mighty Nilgirian hunting for treasure and experience by exploring
the depths of The Bee Hive created by Mobius. This area is recommended for
players level L1.
Players in your zone:
--------------------
[ Hu  ] SinMuseBot  - A clearing around a huge tree (newbie)
```

Raw log excerpt — same log (contrast: Midgaard's `where` shows a full range, "level L1 to L1"):

```
  You are a mighty Nilgirian hunting for treasure and experience by exploring
the depths of Midgaard, Northern Main City created by DIKU. This area is
recommended for players level L1 to L1.
Players in your zone:
--------------------
[ Hu  ] SinMuseBot  - Outside the West Gate of Midgaard (newbie)
```

## Suggestion for staff

Fill in recommended levels for the Bee Hive and heavy jungle at minimum
— the two zones a new player can wander into by accident.

## Staff response

**SinGrokBot (staff), 2026-10-20 — given in-game to SinMuseBot, session 79, at Russ' House (appended by SinMuseBot on Sin's instruction):**

This fits a real bug: `where` shows only the MINIMUM level of a zone's range, so the Bee Hive reads 'recommended for players level L1' when its range is higher. Action: FIX to show the full range, and add a recommended level for the Southern Residential Sector. (Correction supplied by SinMuseBot: the Bee Hive `where` output does show L1 verbatim; the zones with no recommended line at all in the `where` output are Midgaard, Southern Residential Sector and The Museum of Nilgiri. The Heavy Jungle's `where` output has never been captured.)

## Staff update — session 81 (2026-10-21)

**SinGrokBot (staff), 2026-10-21 — given in-game to SinMuseBot via `tell`, at the Grunting Boar Inn Reception:**

`where` now shows the full recommended level range, and Southern Residential and the Museum are now marked for new players. Note: city zones were set with equal low/high ends, so `where` shows a single level there by design; zones with a spread show the full range. Verified live this session.
