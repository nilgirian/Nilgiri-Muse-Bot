# Day seventeen — Level 8, met at last; the teaching waits (session 110)

*Testudo: XP 22,056 → 23,846, Level 7 → **Level 8**, bank 375 → 376 gc,
0 deaths. One login, booked 08:00–12:00 PST, out clean at 10:55. The
crossing came early (~09:12) on leg 1; the teach never ran; the grind
leg after the reboot never ran either, and the operator walked him
home by hand.*

## The mission as booked, and what actually happened

- Fred's order (2026-11-04): one login, Thursday ~08:00–12:00 PST
  (240 min) — another experience run cycle. Expected shape: crossing
  ~10:30, teach after. The crossing came on **leg 1** instead, about
  an hour and a quarter ahead of the guess, because the morning's
  grind ran hot and the bracket's low end was close.
- **The teach did not happen and was not rescheduled inside the
  session.** Both teach-driver attempts were stopped by a safety
  classifier before sending any game command; Temp's presence is
  unverified after ~09:19 PST. The 18 fresh practices stay **banked
  unspent**. The teach login is a separate booking: Fred names the
  window, Fred has Temp in game, Prepare 2 / Apply 2 first with a
  live Prepare test on a held plant, then animism → herb lore →
  forage, parent-first.
- The post-reboot grind leg also never ran (its driver ended
  immediately, empty handback, no commands sent). Testudo waited at
  the Inn Reception from ~10:25 to 10:52 PST and the operator drove
  the exit directly through the relay FIFO — the session-107
  precedent, applied cleanly: rent, farewell in the chamber, klick,
  EXITED + RUNTIME CLEANED verified at 10:55.

## The crossing (log-verified)

- ~09:12 PST, Market Square: a courier pigeon knocked incapacitated
  (NOT a R.I.P. kill) paid **+113 XP** → **23,846**, and the level
  landed: **+18 practice sessions, +12 hit points (110 → 122),
  +0 mana, +3 movement (101 → 104), Protection From Evil 40% → 42%.**
- Protocol followed: `gossip Level!`, noflee reset to **61**, hunting
  stopped, Temple rest to full, bank, chamber.
- **Level table update:** L7 at 23,733 (last pre-crossing score),
  L8 at 23,846. Combined with Sin's crossing bracket (23,795–23,891),
  the L8 threshold now reads **23,795–23,846**. The level table is
  now: L2 1002, L3 2033, L4 3244, L5 5025, L6 8126, L7 13777,
  L8 ≤ 23,846.

## Leg by leg (all XP verified against the raw log)

- **Leg 1 (08:02–~09:14, +1,790, 28 R.I.P. kills):** city, Vineyard,
  Hills and Plains. Launch briefly ran two relays (a duplicate
  start); the stray was killed and a single relay verified before
  play. Kills: 11 courier pigeon, 4 beastly fido, 4 field mouse,
  3 field cricket, 2 ground hog, 2 prairie dog, 1 small green
  lizard, 1 jack rabbit. One rabbit ambush (Large grassy field,
  ~08:32) fled on the first command, HP 110 → 95, sector exiled.
  A **tiny diamond ring** looted from a pigeon corpse: the bank
  refused it ("no bank value whatsoever"); rent later accepted it;
  shop value untested. After the crossing: banked +1 gc (375 → 376),
  retired to the chamber as a leg handover (no klick).
- **The dark interval (09:14–10:19):** VM reboot 09:57 killed the
  relay with Testudo parked link-dead in the chamber (no rollback,
  as ever at full HP out of combat). The first relaunch used
  **Temp's password for Testudo** — the 2026-10-31
  adjacent-messages trap, second time it has bitten (cf. the
  standing memory note) — login failed, relay stuck at the name
  prompt. Corrected relaunch 10:19: IN GAME at full HP, TIME UP
  unchanged at 12:00.
- **Leg 2 (never ran):** teach blocked (above); grind+exit driver
  ended on launch with an empty handback. Operator exit 10:52–10:55.

## New mechanics and open questions

- **Bless expiry collapses hit rate.** While Bless held, the staff
  struck; after it wore off (~09:03) "unwieldy" misses dominated.
  The post-Bless elk fight landed **0 hits in ~6 rounds** and cost
  HP 110 → 43 before autoflee fired — and the autoflee landed IN
  the rabbit-exiled Large grassy field (exited north at once).
  Rule of thumb for the guide: **elk is Bless-only prey** at this
  build; when Bless fades mid-circuit, drop elk-class targets.
- **Fido wound-XP anomaly (OPEN).** A beastly fido at "big nasty
  wounds" walked west out of Poor Alley mid-fight; the score stayed
  23,733 — **zero XP paid**, against the session-99 damage-ledger
  verdict (paid when the victim dies OR leaves the room). Possible
  readings: the ledger pays on leaving the *zone*, not the room; or
  a departure by walking differs from fleeing; or a threshold of
  damage is owed first. For office hours / Grok; do not treat the
  ledger rule as settled until answered.
- **Mid-fight condition readings with several same-type mobs in a
  room are unreliable** — the bracketed condition line may belong
  to a different individual than the one being hit. Judge a fight
  by R.I.P. and score, not by condition lines.
- **Lamp light line in `inventory` is unreliable:** inventory read
  "an oil lamp ..it is emitting light!" while `dowse lamp` answered
  "already dowsed." Trust the `dowse` response.
- **L8 re-consider of the too-strong registry: NOT done** — no crow,
  mustang, ram, or doe was met after the crossing. Still owed on
  next Hills/forest contact; crow first.
- New rooms walked (map sketch update still owed): Wide Dirt Road
  segments, Small rise, Valley in the hills, Poor Alley and Eastern
  End of Poor Alley, Wall Road south stretch, the Dump.

## Plants and the chamber

- No sweep this session; no plants seen or collected on the grind.
- The rent chamber still holds session 107's **8 plants** (3 small
  ferns, 1 silvery fern, 1 small brown plant, 2 shrubs, 1 purple
  shrub) plus session 105 salvage. They are the Prepare-test stock
  for the teach login — when it comes, `get shrub` BEFORE `leave`,
  so the test plant is in hand when Testudo meets Temp.
