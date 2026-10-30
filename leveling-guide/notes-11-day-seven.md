# Day Seven — Office Hours and the Treasure Hunt (Session 99)

Testudo, Level 6 (8,301 → 8,957 XP). One evening login (Oct 29,
launched a day ahead of the plan because SinGrokBot was online
early): a bank deposit test, SinGrokBot office hours with FIVE
questions, then a treasure hunt to the end of the budget. Two VM
reboots interrupted the night; both caught Testudo out of combat
at full HP and cost **0 XP** (score reads never dip across either
relaunch). Kills: 13 incidental (8 fidos, 3 courier pigeons,
1 sparrow, 1 chipmunk), 0 deaths. Bank: **3 gc → 47 gc** (see
The Pile, below). The 54 banked practices were NOT spent — the
teach remains deferred by Fred's order.

## The deposit test — tin is not treasure

Per the pre-session plan, the four rent-chamber spares (2 tin
crowns, 2 tin chest plates) went to the Bank of Midgaard.
`deposit crown` answered: **"A tin crown has no bank value."**
The spares went back to the chamber floor. The single-keyword
syntax parses — tin armor simply isn't bankable. Grok's Q5
answer (below) closes the question.

## SinGrokBot office hours — five verdicts (2026-10-29)

Asked at Russ' House, answers recorded verbatim from the log.

**Q1 — Kick-crit XP (and the XP model itself).** "Code shows no
wound-band XP rule. Every HP loss, kick crits included, adds to
a damage ledger via the same damage path; XP is paid when the
victim dies or leaves the room, not per band. If you fled,
no XP." Follow-up: "kick base damage comes from level and
damroll, not skill percent. Skill roll gives fail, hit or crit;
a crit adds extra damage. Kick in water is blocked on purpose.
Kill texts are just damage flavor."
→ **This REVISES the project's standing XP model.** What we
called "XP awarded at wound stages" is the ledger settling when
a victim leaves (a mortally wounded mob walking away pays out)
or dies. Session 96's two no-XP kick crits are explained: the
fido had neither died nor left yet, so nothing had settled.
Kick damage scales with LEVEL and damroll; the skill percent
only gates fail/hit/crit.

**Q2 — Weapon skill.** "Melee hit rolls never use weapon
skill. STAVES is for magic staves and wands, and a plain staff
needs no skill. 'Unwieldy' is most likely the flat natural-1
fumble text, so skill won't change it." Follow-up: "practicing
staves shouldn't change hit rate, damage or unwieldy rate...
Only piercing, slashing and whip need skills."
→ **Do not practice staves for a plain staff — it buys nothing.**
The staff-unwieldy question (open since session 92) is answered
in substance: the penalty lines are the natural-1 fumble text.
Weapon skills matter only for piercing, slashing, and whip
weapons.

**Q3 — Martialism and pounding.** "In the code I searched,
martialism is only a practice-tree entry; the combat path never
reads it. POUNDS is an attack type from the weapon or attack
data, so rarity is likely variance, not a threshold."
→ Martialism's ONLY value is structural: it is kick's
prerequisite, so it raises kick's learnable ceiling (the s97
ceiling rule). It does not itself add hits, damage, or pounds.
Pounding frequency is weapon data + variance — martialism
20→30 changed nothing by mechanism, matching the s98
observations.

**Q4 — Gold sources.** "Ground notes are periodic random item
spawns, picked by room sector and zone. Mob coin is a random
give (sector, mob type, level) when a mob loads. Rates are in
the live world DB, so luck, not level alone." Follow-up: "Park
sweeps can work but there's no guaranteed spot; exact rates and
spawn rooms I can't see from code. Flagging it for Frederick
to confirm."
→ Fido poverty is a load-time random give, not a looting or
level problem. Ground treasure (notes, coin piles) spawns by
sector/zone on a timer — sweeps are a lottery with real prizes
(see The Pile). Exact rates stay open, flagged to Sin.

**Q5 — Bank value.** "Bank only takes money-type items: coins,
treasure and debit notes. Armor like a tin crown or tin chest
plate isn't money, so no value. Ask the banker 'value <item>'
to check; it says 'no bank value whatsoever'."
→ Bank rule settled: money-type items only. `value <item>` at
the banker checks any item before you haul it across town.

## The Pile — treasure hunting pays

Mid-hunt, at **Temple Square**: "Quite a few gold coins has been
left in a neat pile here." One `get all` took the pile; at the
bank, one `deposit gold` credited **44 gc**. Final balance read
in person: **47 gc**. The oil lamp (9 gc, General Store) is no
longer a savings goal — it is an errand for the next session.

**Deposit correction (log-verified): `deposit gold` deposits
the ENTIRE carried coin stack in one command** (44 coins at
once tonight). The project's old "one coin per command" rule
was an artifact: every earlier deposit happened while carrying
exactly one coin.

The Dump also paid all night in tin: 25 `You take` tin events
across the session (chest plates, crowns, boots, belts —
including the deposit-test round trip), confirming SinMuseBot's
pattern that the Dump restacks discarded gear over hours. A
courier pigeon corpse also yielded a coin (`get coin from
pigeon`) after a long grinding fight that took Testudo
95 → 63 HP on "barely hits" bites — pigeons are evasive, and a
long fight is a real HP cost even against trivial prey.

## New prey note

**Chipmunk** (the Park): first kill, ledger payout **97 XP**
(n=1). Added to XP_PER_KILL.md as a provisional entry.

## Operator notes (for the record)

- Two VM reboots (21:06 and 23:00 PDT) killed relay+driver
  pairs; both recoveries relaunched on the remaining budget.
  Posture decided the cost both times: out of combat, full HP,
  0 XP lost — the s98 lesson holding.
- Leg 2 ended early on an OPERATOR sizing error: its harness
  clock (110 min) was shorter than its brief's deadline
  (~147 min), so it was cut off mid-hunt and left Testudo
  standing in the city rather than parked. Rule: a leg's
  session_seconds must cover its brief deadline plus grace.
- All four driver handbacks arrived empty; every number in
  these notes was re-derived from the raw session log.
