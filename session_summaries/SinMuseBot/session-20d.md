# Session 20d — SinMuseBot treasure hunt, third relaunch (clean retirement)

**Real time:** 2026-09-29, 11:48:23 → ~12:36 PDT (~48 min of the 60-min
budget; retired ~12 min early, clean and deliberate). **First session of
the day to end WITHOUT a reboot:** normal `rent` + `klick` retirement at
the Grunting Boar Inn, relay walked the exit menu, verified cleanup —
no relay process, no FIFO, no PID files.

## Results

- Level 4, 3960 XP (3598 → 3960, **+362**). Zero deaths.
- **7 confirmed kills** (all R.I.P., all corpses empty):
  1–2. Beastly fido x2 — Main Street
  3. Field mouse — Hills
  4. Jack rabbit — Field
  5. Prairie dog — Hills
  6–7. Beastly fido x2 — Main Street
  - Plus **2 courier pigeons** (bakery, Main Street) — Fred's
    aggressive-hunting correction applied live from 12:32; corpses empty.
- **Treasure:** Dump check #1 (~12:00) hit **4x tin chest plates + 3x tin
  crowns** (7 items). Dump check #2 (~12:26): a plate and crown were
  visible but **dissolved before they could be grabbed**.
- **Wearing full tin:** crown (head), chest plate (body), belt (waist),
  boots (feet) + newbie shield/shorts/staff.
- **Rent-room vault: 3x tin chest plates, 3x tin boots, 2x tin crowns,
  4x tin belts** — 12 spare items stashed safely via rent → drop →
  `leave` (no klick). Fred's vault rule worked exactly as designed.
- Bank: 8gc (#0000-11FB) — no change; no gold found.
- Carrying at exit: 2 oil lamps (one lit), Nilgiri Guide. (Rent keeps
  the rest safe.)

## Sin's live orders (all followed)

Gear swap to non-newbie → `equipment` check → rent-room gear-up and
stash spares → remove vest, wear tin plate (the earlier "no wear slot"
was the occupied slot — Sin was right) → same trick worked for boots →
drop the replaced leather → try pigeons → consider first.

## Lessons

- **Dump items dissolve.** A plate and crown vanished between `look`
  and grab. New rule: `get all` IMMEDIATELY on entering the Dump —
  never `look` first.
- **Newbie gear self-destructs when dropped.** The replaced black
  leather vest **exploded** on the ground. (Extends the old `drop all`
  lesson: dropping is destructive, full stop — except in the rent
  room.)
- **SPEECH nag: 3-for-3, but slow.** The nag fired repeatedly and every
  gossip was eventually answered — but the driver kept answering late
  (mid-combat), missing the 10-second target several times. The nag is
  a reliable backstop, not a responsiveness fix; the driver still needs
  to break off and answer first.

## Fixes in production

- Tunnel-timeout fix: holding — zero stalls, zero transport drops.
- Rent-room vault rule (new today): worked — 12 items stashed, session
  continued via `leave` with no exit menu.
- Aggressive-hunting rule (new today): 2 pigeon kills within minutes of
  the correction.

## Notes

- Combined session 20 (all four legs: 20, 20b, 20c, 20d): ~145 min
  played of 300 budgeted across the day, 3 VM reboots survived, ended
  L4 at 3960 XP (from 2791, +1169), full tin equipped, 12-item vault,
  bank 8gc, zero deaths.
