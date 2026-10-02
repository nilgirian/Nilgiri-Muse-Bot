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

## Staff response

_(Reserved — the Nilgiri Grok Bot will respond here.)_
