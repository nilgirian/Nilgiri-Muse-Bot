# Session 14 — Northern city mapping pass (SinMuseBot)

**Date:** 2026-09-28, ~12:44–13:45 PDT (~52 min of a 1-hour budget — ended early at Fred's request)
**Character:** SinMuseBot, Level 3 (2348 XP, unchanged — no combat this session)
**Result:** 13 previously unmapped city rooms recorded by name, description and verified exits; character retired cleanly via rent + klick.

## What happened

Fred activated the "Finish the Midgaard city map in one timed pass" idea: a one-hour
exploration pass to fill the gaps in the northern city notes (Common Square, manhole,
shops and guilds, temple's north portcullis and side rooms). The pass ran as a
mapping-only session — no hunting, no chatting.

Rooms mapped (all by exact title, description, and `exits`-verified exits):

- **The Common Square** — alleys E/W, market square N, town dump S. Lovidamo the
  sheriff patrols here.
- **The manhole** (Market Square, Down) — opened it, climbed down, `where` showed
  **Midgaard Storm Drain** (off-limits); climbed straight back up. The manhole now
  stands open. Do not enter.
- **Ye Olde Reading Room** (E of temple) — bulletin board with posted notes; exit W.
- **Ye Olde Common Room** (W of temple) — piles of old equipment; exit E.
- **The North End of the Temple of Midgaard** — the north portcullis was closed;
  opened with `open portcullis`. Exits: E/W Cloister, S back through the portcullis,
  Down to Garden Path (not entered).
- **The General Store** — grocer; exit S to Main Street.
- **The Pet Shop** — cages of animals, pet shop boy with a kitten; exit N.
- **The Weapon Shop** — weaponsmith, grinding stone; exit S.
- **Liame's Epistolary Dispatch** — parcel counter, storage slots, roof ladder;
  exits N, and Up to a closed hatch.
- **The Armory** — armorer, forge; exit N. MoBen the Seer was standing here.
- **Bank of Midgaard** — banker; exit S. Account #0000-11FB balance: **69gc**
  (bought 'a serving of unagi and inari sushi' for 2gc at the Steak House for hunger).
- **The Magic Shop** — wizard shopkeeper; exit S.
- **Entrance to Mage's Guild** — round tower base; exits N to Main Street, Up to
  Mage's Bar (**blocked** — a sorcerer grabs intruders: "YOU may not enter here!"),
  Down to the basement office.
- **Dootif's Aerial Servant Corpse Retrieval Service** — mage's tower basement,
  summoning diagram; exit Up.

Still unmapped: Todai Food Outlet, East/West Gate interiors, Cleric's Guild
entrance, Swordsmen Guild entrance hall, Steak House interior, Grunting Boar bar.

## How it ended

About 52 minutes in, Fred asked to terminate the session — the bot had gone quiet
in-game (see below) and he wanted a normal rent exit. The driver was stopped, but
the relay had died on a MUD-side timeout ("server nilgiri.net not responding";
the server flapped several times this session), so the relay was relaunched with
the same credentials, the character reconnected at Market Square, and was walked
north → east → up to the Grunting Boar Reception, `rent`ed a private room, and
`klick`ed out through the exit menu (Return, then 0). The MUD closed the
connection cleanly. Inventory at exit: 1 manna, Nilgiri Guide. Bank: 69gc.

## Notes for next time

- The bot stayed heads-down on mapping and did not answer Sin or Motorola when
  they spoke — the mapping brief over-weighted "stay on task" against the standing
  rule to respond naturally to the crew. Future scoped passes should keep the
  respond-naturally rule intact.
- The MUD server dropped the connection multiple times this session ("Timeout,
  server nilgiri.net not responding"); the relay's reconnect logic handled it, but
  one drop outlasted the 5 reconnect attempts and killed the relay outright. Idle
  characters get "pulled into a void" — movement commands bring them back.
- Map file `maps/midgaard-northern-main-city.md` updated: 13 rooms filled in,
  ASCII sketch redrawn; 7 markers remain.
