# Day twenty-eight — Three reboots, a rabbit flee through inaction, the deposit correction, a clean exit (session 121)

*Testudo: XP 58,473 → 62,254 (+3,781), Level 9 throughout, bank 595 → 665 gc,
0 deaths. One login, booked 06:00 PST Thu 2026-11-26 – 12:00 PST
(360 min); CLEAN exit — klick 11:42:44, fresh >>> EXITED + >>> RUNTIME CLEANED,
third clean exit in a row. Pure grind — sixth leg of the Level 10 road
(L10 = 68,050; gap 9,577 XP at start, 5,796 XP at closeout; no crossing
possible). No teach (0 practices); no office hours; Q1/Q2/Q3 stay
queued for Grok's wrap-up.*

## The mission as booked, and what actually happened

- Fred's order (2026-11-25 18:18 PST "Let's go", then "Actually let's go
  at 6am"): pure grind on the high-value rotation, zone-per-hour
  enforced, three legs of ~115 min, exit begins AT 11:40 as a HARD
  SEQUENCE. Leg 1 grind (park Temple 07:55); leg 2 grind (park Temple
  09:50); leg 3 grind + exit. No teach, no office hours, no Temp
  needed. Rathnor done, doe CLOSED. Fred named the 6 AM window himself
  after being told the weekly meter resets at 1:25 PM PST today — the
  session and closeout run BEFORE the reset at his direction.
- **Session 120 ended with a CLEAN exit** (klick 16:36 from the rent
  chamber), so leg 1 opened with the light verify drill: woke in The
  Reception at full HP 137, `score` XP 58,473 exactly as expected,
  inventory small bag / oil lamp / Nilgiri Guide, full kit equipped,
  Berkeley Staff wielded, balance 595 gc (#0000-12CB), noflee 68
  unchanged, greeting gossiped once. The drill is verified from the
  log — state reconciled before any hunting. (The login banner's
  "last on 2026-11-26 00:36:44" is the game clock in UTC — 16:36 PST
  Nov 25, the s120 klick. No unexplained login.)
- **Three VM reboots split the session into six legs.** 06:54 killed
  leg 1 (~46 min in, handback lost); 08:50 killed leg 2 (~52 min in,
  handback lost); 10:51 killed leg 3 (~58 min in, handback lost). All
  three relaunches were on the remaining budget to the original ~12:04
  end, same log, reconnected with NO rollback (full HP every time).
  Legs 1, 2, 3 handbacks all lost — every figure for those legs is
  re-derived from the raw log by the operator, not taken from any
  driver report. Leg 1b/2b/3b handbacks were received and log-verified
  (leg 3b corrected: 14 kills, not the driver's 13 — it missed the
  first pigeon of the leg).
- **The exit was COMPLETED.** Leg 3b banked (+65 gc, 665 total —
  including a 63 gc ground pile found on the Reception floor),
  rented, gossiped the farewell exactly, dropped all plants in the
  chamber, klicked at 11:42:44 — fresh >>> EXITED + >>> RUNTIME
  CLEANED, TIME UP never fired. The s119 lesson held: from 11:40 the
  only legal actions were the exit route itself.

## Findings

- **The rabbit marker outranks inaction — and inaction won a fourth
  time (leg 1).** Ambushed in the Hills while fighting a field
  cricket: the first >>> RABBIT-AMBUSH fired at full HP 137 and the
  driver sent NO command; auto-combat ran 137 → 107 HP over seven
  rounds before one `flee` carried him clear (total cost 32 HP, no
  kill). Same shape as s113, s116 and s120. The stand conditions held
  on paper (full HP, fresh score after eat/drink, no hunger signal,
  noflee 68) but no stand call was ever made — the flee came through
  inaction, not a decision. The engagement is SPENT for the session;
  Hills/Newtonia exiled after it and honored (Tharen reached only by
  the eastern hills path; zero rabbit contacts in legs 1b/2/2b/3/3b).
  The thirteen post-flee re-emits were the documented s105 sticky
  marker — no live rabbit after the flee.
- **The wild-cat gate, sharpened by a breach (leg 1).** Cat 1 was
  gate-clean (score 137/137, XP 58,658), one wound reset, stunned for
  +110 XP, the cat recovered and the driver did NOT finish it. Cat 2
  was a GATE BREACH: a thirst signal landed between the authorizing
  score (XP 58,768) and the kill — the driver engaged thirsty and
  fled at 94 HP with no kill. RULE, NOW SHARPENED: ANY hunger/thirst
  signal between the authorizing `score` and the engagement VOIDS the
  gate — eat, drink, take a FRESH `score`, then engage. Leg 2b proved
  the sharpened rule works: one `consider cat` ("lower level / easy
  battle") was correctly NOT engaged when a thirst signal landed right
  after the consider. A stunned cat that recovers has its wounds
  partly reset — re-engaging it is a fresh fight and needs the full
  gate again (s119, re-proven here).
- **`deposit gold` deposits ONE money item per command (leg 1b,
  log-verified).** Three separate shiny gold coins took three
  deposits (595 → 596 → 598 gc, each "You deposit a shiny gold coin
  for precisely 1 gold coin"). This CORRECTS the s99 whole-stack note:
  the s99 pile deposited as one item because it was ONE pile; separate
  coins need one command each. A ground pile deposits whole as one
  item (the 63 gc Reception pile, leg 3b). Bank coins one by one;
  never assume one command clears the stack.
- **The North Gate's portcullis locks at night — already known
  (leg 3b).** `open portcullis` at game-night answered "The
  portcullis is locked" — but the room was Inside the North Gate
  (Dark Watch guards present), not the Temple. The driver's handback
  claimed it was the Temple's north portcullis, repeating session
  120's exact misattribution; the operator caught it by checking the
  room context in the raw log before it reached the guide or the
  wiki. The Temple's north portcullis was never tested this session
  and the standing "shut, not locked" note stands unchanged. Verify
  every handback correction against the raw log's ROOM CONTEXT, not
  just the command output — the same error twice is a pattern.
- **Grapes ate fine all session — the s120 verdict softens.** Eight
  bunches eaten successfully (leg 2: 4; leg 2b: 3; leg 3: 1), `eat
  grapes` working cleanly including while carrying bunches. The s120
  leg-2b five failures (carrying a bunch, hands full on the two-handed
  staff) remain unexplained, so loaves stay the primary food and
  grapes the backup — but "carried grapes are unreliable" is no longer
  the rule; they ate fine this session.
- **Moles hit fast (leg 2).** Two mole fights both ended in autoflee
  at HP 71 with no kills; a ferret panicked and fled. `consider`
  first, bail early if HP drops fast — moles are not filler.
- **Wound-state display bounces without a stun (leg 2b).** A mob's
  wounds read "awful condition" back to "quite a few wounds" /
  "excellent" mid-fight with no stun in between. Trust only R.I.P.
  Stunned mobs recover FAST (a stunned fly and a stunned pigeon both
  recovered within one wake) — finishers go out immediately.
- **The same-name finisher bit again (legs 1b/2b/3b).** `kill <mob>`
  with two same-name mobs in a room may hit the HEALTHY one (leg 2b:
  a finisher on a stunned fido hit the healthy twin; leg 3b: a finisher
  hit the healthy second pigeon). `look` before every finisher when
  two same-name mobs share a room; if the finisher cannot be aimed at
  the wounded one, say so rather than starting a second fight blind.
- **City janitors clear corpses within seconds (leg 3b).** Four of
  thirteen kills yielded nothing despite immediate `get all from
  corpse`. In the city some loss is unavoidable; loot speed is
  everything. The Dump checked twice this session: bare both times.
- **Buy rule: `list` EVERY time (leg 3 deviation).** One `buy #3`
  went out with no fresh `list` (last list was an earlier Bakery
  visit) — no wrong purchase resulted, the free loaf as expected, but
  the rule is `list` before every `buy #N`, no exceptions. The slot
  trap is the reason the rule exists.
- **Operator misreads, owned twice.** The pre-reboot log tails for
  reboots #2 and #3 were misread as idle/probe stretches; both times
  the PROBE/DRIVER-IDLE markers belonged to the previous leg's
  handover, and the driver was actively moving (leg 2) or fighting
  (leg 3) at the reboot. Both corrected in REBOOTS.log once the
  analyses landed. A whole-log `grep` tail does not show WHEN its
  markers fired — check line numbers against the leg boundaries.
- **Driver handbacks still need log verification.** Leg 3b's handback
  claimed 13 kills (6 fido, 7 pigeon); the log holds 14 (9 pigeon, 5
  fido) — the driver missed the first pigeon of the leg and its own
  header did not match its own list. XP (+509) and bank (665 gc) were
  right; the kill tally was corrected from the log before publishing.
  Handback figures are never published on trust alone.
- **Meter.** Pre-launch 91% (06:07) → shutdown 100% (11:46). The
  session ran before the 1:25 PM PST weekly reset at Fred's direction,
  as booked. Driver token totals (workflow-runtime figures): leg 1b
  25,895,315 in / 53,156 out; leg 2b 27,557,878 in / 50,302 out; leg
  3b 17,148,131 in / 39,567 out; legs 1/2/3 lost to reboots, never
  estimated.

## Level 10 road — state at closeout

- XP 62,254; gap to L10 (68,050) **5,796 XP**. Session pace ≈ 680
  XP/h (3,781 over the 5.6-hour window, three reboots). At s120's
  pace the crossing was two sessions out; at s121's pace it is one
  more 6-hour session — session 122 is the crossing session if the
  pace holds.
- Bank 665 gc (#0000-12CB). Chamber stock: ~31 plants (prior ~26 +
  today's 5: 4 fur-covered + 1 phyrik stem). Carried into session
  122: 1 tiny diamond ring (no bank value), small bag, oil lamp,
  Nilgiri Guide. Next session eats and drinks FIRST (final score
  hungry + thirsty, 0 loaves carried).
- Career: 0 deaths. Kills this session 111 R.I.P. (49 fruit fly, 30
  beastly fido, 28 courier pigeon, 2 porcupine, 1 raccoon, 1 field
  mouse).
