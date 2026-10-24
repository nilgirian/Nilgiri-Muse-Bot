# Leveling guide — Notes 03: the creation of Testudo

*Session 91, 2026-10-24. Character created and verified in
game. Full roll data: `run/rolls_parsed_full.tsv` (573 rolls,
local). Creation logs: `logs/session-20261024-1046-creation*.log`,
`logs/session-20261024-1120-creation2.log`,
`logs/session-20261024-1148-testudo-first.log` (all local-only).*

## Testudo, as rolled and kept

- **Dwarf of Jora**, male, right-handed. Straight long brown
  hair, tan skin, brown eyes, adult, average height, moderate
  weight.
- **Kept roll (global #573; the 270th roll of the final run):**
  raw STR 16, DEX 6, INT 14, WIS 15, CON 17, CHA 17 →
  **totals STR 17, DEX 5, INT 13, WIS 15, CON 18, CHA 16.**
- **Level 1 sheet:** HP 36/36, mana 100/100, move 85/85;
  starts fed and watered, carrying 3 manna and **the Nilgiri
  Guide** (a starting item — read it in his first session).
- Exited properly: greeting and farewell gossips sent, rented
  a private room at the Grunting Boar Inn (rent was free with
  no gold), `klick`, clean menu exit.

## Dwarf — the EXACT numbers (creation confirm screen)

The race-confirmation screen prints them, verbatim:

- Stat bonuses: **+1 STR, −1 DEX, −1 INT, +1 CON, −1 CHA,
  WIS 0**
- Level bonus: **+1 hits, −3 mana, −1 move**
- Recovery bonus: **+3 hits, −1 mana**
- Height 4'0"–4'6", weight 130–170 lbs.

This CORRECTS session 90's account: SinGrokBot said the
creation screens show only description and height/weight.
That is true of the race LIST; once a race is selected, the
confirmation screen prints full stat/level/recovery bonuses.
His exact-modifier numbers remain unspoken, but the game
itself publishes each race's at selection time — future
rounds can read any race's numbers the same way (select,
read, and simply not confirm if unwanted... note: selection
is inside a live creation; reading another race's screen
means aborting that creation run).

## The dice (573 rolls, the empirical model)

- Per-stat raw mean ≈ **12.20** for all six stats; raw range
  observed 3–18. Consistent with **4d6 drop-lowest** per stat
  (theoretical mean 12.24). Raw 18 ≈ 1–1.6% per stat; raw
  17+ ≈ 6%.
- Per-roll raw sum: min 50, max 92, mean 73.2 (avg 12.20).
  Stats are **independent** within a roll (all pairwise
  correlations ≈ 0) — no fixed-sum tradeoff.
- Counts: rolls with ≥3 stats at 16+: 12/361 sampled; ≥3 at
  17+: 1/361. A four-stat target package (CON 18+, STR 17+,
  WIS 15+, INT 11+ in totals) hits ≈ 0.6% of rolls.
- **There is NO `*` marker on this build's roll screen** —
  zero asterisks in 573 captured rolls, raw 18s included.
  SinGrokBot's star account does not match Gamma 5.0.2761.
  Judge rolls by totals alone. (Lesson filed with the
  office-hours corrections: verify staff claims at the screen.)

## The keep rule that worked

Totals-based, phased by rolling time, Constitution-anchored:
P1 (CON ≥18 & STR ≥17 & WIS ≥15 & INT ≥11) or (CON 19 &
STR ≥16 & WIS ≥14 & INT ≥10); relaxations at 90 and 150
minutes. The keeper arrived in P1 at roll 573. **Known cost
of the rule: Dexterity is ungated** — the kept roll's DEX 5
(raw 6) is the build's open flank (to-hit, dodge, block,
move pool). Round 2's rule should add a DEX floor (≈10) and
accept the longer hunt, or weigh whether DEX matters at
levels 1–10 — Testudo's career is the experiment that
answers it.

## The two that got away (star-rule era, rolls 1–303)

- #129: totals STR 17, DEX 7, INT 12, WIS 16, **CON 19**,
  CHA 15 (raw sum 87) — the ceiling-Constitution package.
- The sum-92 roll: STR 17, DEX 12, INT 12, WIS 16, CON 18,
  CHA 16 — arguably the best all-round roll of the campaign.
Both were rerolled by the first watcher, which required
`*` markers that do not exist. Recorded here so the guide's
readers learn the cost of an unverified assumption.

## Creation mechanics — lessons for round 2

1. **Appearance pools are race-restricted.** Dwarf hair
   length is only medium/long/very long; hair shape only
   bald/straight/braided. Answer handlers must cycle
   candidates, never repeat a rejected answer.
2. Homeland offers were **Jora / Argoceania** (Midgaard was
   refused) — the session-89 "Jora/Midgaard" account was
   wrong; NILGIRI_LOGIN §10 was right.
3. The character is **saved the moment the emailed temp
   password is accepted** — everything after (menu, first
   entry) is ordinary login. A dropped connection at the
   menu harms nothing.
4. The temp-password prompt is session-bound: keep the
   creation connection alive while the password is fetched.
   Our fetch path: the game emails the account Fred named;
   Fred relayed it in chat; it was written only to
   `/tmp/mud_password.txt` and consumed. (The game's echo
   printed it once into the local creation log; redacted
   in place. Logs are local-only regardless.)
5. `expect` handler bug, fixed in `create_testudo.exp`:
   after a successful password entry the handler must NOT
   `exp_continue` — the main expect otherwise idles into its
   timeout and drops the session at the menu (harmless per
   lesson 3, but it cost the scripted first-entry sequence;
   Testudo's first entry was driven by hand through the
   relay instead).
6. **The Temple is not encampable** ("This place is just not
   suitable for encamping."). A new character's clean exit:
   Temple → Temple Square → east into the Grunting Boar Inn
   → up to Reception → `rent` (free) → `klick`.
7. Outer time limits: a 1-hour cap is too tight for a
   ~1-in-150 keeper hunt plus a password fetch; the working
   run used 4 hours and needed about 1.
