# Session 20c — SinMuseBot treasure hunt, second relaunch (terminated by VM reboot)

**Real time:** 2026-09-29, 11:01:14 → ~11:41 PDT (~40 min of the 100-min
budget; ~60 min unused). **Ended abnormally:** the VM rebooted at ~11:41
(`who -b` confirms) — the THIRD reboot today, 7th logged — killing the
relay, SSH, and FIFO instantly with zero log markers. The driver
detected it via stale heartbeat + `who -b`, cleaned up the dead
`/tmp/mud_cmd` file, and reported. TIME UP never fired. SinMuseBot is
link-dead Outside the West Gate of Midgaard.

## Results

- Level 4, 3528 XP (3303 at login). Zero deaths.
- **4 confirmed kills** (all with R.I.P., all corpses looted empty):
  1. Beastly fido — Inside the West Gate
  2. Field mouse — Field (Hills and Plains)
  3. Beastly fido — Inside the West Gate
  4. Beastly fido — Inside the West Gate
  - Plus XP from two rabbit engagements that fled (+35, +39) and a stun
    (+72).
- **Treasure — the haul:** Dump check #3 (~11:38 PDT) found **3x tin
  boots + 3x tin belts** on the ground — someone dumped a load of gear.
  All six picked up. **All unbanked when the reboot hit.** Dump checks
  #1 (~11:06) and #2 (~11:08) were empty.
- Bank: 8gc (#0000-11FB) — not re-verified this session; no deposits.
- Inventory at link-dead: 4x tin boots, 2x tin belt carried (+1 tin belt
  worn), 2x oil lamp (one lit; the flickering one dowsed in the city),
  Nilgiri Guide. Fed and watered. HP 47/54.
- The tin belt is wearable and now equipped; tin boots are not wearable
  ("no place to wear").

## Controller speech

- Sin gossiped "how you doing so far SinMuseBot?" — the driver **missed
  the original flag** (mid-fight, wasn't running the bulletproof grep
  scan). The relay's `>>> SPEECH-PENDING` fired at 15s/30s and
  `>>> SPEECH-UNANSWERED` at 60s — that is how the driver caught it.
  Reply confirmed delivered: "Doing well Sin! 2 kills so far, dump
  checks empty, hunting rabbits in the hills. L4."
- **The nag has now saved two missed gossips in two sessions** (20b's
  Dodger question, 20c's check-in). The driver's standing lesson: run
  the grep scan on EVERY wake; the tail window alone is not enough.

## Fixes in production

- Tunnel-timeout fix: holding. One transport drop mid-session; the relay
  reconnected cleanly (`>>> IN GAME (reconnected, skipped menu)`) and
  the session continued intact.
- Lamp lesson confirmed again: dowsed the flickering lamp in daylight,
  relit the good one at the gate before re-entering the dark field.

## Notes

- Relay/SSH/FIFO state after reboot: all gone; no stray processes.
- ~60 min of Fred's budget remain. The character is link-dead carrying
  6 unbanked treasure items — recovery is time-sensitive for the loot.
  Relaunch needs the character password.
