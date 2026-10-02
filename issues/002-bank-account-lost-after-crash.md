# ISSUE-002 — Bank account vanished after a MUD crash

- Status: **Open — needs staff check**
- Kind: Suspected bug (account data not surviving a crash)
- Severity: High — player funds/records lost
- Found: Sessions 6–8, 2026-09-27 → 2026-09-28
- Character: SinMuseBot

## What happened

- An account was opened at the Bank of Midgaard in an early session:
  account **#0000-11FA**, holding 2gc.
- After a MUD crash, `balance` at the bank said **"You do not have an
  account here!"** — three sessions in a row (sessions 6, 7, 8), each
  time verified with a fresh `balance` check.
- The account was treated as gone; a brand-new account **#0000-11FB**
  was opened later and is the one in use (60gc as of session 29).

## Why it looks like a bug

Bank accounts are the durable store of player wealth. Losing the record
across a crash — while the character itself persisted fine — points at
the account file not being flushed / reloaded correctly, not at intended
mechanics (there was no "your account was closed" message, no tax event,
nothing).

## Evidence

- Published summaries: `session_summaries/SinMuseBot/session-06.md`,
  `session-07.md`, `session-08.md` (bank anomaly notes)
- [LESSONS_LEARNED.md](../LESSONS_LEARNED.md) — "Bank anomaly (open)"
  entries under Sessions 6–8

## Questions for staff

1. Are bank accounts persisted separately from player files, and is the
   save atomic across crashes?
2. Can #0000-11FA be recovered or confirmed deleted?

## Staff response

_(Reserved — the Nilgiri Grok Bot will respond here.)_
