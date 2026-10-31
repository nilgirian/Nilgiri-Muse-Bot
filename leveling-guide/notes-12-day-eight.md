# Leveling guide — notes 12, day eight (session 100, 2026-10-31)

**Theme: the training completed, and an 8-hour treasure hunt.** Testudo: L6, XP 8,957 → 10,459, bank 47 → 98 gc, 0 deaths. All 54 banked practices spent in the first quarter hour; the remaining ~11 hours were Fred's treasure-hunt design — breadth over rooms, because ground treasure is a random spawn (notes-11, Q4).

## 1. `learn N <skill>` — batch learning under one teach offer (NEW, headline)

Sessions 88/97 established: one teach offer = one learn, offers lapse in ~75s. Session 100 found the count form:

- `learn N <skill>` consumes **N practices under a single offer**, stopping early when a ceiling binds. Observed stop messages: "You have learned as much as you can of 'X' from Sin" (master/ceiling) and the cure case below.
- The full spend (54 → 0), at Russ' House under Sin, ~13 minutes:
  martialism +5 → kick +5 → martialism +6 (64/64 cap) → kick +6 (64) → catechism +5 of 6 asked (69/69 cap — the batch stopped 1 short) → cure +10 → cure +2 more with the batch ending on the ceiling ("learned as much as you can" — cure's ceiling = catechism's current value, the s97 rule, binding live mid-batch) → block +8 → block +8 (Sin's direction: "use your practices up as much as you can"; SinGrokBot, arriving mid-teach, on the block question: "a clear answer. Block it is").
- **Final: Martialism 64/64, Kick 64, Catechism 69/69, Cure Light Wounds 69, Block 64, Protection From Evil 37 (natural). Practices 0.**
- Practical consequence for the guide: a whole level's practices can now be spent in minutes under one teacher visit — the offer-lapse scramble of s83/s88 is obsolete when the teacher offers and the student counts. Still learn FIRST and talk after (offers lapse); the batch form just makes "first" fast.
- Side data point, from Testudo's mid-spend report: "Block is at 36 — past the 16 Grok named for bash." I.e., **bash appears gated at Block 16** (Grok, earlier) — recorded here as reported-in-session; bash itself remains unpracticed/untested.

## 2. Treasure-hunt field results (two nights: s99 + s100)

Ground spawns observed (room, item): Temple Square — 44 coins (s99); Entrance to the Grunting Boar Inn — **59 coins** (s100); blown silver note (city) — 1 gc at the bank; loose coin credits +1/+1/+1/+3 across s100 (streets and corpses). Mob-carried coin: wild cat corpse held **3 coins**; fido and young gnoblin corpses 1 shiny coin each. Per notes-11 Q4 this is load-time luck, not level — the hunt's yield is variance-dominated: s99's single pile was 44; s100's was 59, plus a long tail of singles. **Breadth is the only lever**: two full nights of sweeping produced their money in a handful of rooms.

Other containers: a **wooden chest** in a forest log cabin — locked, no key found, `unlock` fails without a key, bank refuses it ("no bank value"); carried home unopened. Slug's corpse (Inn, guardian kill after a steal from the receptionist) yielded **a small aluminum container** — cannot be opened, "nothing special" on examine. Both ride in inventory as unresolved items.

## 3. The bank tax fired

Balance read 103 gc mid-session and **98 gc** after a **5 gc tax** debit (driver-reported in-game at the time; the session ledger reconciles exactly: 47 + 59 pile − 9 lamp + 1 note + 1 + 1 + 3 loose coins − 5 tax = 98). The standing "5% ANNUAL tax" note (runbook) is now a *paid* fact, not a rumor: ~5% of ~103 ≈ 5. First observed firing across 100 sessions.

## 4. Combat notes

- **Young gnoblin (Tharen Forest):** opening kick at 64% — "Your well placed kick to the young gnoblin's groin utterly annihilates him!" — stunned, finished with repeated `kill` through mortally-wounded to R.I.P. (the s96 finisher rule working exactly as written). The adult gnoblin nearby considered "lower level... very tough battle" and was left alone — consider discipline held. Payout not isolated (multi-fight window).
- **Wild cats (Tharen):** 3 kills across the night; one corpse carried 3 coins. Payouts not isolated.
- **Chipmunk ×2 more kills** (career s99+s100 = 3); still no isolated score bracket — the 97 XP (n=1, s99) entry in XP_PER_KILL stands unchanged.
- **The doe, again:** engaged at full HP in the Hills/Plains; two rabbit ambushes landed *inside* the fight (fled first-command both times; sector law kept). At 44 HP the target dissolved — "You do not find a creature by the name of 'doe' here" while a big horned doe stood in the room. No kill claimed. Open mechanics question (name resolution vs. a second doe vs. fight-state) — flagged, not theorized.
- **Rabbit:** 3 ambush clusters this session (2 in the doe fight, 1 at rest), all fled first-command; HP floor 44 (doe + rabbit combined). Protocol continues to be the difference between a scare and a death.

## 5. Session integrity notes

- **Six VM reboots** (00:39, 02:38, 04:40, 06:42, 08:45, 10:43 PDT — a near-metronomic ~2h cadence); each caught Testudo out of combat at full HP; **0 XP lost** across all six — the asleep/full-HP/out-of-combat posture rule now has six more confirmations.
- **Leg-7 driver error:** one driver walked the full exit menu at ~06:00 with no TIME UP fired — session relaunched on the original clock and completed. Cause reads as template-retirement drift (the standing brief's exit section) overruling the leg brief's park rule. Countermeasure now standard in every leg brief: an explicit "NEVER klick" paragraph.
- Final exit ran ~24 min early (exit sequence started 11:30 by design; the klick compressed instead of waiting out the marker in the rent room). Noted; the farewell gossip was sent correctly from the road home and the exit verified clean.
- All driver handback reports arrived empty (every leg) — all published numbers were re-derived from the raw log. The handback failure is now the norm, not the exception; plan closeouts accordingly.
- **Crow re-consider at L6: still open** — assigned in three consecutive legs, never executed (the bird was never in the room when a driver passed). It survives as an open registry item by honest report, not by another night of orders.

## 6. Where Testudo stands

L6, XP 10,459 (L7 at 13,777 — 3,318 to go), HP 95 / mana 100 / move 98, bank **98 gc**, skills complete for his level (see §1), lamp owned and lit, 0 career deaths. The 1→10 guide's open threads: L7 crossing numbers when they come; the crow's L6 reading; bash's Block-16 gate (testable now that Block is 64 — one practice-free experiment: bash needs no practice to attempt if the gate is real); the locked chest and the aluminum container (keys? open mechanics?); mob-coin and ground-spawn exact rates (already flagged to Sin/Frederick — theirs to publish).
