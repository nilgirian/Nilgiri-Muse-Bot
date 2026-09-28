# Session 16 — Typical hunt, 1 hour (SinMuseBot)

**Date:** 2026-09-28, ~15:40–16:11 PDT + resume ~16:15–16:35 PDT (full 60-minute budget, split by a VM reboot)
**Character:** SinMuseBot, Level 3 (2370 → 2707 XP, +337)
**Result:** Clean hunt and clean retirement. 19 kills, zero deaths. Banked all gold (75gc), rent + klick exit, no strays.

## What happened

Fred authorized a one-hour typical hunt: Hills and Plains in daylight, Northern Main City after dark, beastly fidos as the proven target, rabbits off-limits. This was the first session run under the new responsiveness rules (event-driven ~2s wakes instead of 30–90s polling, batched movement on known routes).

**First leg (~15:40–16:11).** The driver checked `time` — dawn was coming — and headed out the West Gate into the Hills and Plains. Two field mice killed. Then a small green lizard that `consider` called an "easy battle" dodged nearly every attack while landing ~10 hard bites, dropping the bot from full HP to 27/47; the driver fled, rested back to full, and marked lizards as do-not-engage. Back inside the West Gate well before dark (~1:20 PM game time). Night phase: patrolled Main Street, Market/Common Squares, the alleys, and Central Bridge — 9 beastly fidos killed. Sin gossiped "what's your directive right now and for how long?" and the bot answered truthfully within the session (one-hour hunt, ~20 min in, hills by day / city by night, bank + rent + klick at time up).

**The reboot (16:11 PDT).** The VM rebooted a fourth time today (10:06, 13:37, 14:21, 16:11 — all confirmed via `who -b`), killing the relay mid-hunt with 31 minutes of the hour used. Per Fred's standing reboot rule, the relay was relaunched immediately with the remaining 29 minutes. SinMuseBot reconnected link-dead at Main Street west-1, still holding 3 gold coins and tin gear — one fido had died while it was link-dead during the outage.

**Resume (~16:15–16:35).** Eight more beastly fidos across the city (Common Square, Alley at Levee, Poor Alley, Market Square). All 4 carried gold coins deposited at the Bank of Midgaard — account #0000-11FB now **75gc** (banker's statement showed 71gc at session start, correcting the 69gc recorded in the session-15 summary). Walked to the Grunting Boar Reception, `rent`, `klick` in the private room; the relay walked the exit menu (Return, then `0` atomically) and the MUD closed the connection. Cleanup verified: no relay/ssh processes, no FIFO, no PID files.

## Kills (19 total)

All "is dead! R.I.P.", all corpses looted with `get all from corpse`:

| # | Mob | Location | XP |
|---|-----|----------|-----|
| 1 | beastly fido | Main Street west-1 | +27 |
| 2 | beastly fido | Main Street west-2 | +17 |
| 3 | field mouse | Field south of Outside West Gate | +8 |
| 4 | field mouse | Hill west of Field | +17 |
| 5 | beastly fido | Main Street west-2 | +32 |
| 6 | beastly fido | Main Street west-2 | +31 |
| 7 | beastly fido | Main Street east | +10 |
| 8 | beastly fido | Main Street east / Todai's | +7 |
| 9 | beastly fido | Main Street west-3 | +41 |
| 10 | beastly fido | Eastern end of Alley | +10 |
| 11 | beastly fido | Main Street west-1 | +14 |
| 12 | beastly fido | Main Street west-1 | +39 (died while link-dead during reboot) |
| 13 | beastly fido | Main Street west-1 | +0 (finished, already mortally wounded) |
| 14 | beastly fido | Common Square | +9 |
| 15 | beastly fido | Alley at Levee | +32 |
| 16 | beastly fido | West end of Poor Alley | +16 |
| 17 | beastly fido | Main Street east-2 | +23 |
| 18 | beastly fido | Market Square | +18 |
| 19 | beastly fido | Market Square | +0 (incapacitated by someone else, finished) |

One more fido was incapacitated (+25 XP) just before the reboot but the relay died before the kill was confirmed — not counted.

## Loot, bank, and inventory

- **Loot:** shiny gold coin (Common Square fido corpse), tin boots + tin belt (picked up at the Dump per the standing directive; belt equipped). All other corpses empty.
- **Bank:** 4 gold coins deposited (1 shiny + 3 coins). Account #0000-11FB: **75gc**. Zero gold on the character at exit.
- **Exit inventory:** tin boots ×2, tin belt (carried, plus one worn), tin chest plate, Nilgiri Guide; wearing tin crown + tin belt. HP 47/47. Ate a free half loaf at the bakery for hunger.
- **XP:** 2370 → 2707 (+337). Still Level 3 (Level 4 needs 3244).

## Social

- Answered Sin's gossip promptly and truthfully (responsiveness fix working).
- Gelu the God of Thalodia asked "did you know Rivin quit?" — answered in-character ("I had not heard that. Does that mean the 8th Age is ending?"). No reply; treated as conversation-only per the controller hierarchy (not an authorized controller).
- No speech from Sin, Motorola, Russ, or Mandessa during the resume.

## New lessons

- `consider` lies about small green lizards ("easy battle" — they dodge everything and hit hard). Do not engage.
- The Dump is pitch black at night (field-type room). Do not enter after dark; retreated immediately.
- Janitors pick up corpses — loot IMMEDIATELY after the kill, before anything else.
- Rent accepts wearable tin gear; only treasure-type valuables block it.
- Relay cleanup gap fixed: `scripts/mud_relay.py` now kills the FIFO holder and removes the FIFO/PID files on final exit.

Raw logs (local only): `logs/session-20260928-154000.log`, `logs/session-20260928-161500.log`.
