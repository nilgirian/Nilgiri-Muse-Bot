# Day twenty-nine — Three reboots, a fifth rabbit failure, two cat-gate breaches, a clean exit (session 122)

*Testudo: XP 62,254 → 64,449 (+2,195), Level 9 throughout, bank 665 → 675 gc,
0 deaths. One login, booked 11:00 PST Fri 2026-11-27 – 17:00 PST
(360 min); CLEAN exit — klick 16:42, fresh >>> EXITED + >>> RUNTIME CLEANED,
fourth clean exit in a row. Pure grind — seventh leg of the Level 10 road
(L10 = 68,050; gap 5,796 XP at start, 3,601 XP at closeout; no crossing
possible). No teach (0 practices); no office hours; Q1/Q2/Q3 stay
queued for Grok's wrap-up. Pace ≈ 385 XP/h across the window — the
slowest of the Level 10 road sessions (s119 ~590, s120 ~970, s121 ~680),
three reboots and long night waits eating the pace.*

## The mission as booked, and what actually happened

- Fred's order (2026-11-26, shape A from the corrected sizing): pure
  grind on the high-value rotation, zone-per-hour enforced, three legs
  of ~115 min, exit begins AT 16:40 as a HARD SEQUENCE. Leg 1 grind
  (park Temple 12:55); leg 2 grind (park Temple 14:50); leg 3 grind +
  exit. No teach, no office hours, no Temp needed. Rathnor done, doe
  CLOSED. The corrected sizing held: this session does NOT cross —
  3,601 XP still stands between Testudo and Level 10, and the crossing
  is session 123's job.
- **Session 121 ended with a CLEAN exit** (klick 11:42 from the rent
  chamber), so leg 1 opened with the light verify drill: woke in The
  Reception at full HP 137, `score` XP 62,254 exactly as expected,
  inventory small bag / oil lamp / Nilgiri Guide — PLUS a tiny diamond
  ring carried at login (NOT in s121's final inventory list; a
  valuable with no bank value, see below) — full kit equipped,
  Berkeley Staff wielded, balance 665 gc (#0000-12CB), noflee 68
  unchanged, greeting gossiped once. The drill is verified from the
  log — state reconciled before any hunting. Hungry AND thirsty at
  login; drank at the fountain, ate three free Bakery half loaves.
- **Three VM reboots split the session into six legs.** 11:30 killed
  leg 1 (~30 min in, handback lost); 13:29 killed leg 2 (~31 min in,
  handback lost); 15:11 killed leg 3 (~17 min in, handback lost). All
  three relaunches were on the remaining budget to the original 17:00
  end, same log, reconnected with NO rollback (103 HP at the first
  reconnect, 137 at the second and third). Legs 1, 2, 3 handbacks all
  lost — every figure for those legs is re-derived from the raw log by
  the operator, not taken from any driver report. Leg 1b/2b/3b handbacks
  were received and log-verified (leg 1b: my leg-1b brief's plant count
  was wrong — leg 1 collected SEVEN plants + 1 gem, not 1 plant + 1
  shrub; leg 3b: the mole-flee telling was corrected from the log —
  three PANIC fails, not two, and no clean flee).
- **The exit was COMPLETED.** Leg 3b banked at 16:40 (+2 gc, 675
  total), rented, gossiped the farewell exactly ("Testudo banks his
  coins and turns in - the crossing comes next time."), dropped eight
  plants in the chamber, klicked at 16:42 — fresh >>> EXITED + >>>
  RUNTIME CLEANED, TIME UP never fired. The s119 lesson held: from
  16:40 the only legal actions were the exit route itself.

## Findings

- **The rabbit marker outranks inaction — and inaction won a fifth
  time (leg 1).** Ambushed in the Field at full HP 137 with the stand
  proof in place (fresh `score` at the hunt-block start, quenched,
  noflee 68, zero prior engagements, no hunger/thirst signal since
  the last eat/drink) — and the driver's first command after the
  marker was `look`, not `flee`; auto-combat ran ~10 rounds, 137 →
  93, before one `flee` carried him clear. The rabbit survived, no
  kill. Same shape as s113/s116/s120/s121: the stand conditions held
  on paper, but no stand call was ever made — the `look` was not a
  decision to stand, and the rounds after it were inaction. The
  engagement is SPENT for the session; Hills/Newtonia exiled after it
  and honored. The rule is unchanged and absolute; the failure mode
  persists across drivers. The operator's log-verification caught it
  each time — handback claims about rabbit contacts are never
  published on trust alone.
- **The wild-cat gate, breached twice in one session (legs 1, 2b).**
  Leg 1: the authorizing `score` (XP 62,415, HP 137/137) itself printed
  "Your stomach begins to growl" — a hunger signal IN the score — and
  the driver engaged anyway, killed the cat (+101 XP, 137 → 91). Leg
  2b: the score (XP 63,490, HP 137) was followed by a growl BEFORE the
  kill command; the driver engaged two rounds (cat incapacitated, +30
  XP), then recognized the void and fled at once. The incapacitated
  cat died off-screen; its corpse was found at dawn and looted empty
  — it counts as a kill ONLY by the corpse rule, with the caveat no
  R.I.P. was seen. RULE, NOW SHARPENED TWICE: ANY hunger/thirst signal
  between the authorizing `score` and the engagement VOIDS the gate —
  in the score OR after it — and the driver must RE-CHECK the log for
  hunger/thirst signals after the score and BEFORE the kill. Also:
  fleeing an incapacitated mob breaks "finish what you start" — a
  voided gate means do not START the fight, not abandon a downed one
  mid-fight. The gate-clean counter-example: leg 3 (score XP 63,558,
  HP 137, no signal before the kill; fought 137 → 105, incapacitated
  +81, finished with `kill cat` → R.I.P.).
- **`consider wild cat` FAILS; `consider cat` works (leg 3).** The
  game wants the short name for multi-word mobs — `consider wild cat`
  was tried and rejected before `consider cat` returned "lower level /
  easy battle". Use the short name in `consider` (and in `kill`
  finishers). One line for the wiki's Fighting section.
- **Speech needs blocking waits, not sleep batches (leg 2b).** Ares's
  cart-to-Catharsis question was answered ~2 minutes late because the
  driver was in a 110-second sleep batch; the 15s/30s/60s re-emits
  fired first. Owned. While speech may come, use blocking waits
  (short sleeps that still check the log) — a long sleep batch misses
  the ~10s reply target.
- **Ares's potion ask is NOT a bug report (leg 2b).** Ares asked
  Testudo for a potion of homecoming; Testudo answered "I do not have
  a potion of homecoming, Ares." — no report taken, no relay, no
  promise. Q3 stays queued for Grok's wrap-up. The bug-report rule
  (commit 4fa67722) is about reports TO the bot; a direct ask for an
  item is a question, answered as truly known.
- **Sin's new instruction: welcome new players when their arrival is
  announced (leg 3b).** Sin told Testudo directly (~15:44): "you
  should welcome new players to the game if it is announced". Sunless
  had just joined; Testudo answered at once with `gossip Welcome to
  Nilgiri, Sunless!` This is a standing addition to the template's
  "Talking to people" greeting rule and to MEMORY.md. Temp the
  Immortal was seen standing at the Inn Entrance at the exit — in game
  for the next session's Level 10 teach.
- **The plant-shed works (leg 2).** Renting with the tiny diamond ring
  carried did NOT refuse rent; seven plants were dropped in the rent
  chamber and the driver `leave`d cleanly, no klick. Rent refuses
  valuables in the sense of coin-type carried wealth, but the ring —
  no bank value — rides through. Fifteen plants went into the chamber
  this session (7 mid-session, 8 at the exit); the chamber now holds
  on the order of forty plants by the running count (s120 ~26, s121
  +5, s122 +15). The ring rode through klick in the pack.
- **Grapes: `eat bunch` FAILS, `eat grapes` works (leg 2).** "You need
  to possess a bunch of ripe red grapes in order to eat it" — while
  possessing one. `eat grapes` worked. One Vineyard bunch failed
  `eat grapes` / `eat bunch` / `eat red grapes` while carried (leg
  3b) and was dropped — the inedible-variant question stays open.
  Loaves stay the staple; grapes the backup.
- **The carry limit is item-count, not weight (leg 1b, restated).**
  The pack hit its ~12-item limit and blocked plant, gem, coin, and
  loaf pickups, and two corpse loots. Shed to the chamber early — the
  leg-2 plant-shed is the fix, used mid-session.
- **The inventory light line lies (leg 1b).** "..it is emitting light!"
  printed after the lamp was dowsed. Trust the `light`/`dowse`
  output, not the inventory line.
- **The mole fight: three PANIC fails, cures mid-fight saved the
  character (leg 3b).** HP 137 → 56 with THREE "PANIC! You could not
  escape!" flee fails (the handback's "two fails, third succeeded" is
  wrong — the log shows three fails and no clean flee); two `cast
  "cure light wounds"` mid-fight (56 → 81 → 91) saved him, then rest
  to full — the fight broke off with no kill. Noflee is a backstop,
  not a guarantee: when it fails three times running, curing mid-fight
  is the save, not a fourth flee attempt. Moles hit fast — `consider`
  first, bail early (s121), and know that a fight can end with no
  flee and no kill.
- **Never move into a dark exit (leg 3b).** ~16:06 the driver moved
  north from Outside the East Gate into the Vineyard on a "(too dark
  to tell)" exit. Landed safely, did not repeat it. Darkness is
  intermittent and unexplained (s120) — never enter a dark exit.
- **A dark-exit violation and a mole fight in one leg, both owned in
  the record.** The handback's account of the mole fight was
  corrected from the log before publishing; the dark exit was caught
  by the operator's log check, not the handback.
- **Pigeons are a bad target again (leg 1b).** Two fights, two flees,
  0 XP, wounds resetting mid-fight. Deprioritize; fidos are reliable.
  Fruit flies are the best Vineyard filler (21 kills this session,
  ~27 XP each).
- **The same-name finisher bit again (leg 2b).** With two same-name
  mobs, the finisher targets the HEALTHY twin — `look` before every
  finisher. Restated from s119/s121; still biting.
- **Three reboots, one session — again (sessions 121, 122).** 11:30,
  13:29, 15:11 PST. The recovery pattern held all three times
  (relaunch on the remaining budget to the original 17:00 end, same
  log, reconnect with NO rollback, full HP at two of the three
  reconnects). No duplicate-relay incident (single relay process
  verified after every relaunch).
- **The exit window IS the retirement trigger for the final leg
  (session 122, leg 3b — the s119/s120/s121 precedent, proven a fourth
  time):** the mission's exit window (16:40, hard sequence) retired
  the session at 16:42 with klick, TIME UP never fired, fresh >>>
  EXITED + >>> RUNTIME CLEANED. Fourth clean exit in a row.
- **Crossing math, corrected (for the final report):** 3,601 XP remain
  to Level 10 (68,050). At this session's pace (~385 XP/h overall;
  active legs ~400–570 XP/h), the crossing needs another long session
  — roughly 6–9 hours depending on pace — not a short login. The
  "short session to cross" shape chosen 2026-11-26 no longer holds at
  this pace. Do not promise a short crossing.

## Session stats

- **Level:** 9 throughout. No crossing (L10 = 68,050; gap at session
  start 5,796 XP; gap at closeout **3,601 XP**).
- **XP:** 62,254 → **64,449** (**+2,195** net). Legs: leg 1 +262; leg
  1b +287; leg 2 +238; leg 2b +517; leg 3 +81; leg 3b +810.
- **Confirmed kills (64: 63 R.I.P. + 1 corpse-proven):** 27 beastly
  fido, 21 fruit fly, 5 porcupine, 3 raccoon, 3 mole, 2 wild cat
  (R.I.P.), 1 field mouse, 1 ferret, 1 wild cat (corpse-proven, leg
  2b — no R.I.P. observed).
- **Deaths:** 0 (career 0 deaths stands).
- **Bank:** 665 → **675 gc** (+10 deposited, −0 spent).
- **Rabbit:** ONE engagement (leg 1), fifth protocol failure
  (`look` first, ~10 rounds, 137 → 93, one flee, rabbit survived).
- **Wild cats:** 4 engagements — leg 1 kill (BREACH, +101), leg 2b
  fight 1 gate-clean (stun +49), leg 2b fight 2 BREACH (incapacitated
  +30, corpse-proven kill), leg 3 kill (gate-CLEAN, +81).
- **Spells:** 2 × `cast "cure light wounds"`, both landed (leg 3b
  mole fight).
- **Shutdown:** CLEAN. Rent, farewell, plants dropped, klick 16:42,
  fresh >>> EXITED + >>> RUNTIME CLEANED. TIME UP never fired.
