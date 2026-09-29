# Session 20 — SinMuseBot treasure hunt (interrupted by VM reboot)

**Real time:** 2026-09-29, 08:42:05 → 09:19 PDT (~37 min of the 120-min
budget; ~83 min unused). **Ended abnormally:** the VM rebooted at 09:19
(`who -b`: system boot Sep 29 09:19), killing the relay instantly with
zero log markers — no `>>>` lines, heartbeat froze, FIFO wiped with
`/tmp`. The driver detected the reboot, cleaned up the dead
`/tmp/mud_cmd` regular file its `printf` had created (the exact
post-reboot trap from the lessons), and wrote this report. TIME UP never
fired. SinMuseBot is **link-dead** on Main Street (Steak House room),
Northern Main City, with unbanked treasure.

## Results

- **LEVEL 4!** Leveled at ~09:15 PDT in the Tall rising. `gossip Level!`
  sent; Sin gossipped "gratz SinMuseBot!" and the driver replied
  ("Thanks Sin! Level 4, hunting treasure.") within seconds — the new
  10-second responsiveness rule worked in the field.
- XP: 2791 → **3303** (+512). Zero deaths.
- **13 confirmed kills** (all with R.I.P. or corpse):
  1. Beastly fido — Temple Square
  2. Beastly fido — Inside the West Gate
  3. Field mouse — Valley in the hills
  4. Jack rabbit — Large grassy field → Grassy plain (pursuit)
  5. Jack rabbit — Grassy plain
  6. Prairie dog — Grassy plain (considered first: "easy battle" — new
     prey species for the bot)
  7. Field mouse — Large grassy field
  8. Jack rabbit — Grassy plain
  9. Beastly fido — Temple Square
  10. Beastly fido — Main Street (corpse **snatched by a janitor** ~8s
      after the kill, before looting — see lessons)
  11. Prairie dog — Tall rising
  12. Field mouse — Small mountain
  13. Field mouse — Tall rising (this kill leveled the bot to 4)
- **Treasure:** tin boots + tin belt picked up from the Dump (~09:00,
  Dump check #2). All 13 corpses looted immediately were **empty**.
- Dump checks: #1 ~08:50 (empty), #2 ~09:00 (boots + belt taken),
  #3 ~09:12 (janitor present, no items).
- Bank: 8gc (#0000-11FB) — **no deposits made**; the spare belt + boots
  were still carried when the reboot hit.
- Inventory at link-dead: 2× tin belt, 2× tin boots, 2× oil lamp (one
  was lit), Nilgiri Guide. Manna consumed. HP 49/54, fed, watered.

## Critical intel

1. **The ferocious rabbit is not confined to Newtonia.** It attacked in
   the Hills and Plains (~09:14 PDT, near Small rise / Large grassy
   field); the driver fled per protocol, dropping 45→25 HP. The
   "Newtonia field stretch" framing in the rabbit protocol is wrong —
   treat it as roaming the Hills and Plains generally.
2. **Fluffy the baby dragon is too strong**: `consider` → "higher level
   than you / envision your entrails spread about the room." Seen at
   Inside the West Gate and the Field. Added to the too-strong registry.
3. **Janitors take corpses, not just trash.** A janitor picked up a fresh
   fido corpse on Main Street within ~8 seconds of the kill. Loot the
   *instant* R.I.P. appears — `get all from corpse` first, questions
   later.
4. **The MUD can't match inventory keywords in the dark.** `light lamp`
   failed with "You do not seem to have that" in darkness — light the
   lamp in a lit room BEFORE entering the dark. (Worked fine from
   Common Square.)
5. **Vultures devour corpses** — the driver watched one eat its looted
   prairie dog corpse. Another reason to loot fast.

## Notes

- First session on the fixed tunnel (`proxy_tunnel.py` timeout fix):
  **zero stalls** in 37 minutes. The fix holds in production.
- The 10-second controller-speech rule was exercised live (Sin's
  "gratz") and met.
- Earning rate: no coins this session — both treasure items came from
  the Dump, and the unbanked spare set was lost to the reboot
  (pending relaunch/recovery).
- Relay/SSH/FIFO state after reboot: all gone; no stray processes.
  Character link-dead in-game since 09:19.
