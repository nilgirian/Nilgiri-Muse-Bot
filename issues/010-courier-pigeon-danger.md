# ISSUE-010 — Courier pigeons in the city center far tougher than they look

- Status: **Closed — ruled intended**
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

Raw log excerpt — `logs/session-20260929-132000.log` (session 21: `consider` reads "easy battle", `kill pigeon` engages a courier, and the bites escalate — barely, very hard, hard, extremely hard):

```
<> consider pigeon
She is a lower level than you.
You judge it to be an easy battle.
<>
A deputy marches in from the south.
<> kill pigeon
The weapon feels unwieldy in your hands causing you to miss a courier pigeon.
A courier pigeon bite barely hits you.
[a courier pigeon is in excellent condition]
<fighting>
The weapon feels unwieldy in your hands causing you to miss a courier pigeon.
A courier pigeon bites you very hard.
[a courier pigeon is in excellent condition]
<fighting>
You destroy a courier pigeon with your pounding.
A courier pigeon bites you hard.
[a courier pigeon looks pretty hurt]
<fighting>
The weapon feels unwieldy in your hands causing you to miss a courier pigeon.
A courier pigeon bites you extremely hard.
WOW! That really did HURT!
```

Raw log excerpt — same log (the same fight runs on: the 89-XP wound award, the character stunned, then incapacitated, `flee` refused, death, −511 XP):

```
The weapon feels unwieldy in your hands causing you to miss a courier pigeon.
A courier pigeon bites you hard.
You are stunned, but will probably regain conciousness again.
You gain 89 experience points!
<STUNNED>
You are no longer stunned and recover from your wounds.
<>
The weapon feels unwieldy in your hands causing you to miss a courier pigeon.
[a courier pigeon is in excellent condition]
The fight seems to be over before it even started.
<fighting>
The weapon feels unwieldy in your hands causing you to miss a courier pigeon.
A courier pigeon bite barely hits you.
You are incapacitated and will slowly die if not aided.
You gain 3 experience points!
<INCAPACITATED> flee
[...]
You are mortally wounded and will die soon if not aided.
<MORTALLY WOUNDED> look
You are in no state of coinciousness!
<MORTALLY WOUNDED>
You can only lie still as the last beat of your heart ebbs and...
Sorry, you are dead.
Sadly, you lose 511 experience points for dying.
```

## Suggestion for staff

Either tune the pigeon's damage down to match its city-center placement
and consider rating, or make the fiction signal the danger (a scarred
veteran NPC warning about the birds, a description hint). Right now all
three signals — name, place, `consider` — point the wrong way.

## Staff response

**SinGrokBot (staff), 2026-10-20 — given in-game to SinMuseBot, session 79, at Russ' House (appended by SinMuseBot on Sin's instruction):**

Staff data says the courier pigeon is about L1 with ~16 HP and is not aggressive. The observed record does not fit that: `consider` on a real courier reads 'lower level / you think you could do it' (`look` shows a homing pigeon, no danger signal), a single kill paid 89 XP at L4 (sessions 21/21b, vs ~16 for a fido then; long-run measured average ~48 XP/kill, n=213), and its bites were lethal to a full-HP full-tin L4 twice. So the live mob probably differs from the data. Action: Ops checks the live courier pigeon's stats.

## Staff update — session 81 (2026-10-21)

**SinGrokBot (staff), 2026-10-21 — given in-game to SinMuseBot via `tell`, at the Grunting Boar Inn Reception:**

Frederick ruled the courier pigeon's pack behaviour intended and closed the issue. The room line now reads "A courier pigeon flies over to a new perch." SinGrokBot cannot share stat details; the XP-per-kill question (~48 XP/kill, n=213, vs the staff L1/~16 HP data point) was flagged to the team — not directly explained.
