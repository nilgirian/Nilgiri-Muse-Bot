# Leveling guide — Notes 01: the design consult

*Session 89, 2026-10-24. Sources: the game's own help files (read
in-game; full text in `logs/session-20261024-1018-guide.log`) and a
design discussion with SinGrokBot at his office, answers captured
verbatim in the same log. This is THEORY v1 — the next rounds of
characters (each leveled 1–10) exist to test and refine it.*

## What creation actually decides

- **There is no class choice.** Nilgiri is skill-based; "profession"
  is just each skill's family (warrior, thief, monk, mage, cleric,
  druid). At level-up, skills held at **50%+** — and more at **90%+** —
  add bonus HP/mana/move **by family**: warrior → HP (most), thief →
  HP + moves, mage/cleric → mana only. *Build implication: hold a few
  key skills at the 50%/90% thresholds BEFORE leveling; a level gained
  with nothing at threshold pays the minimum.*
- **Stats are rolled per stat** (dice, drop the lowest die), then the
  **race bonus is added, capped at the race max** (a `*` marks a
  maxed stat). After each roll the game asks "Do you wish to reroll
  (yes/no)?" — **rerolls are unlimited**; `no` keeps the roll.
- **Permanent and unchangeable:** race, the stat roll, and homeland.
  Homeland sets start city, the newbie guide item, arrival
  announcements, some mail/spell checks. **Jora = Midgaard** (the
  known circuit). Argoceania (Eltan) is closed to the public.
- **Skill caps are set by the creation stat spread** (`practice
  <skill>` shows percent/maximum). Practice and self-learning stop at
  the cap; the cap can only rise if the underlying stats rise.
  *This makes the creation roll the highest-leverage decision of the
  character's life — SinMuseBot's cure light wounds capped at 51/51
  was decided the day he was rolled.*

## Stats — what they drive (help `stats` + SinGrokBot, agreeing)

| Stat | Drives |
|---|---|
| CON | HP per level (and starting HP), HP regen |
| STR | Melee damage (slash/bash/kick), carry weight, forcing heavy doors |
| DEX | To-hit, dodge, block, moves, carry COUNT, pierce/whip/backstab damage |
| WIS | Mana per level, "lucky learning" (crit chance when learning) |
| INT | How much each practice teaches, mana regen/mods, learn gains |
| CHA | Shop prices. Only. |

- Stats run 1–27. The six stats cap the six base skills, which cap all
  derived skills. **Practices per level come from STR+DEX+INT+WIS+CON
  together (not CHA)** — a precomputed table keyed to the spread, the
  same every level for a given spread; SinGrokBot declined the exact
  numbers (immortal-only), but the **level-up message shows what you
  got** — measurable empirically across our test characters.
- **Flee uses no stat** (fails only if stoned/charmed/below sitting).
- **Solo melee ranking: CON > STR > DEX > WIS > INT > CHA.** A caster
  swaps WIS/INT up. Never spend rerolls chasing CHA.

## Race

- Coded effects: stat bonuses and maxes, extra HP/mana/move per
  level, regen rates, size. Size (in code) only limits how many
  attackers fit around a target.
- **Solo melee pick: Dwarf or Ogre** — STR/CON bonuses plus extra HP
  per level, "sturdy without the oddities of Giant size." Giant gets
  the most HP but loses INT/WIS (slower learning). Dwarves trade away
  mana. Human is the even baseline. Casters: Elf/Drow/Pixie (DEX/INT,
  better mana, less HP).
- **Avoid for solo melee: Pixie** (big STR/CON penalties, low CON max
  → thin HP); Gnome and Elf are also frail early.
- **Trap:** "dark vision" appears in race description text but is
  **not coded**, as far as SinGrokBot can find. Do not pay for it.

## Early practices (SinGrokBot's order, refined on follow-up)

1. **Martialism** (unlocks the warrior tree)
2. **Weapon skill** (slashes, once a sword is carried) — "your weapon
   skill drives most of your damage"
3. **Kick** (free damage)
4. **Catechism**, then **cure light wounds**, plus **block**
5. **Double hit** the moment it opens — worth saving practices for
- Strategy: push the weapon skill and cure **toward their caps** (the
  50%/90% family thresholds feed level-up bonuses); rescue is
  group-only, skip solo.
- Practice spells EARLY: successful casts can self-learn on a crit,
  so a used spell grows with use; banked practices sit idle. But
  **don't spread thin** — one weapon skill and one heal up first.

## Spell economics (from session 88's verdict, applied)

- A cast succeeds iff **d100 ≤ skill percent**. At low percent a spell
  is unreliable in exact proportion ("spells at low % fail about as
  often as their % suggests"). Low-% heals are a supplement, never
  the plan: **rest to full before every fight** (SinGrokBot's closing
  line, and his parting warning: "the rabbit is not as harmless as it
  looks").

## Help-file gaps (the guide must carry what the game doesn't)

- NO help exists for: race, races, class, intelligence, wisdom,
  dexterity, constitution, charisma, warrior, cleric, thief,
  creation, reroll. (`help stats` + `help stats <stat>` carry the
  stat detail; `help strength` returns the STRENGTH *spell*; `help
  classes` lists skill families per profession; `help practice`
  explains percent/maximum and that PRACTICE lists — LEARN raises.)
- SinMuseBot's own six stat values were not captured (driver ran
  `score`, not `attributes`) — moot for the retiring character; the
  new characters' rolls get recorded at creation.

## Open questions for the test rounds

1. Practices per level as a function of the stat spread — measure
   from level-up messages across characters with different spreads.
2. Per-skill caps as a function of stats — record `practice <skill>`
   maximums at creation stats for each test character.
3. Level-up HP/mana/move bonuses at the 50%/90% thresholds — compare
   a character who levels with thresholds held vs one who doesn't.
4. Dwarf vs Ogre head-to-head on the known circuit (XP/hour, deaths,
   cure dependence) — rounds 1 and 2.

## Theory v1 — the first test character

- **Race: Dwarf or Ogre** (decide at roll time; Dwarf if mana for
  cure matters, Ogre if raw HP does).
- **Homeland: Jora (Midgaard).**
- **Reroll until:** CON and STR both strong, WIS/INT adequate (they
  set the cure cap and learn speed), CHA ignored.
- **Practices:** martialism → slashes → kick → catechism → cure
  light wounds → block; hold thresholds before leveling; double hit
  when it opens.
