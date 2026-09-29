# Session 20b — SinMuseBot treasure hunt, relaunch (terminated by VM reboot)

**Real time:** 2026-09-29, 10:36:43 → ~10:57 PDT (~20 min of the 120-min
budget; ~100 min unused). **Ended abnormally:** the VM rebooted at
~10:57 (`who -b` confirms) — the SECOND reboot today — killing the
relay, SSH, and FIFO instantly with zero log markers. The driver
detected it via stale heartbeat + `who -b`, cleaned up the dead
`/tmp/mud_cmd` file, and reported. TIME UP never fired. SinMuseBot is
link-dead in the Large grassy field area, Hills and Plains.

This was a relaunch of session 20 (killed 09:19 by the first reboot)
on a fresh 2-hour budget from Fred.

## Results

- **Reboot survival check (passed):** everything survived the 09:19
  link-dead hour — all inventory intact including the unbanked Dump
  treasure (spare belt+boots), XP 3303, bank 8gc. The MUD handed the
  session straight back on relogin.
- Level 4, ~3551 XP (3303 at login; 3370 verified by `score`; +~181
  from kills after the last score). Zero deaths.
- **2 confirmed kills** (both with R.I.P., both corpses looted empty):
  1. Field mouse — Valley in the hills
  2. Jack rabbit — Large grassy field (fled south once, pursued)
  - Plus one unconfirmed kill in the dark south of the gate (+67 XP —
    ambushed in pitch black, never saw what it was).
- **Treasure:** none. Dump check #1 (~10:50, lamp-lit) and #2 (~10:57):
  both empty. All corpses empty.
- Bank: 8gc (#0000-11FB) — no deposits (no gold found).
- Inventory at link-dead: 1x tin belt **worn** (equipped this session),
  1x tin belt, 2x tin boots (unwearable — "no place to wear"), 2x oil
  lamp (one lit), Nilgiri Guide. Fed and watered.
- HP was 54/54 after resting; took damage in a rabbit fight; final HP
  unknown.

## The fixes, tested in production

- **SPEECH nag: WORKED.** Sin gossiped "when is the next Dodger game?"
  and the driver missed the original flag (it wasn't running the
  bulletproof grep scan on every wake). The relay's
  `>>> SPEECH-PENDING` fired at 15s/30s/60s exactly as designed — that
  is how the driver caught it. The driver's first reply attempt was
  eaten by a transport drop (broken pipe); it re-sent after the relay
  reconnected and the MUD confirmed delivery. (Sin's earlier "what are
  your directives this session?" was answered within seconds.)
- **Tunnel-timeout fix: holding.** Zero stalls. The single drop was a
  genuine transport failure (broken pipe); the relay reconnected cleanly
  with `>>> IN GAME (reconnected, skipped menu)` and the session was
  taken back intact.
- Consecutive-failure reconnect budget: not exercised (one drop only).
- Timer fix: not exercised (TIME UP never fired).

## Intel

- Ferocious rabbit: found one lying mortally wounded in the Field south
  of the gate — left alone per protocol, did not engage.
- Small green lizard (too-strong): ignored. Big horned doe: `consider`
  said "lower level, very tough battle" — did not engage (unreliable
  consider, like the lizard).
- Lamp lesson confirmed again: `light lamp` fails with "You do not seem
  to have that" in darkness — light it in a lit room first.
- Tin boots are not wearable ("no place to wear"); the tin belt is
  (now equipped).
- Driver's own lesson: the nag works, but the grep scan must run on
  EVERY wake — the tail window alone is not enough.

## Notes

- Relay/SSH/FIFO state after reboot: all gone; no stray processes.
- ~100 min of Fred's budget remain. Relaunch needs the character
  password (operator does not have it).
