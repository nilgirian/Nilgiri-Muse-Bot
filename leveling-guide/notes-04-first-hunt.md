# Leveling guide — Notes 04: level 1, measured (Testudo, day one)

*Session 92, 2026-10-24. Two hours (one VM reboot, recovered
with no loss). Raw log: `logs/session-20261024-1317-testudo-hunt.log`
(local). Testudo: Dwarf, STR 17 / DEX 5 / INT 13 / WIS 15 /
CON 18 / CHA 16. Result: XP 0 → 247, 8 beastly fido kills,
0 deaths, still level 1.*

## Practices at level 1: ZERO

The practice list of a brand-new character reads "You have
nothing practiced" and **"You have 0 practice sessions
remaining."** Nothing can be practiced at level 1 — practice
sessions arrive with level-ups. The theory-v1 practice order
(martialism → weapon → kick → catechism → cure) therefore
begins at level 2, and a level-1 character's only progression
is XP, gear, and gold.

## The cap formula — printed by the game itself

`practice <family>` shows the arithmetic. A stat's
contribution scales as **floor(stat / 21 × 100)** (17 → 80,
18 → 85, 15 → 71, 13 → 61, 5 → 23), weighted by the family's
shares:

- **Martialism** (STR 50% / DEX 30% / CON 20%):
  0.50×80 + 0.30×23 + 0.20×85 = 40 + 6 + 17 = **64 max**
- **Catechism** (WIS 75% / INT 25%):
  0.75×71 + 0.25×61 = 53 + 15 = **69 max**

Testudo's six family maxima: **Martialism 64, Subterfuge 35,
Animism 58, Catechism 69, Elementalism 69, Spellcraft 66.**
For comparison, SinMuseBot's cure light wounds capped at
51/51 — Testudo's catechism ceiling of 69 promises a
materially stronger heal, the WIS-15 roll paying off exactly
as designed.

**Prerequisite gates are real:** Slashes and Kick report
"You need to learn a pre-requisite" (100% Martialism,
unskilled → derived maximum 0); Cure Light Wounds is gated
the same way behind Catechism. You cannot touch a derived
skill until its parent family has points.

## Combat at DEX 5 — the crit lottery

Eight fido kills, and the pattern is absolute:

- **Normal attacks essentially never land.** Round after
  round of "You misplace your footing" — with DEX 5 and no
  weapon skill, the ordinary hit roll fails against even a
  fido. **Every kill came from a barehanded critical hit**
  (crits also pay bonus wound XP; one paid +48 by skipping
  straight to incapacitated).
- **The Dump staff was worse than bare hands:** "The weapon
  feels unwieldy in your hands, causing you to miss" — it
  connected roughly once in 25+ rounds. An unpracticed weapon
  type is a liability, not an upgrade.
- **Consider rates your ARMED state:** the same fido reads
  "easy battle" with the staff wielded but only "you think
  you could do it" barehanded — while the barehanded mode
  actually kills faster (crits). Trust consider for danger,
  not for kill speed, until a weapon is practiced.
- A fido fight runs ~7–9 rounds of bites (2–5 damage; crit
  bites spike hard) while you wait for your crit. Autoflee
  (noflee at half HP) fired ~10 times across the day — it is
  what makes the lottery survivable. Pigeon considers P2
  either way; a stray cat reads "probably die"; a black crow,
  "you shiver". At L1 the city menu is fidos, full stop.
- **Regen is a coarse tick** (roughly +1 HP per 3 ticks
  observed as 24→36 jumps while resting), and it applies to
  mobs too: a downed fido left alone revives at "excellent
  condition" within seconds. **Finish incapacitated mobs
  immediately** — two of the eight kills were mobs that
  "succumbed to their wounds" while being finished.
- `kick` works unlearned at 0% (it starts combat and mostly
  fails, with a few rounds of "fighting" lag after) — a
  curiosity, not a tool, until practiced.

## Economy of a penniless dwarf

- Fido corpses were **empty, all eight**. Gold for the whole
  day: **0**. The first coins must come from somewhere else
  (sales, richer prey, or quests) — plan L1 accordingly.
- Weapon shop prices (General Store): bronze dagger 4 gc,
  wooden club 9 gc, **bronze short sword 9 gc**, bronze
  warhammer 16 gc. The short sword is the L2-practice target
  (slashes) once 9 gc exists.
- Street loot is real armor: by exit he wore a tin crown,
  tin bracer, wooden shield, tin chest plate, black leather
  shorts and boots — AC from "naked" to "lightly covered",
  all free off the ground.
- Hunger/thirst cycle ≈ 35–40 minutes of play. Three manna
  was NOT enough for two hours; he ended the day hungry with
  no gold. **Carry more food** (bakery half-loaves are free)
  on every future hunt.

## Level thresholds

247 XP after two hours and still level 1. Combined with
SinMuseBot's history (still L1 at 334 XP), the L1→L2
threshold is **above 334** — the guide's first open number
to pin down next session.
