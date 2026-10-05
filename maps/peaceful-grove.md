# The Peaceful Grove — map

Mapping pass 2026-10-05 by SinMuseBot (L6), session 47 (mapping mission, ~45 min
in-zone). Session log: `~/workspace/nilgiri/logs/session-20261005-123427.log`
(local-only, never committed).

Zone: **The Peaceful Grove**, created by Rivin, recommended L1. Found exactly
where Fred said: one step east of "Outside the East Gate of Midgaard". Grove
rooms are `(field)`/`(hill)`/`(water)` suffixed. Mapping was done at night and
at dawn; room exits were verified by walking every listed exit (single steps +
`look` + `where`). Several rooms share the identical name "A grove (field)"
and two repeated descriptions ("The trees here fabricate a canopy..." and the
cliff text); rooms are distinguished below by exit signature. A few exits in
the dense canopy mesh were left unverified (marked UNVERIFIED) — they are
almost certainly internal loops of the same mesh.

**Duplicate-room caution:** this zone reuses room descriptions heavily. Do not
assume two "A grove (field)" rooms are the same room without a verified
round-trip.

## Boundaries (other zones — do NOT enter unapproved)

- N of City Entrance, N of Broad Lane, W of A path into the hills:
  **Vineyard (field)** {{Midgaard Vineyard, Mobius, L1 — OFF-LIMITS}}
- E of City Entrance, E of The Turning Point: **Broad Lane (field)**
  {{Midgaard, river and marsh, DIKU, L2}}
- S of The Turning Point: **Marsh Path (field)** {{Midgaard, river and marsh, DIKU, L2}}
- E of The end of the path: **The Forest of Tharen (field)** {{Tharen Forest, Rivin, L5 — UNAPPROVED}}
- N of A grove [cliff-archway]: **The Entrance Archway** {{The Mysterious Caverns, Rivin, L1 — UNAPPROVED}}
  (stone arch, "unnaturally dark" room beyond; not entered)
- W of City Entrance: Outside the East Gate of Midgaard {{Midgaard}}

## Room list

### Western chain (city → hills)

- **City Entrance (field)** — large city west, vineyard north, plains east.
  Exits: N -> Vineyard (off-limits); E -> Broad Lane; W -> Outside the East Gate of Midgaard.
  Mobs: lost squire (P3 "easy battle" — humanoid-ish, not engaged), street mime (passed through).
- **The Turning Point (field)** — trees close, bushy undergrowth; lane north and west.
  Exits: N -> The Lane; W -> Broad Lane; S -> Marsh Path.
- **The Lane (field)** — pleasant shady lane, stately trees.
  Exits: N -> The Plains; S -> The Turning Point.
- **The Plains (field)** — plains; small path into the hills north.
  Exits: N -> A path into the hills; S -> The Lane.
  (youthful courier ran through — humanoid NPC, left alone)
- **A path into the hills (hill)** — small path; fork north and east; south into the plains.
  Exits: N -> A path through the hills [flanked]; E -> A path through the hills [steep];
  W -> Vineyard (off-limits); S -> The Plains.
  Mobs: stray cat; adolescent girl in courier's uniform (humanoid NPC, left alone).
- **A path through the hills (hill)** [flanked] — "To the west and south this path continues...
  tall hills... mountain to the north-east".
  Exits: W -> A path through the hills [curves]; S -> A path into the hills.
- **A path through the hills (hill)** [curves] — "The path curves to the north and east...
  blood stains on a rock".
  Exits: N -> Between the hills and the forest; E -> A path through the hills [flanked].
  Mobs: stray cat (P1 "very tough battle" — not engaged).
- **Between the hills and the forest (hill)** — intersection; forest north (no entrance); path east.
  Exits: E -> Path along the edge of a forest [lining]; S -> A path through the hills [curves].
  Mobs: stray cats.
- **Path along the edge of a forest (hill)** [lining] — "path lining the edge of the forest to the
  north... hills too steep to climb... continues east and west".
  Exits: E -> Path along the edge of a forest [between]; W -> Between the hills and the forest.
  Mobs: stray cat.
- **Path along the edge of a forest (hill)** [between] — "between the forest to the north and the
  hills to the south... mountain beyond the forest to the east".
  Exits: E -> The end of the path; W -> Path along the edge of a forest [lining].
  Mobs: stray cat.
- **The end of the path (hill)** — end of path; steep hills south; dense forest N/E;
  "possible to pass through the trees to the east".
  Exits: E -> The Forest of Tharen (UNAPPROVED, not entered); W -> Path along the edge of a
  forest [between].

### Grove proper (canopy mesh, pond, field, cave)

- **A path through the hills (hill)** [steep] — "path leading through these steep hills...
  mountain to the north... hills flatten to the east".
  Exits: E -> A grove [edge-hills]; W -> A path into the hills.
- **A grove (field)** [edge-hills] — "edge of a very peaceful grove, steep hills to the west,
  mountain to the north; grove continues north and east".
  Exits: N -> A grove [canopy E/W/S]; E -> A grove [canopy E/W]; W -> A path through the
  hills [steep].
  Mobs: raccoon (P2 "you think you could do it"), mole (P1), skunk (P1), ferret (P4 "no
  trouble at all"), porcupine (P3 "easy battle") — none engaged (mapping mission).
- **A grove (field)** [canopy E/W/S] — "The trees here fabricate a canopy... scent of flowers..."
  Exits: E -> A grove [canopy N/E/W/S]; W -> A grove [canopy E/W]; S -> A grove [edge-hills].
  Mobs: porcupine, mole, ferret, bat.
- **A grove (field)** [canopy N/E/W/S] — canopy description.
  Exits: N -> A grove [cliff-archway]; E -> A grove [canopy W/S]; W -> A grove [canopy E/W/S];
  S -> The edge of the pond.
  Mobs: raccoon, mole, porcupines, ferrets; **Tarksu the lammasu** roams here — P1+ ("higher
  level... envision your entrails spread about the room") — AVOID.
- **A grove (field)** [cliff-archway] — "grove comes to an end... cliff... Partially hidden by
  a tree, an entrance into the mountain to the north".
  Exits: N -> The Entrance Archway (UNAPPROVED, not entered); E -> A grove [cliff E/W];
  S -> A grove [canopy N/E/W/S].
  Mobs: porcupine, skunk.
- **A grove (field)** [cliff E/W] — cliff description, no archway.
  Exits: E -> A grove [cliff W/S]; W -> A grove [cliff-archway].
- **A grove (field)** [cliff W/S] — cliff description.
  Exits: W -> A grove [cliff E/W]; S -> A grove [canopy N/W/S]. Mobs: raccoon.
- **A grove (field)** [canopy N/W/S] — canopy description.
  Exits: N -> A grove [cliff W/S]; W -> A grove [canopy E/W/S]; S -> UNVERIFIED (mesh loop).
- **A grove (field)** [canopy E/W/S] — canopy description.
  Exits: E -> A grove [canopy N/W/S]; W -> A grove [canopy N/E]; S -> UNVERIFIED (mesh loop).
  Mobs: bat (P0 "you would probably die..." — AVOID).
- **A grove (field)** [canopy N/E] — canopy description.
  Exits: N -> A grove [canopy W/S]; E -> A grove [canopy E/W/S].
  Mobs: porcupine, skunk, bat.
- **A grove (field)** [canopy W/S] — canopy description.
  Exits: W -> UNVERIFIED (mesh loop); S -> A grove [canopy N/E].
  Mobs: ferret (P4), bat (P0), skunk, raccoon.
- **A grove (field)** [canopy E/W] (west) — canopy description.
  Exits: E -> A grove [canopy E/W/S]; W -> A grove [edge-east]. Mobs: mole, porcupine.
- **A grove (field)** [edge-east] — "edge of a peaceful grove that continues to the east...
  small grassy field to the north... mountain".
  Exits: N -> A small field; E -> A grove [canopy E/W] (west).
- **A small field (field)** — "small field at the base of a mountain... bounded by grove east
  and south, dense forest west... small opening in the face of the mountain".
  Exits: N -> A cave; S -> A grove [edge-east].
- **A cave** — "small, dark, wet cave... narrows too much to fit through". Exits: S -> A small
  field. DEAD END.
- **A grove (field)** [canopy E/W] (central) — canopy description.
  Exits: E -> A grove [canopy E/W/S]; W -> A grove [edge-hills].
- **A grove (field)** [canopy E/W/S] (central) — canopy description.
  Exits: E -> A grove [canopy N/W]; W -> A grove [canopy E/W] (central); S -> UNVERIFIED.
  Mobs: raccoon, skunk, mole, porcupine.
- **A grove (field)** [canopy N/W] (central) — canopy description.
  Exits: N -> A grove [canopy E/S]; W -> A grove [canopy E/W/S] (central).
- **A grove (field)** [canopy E/S] — canopy description.
  Exits: E -> A grove [canopy N/W]; S -> A grove [canopy N/W] (central).
  Mobs: Tarksu the lammasu (AVOID), porcupine, skunk.
- **A grove (field)** [canopy W/S] (east) — canopy description.
  Exits: W -> A grove [canopy N/E/W/S]; S -> A grove [canopy N/E]. Mobs: ferret (P4).
- **A grove (field)** [canopy N/E] (east) — canopy description.
  Exits: N -> A grove [canopy W/S] (east); E -> A grove [canopy E/W/S] (east).
- **A grove (field)** [canopy E/W/S] (east) — canopy description.
  Exits: E -> UNVERIFIED; W -> A grove [canopy N/E] (east); S -> A grove [canopy N/W] (east).
  Mobs: porcupine, mole, bat (P0).
- **A grove (field)** [canopy N/W/S] (far east) — canopy description.
  Exits: N -> A grove [cliff W/S]; W -> A grove [canopy E/W/S] (east); S -> A grove [canopy
  N/E/S] (south-east). No mobs seen.
- **A grove (field)** [canopy N/E/S] (south-east) — canopy description.
  Exits: N -> A grove [canopy N/W/S] (far east); E -> A grove [canopy N/E/W]; S -> UNVERIFIED.
  Mobs: porcupine.
- **A grove (field)** [canopy N/E/W] (south-east) — canopy description.
  Exits: N -> UNVERIFIED; E -> UNVERIFIED; W -> A grove [canopy N/E/S] (south-east).
  Mobs: mole, porcupines, bat (P0).
- **The edge of the pond (field)** — "pond to the west... way through the grove to the north...
  fresh smell of water".
  Exits: N -> A grove [canopy N/E/W/S]; W -> The pond. Mobs: skunks x2 (P1).
- **The pond (water)** — "fed by underground springs... water cold but comfortable... trees
  around except eastern edge". Exits: E -> The edge of the pond. DEAD END.
  Mobs: toads x2 (P3 "easy battle" — not engaged).

## Consider ratings (this session)

| Mob | Rating | Engaged? |
|---|---|---|
| lost squire (Outside East Gate) | P3 easy battle | no (humanoid-ish, mapping) |
| stray cat | P1 very tough battle | no |
| raccoon | P2 "you think you could do it" | no (brief: no P2+) |
| mole | P1 very tough battle | no |
| porcupine | P3 easy battle | no (mapping mission) |
| skunk | P1 very tough battle | no |
| ferret | P4 "no trouble at all" | no |
| bat | P0 "you would probably die..." | no — avoided |
| toad | P3 easy battle | no |
| Tarksu the lammasu | higher level, "entrails spread about the room" | no — avoided |
| youthful courier / adolescent girl (courier) | humanoid NPCs | never attacked |

Kills this session: 0. XP unchanged.

## ASCII sketch (not to scale; verified connections)

```
                                    [mountain / cliff]
  {{Vineyard}}                        A cave
      |                                  |
      |                            A small field
      |                                  |
Broad Lane--City Entrance           A grove [edge-east]--A grove [canopy E/W]--A grove [canopy E/W/S]
      |         |  (E: Broad Lane)          |                  |                     |
The Turning     |                     A grove [canopy     A grove [canopy      A grove [edge-hills]--A path [steep]--A path into the hills
  Point         |                      E/W/S]              N/E/W/S]                  |                    |
      |    (W: Broad Lane,                                                   |              A path through the hills [flanked]
      |     S: Marsh Path)                                    pond<--edge of pond    |                    |
 The Lane                                                     |                     |              A path through the hills [curves]
      |                                                 A grove [cliff-archway]-----+                    |
 The Plains                                          (N: {{Mysterious Caverns}})     |              Between hills and forest
      |                                                 |                           |                    |
A path into the hills--{{Vineyard}}          A grove [cliff E/W]--A grove [cliff W/S] |          Path along forest [lining]
      |                                                 |               |           |                    |
      +--A path through the hills [steep]     A grove [canopy N/W/S]--A grove [canopy E/W/S]--+   Path along forest [between]
                                                                        |                   |          |
                                                              A grove [canopy N/E]--A grove [canopy W/S] |
                                                                                          The end of the path--{{Tharen Forest}}
```

Notes:
- The canopy mesh (rooms marked "A grove (field)") is a dense grid of ~20 rooms with
  repeated descriptions; the sketch shows verified links, not exact geometry.
- Canopy-mesh rooms east/south-east of the pond are omitted from the sketch for space;
  see room list. UNVERIFIED exits are internal mesh loops.
- `{{...}}` marks connections to other areas/zones.
