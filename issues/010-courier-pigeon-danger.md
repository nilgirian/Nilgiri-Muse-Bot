# ISSUE-010 — Courier pigeons in the city center far tougher than they look

- Status: **Open**
- Kind: Playability — danger wildly out of proportion to appearance and
  location
- Severity: High — killed a Level 4 twice (sessions 21/21b)
- Found: Sessions 21/21b (2026-09-29); probed sessions 22 and 29
- Character: SinMuseBot, Level 4

## What happened

Courier pigeons on Main Street / Market Square — the safest-looking
zone in the game — killed a full-HP, full-tin Level 4 **twice**:

- Session 21: `consider` said "you think you could do it"; the pigeon
  dealt "hard" → "very hard" → "extremely hard" bites and took the
  character from full HP to mortally wounded; `flee` failed.
- Session 21b: killed the bot again on Main Street.
- The 89-XP reward was the tell (fidos pay ~16): high XP = high danger,
  whatever `consider` says.

Later probes (Fred's re-test program, 2026-09-30): session 22 scored 4
confirmed courier kills with 0 deaths — but one fight reproduced the
"unhittable" death spiral (~9 straight misses, 54→26 HP) and only the
new `set noflee 27` autoflee backstop saved the character. Session 29
added 2 more clean kills at L4. Verdict: dangerous but survivable with
autoflee + flee-at-50% discipline — the danger is real, the appearance
is not.

## Why it matters

A new player in the starting city sees a pigeon, considers it ("you
think you could do it"), and dies. The `consider` rating, the cute
name, and the city-center location all agree it's safe; the damage
output disagrees lethally. This is the largest consider-vs-reality gap
found before the audit (`consider` liar #3, after the small green
lizard and the large elk).

## Standing rules adopted

Courier pigeon stays in [TOO_STRONG_MOBS.md](../TOO_STRONG_MOBS.md)
until a no-near-loss session: engage only solo, at full HP, fed and
watered, noflee armed, manual flee at 50% HP. Probe protocol in the
re-test queue.

## Evidence

- Published summaries: `session_summaries/SinMuseBot/session-21.md`,
  `session-21b.md`, `session-22.md`, `session-29.md`
- [TOO_STRONG_MOBS.md](../TOO_STRONG_MOBS.md) — courier pigeon entry
  (full history)

## Suggestion for staff

Either tune the pigeon's damage down to match its city-center placement
and consider rating, or make the fiction signal the danger (a scarred
veteran NPC warning about the birds, a description hint). Right now all
three signals — name, place, `consider` — point the wrong way.

## Staff response

_(Reserved — the Nilgiri Grok Bot will respond here.)_
