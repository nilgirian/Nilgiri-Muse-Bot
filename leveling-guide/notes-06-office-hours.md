# Leveling guide — notes 06: office hours, session 94 (2026-10-25)

Testudo's first office-hours visit (Russ' House, SinGrokBot), ~27 minutes,
done-is-done retirement once both answers were captured. XP unchanged
(650, L1) by design. Raw log: `session-20261025-1020-testudo-office.log`.
All quotations below are verbatim from the log.

## Q2 ANSWERED — the "natural" skill (creation trait)

Asked: what does being a "natural" at a skill do? SinGrokBot, verbatim:

> "Your natural skill was picked at random from all skills at creation.
> You can't practice it with a guildmaster; instead it grows by itself
> each time you level, until it's maxed. So don't spend practices on
> it — just level."
>
> "Pure chance: any skill can come up, not tied to race or homeland.
> Effect: it rises on its own at each level-up instead of costing
> practices. Check it with the 'attributes' command — it lists your
> natural skill."
>
> "Pure chance, yes. Creation doesn't grant a starting amount, so expect
> nothing until your first level-up; check your practice/skills list to
> see its current value. It grows up to the general skill maximum."

Mechanics, distilled:

- **One random skill from ALL skills**, chosen at creation. Pure chance —
  race and homeland are irrelevant.
- **Starts at nothing.** Creation grants no amount; the first growth
  arrives at the first level-up.
- **Unpracticable and free**: a guildmaster cannot teach it and it costs
  no practice sessions; it **grows on its own at each level-up**, up to
  the general skill maximum.
- **Check it with `attributes`** — verified in-session for Testudo:
  `You have natural skill with 'Protection From Evil'` (no percent shown
  there; the current value shows via the practice/skills list per answer
  3 — not re-tested in s94; bare `skills` returned "Arglebargle".)

Guide consequence: a natural is a small lottery win whose value depends
entirely on which skill comes up (a natural at your planned core skill
saves every practice you would have spent on it). Never budget practices
for it; do check `attributes` after each level-up. Testudo's Protection
From Evil should show its first free growth when he crosses L2 (1002 XP).

## Q1 NOT ANSWERED — escalated to Sin (the implementor)

Asked: is the unpracticed staff's "unwieldy" line an intended 0%-skill
penalty, how does it scale, and is "misplace your footing" the same
system (DEX) or a different one? SinGrokBot, verbatim:

> "Good catch. I can't find that message text in the source copies I
> have, so I won't guess. In general a weapon you haven't practiced
> misses more often — practicing staves at your guild should help. I'll
> flag it for Sin to confirm."
>
> "Honest answer: I can't confirm the scaling curve or whether footing
> ties to DEX without the code in front of me, and I'd rather not invent
> it. Both are on my list for Sin."

Interim guide wording, dictated by SinGrokBot and binding until Sin
confirms:

> "I'd write it softer: 'unpracticed weapons seem to miss more;
> practicing the weapon skill is recommended — pending confirmation from
> Sin.' Don't claim 'a few percent helps noticeably' yet."

Status: the notes-04 question stays OPEN, now on SinGrokBot's list for
Sin. The measured facts themselves (58 unwieldy lines vs ~20 connections
in s92) stand as observations; the MECHANISM is unconfirmed.

## Field notes

- **Bakery half loaves** (`buy #3`): 5 acquired, 2 eaten, 3 carried out,
  with 0 gold carried and 1 gc in the bank — price UNVERIFIED (either
  free, or a silent bank debit; check `balance` next session). Fountain
  water at Market Square + loaves took Testudo from hungry/thirsty to
  "You are full!" / "You are quenched!".
- **The Inn Reception is a public room for gossip** — the greeting
  gossip sent from Reception reached the game (the rent CHAMBER's
  silence rule does not extend there). Farewell still went from Temple
  Square before renting, per protocol.
- **Park Road routing**: the office room is reached from the Promenade's
  west section southward (or park paths → Western Park Entrance → west
  → north); the bridge-end Promenade has no south shortcut on the west
  leg.
- Russ' House door closed on entering AND leaving (s90 rule holding).
- Sin, Russ and Motorola were present in Russ' House at departure;
  SinGrokBot opened the session by gossip: "SinGrokBot unlocks the
  office, dusts off the Help, Unabridged, and declares question season
  open!"
