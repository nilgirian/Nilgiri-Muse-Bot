# Session 18b — SinMuseBot (2026-09-28, ~23:03–23:24 PDT)

Newtonia follow-up, part 1 of 2. Ended early (relay misdiagnosis —
see below), not by budget.

## Mission

Fred's orders: finish the 2-hour budget properly (18a retired after
~25 min on bad time math), investigate the strange auto-closing-door
building, find and map Newtonia Fishing Village (`open` gates/doors),
find the banker/rent/shops. Track REAL time, not game time.

## Findings

- **Strange building SOLVED — it's Newtonia's rent.** West of the
  gateway cobblestone road. Key: `open west`, NOT `open door` (the
  auto-closing door makes `open door` lie "already open"). Inside: "A
  plain lobby" with a newt receptionist — `rent` works ("A small room
  for rent"). Wall paper: `leave` returns to the realm, `klick` exits.
  Tested `rent` + `leave` (back in lobby, session continued). North
  door (`open north`) → **Newton's Lab** ("Do NOT Disturb!", Sir Issac,
  glowing — too strong, added to TOO_STRONG_MOBS.md). South door won't
  open by any command tried.
- **NOT a bank.** The moss-counter newt is not a banker (`balance` →
  "You cannot do that here"). Banker still unfound at this point.
- **Fishing Village NOT found.** Swept Salamander Way East/West, both
  newt homes off the homes road (dead ends), House of the Mistress
  (dead end). Best lead: the muddy pond west of the Muddy park — but
  the park is lethal (see Death).
- **New rooms mapped** (local `maps/newtonia.md`): A plain lobby,
  Newton's Lab, 2× small abode (newt homes).

## Death

Killed by **mosquitoes** in the Muddy park. They are NOT "weak" — they
swarmed and incapacitated a full-HP L3 in ~8 rounds, then killed. The
session-18a "aggressive but weak" note was dangerously wrong
(corrected in the map). XP 2543 → 2298 (−328 death loss, +~60 mosquito
kill XP net). **Corpse in the Muddy park** with: 2 oil lamps, manna ×2,
Nilgiri Guide. Park impassable alone — recovery needs a plan.

## Controller speech

Both of Sin's gossips from 18a were addressed: sent `gossip On the
way - will gossip the moment I find the Fishing Village.` Full-log
scan for `gossips,`/`yells,`: no other controller speech.

## Why it ended early

After the death, the driver concluded the relay's FIFO command path
was failing (commands "sometimes land, sometimes vanish") and stopped
driving at 23:24 rather than risk the character. **This was a
misdiagnosis** (see session 18c): the network stalled 3 times that
night, and commands vanish into a dead SSH pipe during stalls. The
relay was fine; the correct response is to wait for `>>> STALL` →
`>>> RECONNECTING` → `>>> IN GAME` and resume. Lesson recorded.

## End state

Character idle at the Temple of Midgaard (respawn), EMPTY inventory,
relay still running. Handoff to 18c for the bank hunt.

- Raw log (local-only):
  `~/workspace/nilgiri/logs/session-20260928-230300.log`
