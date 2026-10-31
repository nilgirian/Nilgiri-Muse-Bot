# Leveling guide — notes 14 (day ten, 2026-10-31)

Session 103: the creation of **Temp**, the project's second test character
and its designated future immortal practice bot — a character who will one
day stand as master for other characters' practice sessions. Rolled by
Fred's order in a 2-hour envelope; creation machinery reused from session
91 (`create_temp.exp` + a roll watcher), with the keep rule rewritten for
the job.

## 1. The build brief, and the keep rule it produced

A teacher's ceiling is set by his own sheet: a student cannot learn past
the master's own skill (session 88), and skill caps are computed live
from stats by family — catechism/cure draw mostly on WIS with a smaller
INT share (notes-02), martial skills lean on the warrior stats. So Temp's
rule protected four stats, not three:

- Phase 1 (strict): CON>=18 & STR>=17 & WIS>=15 & INT>=13, or
  CON==19 & STR>=16 & WIS>=15 & INT>=12.
- Phase 2: CON>=18 & STR>=16 & WIS>=15 & INT>=12.
- Phase 3 (safety net): CON>=18 & STR>=16 & WIS>=14 & INT>=11, or
  CON>=17 & STR>=16 & WIS>=14 & INT>=11.

Run 2 ran the phases compressed (25 / 50 / 70 minutes) after run 1 was
lost (section 3).

## 2. Kept roll (run 2, roll #647, kept under Phase 3)

Totals after Dwarf bonuses (+1 STR, -1 DEX, -1 INT, +1 CON, -1 CHA,
WIS 0): **STR 17, DEX 14, INT 11, WIS 14, CON 18, CHA 11**.
Raw dice: 16 / 15 / 12 / 14 / 17 / 12 (raw sum 86).
L1 sheet: HP 36, mana 100, move 94. Homeland Jora, male, right-handed.
Kit: black leather vest/shorts/boots, wooden shield, wielded staff,
3 manna, the Nilgiri Guide. Natural trait: **Charge** (a second random
trait on a second character — consistent with the session-94 verdict
that the trait is a random skill, granted at creation, unpracticable).

## 3. Dice data — 1,223 rolls, and what the phases cost

- Run 1: 576 rolls, killed unsaved by a VM reboot at the reroll prompt
  (14:43 PDT, on the known ~2h cadence). Best roll #123:
  STR 18, INT 17, WIS 14, CON 19 — one WIS under Phase 1's variant bar.
  Class rates from run 1's first 238 rolls: Phase-1 class 0,
  Phase-2 class 1, Phase-3 class 3.
- Run 2: 647 rolls. Class counts over the whole run: Phase-1 class 0,
  Phase-2 class 0, Phase-3 class 6 (rolls #37, #57, #106, #131, #234,
  #647) — but only #647 fell inside Phase 3's own window and was kept;
  the earlier five were correctly rerolled under the stricter phases
  then in force. Notable ghosts: #106 (CON 19, WIS 16, INT 11,
  STR 16 — would have kept in the final window), #326 (CON 19,
  WIS 17, STR 15 — one STR under every phase).
- Frequencies (run 2): CON>=18 in 30/647 (4.6%); CON 19 in 11/647
  (1.7%); Phase-3 class 6/647 (0.93%); Phase-2 class ~0.4% (run 1
  sample). A strict four-stat bar is a sub-half-percent event:
  **phased relaxation is not impatience, it is the method** — the same
  ladder that produced Testudo at roll #573 (notes-03).

## 4. Starting movement tracks the roll (hypothesis, n=2)

Testudo: DEX 5 → starting move 85. Temp: DEX 14 → starting move 94.
Both dwarves, both CON 18 → identical starting HP 36; both mana 100.
The +9 move for +9 DEX suggests starting move is computed off the roll
with DEX at or near 1:1, while starting HP keys on CON. Two characters
is a hypothesis, not a law — flagged for the next creation to test.

## 5. Creation ops, hardened

- An unsaved creation is erased outright by a disconnect/reboot: no
  partial character, no salvage. The temp password is only emailed
  after the reroll loop ends (handedness follows the keep), and it
  saves the character only if entered in the still-connected session
  (NILGIRI_LOGIN.md section 11).
- Roll logs and watcher state now live in the workspace (`run/`), not
  /tmp — the reboot took run 1's TSV with it; its numbers above were
  recovered from samples taken during the run.
- Temp's exit ran the full first-entry path cleanly: Temple greeting
  gossip, walk to the Grunting Boar, `rent` into the private chamber,
  `klick`, menu exit — all verified in the session log.
