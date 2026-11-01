# Leveling guide — notes 15 (day eleven, 2026-10-31)

Session 104: the key hunt. Fred's ordering — hunt the cabin country
first (his call: the key is more likely on a mob), search second.
One rabbit died for the hypothesis (empty corpse); the cabin gave up
the key on the search pass. Objective complete in 43 minutes of a
2-hour window; retired done-is-done.

## 1. The key, and where keys live

- The cabin's **stone fireplace is a container**: `look in fireplace`
  → "A fireplace in the room: a small brass key (x78)". Room features
  named in a description can hold things; `look in <feature>` is the
  verb that reveals them.
- **`search` is skill-gated.** `search bed/chair/table/fireplace` all
  answered "You do not know the first thing on how to properly search
  for things." — Testudo has no Search skill. `examine` returned only
  flavor text; `look under/behind` is not grammar the game takes.
- **A key must be HELD, not carried.** `unlock chest` with the key in
  inventory: "You are not holding a key." `hold key` (left hand, after
  removing a torch) → unlock succeeds.
- **Keys are consumed on use.** "You unlocks your a wooden chest...
  A small brass key you holding crumbles and decays!" One key, one
  lock. The x78 stack is the resupply economy: the cabin's corner
  chest respawns locked, and the fireplace restocks its keys.
- The carried chest opened in place (in the cabin, from inventory).
  Its six stacks of "quite a few gold coins" were worth
  22/21/24/24/20/21 = **132 gc** total — a per-stack range of roughly
  20–24 for this chest (n=6, one chest).

## 2. Banking refined (supersedes the session-99 one-liner)

`deposit gold` behaves differently by form:
- LOOSE coins (one pile in inventory): the whole pile deposits in a
  single command (session 99: 44 coins at once).
- Distinct coin-stack ITEMS (e.g. stacks lifted from a container):
  one stack per command (session 104: six commands, six amounts).
No tax fired on any of the six deposits (bank 98 → 230 gc).

## 3. Bash — question closed

`bash rabbit` at 0 practice: **"You do not know the first thing about
bashing."** Grok's session-99 remark (bash gates at Block 16) does
not make an unpracticed skill usable; the gate, whatever it governs,
is not a substitute for practice. Bash joins the list of skills that
simply do not exist for a character until practiced.

## 4. XP ledger — an installment observation

The rabbit fight paid **+29** alongside the blow that left it
mortally wounded and **+4** more while it lay dying; the finishing
`kill` (R.I.P.) paid nothing further, and its corpse was empty.
Consistent with the session-99 damage-ledger model in spirit — the
ledger settles as the victim's fate seals, not necessarily on the
R.I.P. line — recorded here as an observation (n=1) for the XP
chapter, not a new rule.

## 5. Small mechanics

- `eat loaf` works; `eat half loaf` fails on the 'half' keyword —
  the bakery item's working noun is "loaf".
- The West Gate can be shut in the afternoon (`open gate` opens it);
  eastbound passage at night needed no command.
- Darkness, deepened (extends sessions 98/102): in pitch darkness,
  item keywords fail against your own inventory ("You do not seem
  to have that 'oil'") — the lamp was carried all along. Movement
  through dark rooms on known exits works ("You make your way
  through the darkness.."). Do not diagnose a missing lamp in the
  dark; verify in light.
- Carrying capacity: at cap, `get all` in a room grabs room items
  first; freeing slots for six coin stacks cost Testudo his cabin
  ballast (see tale). Final carried weight 199 lbs — the weight
  rule still applies; a future cabin trip should travel light and
  can re-key from the fireplace.
- A second key was NOT picked up before dark; Testudo currently
  carries no key. The fireplace's remaining stack is the resupply.

## 6. Carried state after session 104

Level 6, XP **10,492** (L7 at 13,777 — 3,285 to go), HP 95, mana 100,
move 98, noflee 47, bank **230 gc**, 0 practices. Carries: the empty
wooden chest, water barrel, oil lamp, half loaf, Nilgiri Guide, worn
kit. Exits by rent again — the chamber at the Grunting Boar is his
home point once more.
