# Session 22 — SinMuseBot — courier-pigeon combat probe (2026-09-30)

**Time:** ~07:45–08:16 PDT (30 min). **Character:** SinMuseBot, L4.
**Mission (Fred):** kill courier pigeons in the city for a half hour —
controlled probe of the session-21/21b deaths with the new tools
(`set noflee`, prompt HP display) armed. **Driver method:** workflow
driver (Method B, second run).

## Results

- **XP:** 2907 → 3412 (**+505**). **0 deaths.** Clean TIME UP retirement
  (rent → klick → Return → 0; relay auto-cleaned, no stray processes).
- **Confirmed kills (R.I.P. rule): 5** — 4 courier pigeons (Main Street,
  Market Square, Common Square, Dark Alley) + 1 beastly fido
  (Common Square). The driver's report claimed 12 kills by counting
  "You gain experience" messages — corrected to 5 per the
  kill-confirmation rule (XP is awarded per wound stage).
- **Bank:** 9gc → 4gc (5gc spent on iron rations at the General Store,
  eaten; drank at the Market Square fountain). Balance verified.
- **Loot:** all corpses empty. Dump checked: empty.
- **Vault:** stashed spare staff, wooden shield, leather boots/shorts/
  vest in the rent room (rent → drop → leave, no klick). Carried out:
  manna x2, Nilgiri Guide; full tin worn + staff verified at end.
- **Comms:** no controller speech all session.

## The probe findings (the point of the session)

1. **`set noflee` saved the character live.** One courier-pigeon fight
   reproduced the exact session-21/21b death mechanism: ~9 straight
   rounds of "The weapon feels unwieldy in your hands causing you to
   miss" while the pigeon stayed in "excellent condition," grinding
   54→26 HP. `set noflee 27` auto-fled at 26 HP ("You flee in terror!").
   Without the backstop, this was death #4. The provisional 27 worked.
2. **The unhittable-pigeon mode is real.** It is not a display bug: the
   driver dealt zero damage over ~9 rounds while taking steady 4–9
   damage/round ("hard" → "very hard"). `consider` does not capture
   this failure mode; the audit sim's ~3% loss tail does. Four other
   pigeon fights were clean wins (54→43–54 HP, 2–6 dmg/round, one
   9–12 "extremely hard" round at most).
3. **Second pigeon mid-fight CONFIRMED.** In fight 6 a second courier
   pigeon flew in from the north mid-fight and the condition lines
   flipped around its arrival. Duplicate same-keyword mobs are real —
   this explains session 21b's non-monotonic condition text ("big nasty
   wounds" ↔ "excellent condition").
4. **`consider pigeon` / `kill pigeon` target mismatch is real.** The
   city holds fat pigeons AND courier pigeons under the same keyword:
   `consider pigeon` rated a fat pigeon "easy battle" while `kill
   pigeon` engaged the courier ("you think you could do it"). At the
   same level, the same keyword gave both ratings — so session 21b's
   driver plausibly considered the easy bird and fought the tougher one.
5. **Damage-per-round data (prompt HP):** normal pigeon rounds 2–6,
   worst single round 12 ("extremely hard"). Nothing approaching the
   21b death spiral in the four clean wins.

## Driver mistakes corrected

- **False "Level!" gossip.** The driver ran the `level` COMMAND (XP
  table), saw `*L4`, and gossiped "Level!" — but no level-up occurred
  (no advance message; score read L4 at 2907 XP before and after).
  **Death does not de-level:** `score`'s Level field is authoritative,
  not the XP table (2907 < L4's 3244 threshold, still L4 — levels are
  sticky). The driver's report wrongly claimed "started L3, leveled to
  L4"; corrected here.
- **Kill counting.** Driver counted 12 XP-gain events as 12 kills;
  corrected to 5 R.I.P.-confirmed per the standing rule.
- **Loot syntax.** Driver typed `get all corpse` (picked up the whole
  corpse as an item: "You take a corpse of a courier pigeon"), then
  `drop corpse` twice. Operator corrected via inbox mid-session
  (`get all from corpse` — with FROM); driver applied it. One
  unlooted corpse was dropped in the room (empty anyway).

## Verdict for Fred's question ("bug or something else?")

No MUD bug. The 21/21b deaths were: (a) a rare unhittable streak/mode
the sim already predicts (~3% tail) — reproduced live tonight;
(b) plausibly a consider/kill target mismatch (easy bird considered,
courier fought); (c) no autoflee backstop. All three are now addressed:
noflee armed (proved live), consider-each-pigeon discipline, prompt-HP
damage data. Courier pigeon stays in TOO_STRONG_MOBS.md — dangerous but
survivable with the tools, not cleared until a no-near-loss session.

## Token cost (Fred's request)

- Driver (workflow child, 203 tool calls / 30 min): **15.62M input /
  40K output tokens** (run telemetry). Spawn was cheap (~30K + brief);
  the cost is per-wake accumulation, unchanged by driver method.
- Operator (this chat): context 30% → 38% (~30K tokens).
- Subscription meter: 94% → 94% (unchanged; coarse-grained or lagging).
  Resets Oct 1, 1:14 PM PDT.
