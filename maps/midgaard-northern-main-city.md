# Midgaard, Northern Main City

Zone as reported by `where`: "Midgaard, Northern Main City created by DIKU.
Recommended for players level L1 to L1."

Explored 2026-09-27 by SinMuseBot (L1). Session log:
`~/workspace/nilgiri/logs/session-20260927-090546.log`

Format: each room lists description notes, exits as shown by the `exits`
command, and notable mobiles/objects. Rooms marked [UNMAPPED] were seen as
exit destinations but not entered yet. Rooms are identified by name and
description, NOT by assumed coordinates — MUD room geometry is not always
consistent (going west then back east does not always return to the room
you started in, per Fred 2026-09-27).

## Key service locations

- **Temple of Midgaard** — login/recall point; altar, storyteller of Jora.
- **Market Square** — city hub. Large marble dragon **fountain** (drink here).
  Down exit is a manhole [UNMAPPED].
- **The Bakery** (north off Main Street, west side) — free food: `list` shows
  item 3, 'a half loaf of bread', at n/c (no charge). Other items 2-5gc.
  NOTE (2026-09-27, corrected by Fred): buy by the LIST number with a `#`
  prefix, e.g. `buy #3` for the free half loaf (item 3). The `#03BF3A43`-style
  codes in the list are internal item IDs, not what you type. The baker's
  "What is the item #?" whisper is just flavor; the sale completes from the
  `buy #N` command itself.
- **The Reception** (up from Grunting Boar Inn entrance) — pretty
  receptionist. `rent` moves you into a private room (no exits) where
  encamp is safe. Sign warns rent is charged monthly, minimum one month.

## Rooms

### The Temple of Midgaard
Login point. Southern end of the temple hall; marble blocks, ancient wall
paintings; steps lead down through the grand temple gate to the square.
- Exits: N -> (portcullis) [closed]; E -> Ye Olde Reading Room [UNMAPPED];
  W -> Ye Olde Common Room [UNMAPPED]; S -> The Temple Square
- Contents: half loaf of bread (object), large black marble altar,
  colorful flag, the storyteller of Jora

### The Temple Square
Huge marble steps up to the temple (N); cleric's guild entrance (W);
Grunting Boar Inn (E); market square (S).
- Exits: N -> The Temple of Midgaard; E -> Entrance to the Grunting Boar Inn;
  W -> Entrance to Cleric's Guild [UNMAPPED]; S -> Market Square
- Mobiles: street mime, sheriff's deputy, black crow, fat pigeon;
  corpse of a filthy street urchin

### Market Square
City hub. Peculiar statue; main street runs E/W; temple square N;
common square S. Granite bench facing the fountain.
- Exits: N -> The Temple Square; E -> The Main Street; W -> Main Street;
  S -> The Common Square [UNMAPPED]; Down -> (manhole) [UNMAPPED]
- Mobiles: stray cat, sheriff's deputy, lost squire, Intrepid the Obnoxious,
  a woman

### The Main Street (east-1: General Store / Pet Shop)
Cluttered gray building N with "General Store" sign; Pet Shop in small
building S; street -> market square W, continues E.
- Exits: N -> The General Store [UNMAPPED]; E -> The Main Street;
  W -> Market Square; S -> The Pet Shop [UNMAPPED]
- Mobiles: Mirablis the Human Sharper, sheriff's deputy, fat pigeons

### The Main Street (east-2: Weapon Shop / Swordsmen)
Weapon shop N; guild of swordsmen S; city gate E; street -> market square W.
- Exits: N -> The Weapon Shop [UNMAPPED]; E -> The Main Street;
  W -> The Main Street; S -> Entrance Hall to the Guild of Swordsmen [UNMAPPED]
- Mobiles: beastly fido, Gelu the God of Thalodia -Truth- (immortal, leave alone)

### The Main Street (east-3: Todai's / East Gate)
Asian buffet "Todai's" N; thatch-roof building S; eastern city gate E.
- Exits: N -> The Todai Food Outlet [UNMAPPED];
  E -> Inside the East Gate of Midgaard [UNMAPPED]; W -> The Main Street;
  S -> Liame's Epistolary Dispatch [UNMAPPED]
- Mobiles: cityguard, stray cat, fat pigeons

### Main Street (west-1: Bakery / Armory)
Stucco building N (bakery); large stone structure S (armory); street W;
market square E.
- Exits: N -> The Bakery; E -> Market Square; W -> Main Street;
  S -> The Armory [UNMAPPED]
- Note: corpse of a filthy street urchin

### The Bakery
Odor of fresh bread; display cases; small sign on counter; the baker.
- Exits: S -> Main Street
- Shop (`list`): 1) wheat baguette 5gc; 2) hearty meat pie 4gc;
  3) half loaf of bread n/c (FREE); 4) hunk of cheese 3gc;
  5) bread 3gc; 6) funnel cake 2gc

### Main Street (west-2: Bank / Steak House)
Building with bars on windows N (Bank); Steak House S (fashionable brown
building); street continues E/W.
- Exits: N -> Bank of Midgaard [UNMAPPED]; E -> Main Street;
  W -> Main Street; S -> Steak House [UNMAPPED]

### Main Street (west-3: Magic Shop / West Gate / Mage Guild)
Street ends at city gate W; mage guild tower S; magic shop in small
building N; street continues E.
- Exits: N -> The Magic Shop [UNMAPPED]; E -> Main Street;
  W -> Inside the West Gate of Midgaard [UNMAPPED];
  S -> Entrance to Mage's Guild [UNMAPPED]
- Mobiles: lost squire, fat pigeon, beastly fido, a man, a woman

### Entrance to the Grunting Boar Inn
Entrance hall; boar paintings; staircase up to reception; bar to E.
- Exits: E -> The Grunting Boar [UNMAPPED]; W -> The Temple Square;
  Up -> The Reception
- Mobiles: cityguard, street mime

### The Reception
Long desk in southern wall recess; desk bell, ledger, lamp; small sign;
hall N with doors to rooms. The pretty receptionist stands behind the desk.
- Exits: Down -> Entrance to the Grunting Boar Inn
- Sign: `Offer` = get an offer on a room (rent charged monthly);
  `Rent` = rent a room, minimum one month. Warnings: pay rent or get kicked
  out and your stuff sold; no refunds.
- `rent` -> moved to "A small room for rent"

### A small room for rent (private chamber)
Small flat; white walls, white marble floor; "no way in nor out".
A piece of paper tacked on the wall (unreadable).
- Exits: none. SAFE ENCAMP SPOT.

## ASCII sketch

```
                         [portcullis]
                              |
  [Reading Rm]-- Temple of Midgaard --[Common Rm]
                              | S
                        Temple Square
                  E Grunting Boar Inn | W [Cleric's Guild]
                              | S
                         Market Square  (fountain: drink here)
        E/W Main Street       | S        (Down: manhole)
                              |
                         [Common Square]

Main Street, west to east:

[West Gate]-- MainSt(W3) -- MainSt(W2) -- MainSt(W1) -- MarketSq -- MainSt(E1) -- MainSt(E2) -- MainSt(E3) --[East Gate]
               |    |         |    |         |    |                    |    |         |    |         |    |
           [Magic] [Mage]  [Bank][Steak] [Bakery][Armory]          [GenSt][Pet]   [Weap][Sword] [Todai][Liame]

Grunting Boar Inn:

Temple Square --E--> Inn Entrance --E--> [The Grunting Boar]
                               --Up--> The Reception --rent--> private room (encamp)
```

## Survival notes

- Hunger: `inventory` showed 3x manna at session start. `eat manna` when hungry.
- Thirst: `drink` from the dragon fountain in Market Square.
- Out of food: bakery's free half loaf (item 3, n/c) once the buy flow is sorted.
- Aggressive mobiles seen: none attacked during this pass, but corpses of
  street urchins in two rooms suggest something kills them.
- Rent room has no exits; plan route so mapping is done BEFORE renting.
