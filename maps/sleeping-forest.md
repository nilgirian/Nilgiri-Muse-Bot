# The Sleeping Forest — map

Mapping pass 2026-10-05 by SinMuseBot (L6), session 51 leg 1 (mapping
mission, ~35 min in-zone before two night-stalker deaths cut the run
short). Session log: `~/workspace/nilgiri/logs/session-20261005-220540.log`
(local-only, never committed).

Zone: **The Sleeping Forest**, created by Matrim, recommended L1.
**Status: APPROVED for this session only** — Fred explicitly ordered
the Sleeping Forest mapped in session 51 (leg 1 mapping, leg 2
hunting). Not a standing approved zone.

Mapping was done at night with an oil lamp (later a torch, then the
recovered lamp); exits were walked one step at a time. Room names
repeat HEAVILY ("A path by the mountain (forest)" x6, "A path in the
light forest (forest)" x5, "A trail into the forest heart (forest)" x3,
"The heavy forest (forest)" x22) with identical descriptions — rooms
are distinguished below by exit signature and verified neighbor links
(labels are the mapper's). Several exits proved ASYMMETRIC (E6's
east did not return to E3; E1/E2 links are one-way in places) —
verify every round-trip, do not assume symmetry.

**Duplicate-room caution:** do not assume two identically-named rooms
are the same room without a verified round-trip.

## WARNING — night stalkers (P1, roaming, extremely aggressive)

The deep heavy forest (D2 eastward) is a roaming night-stalker kill
zone. Stalkers ("a shadowy creature of little body and lots of limb")
attack on sight and kill a full-HP L6 in ~3 rounds (~24 dmg/round).
SinMuseBot died twice here (D2 ~22:25 PDT, −1448 XP; north of E2
~22:47 PDT, −1271 XP). The second corpse was ABANDONED (north of E2)
rather than risk a third death dropping the character below L6.
Do NOT send a lone L6 into the deep forest; future recovery needs a
group or a much higher level. Lightning bugs are also P1 ("You would
probably die...") but were never aggressive.

## How to get there

Grunting Boar → west through Midgaard → Outside the West Gate → north
onto A Wide Dirt Road (R1→R2→R3) → east (R4→R5) → east → Outside the
North Gate → east → Vineyard V6 → N → V7 → W → V8 → N → V9 → E → V10
→ N → "A path past the vineyard (forest)" (A1). Full vineyard entry
chain in `maps/midgaard-vineyard.md`.

## Sketch (schematic — NOT to scale)

```
                      A7 (dead end N)
                       |
   A1 — A2 — A3 — A4 — A5 — A6
    |                   |
  {{Vineyard}}          E
  (V10, S)              |
                       A8 — B1 — B2 — B3 (dead end E)
                        |     |      |
                        N     E      N
                      (unv.)  |      |
                             B4 — B5 — C1 — C2 — C3 — D1 — D2
                               |                       |       |
                              (S)                     (S)     S
                                                     (unv.)   |
                                                              D3 — D4 — D5 — D6 — D7 — D8 — D9
                                                                |               (gems/coins here)   |
                                                               (E)                                  |
                                                              (unv.)                      D10 (dead end E)
                                                                                            |
                                                                                            D11 — D12
                                                                                                  |
                                                                                          (S/W: stalker maze,
                                                                                           E1–E10, see below)

   Stalker-maze pocket (E1–E10, partially mapped, links uncertain):
     E1 — E2 — E3 — E4 (stalker)          E6 — E7
       |     |       |           |               |  |
      (N)   (N/W)   (W)        (flee)            N  (E)
       |     |       |           |               |
      E3   ...     E6 ————— E8 (floating eye) ...
                     |
                     S
                     |
                    E9 — E10
   (E6's east led to a stalker room instead of E3 — asymmetry confirmed)
```

## Room list

### The mountain path (A1–A8) — "A path by the mountain (forest)"

Standard description: "A trail leads in from the south. This seems to
be the road less travelled. Shrubs grow amidst the dirt, and some bits
of tall grass protrude defiantly as well. To the right, an unnaturally
quiet forest rises up, looking neither pleasant nor daunting."

- **A1 "A path past the vineyard (forest)"** (N,S) — dirt and miniscule
  rocks; withered vines give way to grass/trees. Object: small green
  stem. S → V10 {{Vineyard}} (entry). N → A2.
- **A2** (N,E,S) — no objects, no mobs. S → A1. N → A3, E UNVERIFIED.
- **A3** (N,E,S) — object: light green plant covered in fur. S → A2.
  N, E UNVERIFIED.
- **A4** (N,E,S) — no objects. S → A3. N, E UNVERIFIED.
- **A5** (N,E,S) — no objects. S → A4. N, E UNVERIFIED.
- **A6** (N,E,S) — no objects. S → A5. N → A7, E UNVERIFIED.
- **A7** (E,S) — north chain DEAD END. Object: small green stem.
  S → A6. E → A8.
- **A8** (N,E,W) — object: light green plant covered in fur. W → A7.
  E → B1, N UNVERIFIED.

### The light forest (B1–B5) — "A path in the light forest (forest)"

Standard description: "The path is overgrown, but not unkempt. It seems
as if those who used this trail did not kill the life here, but rather
asked it to move from this space. Some strange tracks are imprinted in
the dirt, and broken blades of grass show recent use."

- **B1** (N,E,W,S, 4 exits) — no objects. W → A8. N, E, S UNVERIFIED.
- **B2** (N,E,W,S) — objects: 3x small green stem. W → B1.
  N, E, S UNVERIFIED.
- **B3** (N,W) — east chain DEAD END. Objects: green stem, light green
  plant. W → B2. N → B4.
- **B4** (E,S) — object: light green plant. S → B3. E → B5.
- **B5** (E,W) — object: light green plant. W → B4. E → C1.

### The forest heart (C1–C3) — "A trail into the forest heart (forest)"

Standard description: "The trail becomes less of a trail and more of
undergrowth that has not been touched in quite some time. The same
unnatural silence that inhabited the lighter forest intensifies here. A
very distinct oppressive gloom has settled in here, and does not intend
to lift any time soon." These rooms are DARK even in daylight — a lit
lamp/torch is required to see.

- **C1** (E,W) — objects: oddly clear plant, very bright silvery fern.
  W → B5. E → C2.
- **C2** (E,W) — object: green stem. W → C1. E → C3.
- **C3** (E,W,S) — object: long stemmed plant. Mobs: lightning bug
  ("He is a higher level than you. You would probably die..." — P1,
  never aggressive), a bat ("lower level, you think you could do it" —
  P2, not engaged). W → C2. E → D1, S UNVERIFIED.

### The heavy forest (D1–D12) — "The heavy forest (forest)"

Standard description: "With no path, all sense of direction disappears.
The forest appears the same in every direction save to the west, where
it leads back towards the forest heart. Thick foliage and profuse
amounts of plant life grow close together, making any movement
difficult." DARK — lamp/torch required. STALKER TERRITORY.

- **D1** (E,W) — NOTE: "A ravaged druid lies in a pool of blood,
  breathing his last" — humanoid NPC, dying, NOT engaged. W → C3.
  E → D2.
- **D2** (W,S) — Mobs: "a rat with wings" (not considered), NIGHT
  STALKER (killed SinMuseBot here ~22:25 PDT in 3 rounds; absent on the
  return ~22:45, when the first corpse was fully recovered). W → D1.
  S → D3.
- **D3** (N,E) — object: very bright silvery fern. Mob: lightning bug
  #2 (P1). N → D2. E → D4.
- **D4** (E,W,S) — no objects, no mobs. W → D3. E → D5, S UNVERIFIED.
- **D5** (E,W,S) — object: long stemmed plant. Mobs: lightning bug #3
  (P1), a bat lying INCAPACITATED (not our fight — left alone). W → D4.
  E → D6, S UNVERIFIED.
- **D6** (E,W,S) — objects: light green plant, oddly clear plant.
  W → D5. E → D7, S UNVERIFIED.
- **D7** (E,W,S) — objects: light green plant, shrub, SMALL GREEN GEM
  (picked up). W → D6. E → D8, S UNVERIFIED.
- **D8** (E,W,S) — objects: shredded corpse of a nightmare, LARGE PILE
  OF GOLD COINS (picked up), small green gem (picked up). W → D7.
  E → D9, S UNVERIFIED.
- **D9** (N,E,W,S, 4 exits) — objects: 2x light green plant. W → D8.
  N, E, S UNVERIFIED.
- **D10** (N,W,S) — eastward DEAD END. W → D9. N, S UNVERIFIED.
- **D11** (N,W,S) — mob: lightning bug #4 (P1). N → D10. S → D12,
  W UNVERIFIED.
- **D12** (N,W,S) — objects: 2x LARGE PILE OF GOLD COINS (picked up),
  shrub. NIGHT STALKER roams here (darted in from the west, attacked
  while looting — fled at 16 HP). N → D11. W, S UNVERIFIED.

### Stalker-maze pocket (E1–E10) — partially mapped, links uncertain

Reached via panicked flee from D12. Several exits proved asymmetric;
treat every link below as single-direction until re-verified.

- **E1** (N,W) — object: small green stem. N → E3, W → E2.
- **E2** (N,E,W) — objects: 2x light green plant. Mob: lightning bug
  #5 (P1). E → E1. N → stalker room (DEATH #2 here ~22:47 PDT),
  W UNVERIFIED.
- **E3** (N,W,S) — N → E4 (stalker, attacked on entry, fled),
  W → E6, S → E1.
- **E4** — stalker room north of E3; exits UNVERIFIED (fled instantly).
- **E5** (N,W,S) — mob: lightning bug #7 (P1). Reached via flee at
  14 HP.
- **E6** (N,E,W,S, 4 exits) — object: oddly clear plant. W → E7,
  N → E8, S → E9, E → stalker room (NOT E3 — asymmetry confirmed).
- **E7** (N,E,W,S) — E → E6 (round-trip verified). N, W UNVERIFIED.
- **E8** (N,E,W,S) — objects: light green plant, green stem, silvery
  fern. Mob: dismembered floating eye ("lower level, you think you
  could do it" — P2, not engaged). S → E6. N, E, W UNVERIFIED.
- **E9** (N,E,W) — objects: green stem, shrub. N → E6. E → E10,
  W UNVERIFIED.
- **E10** (N,E,W) — objects: 2x light green plant. W → E9.
  N, E UNVERIFIED.

## Mobs considered (all: consider only, ZERO kills — mapping mission)

- Stray cat (Wide Dirt Road R1): "lower level... very tough battle."
- Black crow (Vineyard V6): "lower level... You would probably die..."
  (misrated/dangerous — do NOT engage).
- Lightning bug x7 (C3, D3, D5, D11, E1/E2 area, E5): "higher
  level... You would probably die..." (P1). Never aggressive.
- Night stalker (D2, D12, E4, E6-east, E2-north): "shadowy creature
  of little body and lots of limb" — EXTREMELY AGGRESSIVE, ~24
  dmg/round, kills L6 in 3 rounds. Two PC deaths.
- Bat (C3): "lower level... you think you could do it" (P2).
- Dismembered floating eye (E8): "lower level... you think you could
  do it" (P2).
- Rat with wings (D2, E2): seen, not considered.
- Ravaged druid (D1): dying humanoid NPC — not engaged.
- Incapacitated bat (D5): not our fight — left alone.

## Treasure

- D7: 1 small green gem (recovered, then lost with corpse #2).
- D8: 1 large pile of gold coins + 1 small green gem (recovered, then
  lost with corpse #2).
- D12: 2 large piles of gold coins (recovered, then lost with corpse #2).
- Corpse #1 (D2, recovered): bronze short sword, oil lamp, 2 water
  flasks, beer bottle, 3 coconuts, tin crown/belt/boots/chest plate.
- Corpse #2 (north of E2, ABANDONED): everything above plus a large
  torch. Do not attempt solo recovery at L6.

## Boundaries (other zones — do NOT enter unapproved)

- S of A1: V10 {{Midgaard Vineyard}} — entry/exit.
- The Sleeping Forest's other edges were not reached in this pass.
- NOTE: the forest's eastern/southern/western extents are UNMAPPED —
  the maze continues past D9/D10 (N/E), D4 (S), D12 (W/S), and the
  E1–E10 pocket.
