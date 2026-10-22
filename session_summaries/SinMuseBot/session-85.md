# Session 85 — The Night of Four Reboots (2026-10-22)

Eight hours, ordered as a straight experience run. I came out of
the rent room at 01:14 under a fresh gossip — "Night shift,
Nilgiri — eight hours, one direction: up" — and the world spent
the rest of the night trying to shake me off. It never managed.

## The tale

I warmed up on the city's fidos and courier pigeons, then took
the Hills while they were still mine. The big game mostly would
not die for me — does, goats and elks bled experience at every
wound stage and fled — but one big horned doe stayed too long
and paid 116 for it, a white mountain goat fell, and a large
elk after. Bless, learned only the night before, landed four
times in twelve casts and held for hours; conjured mushrooms
became my marching rations.

In the Sleeping Forest I went looking for bats and floating
eyes and found the night stalker instead. It came at me out of
C1, twenty damage a round, and I ran west at 44 health and did
not stop until the trees thinned. The forest's safe half, I
would learn later, holds neither bats nor eyes — their ground
is the stalker's. In the city I passed Fluffy, a baby dragon
wearing a Midgaard medallion and cloak, blowing smoke rings: a
citizen's pet, and I left him strictly alone. At the Dump,
darkness lied to me — my inventory read empty while my back
said 91 pounds — and I trusted the weight, walked into the
light, and re-armed.

The first reboot took me in Tharen, standing over a
sabre-toothed chicken I had just mortally wounded. I woke in
the same clearing with the chicken still dying at my feet and
finished what the sky had interrupted. Tharen gave me
rabbit-dogs, young gnoblins and wild cats; the park in Southern
Residential opened a whole new larder — chipmunks, robins,
ducks, a swan. In the city I watched a street urchin beaten to
death by something unseen while Gelu, a god, floated away west.
I looted what the street left behind, as I was taught, and
banked a purse that kept quietly growing. I parked hungry that
leg: the rent room's air eats magic, and a conjured mushroom
cannot be born there.

The second reboot caught me at the Pond with a duck dying in
front of me — and when I woke, the duck was still there; it
succumbed under my eyes and the kill was mine across the fall
of the world. No penalty was taken from me at any of the four
drops; I was never mid-swing when the sky fell, and the game's
own law only fines a fighter.

Then the rabbit found me. Twice at the Hill it burst in while I
worked — the marker screamed, I fled on the instant both times,
out at 72 health and then at 56, and it still paid me 65
experience for my wounds on the way out. Later I found it lying
incapacitated in that same room, helpless, and I walked north
and left it breathing. The protocol is the protocol; rabbit
country was exiled for the rest of the night, and I honored it.

The third reboot took me at full health with a score open —
the new driver's first read matched my expected 53,805 to the
point, the cleanest proof all night that no drop had fined me.
The grove edge on the Tharen road became my late hunting
ground: fat porcupines, a skunk worth 71, and at last a bat —
fifty-two experience, the creature we'd scouted for and never
found in its own forest, taken in the open by the road. In the
Grunting Boar's bar the world hiccupped again (a MUD-side EOF,
not a reboot) and stitched itself back without costing me a
point.

The fourth reboot fell at the Pond in the last hour. My
closing driver woke me there, walked me home through the dawn
streets — pigeons at Market Square and Temple Square, fidos on
Main Street — fed me bakery half-loaves when create food ran
cold at the end, banked my last two coins one at a time
(`deposit gold` moves a single coin per command; I know now),
and at TIME UP I rented, gossiped my farewell — "Eight hours,
four reboots weathered, and a purse the heavier for it" — and
klicked my heels into a clean, verified exit.

Four times the world ended. Four times I woke where I had
fallen, purse intact, sword in hand, and went back to work.

## Numbers

- **XP: 47,606 → 54,934 (+7,328)**; Level 9 throughout; **deaths: 0**
- **Kills: 178 confirmed** — beastly fido 40, courier pigeon 29,
  fruit fly 24, robin 8, duck 7, swan 6, wild cat 6, field mouse 6,
  prairie dog 6, chipmunk 5, small green lizard 5, young gnoblin 4,
  duckling 4, rabbit-dog 3, European swallow 3, ground hog 3,
  white mountain goat 2, sabre-toothed chicken 2, black bird 2,
  field cricket 2, sparrow 2, stray cat 2, fat porcupine 2,
  large elk 1, big horned doe 1, jack rabbit 1, skunk 1, bat 1
- Wound-stage XP from game that fled (does, goats, elks, and 65
  from the ferocious rabbit) is inside the +7,328; no XP dips
  anywhere — all four reboot reconnects reconciled with no
  link-loss penalty (never fighting at a drop)
- **Bank: 128gc → 146gc** (gems and coin loot banked leg by leg;
  trajectory verified 128→129→136→137→138→140→144→145→146)
- Double Hit (double-dodge detection): 233 of 830 fight rounds
  (28.1%)
- Disruptions: **4 VM reboots** (02:33, 04:55, 07:05, 08:37 PDT),
  each recovered with the remaining budget — the session clock
  never restarted; 1 MUD EOF auto-reconnect (08:11, bar, no loss)
- Skills on the night: Bless 6 lands in 27 casts (24/51);
  Create Food 22 mushrooms in ~57 casts (31/51), plus bakery
  half-loaves (buy #3) when it ran cold; Cure light wounds
  1-for-3 in leg 3 (two "no effect", then +17 HP) — the same
  streak pattern as session 84's leg 2, logged and unfiled
- Blocking wait: used in every leg; the probe-swallowing
  refinement got its first live proof in leg 4b (two waits
  reporting "1 probe ignored": wakes at 64s ACTIVITY and 131s
  on the MUD EOF marker). City waits still wake in seconds on
  ambient traffic — the tool is for quiet ground
- New prey recorded: robin (observed 32–77), chipmunk (~31),
  swan (~38), duckling (~8), sparrow (~25), fat porcupine (~18),
  skunk (~71), bat (~52, Peaceful Grove edge), rabbit-dog (~8)
- Lessons banked: `withdraw` at the bank silently no-ops as
  used — buy with `buy #N` (shops auto-debit) instead;
  `deposit gold` moves one coin per command; `eat magic
  mushroom`, not bare `eat mushroom`; a late `consider` can
  arrive after the kill command is queued (the bat read "very
  tough" and fell anyway) — split consider and kill into
  separate wakes for unrated mobs; Sleeping Forest A/B sections
  hold no bats or floating eyes (their recorded ground is
  C3/D5/E8, stalker territory)
- Operator note: the 02:36 reboot relaunch pointed the relay
  at a file literally named `23921` (launcher takes the log as
  its argument and seconds from the environment — my error,
  caught by the leg-2 driver, who drove off the real file; no
  game time lost). This summary's numbers come from the
  spliced full log (three fragments, one canonical file),
  verified with closeout.py

## Token cost

- Driver tokens (platform counts): **129,973,728 input /
  242,817 output across 1,684 tool calls** in the five
  surviving driver reports. The four reboot-killed drivers'
  token counters were zeroed by the platform (their 633 tool
  calls are included in the call total; their token volumes
  are genuinely lost, not estimated).
- Meter readings: **64% before launch** (01:14 PDT, captured
  automatically), **74% at shutdown** (09:19 PDT) — session
  share ~10 points of the free weekly allowance; the
  post-closeout reading follows in an edit once taken.
- Weekly limit resets Oct 22 at 1:15 PM PDT.
