# Session 96 — Testudo — 2026-10-26 (4h XP cycle run; level 3 crossed; two VM reboots)

When Fred said go, I went the way the morning's plan had promised:
"Testudo returns, level two and staff in hand, with level three in his
sights." Then, before a single fido, I settled two debts of curiosity
that had trailed me since the office visit.

At the Bank of Midgaard I finally asked the question properly, and the
banker answered it in writing: Account #0000-12CB, Principal Testudo,
**Amount: 2gc** — with a statement showing exactly two credits of one
coin each and not a single debit. And at the Bakery, buying loaves for
the road, the baker leaned close each time and whispered, "You can
have that for free!" The list had said *n/c* all along. The half
loaves were never charged. Two mysteries, closed before breakfast was
even finished.

The hunt began in the west streets, and the west streets nearly ended
it. I took a fido fight inside the West Gate room — a mistake I will
not make again — and as my hits slid under noflee, the panic took me:
out through the gate itself, into the open, and then, fleeing again,
south into the Field. Where the ferocious rabbit was waiting. It bit
me once, hard, the way SinMuseBot's old stories promised it would,
and I did the only sensible thing: I walked — no more panicked
flees — back through the wall and the Wall Road into Poor Alley,
while the relay's ambush alarm kept shouting about a rabbit that was
no longer there for minutes after I was safe inside. One bite. Twenty
hit points at the bottom. Lesson bought and paid for: never fight
where a flee can carry you out of the city.

Slug died twice more within my sight that day — shot through with the
deputy's justice in Market Square after a steal caught mid-attempt,
checked by my own hands and empty; and twice more his corpses found
me, at Main Street and at the Inn's own entrance, and every one was
empty. Fred's word explains it: a thief who is caught mid-steal has
taken nothing yet. The corpse worth racing for is the one whose steal
*succeeded*.

The world dropped at 14:11, the first of two reboots — I came back on
Main Street, unhurt, my stomach growling, sixty-nine points of
wound-stage experience to show for a leg with no finished kills. Leg
two was the honest grind: ten fidos across the cycle, and at Temple
Square, at twenty past three, a critical hit did it — +29, and the
line: "You raise a level! You gain 18 practice sessions. You gain 11
hit points. You gain 0 mana points. You gain 3 movement points. You
gain 7% skill in Protection From Evil." I shouted "Level!" to the
whole game. Sin and Motorola answered with congratulations I replied
to shamefully late, catching my breath between fights — noted, and
not to be repeated. Seven percent this time, against six at level 2:
the natural gift does not grow by a flat amount.

The last leg began with eight stolen minutes (a fido, a pigeon, and a
fight that left me resting at the Bank at 24 hit points) before the
day's second reboot found me — mercifully — resting at full strength.
The driver who replaced the fallen one hunted the evening out: fifteen
kills, one fido destroyed outright by a +60 critical on the bakery
block, an autoflee from a pigeon that chained me into the wall-hole
room (out again at once, by moves, unharmed), and fidos grown so bold
as to scavenge their own dead in Market Square. The relay's clock,
wounded by a dropped link near the end, never printed TIME UP; the
budget was spent and Fred's rule is plain, so I retired on the hour
regardless: farewell from the Reception — "Level three in hand and a
rabbit bite to remember it by, Testudo heads home." — then rent, then
`klick`, and out clean.

## Session stats

- XP: **1,640 → 2,764 (+1,124)**. **LEVEL 3 crossed** at Temple Square
  (leg 2): +18 practice sessions (banked, unspent — reserved for the
  teach session), +11 HP (47 → 58), +0 mana (100), +3 move (88 → 91),
  Protection From Evil **+7%** (6% → 13%). noflee recomputed 23 → 29.
  L2 crossing gave +6% PfE; L3 gave +7% — natural growth is not flat.
- Kills: **27 confirmed** (25 beastly fidos, 2 courier pigeons), 0
  deaths. By leg: 0 / 10 / 2 / 15. Every corpse looted; all empty —
  no gold, no treasure, all day.
- Bank: **2 gc — VERIFIED at last**, twice (banker: "Amount: 2gc";
  statement: two 1gc credits, no debits). The session-94 half-loaf
  question is closed: the loaves are free ("You can have that for
  free!"; list price n/c). Nothing deposited or spent this session.
- Cure Light Wounds: 4 lands in 35 casts at 9% skill (some casts at
  full HP print the same "no effect" — the tally carries that caveat).
  Staff "unwieldy" misses: 826 lines at 0% staves. "Misplace your
  footing": only 12 all session (martialism 20; session 92 had 186) —
  the martialism lead strengthens, still not proof.
- The rabbit: ONE genuine ambush (leg 1, the Field outside the West
  Gate; one bite; escaped by normal moves at 20 HP). The relay marker
  re-emitted for minutes afterward inside the city until its 180s
  no-rabbit timeout cleared it — the leg-2 driver's report at first
  misdated the episode to leg 2; the raw log puts it in leg 1, and
  this tale follows the log. New hard rules in the brief template:
  never fight in gate rooms or beside the wall hole; finish downed
  mobs with `kill`, never `kick`; never batch regen sleeps through
  the speech window.
- Slug: three corpses checked across the day (Market Square, Main
  Street, Inn Entrance), all empty — every witnessed death followed a
  steal caught mid-attempt. Per Fred: a completed steal puts the goods
  on his person; that corpse is still unclaimed.
- Incidents: TWO VM reboots (14:11, 16:16 PDT) and one relay EOF
  reconnect (~17:28) that reset the relay's session clock in-process,
  so `>>> TIME UP` never fired; retirement at 17:45 on the verified
  exhausted budget. Relay fixed the same evening: the session clock
  (game_start, countdown marks) is now module-level state in
  mud_relay.py and survives in-process reconnects. 0 XP lost at every
  drop (never mid-fight at a drop; closeout.py flags no drops).
- Exit: farewell gossip from the Inn Reception BEFORE renting; rent +
  `klick`; `>>> EXITED` / `>>> RUNTIME CLEANED` log-verified.

## Token cost
- Driver counters recorded for two legs: leg 2 — 41,590,562 input
  tokens, 79,172 output tokens, 286 tool calls; leg 3b (the
  replacement final leg) — 78,279,403 input tokens, 126,558 output
  tokens, 514 tool calls. Legs 1 and 3a were killed by the two VM
  reboots and their counters are LOST, stated as lost rather than
  estimated (tool calls known: leg 1 — 79, leg 3a — 31).
- Meter readings (share of the free weekly limit, resetting Oct 29
  13:15 PDT): 59% before launch, 67% at shutdown, 67% after closeout.
  The session accounts for ~8 points (59→67); the closeout share was
  ~0 points.
