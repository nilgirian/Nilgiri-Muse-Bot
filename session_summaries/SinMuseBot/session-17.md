# Session 17 — SinMuseBot (2026-09-28, ~21:28–22:25 PDT)

Lamp run in the Hills and Plains. 1-hour budget, retired normally with
time to spare.

## Mission

Fred's orders: explore the Hills and Fields, buy oil lamps from the
store (`light` when dark, `dowse` when light to conserve fuel — two
lamps in case one runs out), finish the zone map, hunt animals for XP.

## Result

- **XP:** 2707 → **2800 (+93)**. Still L3; L4 at 3244 (444 to go).
- **Kills (3 confirmed):**
  1. Beastly fido — Outside the West Gate (+9, +23 XP). Corpse LOST: a
     network stall froze the relay ~5 min; a janitor took the corpse
     before it could be looted after reconnect.
  2. Brown fox — small path in the dense forest (+45 XP). `consider`
     read "lower level, very tough battle". Corpse looted immediately —
     empty.
  3. Beastly fido — Main Street west end (+16 XP). Corpse looted
     immediately — empty.
- **Deaths:** 0. Exit HP 47/47.
- **Loot:** none — all corpses empty.
- **Bank:** #0000-11FB, **75gc → 52gc**. Spent 23gc: two oil lamps @9gc
  each + iron rations @5gc. Nothing to deposit. Balance verified. The
  transaction history showed "credited 1gc in treasure" entries —
  confirming the bank takes treasure deposits (validates Fred's rule).
- **Retirement:** bank → Grunting Boar Reception → `rent` → `klick` →
  Return → menu `0` → MUD closed the connection. No relay, SSH, holder,
  FIFO, or PID files remained.
- **Exit inventory:** 2 oil lamps, tin boots ×2, tin belt, tin chest
  plate, Nilgiri Guide.

## Lamps

- Bought two oil lamps at the General Store. The store stocks one lamp
  at a time — after buying, it restocked under a new `#` code
  (#04178EC2); re-`list` after buying.
- Lamp #1 lit at sunset, dowsed at dawn (Fred's fuel discipline); lamp
  #2 kept as unused backup. Both passed `rent`.
- `light lamp` works from inventory; `hold lamp` fails ("You cannot hold
  that"). The lamp stays lit through relay reconnects. At night `exits`
  still shows "(too dark to tell)" with a lit lamp, but movement works
  and room descriptions are visible — map by moving.

## Map

- **Dense-forest west branch RESOLVED:** west of "A trail through the
  dense forest" is **"Haon-Dor Forest - dark", a separate L5-recommended
  zone**. Entered one room with the lamp lit, `where` showed the new
  zone identity, turned back east immediately per the zone rule. Marked
  OFF-LIMITS in the exit list and ASCII sketch.
- Small rise was already mapped; the manor door is still locked, no key.
- The Hills and Plains map is now effectively complete for all approved
  ground.

## Network

- Two SSH stalls (~75s, ~89s of MUD silence). The relay detected both
  itself (PROBE → STALL → kill ssh → reconnect, attempts 1/5 and 2/5)
  and recovered without intervention. The first stall cost the fido
  corpse (janitor).

## Notes

- TOO_STRONG_MOBS.md: no changes — nothing new fought (the dark zone is
  a zone boundary, not a mob).
- No level-up this session, so no re-`consider` pass yet.
- Raw log (local-only): `~/workspace/nilgiri/logs/session-20260928-212800.log`
