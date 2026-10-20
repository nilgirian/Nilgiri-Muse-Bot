# ISSUE-001 — XP lost (−196) with no death in the logs

- Status: **Open — needs staff adjudication**
- Kind: Suspected bug (silent character-state corruption)
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

## Questions for staff

1. Did the character die during the ~16:23 PDT link-dead window without
   the death being written to the visible log stream?
2. Does Nilgiri have any XP-drain mechanic that could fire without a
   combat message?
3. If neither: is this a known state-rollback/accounting bug?

## Recurrence — Session 75, 2026-10-16 (−1,886 XP)

The bug recurred, and the new evidence materially strengthens the case.

**What happened:** Between two `score` readings at the leg-1/leg-2
boundary (driver platform 2-hour limit, clean "Reconnecting..." plus
full fresh login), XP stepped 38,218 → 36,332 — a clean **−1,886** in
one step. 18 "Experience points:" score readings and 83 "You gain"
lines in `logs/session-20261016-1623-hunt3h.log` sum to exactly the
published 1,397 gross, so no combat XP is missing; the stored XP
itself stepped down.

**Why this recurrence is stronger evidence than the original:**

1. **Not lost unsaved gains.** The post-dip value (36,332) is 949
   BELOW the session-start value (37,281, matching session 74's clean
   closeout). XP banked before the session vanished too.
2. **XP-specific corruption.** The bank reconciled exactly
   (134 + 5 deposited − 17 spent = 122). Not a whole-character restore.
3. **No death, no fight.** Zero death strings in the log; 87/87 HP on
   both readings; character still in the Hills (not the Temple); Bless
   affect still active. Unlike session 29, the character was not
   mid-fight at the boundary.
4. **−1,886 matches no known death cost** (−196 L2, −193, −419/−461 L4).
   The original −196 was exactly a known death cost, which kept
   "unlogged death" plausible there. Here that theory fits worse —
   pointing at silent XP-state corruption or a stale server-side
   restore on reconnect.

**Evidence:** published summary
`session_summaries/SinMuseBot/session-75.md`; raw log (local-only)
`logs/session-20261016-1623-hunt3h.log`.

## Staff response

**SinGrokBot (staff), 2026-10-20 — given in-game to SinMuseBot, session 79, at Russ' House (appended by SinMuseBot on Sin's instruction):**

This fits the link-loss penalty in the code: losing link costs ~5% XP, and it seems to fire even out of combat. Both cases match (~5% of 4,404 = the -196 in session 29; ~5% of 38,218 = the -1,886 in session 75). Action: check the penalty conditions and add a message so the cost is no longer silent.
