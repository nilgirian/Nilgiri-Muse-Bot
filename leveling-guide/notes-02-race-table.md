# Leveling guide — Notes 02: the race table (qualitative)

*Session 90, 2026-10-24. Source: SinGrokBot at his office; full
exchange in `logs/session-20261024-1036-races.log`. Exact stat
modifiers are IMMORTAL-ONLY — declined, same as the practices
table ("Exact stat modifiers stay with Sin, Motorola, Russ and
Mandessa, but I can compare them for you in words."). What
follows is his qualitative table, verbatim in substance. The
creation screen does NOT substitute: at race pick it shows only
description and height/weight ranges; bonuses appear on the
roll screen AFTER the race is committed (roll + race bonus =
total, `*` at the race max).*

## Roster (13, all selectable)

Human, Drow, Dwarf, Elf, Giant, Gnoll, Gnome, Goblin, Halfling,
Ogre, Orc, Pixie, Saurian.

## The candidates for a solo melee life

| Race | Bonuses | Maxes | Per level | Regen |
|---|---|---|---|---|
| Dwarf | STR, CON up; **WIS even**; INT, DEX, CHA down | STR/CON high, WIS mid, INT/DEX/CHA low | more HP, **much less mana**, less move | HP better, mana worse |
| Ogre | STR, CON up **more than Dwarf**; WIS, DEX down; INT, CHA down more | STR/CON high, DEX/WIS mid, INT/CHA low | more HP, less mana, even move | HP better, mana worse |
| Giant | STR, CON up most; INT, WIS, DEX down more; CHA down | STR highest, CON high, CHA mid, INT/DEX low, **WIS lowest** | most HP, much less mana, more move | stronger both ways |
| Orc | STR, CON up; DEX, INT, CHA down — "like Dwarf, plainer" | — | — | — |
| Saurian | STR, DEX, CON up; INT, WIS, CHA down — **"a sleeper pick for melee"** | — | — | — |
| Human | none ("no bonuses or penalties, every max mid") | all mid | even | even |

Others (bonus direction only): Drow DEX/INT/CHA up, STR/CON
down. Elf CHA way up, DEX/INT/WIS up, STR/CON down. Gnoll
DEX/STR up, INT/WIS/CHA down. Gnome INT/WIS up, STR down.
Goblin DEX up, STR/INT/CHA down. Halfling DEX/WIS/CHA up,
STR/CON down. Pixie DEX/INT up big, WIS/CHA up, STR/CON way
down.

## Size (coded)

Human medium, Dwarf small, Ogre large, Giant big. Size ONLY
does the crowding check — bigger attackers take more room
around a target, so fewer fit. No size effect on to-hit, being
hit, or carrying (carrying is STR and DEX). Race also sets
height/weight range and an internal creature type some
spells/scripts check. Dark vision: description text only, not
race code (confirmed again).

## Cap mechanics (new, session 90)

- Each skill draws on stats in shares: **catechism (and so
  cure) draws mostly on WIS, with a smaller share of INT**;
  martialism draws mostly on STR, then DEX, then a little CON.
- **Caps are computed LIVE from CURRENT stats, including gear
  and spell bonuses.** Race max limits only the base roll; a
  WIS item or buff raises the effective stat — and the cap
  with it — while worn. **The cap is checked when you
  practice or learn, so gain while buffed.**

## Decision analysis — Testudo (round 1)

The build's self-heal is cure light wounds, which sits under
catechism → WIS-led cap. Of the three brutes, **Dwarf is the
only one that does not pay for its CON in WIS**: WIS bonus
even, max mid. Ogre buys slightly more STR/CON with a WIS
penalty that directly lowers the cure ceiling; Giant's WIS
max is the lowest of all and it learns slowly besides.
Dwarf's costs are budgetable at levels 1–10: much less mana
per level and worse mana regen (cure becomes a budgeted
resource, rest discipline matters), less move, and a low INT
max (slower learning, trims the small INT share of the cure
cap).

**Recommendation: DWARF** — and DECIDED: Fred left the final
call to Muse (2026-10-24), and the analysis above is the
reasoning: of the sturdy races, Dwarf alone keeps the
WIS-led cure ceiling intact. At creation: reroll until CON
and STR sit near their high maxes with WIS at least mid. Note the
information asymmetry: bonuses/maxes reveal themselves only
on the roll screen, after the race is committed — the `*`
marks tell you when a stat has hit its race max, which is the
signal to keep a roll.
