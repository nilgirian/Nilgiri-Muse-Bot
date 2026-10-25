# Leveling guide — Notes 05: day two, the long level (Testudo)

*Session 93, 2026-10-24 — a 4-hour XP run in three driver
legs (one link drop, one VM reboot — both while NOT
fighting, zero XP lost either time). Result: XP 247 → 650
(+403), 10 beastly fido kills, 0 deaths, still level 1.
Raw log: `logs/session-20261024-1608-testudo-xp.log`.*

## The L1→L2 threshold is 1002 XP — established

Cross-checked against SinMuseBot's record: the score bands
are L1 0–1001, L2 1002–2032 (LESSONS_LEARNED), and
SinMuseBot crossed into L2 in his session 05 at 1023 XP.
Testudo's progress therefore reads plainly: **650 of 1002
after six total hours of L1 hunting** (~100 XP/hour
average; legs ran +128/89 min, +172/74 min, +103/83 min —
variance is crit luck). Budget roughly **3–4 more hours**
to the crossing, then practices unlock.

Per-fido XP is wound-stage based and swings hard: day-two
kill totals ran **14, 24, 29, 32, 36, 47, 49**. Stage
awards are inconsistent — a crit straight to "quite a few
wounds" once paid 0 XP while stun/incapacitated/mortal
stages paid +2 to +31. XP alone never proves a kill
(standing rule); count R.I.P.s.

## The real L1 killer: PANIC flee streaks

Twice in one day, autoflee **PANIC-failed three times in a
row** at critical HP (bottoming at 7 HP in the Pet Shop,
8 HP in leg 3). Both times he was saved by a **regen pulse
landing mid-fight** (+9 to +26 HP — the coarse regen tick
does not care that you are fighting) and a following crit.
Doctrine added (now in the brief template for Testudo):
**a fight that reaches ~8 rounds with no crit and HP
under 15 gets manual `flee` commands every round** — do
not trust autoflee alone. Autoflee is a backstop, and
backstops streak-fail.

## Fight mechanics, continued

- **Target swap:** with two fidos in a room, the condition
  line flips between them and `kill fido` latches onto the
  HEALTHY roamer — a wounded fido cannot be finished
  until it is alone (`kill 2.fido` unsupported). Wounded
  fidos also wander off mid-fight. BUT: a mortally wounded
  fido can linger for minutes and then die on its own,
  paying full kill credit — worth a return sweep.
- **Corpse races:** janitors clear corpses and ground
  loot within seconds. Several of the day's kills lost
  their corpses before looting; fido corpses were empty
  10/10 anyway. Grab ground items the moment they appear.
- **Density:** after 10 kills, Main Street stood empty
  ~19:13–19:31 — repopulation lags behind a heavy hunt.
  Rotate streets and check shop interiors (fidos shelter
  in the Bakery, Pet Shop, Steak House).
- Resting regen comes in large pulses (+9 to +14) — most
  rests complete in one or two ticks.

## Banking — how it actually works (newbie-critical)

- At the Bank of Midgaard, **type `Initiate New Account`
  as a raw command line**. Doing it via `say` does
  nothing.
- Opening an account makes you a **citizen of Midgaard**;
  the banker notes a **5% annual account tax**. Testudo's
  first account now holds his entire fortune: **1 gc**
  (one shiny gold coin, found by leg 2 — the day's only
  gold from 10 kills).
- **RENT REFUSES VALUABLES — including gold coins.** One
  coin in hand ("These items are not allowed") blocks
  renting. Bank EVERYTHING before the Inn, every time.
- `deposit gold` still moves one coin per command.

## Shops — corrected listings

- **Bronze short sword: Weapon Shop** (Main Street E2,
  north), list item #3, **9 gc** — NOT the General Store
  (correcting notes-04's attribution).
- General Store: rations 5 gc, map 1 gc, small bag 5 gc,
  oil lamp 9 gc, torch 1 gc, quill/parchment 1 gc.
- The **Dump is pitch black** without a lamp at some
  hours — no lamp yet (9 gc), so no Dump diving.

## Voice and rooms

- **Rent chambers are SILENT:** `gossip` inside one
  returns "Shhhh! Silence is golden." — this session's
  farewell never reached the game. Speak farewells
  BEFORE renting, from a public room.
- Strangers will gossip at you (today: Quenyarhun, four
  questions — who are you / do you talk / do you group).
  Answer politely and briefly; orders only ever come
  from authorized controllers.

## Food math

A bakery loaf buys roughly **35–40 minutes** (first
growl at ~15–20). Leg 3 burned **six loaves in ~80
minutes** of fighting and still ended hungry and
thirsty. Rule stands: food-first every session, count
loaves by `inventory`, never by memory.
