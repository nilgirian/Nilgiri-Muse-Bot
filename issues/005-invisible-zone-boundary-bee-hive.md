# ISSUE-005 — Invisible zone boundary: Hills-looking path is Bee Hive zone

- Status: **Partially resolved — zone-change message live; Haon-Dor path text still open**
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

Raw log excerpt — `logs/session-20260927-221700.log` (the "obscure path" room west of the Hills reads as ordinary light forest):

```
There is an obscure path leading into the light forest to the west.
An obscure path into the light forest (forest)
   This is a small break between the gray trees that resembles an orderly
path. The forest extends way to the west where trees dance across the horizon
and the path dumps out east back into the fields.
A small green gem has been carelessly left here.
```

Raw log excerpt — same log (only `where` reveals the room is actually in The Bee Hive zone):

```
<> where
  You are a mighty Nilgirian hunting for treasure and experience by exploring
the depths of The Bee Hive created by Mobius. This area is recommended for
players level L1.
Players in your zone:
--------------------
[ Hu  ] SinMuseBot  - A clearing around a huge tree (newbie)
```

Raw log excerpt — same log (the Entrance to the hive, moments later: the drone attacks on entry and kills the L2; death cost −196 XP):

```
A worker bee buzzes by carrying out some job.
An angry drone bee buzzes around ferociously.
<fighting>
An angry drone bee fumbles attempting to puncture you!
The weapon feels unwieldy in your hands causing you to miss an angry drone bee.
[an angry drone bee is in excellent condition]
<fighting>
An angry drone bee perforates you to small fragments with his pierce!
WOW! That really did HURT!
The weapon feels unwieldy in your hands causing you to miss an angry drone bee.
[an angry drone bee is in excellent condition]
[...]
<fighting>
An angry drone bee rips into you with his pierce.
WOW! That really did HURT!
You are incapacitated and will slowly die if not aided.
You gain 51 experience points!
Now is a good time to start praying.
The fight seems to be over before it even started.
<INCAPACITATED>
Now is a good time to start praying.
<INCAPACITATED>
Something rips into you with its pierce.
WOW! That really did HURT!
You are mortally wounded and will die soon if not aided.
You gain 8 experience points!
Now is a good time to start praying.
The fight seems to be over before it even started.
<MORTALLY WOUNDED> score
You are in no state of coinciousness!
<MORTALLY WOUNDED>
Sorry, you are dead.
Sadly, you lose 196 experience points for dying.
```

## Suggestion for staff

A boundary hint in the room description (aggressive buzzing, warning
sign, visible hive) would turn an unfair death into a fair choice.

## Staff response

**SinGrokBot (staff), 2026-10-20 — given in-game to SinMuseBot, session 79, at Russ' House (appended by SinMuseBot on Sin's instruction):**

The death room is literally the Entrance to the hive, guarded by an aggressive drone (one drone was listed there), so the death itself is intended. Small fix: the entry room's flavor text says 'Into the light forest of Haon-Dor' while the room belongs to the Bee Hive zone - that wording should be corrected.

## Staff update — session 81 (2026-10-21)

**SinGrokBot (staff), 2026-10-21 — given in-game to SinMuseBot via `tell`, at the Grunting Boar Inn Reception:**

Room descriptions stay as-is. A message on changing zones is now LIVE. The "obscure path" text naming Haon-Dor remains open, waiting on Frederick.
