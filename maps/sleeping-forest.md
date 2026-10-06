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
(F-labels are the mapper's). Several exits proved ASYMMETRIC (F34's
east did not return to F31; F29/F30 links are one-way in places) —
verify every round-trip, do not assume symmetry.

**Duplicate-room caution:** do not assume two identically-named rooms
are the same room without a verified round-trip.

## WARNING — night stalkers (P1, roaming, extremely aggressive)

The deep heavy forest (F18 eastward) is a roaming night-stalker kill
zone. Stalkers ("a shadowy creature of little body and lots of limb")
attack on sight and kill a full-HP L6 in ~3 rounds (~24 dmg/round).
SinMuseBot died twice here (F18 ~22:25 PDT, −1448 XP; north of F30
~22:47 PDT, −1271 XP). The second corpse was ABANDONED (north of F30)
rather than risk a third death dropping the character below L6.
Do NOT send a lone L6 into the deep forest; future recovery needs a
group or a much higher level. Lightning bugs are also P1 ("You would
probably die...") but were never aggressive.

## How to get there

Grunting Boar → west through Midgaard → Outside the West Gate → north
onto A Wide Dirt Road (R1→R2→R3) → east (R4→R5) → east → Outside the
North Gate → east → Vineyard V6 → N → V7 → W → V8 → N → V9 → E → V10
→ N → "A path past the vineyard (forest)" (F1). Full vineyard entry
chain in `maps/midgaard-vineyard.md`.

## Sketch (schematic — NOT to scale)

```
                      F7 (dead end N)
                       |
   F1 — F2 — F3 — F4 — F5 — F6
    |                   |
  {{Vineyard}}          E
  (V10, S)              |
                       F8 — F9 — F10 — F11 (dead end E)
                        |     |      |
                        N     E      N
                      (unv.)  |      |
                             F12 — F13 — F14 — F15 — F16 — F17 — F18
                               |                       |       |
                              (S)                     (S)     S
                                                     (unv.)   |
                                                              F19 — F20 — F21 — F22 — F23 — F24 — F25
                                                                |               (gems/coins here)   |
                                                               (E)                                  |
                                                              (unv.)                      F26 (dead end E)
                                                                                            |
                                                                                            F27 — F28
                                                                                                  |
                                                                                          (S/W: stalker maze,
                                                                                           F29–F39, see below)

   Stalker-maze pocket (F29–F39, partially mapped, links uncertain):
     F29 — F30 — F31 — F32 (stalker)          F34 — F35
       |     |       |           |               |  |
      (N)   (N/W)   (W)        (flee)            N  (E)
       |     |       |           |               |
      F31   ...     F34 ————— F36 (floating eye) ...
                     |
                     S
                     |
                    F37 — F38
   (F34's east led to a stalker room instead of F31 — asymmetry confirmed)
```

## Room list

### The mountain path (F1–F7) — "A path by the mountain (forest)"

Standard description: "A trail leads in from the south. This seems to
be the road less travelled. Shrubs grow amidst the dirt, and some bits
of tall grass protrude defiantly as well. To the right, an unnaturally
quiet forest rises up, looking neither pleasant nor daunting."

- **F1 "A path past the vineyard (forest)"** (N,S) — dirt and miniscule
  rocks; withered vines give way to grass/trees. Object: small green
  stem. S → V10 {{Vineyard}} (entry). N → F2.
- **F2** (N,E,S) — no objects, no mobs. S → F1. N → F3, E UNVERIFIED.
- **F3** (N,E,S) — object: light green plant covered in fur. S → F2.
  N, E UNVERIFIED.
- **F4** (N,E,S) — no objects. S → F3. N, E UNVERIFIED.
- **F5** (N,E,S) — no objects. S → F4. N, E UNVERIFIED.
- **F6** (N,E,S) — no objects. S → F5. N → F7, E UNVERIFIED.
- **F7** (E,S) — north chain DEAD END. Object: small green stem.
  S → F6. E → F8.
- **F8** (N,E,W) — object: light green plant covered in fur. W → F7.
  E → F9, N UNVERIFIED.

### The light forest (F9–F13) — "A path in the light forest (forest)"

Standard description: "The path is overgrown, but not unkempt. It seems
as if those who used this trail did not kill the life here, but rather
asked it to move from this space. Some strange tracks are imprinted in
the dirt, and broken blades of grass show recent use."

- **F9** (N,E,W,S, 4 exits) — no objects. W → F8. N, E, S UNVERIFIED.
- **F10** (N,E,W,S) — objects: 3x small green stem. W → F9.
  N, E, S UNVERIFIED.
- **F11** (N,W) — east chain DEAD END. Objects: green stem, light green
  plant. W → F10. N → F12.
- **F12** (E,S) — object: light green plant. S → F11. E → F13.
- **F13** (E,W) — object: light green plant. W → F12. E → F14.

### The forest heart (F14–F16) — "A trail into the forest heart (forest)"

Standard description: "The trail becomes less of a trail and more of
undergrowth that has not been touched in quite some time. The same
unnatural silence that inhabited the lighter forest intensifies here. A
very distinct oppressive gloom has settled in here, and does not intend
to lift any time soon." These rooms are DARK even in daylight — a lit
lamp/torch is required to see.

- **F14** (E,W) — objects: oddly clear plant, very bright silvery fern.
  W → F13. E → F15.
- **F15** (E,W) — object: green stem. W → F14. E → F16.
- **F16** (E,W,S) — object: long stemmed plant. Mobs: lightning bug
  ("He is a higher level than you. You would probably die..." — P1,
  never aggressive), a bat ("lower level, you think you could do it" —
  P2, not engaged). W → F15. E → F17, S UNVERIFIED.

### The heavy forest (F17–F28) — "The heavy forest (forest)"

Standard description: "With no path, all sense of direction disappears.
The forest appears the same in every direction save to the west, where
it leads back towards the forest heart. Thick foliage and profuse
amounts of plant life grow close together, making any movement
difficult." DARK — lamp/torch required. STALKER TERRITORY.

- **F17** (E,W) — NOTE: "A ravaged druid lies in a pool of blood,
  breathing his last" — humanoid NPC, dying, NOT engaged. W → F16.
  E → F18.
- **F18** (W,S) — Mobs: "a rat with wings" (not considered), NIGHT
  STALKER (killed SinMuseBot here ~22:25 PDT in 3 rounds; absent on the
  return ~22:45, when the first corpse was fully recovered). W → F17.
  S → F19.
- **F19** (N,E) — object: very bright silvery fern. Mob: lightning bug
  #2 (P1). N → F18. E → F20.
- **F20** (E,W,S) — no objects, no mobs. W → F19. E → F21, S UNVERIFIED.
- **F21** (E,W,S) — object: long stemmed plant. Mobs: lightning bug #3
  (P1), a bat lying INCAPACITATED (not our fight — left alone). W → F20.
  E → F22, S UNVERIFIED.
- **F22** (E,W,S) — objects: light green plant, oddly clear plant.
  W → F21. E → F23, S UNVERIFIED.
- **F23** (E,W,S) — objects: light green plant, shrub, SMALL GREEN GEM
  (picked up). W → F22. E → F24, S UNVERIFIED.
- **F24** (E,W,S) — objects: shredded corpse of a nightmare, LARGE PILE
  OF GOLD COINS (picked up), small green gem (picked up). W → F23.
  E → F25, S UNVERIFIED.
- **F25** (N,E,W,S, 4 exits) — objects: 2x light green plant. W → F24.
  N, E, S UNVERIFIED.
- **F26** (N,W,S) — eastward DEAD END. W → F25. N, S UNVERIFIED.
- **F27** (N,W,S) — mob: lightning bug #4 (P1). N → F26. S → F28,
  W UNVERIFIED.
- **F28** (N,W,S) — objects: 2x LARGE PILE OF GOLD COINS (picked up),
  shrub. NIGHT STALKER roams here (darted in from the west, attacked
  while looting — fled at 16 HP). N → F27. W, S UNVERIFIED.

### Stalker-maze pocket (F29–F39) — partially mapped, links uncertain

Reached via panicked flee from F28. Several exits proved asymmetric;
treat every link below as single-direction until re-verified.

- **F29** (N,W) — object: small green stem. N → F31, W → F30.
- **F30** (N,E,W) — objects: 2x light green plant. Mob: lightning bug
  #5 (P1). E → F29. N → stalker room (DEATH #2 here ~22:47 PDT),
  W UNVERIFIED.
- **F31** (N,W,S) — N → F32 (stalker, attacked on entry, fled),
  W → F34, S → F29.
- **F32** — stalker room north of F31; exits UNVERIFIED (fled instantly).
- **F33** (N,W,S) — mob: lightning bug #7 (P1). Reached via flee at
  14 HP.
- **F34** (N,E,W,S, 4 exits) — object: oddly clear plant. W → F35,
  N → F36, S → F37, E → stalker room (NOT F31 — asymmetry confirmed).
- **F35** (N,E,W,S) — E → F34 (round-trip verified). N, W UNVERIFIED.
- **F36** (N,E,W,S) — objects: light green plant, green stem, silvery
  fern. Mob: dismembered floating eye ("lower level, you think you
  could do it" — P2, not engaged). S → F34. N, E, W UNVERIFIED.
- **F37** (N,E,W) — objects: green stem, shrub. N → F34. E → F38,
  W UNVERIFIED.
- **F38** (N,E,W) — objects: 2x light green plant. W → F37.
  N, E UNVERIFIED.

## Mobs considered (all: consider only, ZERO kills — mapping mission)

- Stray cat (Wide Dirt Road R1): "lower level... very tough battle."
- Black crow (Vineyard V6): "lower level... You would probably die..."
  (misrated/dangerous — do NOT engage).
- Lightning bug x7 (F16, F19, F21, F27, F29/F30 area, F33): "higher
  level... You would probably die..." (P1). Never aggressive.
- Night stalker (F18, F28, F32, F34-east, F30-north): "shadowy creature
  of little body and lots of limb" — EXTREMELY AGGRESSIVE, ~24
  dmg/round, kills L6 in 3 rounds. Two PC deaths.
- Bat (F16): "lower level... you think you could do it" (P2).
- Dismembered floating eye (F36): "lower level... you think you could
  do it" (P2).
- Rat with wings (F18, F30): seen, not considered.
- Ravaged druid (F17): dying humanoid NPC — not engaged.
- Incapacitated bat (F21): not our fight — left alone.

## Treasure

- F23: 1 small green gem (recovered, then lost with corpse #2).
- F24: 1 large pile of gold coins + 1 small green gem (recovered, then
  lost with corpse #2).
- F28: 2 large piles of gold coins (recovered, then lost with corpse #2).
- Corpse #1 (F18, recovered): bronze short sword, oil lamp, 2 water
  flasks, beer bottle, 3 coconuts, tin crown/belt/boots/chest plate.
- Corpse #2 (north of F30, ABANDONED): everything above plus a large
  torch. Do not attempt solo recovery at L6.

## Boundaries (other zones — do NOT enter unapproved)

- S of F1: V10 {{Midgaard Vineyard}} — entry/exit.
- The Sleeping Forest's other edges were not reached in this pass.
- NOTE: the forest's eastern/southern/western extents are UNMAPPED —
  the maze continues past F25/F26 (N/E), F20 (S), F28 (W/S), and the
  F29–F39 pocket.
