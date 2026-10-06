# Midgaard Monastery — map

Mapping pass 2026-10-06 by SinMuseBot (L6), session 55 (mapping mission,
consider-only, kill nothing). Session log:
`~/workspace/nilgiri/logs/session-20261006-1259.log` (local-only, never
committed).

Zone: **Midgaard Monastery**, created by Mobius, recommended L2.
**Status: APPROVED for session 55 only** — Fred explicitly ordered the
Monastery mapped in session 55. Not a standing approved zone.

**How to get there:** Grunting Boar → Reception → down → Entrance →
west → Temple Square → south → Market Square → west ×3 (Main Street)
→ west → Inside the West Gate → west → Outside the West Gate → north
onto A Wide Dirt Road (R1→R2→R3) → east (R4→R5) → east → Outside the
North Gate of Midgaard. **Shortcut found session 55:** from Main Street
(west-3) → west → Inside the West Gate → north → Wall Road → east
along the wall → Inside the North Gate of Midgaard → north (through
gate) → Outside the North Gate. (Wall Road route verified 2026-10-06.)

From Outside the North Gate: NORTH → the orchard path (M1).

## Key discovery: the marble hall has NO entrance

The grand marble hall stands north of M5 ("A bend in the path"), but
there is **no north exit** ("Alas, there is no path north." / `open
north`: "There is nothing by that name to open." / `look hall`: "You
cannot seem to find a 'hall'." / `look north`: "You see nothing special
to the north."). The hall is pure scenery/description text.

**Correction (session 55):** The driver initially thought the north
exit was "night-only" because `north` from M4 at night moved through
darkness. Re-examination of the log proved this was just normal outdoor
movement at night (M4→M5→M4→M3→M2→M1→ONG, all pitch black without a
lamp). There is no hidden/night-only entrance. The mappable monastery
is the 6-room orchard path (M1-M6).

At night, outdoor rooms go pitch black; with a lit lamp, room
descriptions are visible but `exits` shows "(too dark to tell)" — map
by moving.

## Boundaries (other zones — do NOT enter unapproved)

- S of M1: **Outside the North Gate of Midgaard** (edge room, 4 exits
  N/E/W/S).
- E of ONG: **Vineyard** {{Midgaard Vineyard, Mobius, L1 — OFF-LIMITS
  except by Fred's direct session-scoped order}}.
- NW: **Barrow-Downs / Old Forest** {{Ancaglon, L15 — DANGEROUS, do
  not enter}} (per brief; not verified this session).

## Room list (outdoor approach — all verified by round-trip)

All rooms are `(field)` type. `where` reports the area as "Midgaard
Vineyard created by Mobius... L1" (the zone system groups Mobius's
areas; the Monastery proper is L2 per the brief).

- **M1 "A path between orchards"** (N,S) — "A small path winds its way
  between two orchard groves to the east and west. To the south stands
  the imposing northern gate to the City of Midgaard. The city walls
  extend to the east and west. To the north the path continues."
  Exits: N -> M2; S -> Outside the North Gate of Midgaard.
- **M2 "A path between orchards"** (N,S) — "A small path winds its way
  between two orchard groves to the east and west. Healthy apple trees
  are scattered in an even pattern as far as the eye can see to the
  west. To the east is a dense orange grove. The path continues north
  and south."
  Exits: N -> M3; S -> M1.
- **M3 "A path between orchards"** (N,S) — identical desc to M2.
  Exits: N -> M4; S -> M2.
- **M4 "A path between orchards"** (N,S) — identical desc to M2/M3,
  except north exit reads "A bend in the path".
  Exits: N -> M5; S -> M3.
- **M5 "A bend in the path"** (W,S) — "The small path bends to the west and
  south here. To the east extends a dense orange grove. To the south the
  path continues between an apple orchard and the dense orange grove. To
  the north stands a grand hall made of bright marble. The path continues
  to the west." (The marble hall is scenery — no entrance.)
  Exits: W -> M6; S -> M4.
- **M6 "A path between orchards"** (E only) — "A small path winds its
  way between two orchard groves to the north and south. Healthy apple
  trees are scattered in an even pattern as far as the eye can see.
  The path continues to the east and it bends to the south."
  ("bends to the south" is flavor text — no south exit; verified.)
  Exits: E -> M5.

## Mobs (considered, none engaged — mapping protocol)

None seen on the outdoor path (session 55, day and night).

Kills: 0 (mapping mission — consider only).

## Notes

- **Darkness lies.** In pitch-black rooms, `inventory` shows "nothing"
  and item-targeting commands (`light lamp`, `get X from bag`) fail —
  even for items you are actually carrying. This is a darkness
  display/parser limitation, NOT theft. Session 55: the driver
  concluded a footpad theft in the dark, bought a replacement oil lamp
  (9gc), then found all "stolen" items (oil lamp, clear plant, staff)
  still in inventory in the light. **Lesson: never diagnose theft in
  the dark — verify in a lit room first.**
- **Held-bag container access needs light.** `get X from bag` fails in
  the dark even for a held bag ("You cannot seem to find a 'bag'.").
  `put X bag` works in the light. `remove bag` (unhold) works, `hold
  bag` re-holds.
- **Unnecessary purchase (session 55):** 1 oil lamp, 9gc, General Store
  (debited from bank account #0000-11FB) — bought because darkness hid
  the original lamp. Now carrying 2 oil lamps.
- The monastery grounds are fully mapped (6 outdoor rooms). The marble
  hall north of M5 is scenery with no entrance (verified by `north`,
  `open north`, `look hall`, `look north`).

## Sketch (schematic — NOT to scale)

```
                    {{Marble hall (scenery, no entrance)}}
                          |
                     (no exit)
                          |
  ONG --- M1 --- M2 --- M3 --- M4 --- M5 --- M6
   |                                    (E only)
   S: Inside North Gate {{Midgaard}}
   E: Vineyard {{OFF-LIMITS}}
```

Entry: Outside the North Gate → N → M1 → N → M2 → N → M3 → N → M4 →
N → M5 → (W) → M6. The monastery grounds are the 6-room orchard path;
the marble hall north of M5 is decorative.
