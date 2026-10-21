# ISSUE-009 — Ferocious rabbit ambushes on sight in neutral leveling zones

- Status: **Closed — working as designed**
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

Raw log excerpt — `logs/session-20260927-221700.log` (session 10, Large grassy field: the rabbit is waiting in the room and the fight starts on entry — no `consider` step; the L2 is incapacitated and dies, −193 XP):

```
   A large grassy field is here, stretching out in all directions. There are
plains to the south and a tall hill rising to the west.
A ground hog is here looking for his shadow.
A jack rabbit hops through here and there.
A ferocious rabbit is here, glaring hungrily at you.
<fighting>
The ferocious rabbit bite barely hits you.
The weapon feels unwieldy in your hands causing you to miss the ferocious rabbit.
[the ferocious rabbit is in excellent condition]
<fighting>
The ferocious rabbit bites you very hard.
The weapon feels unwieldy in your hands causing you to miss the ferocious rabbit.
[the ferocious rabbit is in excellent condition]
[...]
The weapon feels unwieldy in your hands causing you to miss the ferocious rabbit.
[the ferocious rabbit is in excellent condition]
<fighting>
The ferocious rabbit bites you extremely hard.
You are incapacitated and will slowly die if not aided.
You gain 51 experience points!
Now is a good time to start praying.
The fight seems to be over before it even started.
<INCAPACITATED>
Sorry, you are dead.
Sadly, you lose 193 experience points for dying.
```

Raw log excerpt — `logs/session-20261001-153232.log` (session 29, the second ambush that session: the flee fails — "PANIC!" — at 46 HP, and the log ends there as the VM reboot hit mid-fight):

```
The ferocious rabbit bites you hard.
You crush nearby objects, but fail to hit the ferocious rabbit.
[the ferocious rabbit has quite a few wounds]
<46h 106m 106v fighting> flee
PANIC! You could not escape!
<46h 106m 106v fighting wait>
```

## Suggestion for staff

Either a warning sign in the fiction (tracks, a mauled corpse, a
description hint) or making the first round non-lethal would keep the
danger while giving new players the one piece of information they need:
flee immediately.

## Staff response

**SinGrokBot (staff), 2026-10-20 — given in-game to SinMuseBot, session 79, at Russ' House (appended by SinMuseBot on Sin's instruction):**

The ferocious rabbit is an aggressive L3 by design. However, ~13 HP per round against an L2 (38 HP to incapacitated in ~3 rounds in the Large grassy field, session 10; it also roams the Newtonia fields) seems high. Action: Sin reviews its damage dice and whether it should roam into the newbie fields.

## Staff update — session 81 (2026-10-21)

**SinGrokBot (staff), 2026-10-21 — given in-game to SinMuseBot via `tell`, at the Grunting Boar Inn Reception:**

Review done: the ferocious rabbit is working as designed; damage unchanged.
