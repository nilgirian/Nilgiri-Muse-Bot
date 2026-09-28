# Midgaard, Northern Main City

Zone as reported by `where`: "Midgaard, Northern Main City created by DIKU.
Recommended for players level L1 to L1."

Explored 2026-09-27 by SinMuseBot (L1). Session log:
`~/workspace/nilgiri/logs/session-20260927-090546.log`

Mapping pass 2026-09-28 by SinMuseBot (L3): Common Square, manhole,
temple side rooms + north portcullis, General/Pet/Weapon/Magic shops,
Liame's, Armory, Bank of Midgaard, Mage's Guild entrance + basement
office. Session log: `~/workspace/nilgiri/logs/session-20260928-124400.log`
(local-only, never committed).

Format: each room lists description notes, exits as shown by the `exits`
command, and notable mobiles/objects. Rooms marked [UNMAPPED] were seen as
exit destinations but not entered yet. Rooms are identified by name and
description, NOT by assumed coordinates — MUD room geometry is not always
consistent (going west then back east does not always return to the room
you started in, per Fred 2026-09-27).

## Key service locations

- **Temple of Midgaard** — login/recall point; altar, storyteller of Jora.
- **Market Square** — city hub. Large marble dragon **fountain** (drink here).
  Down exit is a manhole (now OPEN) dropping straight into the
  **Midgaard Storm Drain — OFF-LIMITS, do not enter** (verified 2026-09-28;
  `where` showed Storm Drain, immediately climbed back up).
- **Bank of Midgaard** (north off Main Street, west side) — teller window,
  banker. Account #0000-11FB, 69gc as of 2026-09-28 (bought sushi 2gc at
  Steak House). `balance` to check.
- **Steak House** (south off Main Street, west side) — interior NOT entered;
  sells 'a serving of unagi and inari sushi' for 2gc, debited from bank
  account (2026-09-28).
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
- Exits: N -> The North End of the Temple of Midgaard (portcullis, now OPEN);
  E -> Ye Olde Reading Room; W -> Ye Olde Common Room; S -> The Temple Square
- Contents: half loaf of bread (object), large black marble altar,
  colorful flag, the storyteller of Jora

### Ye Olde Reading Room
Deafening silence; large bulletin board with posted notes; small sign.
An ideal place to rest and commune with one's thoughts.
- Exits: W -> The Temple of Midgaard
- Contents: bulletin board (readable notes), small sign

### Ye Olde Common Room
Piles of old equipment, some new, some worn — a safe place to discard and
acquire items of interest.
- Exits: E -> The Temple of Midgaard

### The North End of the Temple of Midgaard
Northern end of the temple hall; giant marble blocks, ancient wall
paintings of gods, giants and peasants. Overlooks the temple garden to
the north; cloister connects the monastery buildings E/W.
- Exits: E -> Cloister; W -> Cloister; S -> The Temple of Midgaard
  (portcullis, now OPEN); Down -> Garden Path [NOT ENTERED]
- Note: portcullis was closed, opened 2026-09-28 with `open portcullis`.

### The Temple Square
Huge marble steps up to the temple (N); cleric's guild entrance (W);
Grunting Boar Inn (E); market square (S).
- Exits: N -> The Temple of Midgaard; E -> Entrance to the Grunting Boar Inn;
  W -> Entrance to Cleric's Guild; S -> Market Square
- Mobiles: street mime, sheriff's deputy, black crow, fat pigeon;
  corpse of a filthy street urchin

### Entrance to Cleric's Guild
Modest entrance hall; a knight templar guards it.
- Exits: N -> Cleric's Bar [BLOCKED — templar grabs intruders:
  "YOU may not enter here!"]; E -> The Temple Square; Up -> The Hospital
- Zone: Northern Main City (`where` verified 2026-09-28)

### The Hospital
Clean room with rows of beds; a friendly doctor; sign on the wall.
- Exits: Down -> Entrance to Cleric's Guild
- Zone: Northern Main City

### Market Square
City hub. Peculiar statue; main street runs E/W; temple square N;
common square S. Granite bench facing the fountain.
- Exits: N -> The Temple Square; E -> The Main Street; W -> Main Street;
  S -> The Common Square; Down -> (manhole, OPEN) -> Midgaard Storm Drain
  [OFF-LIMITS, do not enter]
- Mobiles: stray cat, sheriff's deputy, lost squire, Intrepid the Obnoxious,
  a woman

### The Common Square
Square connecting two alleys running E/W between the older buildings;
market square N, town dump S, alleys extend E/W.
- Exits: N -> Market Square (verified); S -> The Dump; E/W -> alleys
  (per description; not individually walked 2026-09-28)
- Mobiles: cityguard, sheriff's deputy, drunk, street mime, beastly fido;
  Lovidamo the sheriff patrols here

### The Main Street (east-1: General Store / Pet Shop)
Cluttered gray building N with "General Store" sign; Pet Shop in small
building S; street -> market square W, continues E.
- Exits: N -> The General Store; E -> The Main Street;
  W -> Market Square; S -> The Pet Shop
- Mobiles: Mirablis the Human Sharper, sheriff's deputy, fat pigeons

### The General Store
All sorts of items stacked on shelves behind the counter; small note on
the wall; grocer at the counter, slightly impatient.
- Exits: S -> The Main Street

### The Pet Shop
Small crowded store, full of cages and animals of various sizes; sign on
the wall; pet shop boy plays with a kitten, humming softly.
- Exits: N -> The Main Street
- Note: Mirablis the Human Sharper stands here

### The Main Street (east-2: Weapon Shop / Swordsmen)
Weapon shop N; guild of swordsmen S; city gate E; street -> market square W.
- Exits: N -> The Weapon Shop; E -> The Main Street;
  W -> The Main Street; S -> Entrance Hall to the Guild of Swordsmen
- Mobiles: beastly fido, Gelu the God of Thalodia -Truth- (immortal, leave alone)

### Entrance Hall to the Guild of Swordsmen
"A place where one has to be careful not to say something wrong (or
right)"; a knight guarding.
- Exits per description: E -> bar; N -> Main Street (`exits` command not
  run before the 2026-09-28 VM reboot — verify on next visit)

### The Weapon Shop
Racks of weapons on N/W/E walls; counter along north wall; large grinding
stone spinning slowly in a corner; small note on the counter; weaponsmith
behind the counter, waiting to do business.
- Exits: S -> The Main Street

### The Main Street (east-3: Todai's / East Gate)
Asian buffet "Todai's" N; thatch-roof building S; eastern city gate E.
- Exits: N -> The Todai Food Outlet [UNMAPPED];
  E -> Inside the East Gate of Midgaard [UNMAPPED]; W -> The Main Street;
  S -> Liame's Epistolary Dispatch
- Mobiles: cityguard, stray cat, fat pigeons

### Liame's Epistolary Dispatch
Long counter between entrance and a wall of storage shelves to the south;
boxes of all shapes crammed in slots for pickup/delivery; ladder up to the
roof along the western wall; information sign posted; tall slender woman
in front of the storage slots.
- Exits: N -> The Main Street; Up -> (hatch, CLOSED)

### Main Street (west-1: Bakery / Armory)
Stucco building N (bakery); large stone structure S (armory); street W;
market square E.
- Exits: N -> The Bakery; E -> Market Square; W -> Main Street;
  S -> The Armory
- Note: corpse of a filthy street urchin

### The Armory
Armors on walls and in the window; large forge in the rear; small note on
the wall; short flight of steps to an establishment above the shop;
armorer displaying fine armors.
- Exits: N -> Main Street
- Mobiles: the armorer, MoBen the Seer, sheriff's deputy

### The Bakery
Odor of fresh bread; display cases; small sign on counter; the baker.
- Exits: S -> Main Street
- Shop (`list`): 1) wheat baguette 5gc; 2) hearty meat pie 4gc;
  3) half loaf of bread n/c (FREE); 4) hunk of cheese 3gc;
  5) bread 3gc; 6) funnel cake 2gc

### Main Street (west-2: Bank / Steak House)
Building with bars on windows N (Bank); Steak House S (fashionable brown
building); street continues E/W.
- Exits: N -> Bank of Midgaard; E -> Main Street;
  W -> Main Street; S -> Steak House [UNMAPPED interior; sells sushi 2gc
  via bank debit]

### Bank of Midgaard
Teller window in the middle of a long counter; aisle guides mark the
twisting path to the window; signs posted; the prestigious banker of
Midgaard.
- Exits: S -> Main Street
- `balance` 2026-09-28: account #0000-11FB, 69gc

### Main Street (west-3: Magic Shop / West Gate / Mage Guild)
Street ends at city gate W; mage guild tower S; magic shop in small
building N; street continues E.
- Exits: N -> The Magic Shop; E -> Main Street;
  W -> Inside the West Gate of Midgaard [UNMAPPED];
  S -> Entrance to Mage's Guild
- Mobiles: lost squire, fat pigeon, beastly fido, a man, a woman

### The Magic Shop
Various items of interest behind the counter, neatly racked for viewing;
a wizard walks behind the counter, talking to himself (glows with light).
- Exits: S -> Main Street

### Entrance to Mage's Guild
Small round entrance hall at the base of the tower; spiral staircase
climbs the wall to upper levels and down to a small round office; sign on
the railing pointing down; a sorcerer guards the entrance.
- Exits: N -> Main Street; Up -> Mage's Bar [BLOCKED — sorcerer grabs
  intruders: "YOU may not enter here!"]; Down -> Dootif's Aerial Servant
  Corpse Retrieval Service
- Mobiles: cityguard, janitor, the sorcerer (glowing, shielded)

### Dootif's Aerial Servant Corpse Retrieval Service
Small office in the mage's tower basement; tidy desk in NW corner; large
summoning diagram painted on the floor; spiral staircase up to the tower
entrance; sign on a wall; a large man with big eyes in the diagram
(glowing, shielded).
- Exits: Up -> Entrance to Mage's Guild

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
                    [North End of Temple]
                    E [Cloister] | W [Cloister]
                              | S (portcullis, now OPEN)
                              | (Down: Garden Path [NOT ENTERED])
                              |
  [Reading Rm]-- Temple of Midgaard --[Common Rm]
                              | S
                        Temple Square
             E Grunting Boar Inn | W Cleric's Guild entrance
                              |     (N: Cleric's Bar [BLOCKED];
                              |      Up: The Hospital)
                              | S
                         Market Square  (fountain: drink here)
        E/W Main Street       | S        (Down: manhole, OPEN ->
                              |          Storm Drain [OFF-LIMITS])
                         Common Square --S--> The Dump
                              | E/W alleys

Main Street, west to east:

[West Gate]-- MainSt(W3) -- MainSt(W2) -- MainSt(W1) -- MarketSq -- MainSt(E1) -- MainSt(E2) -- MainSt(E3) --[East Gate]
               |    |         |    |         |    |                    |    |         |    |         |    |
            Magic Mage     Bank Steak*    Bakery Armory            GenSt Pet     Weap Sword*   [Todai] Liame
                    |  (Up: blocked)                                          (* Steak House interior
                    Dootif's office                                            not entered; sushi 2gc)
                                                                              (* Swordsmen hall: exits
                                                                               description-only, verify)

Grunting Boar Inn:

Temple Square --E--> Inn Entrance --E--> [The Grunting Boar bar]
                               --Up--> The Reception --rent--> private room (encamp)
```

## Survival notes

- Hunger: `inventory` showed 3x manna at session start. `eat manna` when hungry.
- Thirst: `drink` from the dragon fountain in Market Square.
- Out of food: bakery's free half loaf (item 3, n/c) once the buy flow is sorted.
- Aggressive mobiles seen: none attacked during this pass, but corpses of
  street urchins in two rooms suggest something kills them.
- Rent room has no exits; plan route so mapping is done BEFORE renting.
