# Midgaard Vineyard — map

Mapping pass 2026-10-05 by SinMuseBot (L6), session 48 (mapping mission,
~55 min in-zone). Session log: `~/workspace/nilgiri/logs/session-20261005-132907.log`
(local-only, never committed).

Zone: **Midgaard Vineyard**, created by Mobius, recommended L1.
**Status: OFF-LIMITS** — not an approved zone (this session was
Fred-authorized for mapping only; the standing off-limits note remains
for other sessions).

Mapping was done at night (oil lamp) and at dawn; room exits were
verified by walking every listed exit (single steps + `look` + `where`).
All 73 in-zone rooms share the identical name "Vineyard (field)" (or
"A Wide Dirt Road") and identical descriptions; rooms are distinguished
below by exit signature and verified neighbor links (V-labels are the
mapper's).

**Duplicate-room caution:** this zone reuses room descriptions heavily.
Do not assume two "Vineyard (field)" rooms are the same room without a
verified round-trip. 18 in-zone exits were left UNVERIFIED (frontier) —
the maze is larger than one hour allows; they are marked below.

**How to get there:** Grunting Boar → west through the city → Outside
the West Gate → north onto **A Wide Dirt Road** → east along the road →
east from Outside the North Gate into the vineyard proper.

## Boundaries (other zones — do NOT enter unapproved)

- W of R5 / E of R5: **Outside the North Gate of Midgaard**
  {{Midgaard Monastery, Mobius, L2}} — 4 exits (N/E/W/S).
- N of R4: **A path through the fields** {{The Barrow-Downs and Old
  Forest, Ancagaclon, L15}} — DANGEROUS, L15 zone adjacent to L1 road.
  Probed 1 room, retreated immediately.
- N of V10: **A path past the vineyard (forest)** {{The Sleeping Forest,
  Matrim, L1}} — 2 exits (N/S).
- N of V47, V54, V61, V68: **Sleeping Forest** rooms (N/S) or "A path
  past the vineyard (forest)" — the vineyard's entire northern edge
  borders The Sleeping Forest. Probed 1 room each, retreated.
- E of V27, E of V37: **The Peaceful Grove** {{The Peaceful Grove,
  Rivin, L1}} rooms (N/E/W/S) — the vineyard's eastern edge borders the
  Grove. Probed 1 room each, retreated.
- S of R1: Outside the West Gate of Midgaard {{Midgaard}} (city).

## Room list

### The Wide Dirt Road (5 rooms, all Midgaard Vineyard zone)

- **R1 "A Wide Dirt Road"** (N,S) — road comes out of the west gate
  from the south, corners off to the east. Exits: N -> R2; S -> Outside
  the West Gate of Midgaard {{Midgaard}}.
- **R2 "A Wide Dirt Road"** (N,S) — same desc. Exits: N -> R3; S -> R1.
- **R3 "A Wide Dirt Road"** (E,S) — same desc. Exits: E -> R4; S -> R2.
- **R4 "A Wide Dirt Road"** (N,E,W) — "road runs east to west around the
  northern wall... intersection to the west... north city gate to the
  east". Exits: N -> A path through the fields {{Barrow-Downs, L15 —
  EDGE, do not enter}}; E -> R5; W -> R3.
- **R5 "A Wide Dirt Road"** (E,W) — "intersection off to the west...
  north city gate directly to the east". Exits: E -> Outside the North
  Gate of Midgaard {{Monastery L2 — EDGE}}; W -> R4.

### The Vineyard maze (68 rooms, all "Vineyard (field)", Midgaard Vineyard zone)

Standard description (all rooms): "Rows upon rows of unkept grapevines
hang from rotten, wooden horizontal lattices. The bunches of bright red
grapes that hang from the vines seem to be on the verge of rotting. The
vineyard extends around and right up to the northeastern city walls of
Midgaard." Notable object (most rooms): "A bunch of ripe red grapes
hang from a vine." — `get grapes` + `eat grapes` works as food.

**Entry chain (gate → heart):**
- **V6** (N,W) — "Haphazard rows of grapevines start up to the east."
  Exits: N -> V7; W -> Outside the North Gate {{Monastery L2 — EDGE}}.
  Mobs: 2x small fly (seen).
- **V7** (E,W,S) — Exits: S -> V6; W -> V8; E -> V13.
- **V8** (N,E) — Exits: E -> V7; N -> V9. Mob: small fly (P4).
- **V9** (E,S) — Exits: S -> V8; E -> V10.
- **V10** (N,E,W) — Exits: W -> V9; E -> V12; N -> "A path past the
  vineyard (forest)" {{Sleeping Forest L1 — EDGE}}.

**Western branch (from V7):**
- **V12** (E,W) — Exits: W -> V10; E -> UNVERIFIED (frontier).
- **V13** (N,E,W) — Exits: W -> V7; N -> V14; E -> V21. (courier NPC ran through)
- **V14** (W,S) — Exits: S -> V13; W -> V15.
- **V15** (E,W) — Exits: E -> V14; W -> V16. Mob: small fly (P4).
- **V16** (N,E,W) — Exits: E -> V15; W -> V17; N -> UNVERIFIED (frontier).
- **V17** (E,S) — Exits: E -> V16; S -> V18.
- **V18** (N,E) — Exits: N -> V17; E -> V19.
- **V19** (E,W,S) — Exits: W -> V18; S -> V6 (verified); E -> UNVERIFIED
  (frontier). Mob: small fly (P4). (Grapes eaten here.)

**Eastern mesh (from V13):**
- **V21** (E,W,S) — Exits: W -> V13; S -> V22; E -> UNVERIFIED (frontier).
- **V22** (N,E,S) — Exits: N -> V21; E -> V23; S -> V24.
- **V23** (W) — dead end. Exits: W -> V22.
- **V24** (N,E) — Exits: N -> V22; E -> V25. Mob: small fly (P4).
- **V25** (E,W,S) — Exits: W -> V24; E -> V26; S -> UNVERIFIED (frontier).
- **V26** (N,W) — Exits: W -> V25; N -> V27.
- **V27** (N,E,S) — Exits: S -> V26; N -> V28; E -> Peaceful Grove room
  {{The Peaceful Grove, Rivin, L1 — EDGE, probed 1 room}}.
- **V28** (W,S) — Exits: S -> V27; W -> V29.
- **V29** (N,E,W) — Exits: E -> V28; N -> V30; W -> V32. Mob: small fly (P4).
- **V30** (W,S) — Exits: S -> V29; W -> V31.
- **V31** (E) — dead end. Exits: E -> V30.
- **V32** (E,W,S) — Exits: W -> V29; E -> V33; S -> UNVERIFIED (frontier).
- **V33** (N,E,W) — Exits: W -> V32; N -> V34; E -> V36.
- **V34** (W,S) — Exits: S -> V33; W -> V35.
- **V35** (E) — dead end. Exits: E -> V34.
- **V36** (W,S) — Exits: W -> V33; S -> V37.
- **V37** (N,E,S) — Exits: N -> V36; S -> V38; E -> Peaceful Grove room
  {{The Peaceful Grove, Rivin, L1 — EDGE, probed 1 room}}.
- **V38** (N,W) — Exits: N -> V37; W -> V39.
- **V39** (E,W,S) — Exits: E -> V38; W -> V40; S -> UNVERIFIED (frontier).
- **V40** (N,E) — Exits: E -> V39; N -> V41.
- **V41** (N,E,S) — Exits: S -> V40; E -> V42; N -> V43.
- **V42** (W) — dead end. Exits: W -> V41.
- **V43** (E,W,S) — Exits: S -> V41; W -> V44; E -> UNVERIFIED (frontier).
- **V44** (N,E,W) — Exits: E -> V43; N -> V45; W -> UNVERIFIED (frontier).
- **V45** (W,S) — Exits: S -> V44; W -> V46.
- **V46** (E,W) — Exits: E -> V45; W -> V47.
- **V47** (N,E,W) — Exits: E -> V46; W -> V48; N -> Sleeping Forest room
  {{The Sleeping Forest, Matrim, L1 — EDGE, probed 1 room}}.
- **V48** (E,S) — Exits: E -> V47; S -> V49.
- **V49** (N,E) — Exits: N -> V48; E -> V50.
- **V50** (E,W,S) — Exits: W -> V49; E -> V51; S -> UNVERIFIED (frontier).
- **V51** (N,E,W) — Exits: W -> V50; N -> V52; E -> UNVERIFIED (frontier).
- **V52** (W,S) — Exits: S -> V51; W -> V53.
- **V53** (E,W) — Exits: E -> V52; W -> V54.
- **V54** (N,E,W) — Exits: E -> V53; W -> V55; N -> Sleeping Forest room
  {{The Sleeping Forest, Matrim, L1 — EDGE, probed 1 room}}.
- **V55** (E,S) — Exits: E -> V54; S -> V56.
- **V56** (N,E) — Exits: N -> V55; E -> V57.
- **V57** (E,W,S) — Exits: W -> V56; E -> V58; S -> UNVERIFIED (frontier).
- **V58** (N,E,W) — Exits: W -> V57; N -> V59; E -> UNVERIFIED (frontier).
- **V59** (W,S) — Exits: S -> V58; W -> V60.
- **V60** (E,W) — Exits: E -> V59; W -> V61.
- **V61** (N,E,W) — Exits: E -> V60; W -> V62; N -> "A path past the
  vineyard (forest)" {{Sleeping Forest — EDGE}}.
- **V62** (E,S) — Exits: E -> V61; S -> V63.
- **V63** (N,E) — Exits: N -> V62; E -> V64.
- **V64** (E,W,S) — Exits: W -> V63; E -> V65; S -> UNVERIFIED (frontier).
- **V65** (N,E,W) — Exits: W -> V64; N -> V66; E -> UNVERIFIED (frontier).
- **V66** (W,S) — Exits: S -> V65; W -> V67.
- **V67** (E,W) — Exits: E -> V66; W -> V68.
- **V68** (N,E,W) — Exits: E -> V67; W -> V69; N -> "A path past the
  vineyard (forest)" {{Sleeping Forest — EDGE}}.
- **V69** (E,S) — Exits: E -> V68; S -> V70.
- **V70** (N,E) — Exits: N -> V69; E -> V71.
- **V71** (E,W,S) — Exits: W -> V70; E -> V72; S -> UNVERIFIED (frontier).
- **V72** (N,E,W) — Exits: W -> V71; N -> V73; E -> UNVERIFIED (frontier).
- **V73** (W,S) — Exits: S -> V72; W -> UNVERIFIED (frontier). (deepest mapped)

## Mobs (all considered, none engaged — mapping protocol)

- small fly ×7 (V8, V15, V19, V24, V29, +2 seen at V6, 2 seen at V12):
  all P4 "It is a lower level than you. Looks like you wouldn't have any
  trouble at all."
- adolescent girl in a courier's uniform (V13) — humanoid NPC, ran through,
  left alone.
- Shargugh the Forest Brownie (player) — seen at R4/V4 area, walked off.

Kills: 0 (mapping mission — consider only).

## Notes

- **Grape bunches are food:** `get grapes` + `eat grapes` ("a bunch of
  ripe red grapes") cures hunger. Renewable in-zone food source.
- **Footpad theft (session 48):** entire inventory stolen silently in
  Midgaard city — 2 water flasks, 3 coconuts, 1 beer bottle, 1 oil lamp.
  (Same MO as session 45.) Recovered 1 oil lamp from the rent-room vault
  to finish the mission. Standing lesson reinforced: travel light in the
  city.
- **Night mapping:** the vineyard is pitch black at night; the Wide Dirt
  Road near the gates stays lit (city light). Oil lamp required off-road.
- **The maze is large:** 68 vineyard rooms mapped in ~55 min; 18 exits
  remain UNVERIFIED (frontier). The northern edge throughout borders The
  Sleeping Forest; the eastern edge borders The Peaceful Grove; the
  north-west road exit borders a L15 Barrow-Downs room (dangerous).
- **Lamp:** `light lamp` works from inventory; `dowse` to conserve.

## Sketch (schematic — NOT to scale; maze topology simplified)

```
                    {{Sleeping Forest (Matrim, L1)}}  — northern edge throughout
                    {{Barrow-Downs (Ancagaclon, L15)}} — N of R4 (DANGER)
         ┌──────────────────────────────────────────────────┐
         │              VINEYARD MAZE (68 rooms)              │
         │  Entry: V6 ─ V7 ─ V8 ─ V9 ─ V10                   │
         │         │     │           ├── V12 (E UNVERIFIED)   │
         │        ONG   V13 ─ V14 ─ V15 ─ V16 (N UNVERIFIED)  │
         │               │                     │              │
         │              V21 ─ V22 ─ V23(dead)  V17 ─ V18 ─ V19│ (E UNVER.)
         │               │     │                         │   │
         │              V24 ─ V25 (S UNVER.) ─ V26 ─ V27 ─ V28│
         │               │                           │E:Grove│
         │              V29 ─ V30 ─ V31(dead)        V28...   │
         │               │                                    │
         │         ... (mesh continues: V32–V73, 40+ rooms)   │
         │               │                             │E:Grove│
         │              V37 ─ V38 ─ ... ─ V68 ─ V69 ─ V70 ... │
         │                    northern edge = Sleeping Forest│
         └──────────────────────────────────────────────────┘
   R1 ─ R2 ─ R3 ─ R4 ─ R5 ── ONG {{Monastery L2}}
   │                    │N: Barrow-Downs L15 (EDGE)
 Outside West Gate {{Midgaard}}
```

Entry route: Outside West Gate → N → R1 → N → R2 → N → R3 → E → R4 →
E → R5 → E → ONG → E → V6 → (maze).
```

## Frontier (UNVERIFIED in-zone exits — next session)

V12.E, V16.N, V19.E, V21.E, V25.S, V32.S, V39.S, V43.E, V44.W, V50.S,
V51.E, V57.S, V58.E, V64.S, V65.E, V71.S, V72.E, V73.W.
