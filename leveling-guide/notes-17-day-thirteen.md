# Day thirteen — Level 7, the herb chain, and the crow's last word (session 106)

*Testudo: XP 12,866 → 14,049, Level 6 → **7**, bank 346 → 350 gc, 0 deaths.
One login, three legs; the day the practice project turned herbalist.*

## Level 7

- Crossed at 13,798 XP (threshold 13,777) on a 71-XP courier pigeon in the
  Dark Alley. Gains: **+18 practices, +15 HP (95 → 110), +0 mana,
  +3 movement (98 → 101), Protection From Evil +3% (37% → 40%)**.
  HP gains by level now run +11/+11/+14/+12/+11/+15 — the +15 is the
  largest step yet; no clean pattern claimed. noflee reset to 55
  (half of 110). The level table in notes-15 gains its L7 row.

## The herb (Animism) tree — office hours with SinGrokBot, verbatim core

- **PREPARE turns shrubs into herbs.** Chain: **animism > herb_lore >
  forage > prepare**, and **APPLY hangs off forage too**
  (animism > herb_lore > forage > apply). APPLY uses prepared herbs on
  yourself or creatures.
- **Ceilings:** every skill in the chain is capped by its parent's
  CURRENT learned level (herb_lore by animism, forage by herb_lore,
  prepare and apply by forage). Animism itself is capped by stats —
  the practice screen prints the formula for this build:
  40% wisdom [15 => 71] = 28, 40% intelligence [13 => 61] = 24,
  20% dexterity [5 => 23] = 4 → **58 maximum Animism**.
- **FORAGE is a spell**, not a gathering verb: it lists herbal plants
  nearby, radius growing with level/skill. **Shrubs are items placed in
  rooms** — hold one and cast PREPARE on it. **Which zones hold shrubs
  is unknown** (Grok: needs the live world DB; flagged to Ops).
- Teach rule confirmed again: any craft master works, no family check;
  one skill per teach command; **the STUDENT can also end an
  apprenticeship with `apprentice none`** (new — previously only the
  master's side was documented).

## The spend — all 18 under Temp

- Master: **Temp**, driven by Fred's teachbot script (follow →
  auto-apprentice → "teach me X" → teach). Sin directed live in the
  room. **Status caveat, confirmed by Fred afterward: Temp had been
  promoted to immortal before this test**, so the verified result is
  *a script-driven immortal master teaches cleanly, batched learns and
  all*. **Whether a MORTAL can teach remains untested.**
- Final after 18 points: **Animism 40/58, Herb Lore 9/40, Forage 9/9,
  Prepare 0/09, Apply 0/09.** Bottleneck order for the next grant:
  raise animism and herb lore first; forage follows; prepare/apply
  already wait at a 9 ceiling.
- **Learn gains are ROLLED per point, not flat +1** — animism's first
  point bought +1, later batches averaged ~+4 per point.
- The chain enforced itself live: Sin's guess "skip forage, learn
  prepare" produced `but fail to learn anything new / You used no
  practice points` — prepare's ceiling was forage 0. Grok's map beat
  the guess; Sin corrected on the spot.
- **Charge, closed:** two `learn 1 charge` attempts (under Temp, then
  under Sin) failed identically at no cost. Grok's verdict: **Charge's
  cap is the student's CURRENT mounted_combat (Testudo's: 0), and it
  needs battlecry too.** Natural traits are NOT unteachable — the
  student was capped at 0. Retire the old open question.

## Forage in the field (first casting data)

- 32 casts of `cast "forage"` across 7 rooms (grassy knoll, the Field,
  the wall-hole hill room, two light-forest rooms, Garden Path, Garden
  Center): **1 success**, cast #5 at the grassy knoll. Verbatim:
  *"You call upon the four winds to aid you in your search for plants
  nearby. / There are no indications of any useful plants in your
  surroundings."* All other casts: no effect. 1/32 at skill 9 is
  within variance of the d100 ≤ skill% rule.
- **Cost: 23 mana per cast** (success or failure) — four casts per full
  bar; rest-regen ~19/tick. Spell economics for any future shrub hunt.
- **No shrub item was seen in any room**, including the Temple garden
  ("Plants of many types grow in the garden") — garden plants are
  scenery, not items. The Prepare test remains blocked on the
  shrub-zones answer (Ops).
- **Bare Prepare at 0 learned garbles** — *"BylleGrylle Grop Gryf???"* —
  a failed cast by the garble rule, **no mana deducted** (unlike
  forage's failures, which cost full price).

## Small mechanics

- **`where <name>` is effectively zone-scoped**: from Russ' House it
  returned only the zone header; from inside Midgaard it lists the
  zone's players WITH rooms ("[ IMM ] Temp - The Grunting Boar").
  Use it from inside the target's zone. (Fred's mechanics, confirmed
  both ways the same day.)
- **`drink barrel`** is the syntax; `drink from barrel` fails
  ("You cannot seem to find a 'from'").
- **Bakery**: north off the EASTERN Main Street room (that room: N
  Bakery, E Market Square, W Main Street, S Armory). **Bank**: north
  off the MIDDLE Main Street room. Temple garden route: Temple →
  open portcullis → N (North End) → down (Garden Path).

## The crow — registry update

- **Considered at Level 7** (light-forest trail at the Faint Path
  junction; followed it one room south for the reading): *"He is a
  lower level than you. You would probably die..."* At L5 it was
  "same level as you"; the relative level moved, **the verdict did
  not**. The crow stays do-not-engage; the L5-era "re-consider at L6/L7"
  obligation is now discharged — re-consider again only if the build
  changes materially.

## Kills and XP

- Day: +1,183 (leg 1 +932, leg 2 +0, final leg +251). Final leg detail:
  ground hog ×2 R.I.P. (one crit-pound totaling 55 across installments;
  one incapacitated, finished with `kill`), a third ground hog fled at
  mortal wounds paying **+26 on departure** (ledger model, again),
  black bird R.I.P. (+28 stunned, +8 mortally wounded installments,
  finished with `kill`), courier pigeon R.I.P. at Temple Square (+43,
  +7), beastly fido R.I.P. (+34). All corpses empty.
- Zero ferocious-rabbit markers all day; the ~12:22 VM reboot never
  came at all — first full session day without one.

## Open after day thirteen

- Shrub zones (with Ops). Prepare/Apply first real use (needs shrubs +
  practices; ceiling 9 waits). Mortal-teacher test (needs a mortal
  master). Level 8's threshold (unknown). The doe name anomaly (s100)
  and bare `teach <skill>` — still open, still small.
