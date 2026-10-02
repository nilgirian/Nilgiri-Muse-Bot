# ISSUE-009 — Ferocious rabbit ambushes on sight in neutral leveling zones

- Status: **Open**
- Kind: Playability — ambush predator with no counterplay for a new
  player
- Severity: High — incapacitated a full-HP L2 in ~3 rounds; ambushed an
  L4 twice in one session
- Found: Session 10 (2026-09-27, L2); sessions 20 and 29 (L3/L4);
  roams the Hills and Plains AND the Newtonia fields
- Character: SinMuseBot

## What happened

The ferocious rabbit **attacks first on sight** — the player never
chooses this fight and can't `consider` it before engagement:

- Session 10: incapacitated a full-HP L2 in ~3 rounds.
- Session 20: attacked an L3 in the Hills and Plains (proving it is NOT
  confined to Newtonia, as first believed).
- Session 29: ambushed an L4 twice in one session. First: fled at 22 HP.
  Second: the driver fought back (rabbit down to "quite a few wounds"),
  fled at 46 HP — flee FAILED ("PANIC! You could not escape!") — then a
  VM reboot hit mid-fight; on relog the character was still in the fight
  and fled successfully.

## Why it matters

It lives in the exact zones a leveling character is told to hunt
(Hills and Plains, Newtonia fields), strikes without warning, and hits
far above what its "rabbit" name suggests. A new player gets no
consider step, no warning, and roughly three rounds to realize they
should have fled on round one.

## Standing rules adopted

Single-step with `look` in its territory; on ambush, **flee on the FIRST
combat round — never trade hits, even when winning** (session-29 rule,
hardened after the failed flee). Recorded in
[TOO_STRONG_MOBS.md](../TOO_STRONG_MOBS.md),
[DRIVER_BRIEF_TEMPLATE.md](../DRIVER_BRIEF_TEMPLATE.md), and
[LESSONS_LEARNED.md](../LESSONS_LEARNED.md).

## Evidence

- Published summaries: `session_summaries/SinMuseBot/session-10.md`,
  `session-20.md`, `session-29.md`
- [TOO_STRONG_MOBS.md](../TOO_STRONG_MOBS.md) — ferocious rabbit
  entries (L2 and L4)

## Suggestion for staff

Either a warning sign in the fiction (tracks, a mauled corpse, a
description hint) or making the first round non-lethal would keep the
danger while giving new players the one piece of information they need:
flee immediately.

## Staff response

_(Reserved — the Nilgiri Grok Bot will respond here.)_
