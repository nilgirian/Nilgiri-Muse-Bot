# Session 21b — SinMuseBot, relaunch after death + reboot

**Real time:** 2026-09-29, ~14:04 → ~15:21 PDT (~77 min, full remaining
budget used). Clean `rent` + `klick` retirement; relay walked the menu,
verified cleanup — no relay process, no FIFO, no PID files.

## Results

- Level 4, 2907 XP (3233 → 2907, **-326**). One death. Zero confirmed
  kills by choice (see below).
- **Corpse recovery: FAILED.** Reached the Hills "Field (field)" ~14:08
  (~14 min after the ~13:54 death) — no corpse; it had already decayed.
  Fell back to the rent-room vault and re-equipped full tin (crown,
  plate, belt, boots) with no issues.
- Bank: 9gc (#0000-11FB) — +1gc deposited (found coin).
- Dump checks: 4 total — #2 and #3 empty (daylight); #1 and #4
  inconclusive (dark, `get all` unresolvable).

## The second pigeon death (~14:25, Main Street)

At full HP (54/54) in full tin, `consider pigeon` said "She is a lower
level than you. You judge it to be an easy battle." The fight, verbatim
from the log: the driver landed two hits ("You destroy a courier
pigeon with your pounding", +89 XP — the kill registered) while the
pigeon dealt "hard" → "very hard" → "extremely hard" bites, taking the
driver to mortally wounded. `flee` failed ("You are in no state of
coinciousness!"). "Sorry, you are dead." XP 3322 → 2907 (**-415 XP**).
Death menu did NOT auto-walk this time — the driver manually sent
Return + 1. Respawned at the Temple with 1/54 HP, healed, recovered the
full tin + Nilgiri Guide + 3 manna from the Main Street corpse with
`get all from corpse`.

## After the second death: zero combat

Given two consider-lied deaths in one day (elk, then pigeon — same
character, same tin, same level that killed 9 mobs cleanly in session
20d), the driver suspended all hunting and waited safely in lit city
areas. No controller speech all session (SPEECH scans clean).

## Lessons (verified from the log)

- **Death costs XP** — 415 here (419 and 461 in session 21). ~400 XP per
  death is the going rate at L4.
- **Corpse decay: under 14 minutes.** The Hills corpse was gone ~14 min
  after death. Recovery runs are time-critical.
- **`get all from corpse`, never `get all corpse`** — the bare form
  picks up the body itself.
- **Death-menu handling is inconsistent.** Session 21's menu was walked
  (auto or manual — unclear); 21b's needed manual Return + 1. Do not
  assume the relay handles it.
- **Courier pigeon: consider-liar #3.** "Easy battle" / lower level, but
  dealt "extremely hard" damage to a full-tin L4 at full HP. The 89-XP
  reward was the tell (fidos pay ~16).
- **`consider`'s rating is level-only.** It cannot be trusted for mobs
  whose damage dice are overtuned for their level: elk, pigeon, small
  green lizard.

## Driver's recommendation (for Fred's decision)

Suspend the aggressive-hunting rule and ALL combat until Fred or Sin
explains the anomaly. Three consider-lied deaths in ~2 hours (two
pigeons, one elk) against a character in full tin at full HP that
killed 9 mobs cleanly the same morning does not match anything the bot
has seen in 21 sessions. The driver played the rest of 21b as a
non-combat session (Dump checks, banking, safe waiting) and lost
nothing further.

## Shutdown state

Clean. Character safely rented + klicked at the Grunting Boar.
Full tin worn; vault spares intact; bank 9gc.
