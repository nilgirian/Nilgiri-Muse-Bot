# Leveling guide — notes 07: day three, the level-2 crossing (session 95, 2026-10-25)

Four hours, three VM reboots, one crossing. XP 650 → **1640 (+990)**,
**32 beastly fido kills**, 0 deaths. closeout.py: no XP drops flagged —
both mid-session link drops found him NOT fighting (the toll is
mid-fight only), and the third found him mid-teach. Raw log:
`session-20261025-1341-testudo-xp.log`.

## The crossing (measured)

The level-up line, verbatim:

> "You raise a level! You gain 18 practice sessions. You gain 11 hit
> points. You gain 0 mana points. You gain 3 movement points. You gain
> 6% skill in Protection From Evil."

- **18 practice sessions granted at L2** (L1 grants none — notes-04).
- Gains for this build (Dwarf, CON 18, no mana-family skills practiced
  at the moment of crossing): **+11 HP** (36 → 47), **+0 mana**,
  **+3 move** (85 → 88). The +0 mana is theory-consistent: mana gains
  scale off practiced mage/cleric-family skills, and he had none yet.
- **Protection From Evil +6%** — the natural trait's first free growth,
  exactly as SinGrokBot described in session 94 (random skill, no
  starting amount, grows per level-up, unpracticable). Displayed as
  [06/00] on the practice screen.
- Crossing kill paid +36 XP; first post-crossing score: 1,135 XP.
  Session ended at 1,640 — L2 hunting at L2 pays noticeably better per
  hour than the L1 grind (~250 XP/h across the day's chaos vs ~100).

## Practices — spent under Sin, and the plan was CORRECTED

Testudo apprenticed himself to Sin (in person, Russ' House) and the
brief's order — martialism → staves → catechism → cure — did NOT
survive contact with the master. Final state, all 18 sessions spent,
verbatim from Testudo's own report to Sin in the log:

> "All 18 spent — martialism 20, catechism 19, cure light wounds 9,
> kick 15, and staves rightly skipped. Thank you for the lessons, and
> for the correction."

- **Martialism 20** (cap 64), **Catechism 19** (cap 69), **Cure Light
  Wounds 9** (displayed [09/19]), **Kick 15** (displayed [15/20]),
  **Staves 0 — skipped on Sin's correction.**
- The weapon skill was judged the wrong early spend; **kick took its
  place**. The driver deferred the weapon-skill question itself to the
  next office hours ("save the weapon-skill question for SinGrokBot").
  Guide status: the theory-v1 practice order is REVISED at the weapon
  step — martialism first stands; the weapon skill no longer goes
  second by default.
- Learn mechanics under a master, as printed: `learn N <skill>` after
  each teach consumed points in chunks (the log prints "You used 4
  practice points" and "You used 5 practice points" on successive
  learns; 18 granted → 0 remaining). Per-skill point costs are not
  cleanly separable in the log; the endpoints and final percentages
  above are exact.
- **Cure's displayed ceiling [09/19]**: cure's cap printed 19 while its
  family (catechism) maximum is 69 and catechism itself stood at 19
  when cure was learned. HYPOTHESIS (unverified): a derived skill's
  learnable ceiling tracks its prerequisite's CURRENT value. Test at L3
  by raising catechism first, then re-checking cure's bracket.

## The staff question — still open, reframed

Staves was never practiced, so there is NO post-practice staff
comparison; the session-92 baseline (58 unwieldy vs ~20 connections)
still stands alone, and the mechanism question is still with Sin
(notes-06). What the day did show, windows labeled honestly:

- The staff, still at 0%, kept printing "unwieldy" lines whenever
  wielded (295 in the post-lesson window, which also includes the
  hunt to TIME UP — it never stopped being a 0% weapon).
- "Misplace your footing" nearly vanished after martialism 20 (5 in
  the same post-lesson window vs 186 across session 92) — consistent
  with footing belonging to the martialism/fundamentals system rather
  than raw DEX alone, but the windows and fight lengths differ; treat
  as a lead for office hours, not a result.
- Kick, once learned, became a real second attack in the rotation.

## Field notes

- **Fido loot is rare but real**: 32 kills paid exactly one gold coin
  (deposited mid-session: "Account #0000-12CB credited 1gc") and one
  copper bracelet (from a corpse; carried out at exit — and rent did
  NOT refuse it). Sessions 92–93 saw 0 gold in 18 kills.
- **The bank `balance` figure was never isolated in the log** — the
  session-94 half-loaf question (free vs debited) is STILL open; the
  deposit above is the day's only hard bank fact. Next session: run
  `balance` and capture the banker's exact reply line.
- Three VM reboots in one session (14:24, ~16:01, ~17:30 PDT) — the
  recovery drill (relaunch relay on remaining budget, fresh score,
  compare XP) worked three times; the final exit (farewell → rent →
  klick) was operator-driven by hand after the third.
- "Your master is Sin" — the practice screen names the master after
  apprenticing; guild practice remains the fallback route.
