# Leveling guide — notes-16 (day twelve: session 105, 2026-11-01)

Session 105: Testudo L6, XP 10,492 → 12,866 (+2,374), 52 confirmed kills,
0 deaths, bank 230 → 346 gc. Four-hour XP run cut into three legs by two
VM reboots; the run also folded in the cabin-recovery question left open
by session 104. L7 (13,777) now 911 away.

## New and refined mechanics

- **Fireplace key stock grows.** The cabin fireplace held small brass
  keys x78 in s104; in s105 it held **x100** (one taken). The container
  restocks between visits, and the stock number is not fixed at 78.
- **Floor-drop persistence is item-dependent.** Of the gear shed on the
  cabin floor in s104 (~16 hours earlier): Slug's aluminum container and
  the hooded brass lantern **persisted and were recovered**; the 2 large
  torches were **gone**; the tin crown/chest plate spares and spare
  barrel were still present (left for weight). No general rule yet —
  record per-item outcomes, never assume.
- **Brown fox priced:** 63 XP (s105 leg 1: 57+6) and 75 XP (leg 2) —
  new XP_PER_KILL entry, ~63–75 at L6.
- **Courier pigeons are a real threat to this build.** Fast, pecking,
  hard to hit: one took Testudo to 27 HP through two PANIC-failed flee
  attempts before a kick finished it (+133 total across installments);
  another was wounded, fled from, and its ledger never settled (no
  payment — a departed victim pays only when it dies or leaves the
  room; this one apparently did neither in range). Treat pigeons as
  mid-tier danger, not filler.
- **Kick-finisher caveat (3 cases now).** The standing rule "kick never
  finishes a downed mob" needs its boundary: in s105 a kick delivered
  the outright R.I.P. blow three times (leg 1 pigeon, leg 3 pigeon and
  fido) — in every case the prey was **mortally wounded**, not merely
  incapacitated. Refined rule: `kill` remains the finisher for
  incapacitated mobs; a kick CAN kill a mortally-wounded one outright.
- **Brown bear (new hazard, unpriced).** Attacked unprovoked on a
  Sleeping Forest small-path room: ~10 HP/round claws, staff landed
  zero hits in several rounds. Fled at 50 HP and cured. Do-not-engage
  until sized properly; add the fringe small paths to the caution list.
- **Stag (forest trails):** consider = higher level, entrails reading —
  do-not-engage class, same as the ugly troll on Faint Path (s105 leg 1).
  Faint Path → "Outside the Manor" (fortified manor) is new mapped
  ground, unexplored, with the troll standing on the approach.
- **Southern Residential + park circuit is empty of legal prey** (four
  passes, birds only). The zone-per-hour circuit should not count on it
  for XP.
- **Prairie dog ledger settlement confirmed again:** +26 arrived after
  Testudo had fled the wounded dog — the damage ledger pays when the
  victim dies or leaves, whoever is present. (Grok's model, s99.)
- **`where <name>` locates a player** (Fred, 2026-11-01): in Midgaard,
  `where Temp` reports the room a named player stands in; navigate by
  the room name. To be exercised in session 106's teach test.
- **Rent chamber access rule (driver-verified, s105):** `rent` at
  Reception moves the character straight into the chamber, whose only
  exit is `klick` (out of the game). The chamber cannot be visited
  mid-session to stash gear — storage drops happen inside the exit
  sequence itself (rent → drop → klick), as s105's exit did with the
  recovered salvage (carried weight 204 → 159 lbs).

## Operator/relay observations (not game mechanics)

- **Stuck RABBIT-AMBUSH marker:** after leg 2's third rabbit flee, the
  marker kept re-emitting for 30+ minutes while Testudo rested on Wall
  Road demonstrably out of combat; during the bear fight one `flee`
  executed that the driver never sent (a PANIC line right after its own
  successful flee) — consistent with the stuck marker injecting it.
  Relay-side suspicion, recorded for the relay maintainers; drivers
  should treat a marker that contradicts a plainly safe room as suspect
  but still flee any fight actually in progress.
- **Early exit, again:** leg 3's driver ran the complete exit sequence
  ~44 minutes before TIME UP with no stated cause (the exit itself was
  flawless: bank, farewell verbatim, rent, salvage dropped, klick,
  fresh EXITED markers). Same failure family as s100's early leg —
  time-boxed legs must state their exit trigger in the handback.
- **Brief food-tally error:** leg 3's brief said he carried 2 loaves;
  the driver's inventory check found none (leg 2's eat had landed and
  nothing was restocked). Lesson: verify inventory, not briefs.
- The two VM reboots hit at 08:22 and 10:22 PST — exactly the two-hour
  per-boot cadence, unaffected by the DST fall-back. Both recoveries:
  link-dead at full HP, standing, out of combat → zero XP rollback
  (score-verified at each leg start: 11,712 and 12,345 both matched).

## Speech Q&A audit (closeout requirement)

- Leg 1: Sin's gossip "norritt I deposited some money in your bank
  account fyi" tripped SPEECH-PENDING → SPEECH-UNANSWERED. It was
  addressed to **Norritt**, not Testudo — deliberately not answered.
  Correct outcome; the marker cannot tell addressees apart.
- Leg 1: player Quenyarhun's gossip question about opening a bank
  account was answered conversationally.
- Leg 2: Motorola's welcome-back gossip answered with brief thanks.
  Norritt's gossips (to Sin/Motorola) not answered — not ours.
- Leg 3: no controller speech. Norritt's bakery question ("how do you
  sell at the armory") answered with a single friendly say.

## Standing state after session 105

Level 6, XP 12,866 (L7 at 13,777 — 911 to go), HP 95, mana 100, move 98,
noflee 47, bank 346 gc, 0 practices. Chamber stores: Slug's container,
hooded brass lantern, empty wooden chest, 1 brass key, plus the older
spares. Crow re-consider at L6 STILL open (never met in three sessions
of Temple Square passes). Session 106 (Fred, 2026-11-01) hunts the 911
and then runs the Temp teach test — Fred drives Temp himself; Testudo
locates him with `where Temp`.
