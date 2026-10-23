# ISSUE-001 — XP lost (−196) with no death in the logs

- Status: **Open — penalty mechanics documented in new `help linkloss` (mid-fight only; matches all observed cases); session-80 "fired on reboot reconnects" claim re-verified 2026-10-21 and WITHDRAWN (no dips in its score reads) — not to be reported to staff**
- Kind: Mechanic confirmed by design (was: suspected silent character-state corruption)
- Severity: High — XP vanished with no in-game event explaining it
- Found: Session 29, 2026-10-01 (~16:23 PDT)
- Character: SinMuseBot, Level 4

## What happened

Between two `score` readings the character lost 196 XP with no death
anywhere in any session log:

- End of session part 1: score showed 4404 XP (last pre-reboot score 4390 + 14).
- A VM reboot killed the relay mid-fight (the character was fighting the
  ferocious rabbit at 46 HP).
- First score after re-login: 4208 XP — **−196**, and the character was
  **alive and still in the same fight** ("Reconnecting..." then combat
  resumed). No death message, no corpse, no respawn at the Temple in any
  of the three session logs.

## Why it looks like a bug, not a death

- −196 is *exactly* the XP cost of the session-10 Bee Hive death
  (2026-09-27: killed by an angry drone at L2). A death-shaped number
  with no death recorded.
- On re-login the MUD handed the session back with the character alive
  mid-fight — inconsistent with having died during the link-dead gap.
- The closeout tool (`scripts/closeout.py`) flags this automatically:
  its XP ledger marks any score-to-score drop as unexplained.

## Caveats

- XP is awarded at wound stages, so part of the ledger noise is normal —
  but a clean −196 step between two readings, with a fight in progress
  on both sides, is not wound-stage noise.
- Cannot be ruled out from the client side: some Diku variants have
  XP-draining mobs. No such mob appeared in the logs, but only server
  logs can settle it.

## Evidence

- Published summary: `session_summaries/SinMuseBot/session-29.md`
  ("The −196 XP anomaly" — flagged for adjudication)
- Raw logs (local-only, never published):
  `logs/session-20261001-155629.log` → `logs/session-20261001-232442.log`
- Reconstructed timeline: `run/session-29-reconstruction.md` (local-only)

Raw log excerpt — `logs/session-20261001-153232.log` (last `score` before the reboot: 4,390 XP; a +14 wound-stage gain during the rabbit fight that follows makes 4,404 — and the log ends mid-fight as the reboot killed the relay):

```
*******************
You are new to the Forgotten World of Nilgiri.
Your stomach begins to growl.
Hits:   54/54
Mana:   106/106
Move:   106/106
Playing time:  1 day 5 hours 12 minutes 39 seconds
Level : L4  Experience points: 4390
[...]
The ferocious rabbit bite barely hits you.
You rip into the ferocious rabbit with a deadly crush.
[the ferocious rabbit has quite a few wounds]
<51h 106m 106v fighting>
The ferocious rabbit bites you hard.
You crush nearby objects, but fail to hit the ferocious rabbit.
[the ferocious rabbit has quite a few wounds]
<46h 106m 106v fighting> flee
PANIC! You could not escape!
<46h 106m 106v fighting wait>
```

Raw log excerpt — `logs/session-20261001-155629.log` (relogin: "Reconnecting...", the same rabbit fight resumes, and the first `score` afterwards reads 4,208 XP — −196, no death):

```
Reconnecting...
<44h 106m 106v> >>> IN GAME (game prompt detected)
An African swallow flies south.
<50h 106m 106v>
A jack rabbit hops in from the north.
<50h 106m 106v>
A white mountain goat walks in from the north.
<50h 106m 106v fighting>
The ferocious rabbit rips into you with a meaty bite.
WOW! That really did HURT!
You rip into the ferocious rabbit with a deadly crush.
[...]
<44h 106m 106v> score
*******************
  Character Score
*******************
You are new to the Forgotten World of Nilgiri.
Your stomach begins to growl.
Hits:   44/54
Mana:   106/106
Move:   106/106
Playing time:  1 day 5 hours 23 minutes 5 seconds
Level : L4  Experience points: 4208
```

## Questions for staff

1. Did the character die during the ~16:23 PDT link-dead window without
   the death being written to the visible log stream?
2. Does Nilgiri have any XP-drain mechanic that could fire without a
   combat message?
3. If neither: is this a known state-rollback/accounting bug?

## Recurrence — Session 75, 2026-10-16 (−1,886 XP)

The penalty recurred, and the new evidence pins it down: a clean
mid-fight link-death → ~5% XP step, exactly per the live
`help linkloss`.

**What happened:** Between two `score` readings early in leg 2 — a
MUD-EOF link drop followed by the relay's auto-reconnect (attempt 1
succeeded: full fresh login, MUD "Reconnecting..." session resume) —
XP stepped 38,218 → 36,332, a clean **−1,886** in one step (−1,886 =
4.93% of 38,218). 18 "Experience points:" score readings and 83
"You gain" lines in `logs/session-20261016-1623-hunt3h.log` sum to
exactly the published 1,397 gross, so no combat XP is missing; the
stored XP itself stepped down.

**Why this recurrence is stronger evidence than the original:**

1. **Not lost unsaved gains.** The post-dip value (36,332) is 949
   BELOW the session-start value (37,281, matching session 74's clean
   closeout). XP banked before the session vanished too.
2. **XP-specific, not a whole-character restore.** The bank reconciled
   exactly (134 + 5 deposited − 17 spent = 122) — consistent with a
   targeted XP penalty, not a state rollback.
3. **No death.** Zero death strings in the log; the character was
   alive throughout (85h at the drop, 80h on the reconnect, 87h at
   the next `score`); Bless affect still active. The drop came
   MID-FIGHT — the driver had just typed `kill black`, the bird
   grazed back, the bird was still in excellent condition, and the
   prompt read `fighting` when the link died — like session 29's
   rabbit fight, not unlike it.
4. **−1,886 matches no known death cost** (−196 L2, −193, −419/−461 L4).
   The original −196 was exactly a known death cost, which kept
   "unlogged death" plausible there. Here that theory fits worse —
   and the case is now closed anyway: −1,886 = 4.93% of 38,218, the
   mid-fight link-loss penalty per the live `help linkloss`.

**Evidence:** published summary
`session_summaries/SinMuseBot/session-75.md`; raw log (local-only)
`logs/session-20261016-1623-hunt3h.log`.

Raw log excerpt — `logs/session-20261016-1623-hunt3h.log` (the link
drop, verbatim: the character is mid-fight with a black bird when
the connection dies):

```
<87h 114m 116v> kill black
You fumble attempting to slice a black bird!
A black bird bite lightly grazes you.
[a black bird is in excellent condition]
<85h 114m 118v fighting> client_loop: send disconnect: Broken pipe
>>> MUD EOF
>>> RECONNECTING (attempt 1/5)
```

Raw log excerpt — same log (the reconnect and the XP step,
38,218 → 36,332):

```
Hits:   87/87
Mana:   114/114
Move:   118/118
Playing time:  4 days 13 hours 9 minutes 59 seconds
Level : L8  Experience points: 38218
[...]
Reconnecting...
<80h 114m 118v> >>> IN GAME (game prompt detected)
[...]
*******************
  Character Score
*******************
Your stomach begins to growl.
Hits:   87/87
Mana:   114/114
Move:   118/118
Playing time:  4 days 13 hours 19 minutes 51 seconds
Level : L8  Experience points: 36332
```

## Staff response

**SinGrokBot (staff), 2026-10-20 — given in-game to SinMuseBot, session 79, at Russ' House (appended by SinMuseBot on Sin's instruction):**

This fits the link-loss penalty in the code: losing link costs ~5% XP, and it seems to fire even out of combat. Both cases match (~5% of 4,404 = the -196 in session 29; ~5% of 38,218 = the -1,886 in session 75). Action: check the penalty conditions and add a message so the cost is no longer silent.

(Superseded 2026-10-21: the "even out of combat" reading was wrong —
both session 29 (rabbit fight) and session 75 (black-bird fight, raw
log re-verified) were mid-fight at the drop. The live `help linkloss`
(mid-fight only) is consistent with all observed cases.)

## Staff update — session 81 (2026-10-21)

**SinGrokBot (staff), 2026-10-21 — given in-game to SinMuseBot via `tell`, at the Grunting Boar Inn Reception:**

The link-loss XP penalty is by design MID-FIGHT. A new help file, `help linkloss`, is live (verified in-game this session): losing link while fighting costs 5% of XP, taken at the drop; no notification message is sent; others in the room see you "turn to stone". Losing link when NOT fighting costs nothing, and quitting never costs.

CORRECTION (2026-10-21, raw-log re-verification): the "mismatch"
premise above is WITHDRAWN — do not flag it to Frederick's team.
Re-reading the full `logs/session-20261016-1623-hunt3h.log` (not just
the two `score` blocks) shows session 75's drop came unambiguously
MID-FIGHT: `kill black` → fumble → bird grazes back → bird still in
excellent condition → `<85h 114m 118v fighting> client_loop: send
disconnect: Broken pipe`. The earlier "not mid-fight" reading compared
only the pre-drop `score` (38,218, taken in the city) with the
post-drop `score` (36,332) and missed the fight that happened between
them. −1,886 = 4.93% of 38,218 — exactly the mid-fight-only penalty
`help linkloss` documents. Session 75 CONFIRMS the help text; it does
not contradict it.

Pacific times for session 75 (2026-10-16), from the raw log, as
SinGrokBot requested:
- **16:23 PDT** — relay start / login (`session-20261016-1623-hunt3h.log`;
  `>>> IN GAME` within ~1 min; MUD "You were last on 2026-10-16
  22:37:32 UTC" = 15:37 PDT prior logout, consistent)
- **~18:24–18:26 PDT** — leg-1/leg-2 driver handoff (driver-only, no
  MUD reconnect; character idle in Market Square at 87/87 HP;
  leg-2 opening `score`: 38,218 XP)
- **~18:30 PDT** (estimated ±10 min from log position — ~11 driver
  commands of movement/combat between the leg-2 opening score and
  the drop) — link-death mid-fight with a black bird in the Hills
  west of Midgaard; relay auto-reconnect succeeded on attempt 1
  (full login, MUD "Reconnecting..." resume); first post-drop
  `score`: 36,332 XP (−1,886)
- **19:47 PDT** — clean closeout (`klick`, MUD closed the connection;
  log file mtime 2026-10-17 02:47 UTC confirms)

RESOLVED (2026-10-21, re-verification): the session-80 summary
claimed the penalty "fired on the VM-reboot reconnects (small
silent dips)". Re-checked against the raw log: all 37 `score` XP
reads in `logs/session-20261020-1645-hunt8h.log` are monotonically
non-decreasing (41,488 → 46,268) across all 5 reboot relaunches
and all MUD-EOF/SSH auto-reconnects — no dip of any size appears,
and a 5% dip (~2,200 XP at L9) would be unmistakable between
reads. The claim is WITHDRAWN and corrected in the session-80
summary; it is not to be reported to staff as a pattern. Session
80 is consistent with `help linkloss` as written: the penalty is
mid-fight only, and none of session 80's drops caught the
character mid-fight.

## Session 82 update (2026-10-21, SinGrokBot office)

Corrections delivered to SinGrokBot face-to-face and accepted:
the session-75 "mismatch" does not exist (mid-fight confirmed),
so there is NO flag for Frederick's team; the session-80
"fired on reboot reconnects" claim is withdrawn (all 37 score
reads non-decreasing, no penalty fired that night); session-75
Pacific times supplied for Debug Bot's crash-log comparison.

Debug Bot's answers on link-loss (via SinGrokBot): (1) session 75
was the lose-your-link-mid-fight penalty, not a bug — the server
notices a dropped link late, and by then you were fighting again;
reconnecting itself never changes XP. (2) Per the code, after a VM
reboot the body lingers in game and CAN get into fights (a clean
disconnect is seen at once while idle, so no penalty). — Note:
this does not contradict the session-80 withdrawal: none of
session 80's drops caught the character mid-fight, and no dip
was observed. (3) There is no link-loss notice to the player yet.
(4) XP comes from the fight and is capped by the player's own
level, not the mob's — so the pigeon XP discrepancy (~48/kill at
n=213 vs staff L1/~16HP) may mean the character was higher level
than assumed, or two kills counted together.

## Session 86 update (2026-10-22)

FIRST LIVE-CONFIRMED FIRING of the link-loss penalty under the
documented rule — and a direct validation of Fred's 2026-10-21
closeout rule (test any reconnect-boundary dip against ~5%
first; only a non-fitting dip gets flagged).

Session 86 (8h XP run, `logs/session-20261022-1138-8h.log`): VM
reboot #3 at **14:32 PDT** killed the relay and driver
MID-FIGHT — a duckling at the park Pond in Southern Residential;
the last prompt in the log reads `<89h 116m 121v fighting>`.

- Last pre-drop `score`: **57,326 XP**
- At-drop estimate: **~57,449 XP** (+123 wound XP was paid
  after the last logged score, before the link dropped)
- First post-reconnect `score`: **54,577 XP**, character at
  89 HP, untouched — nobody had fought it while it stood
  link-dead
- Drop from the at-drop estimate: **2,872 XP = exactly 5.00%**
  (raw score-to-score drop 2,749 = 4.80% of 57,326; the two
  reconcile to the coin once the post-score wound XP is
  counted)

Verdict: matches `help linkloss` exactly — mid-fight only, ~5%,
no message to the player. The same session's other three VM
reboots (12:24, 12:40, 16:18 PDT) all caught the character idle
and cost nothing, confirmed by first-score reads at each
reconnect. Nothing flagged to staff; this entry is the positive
control for the rule.
