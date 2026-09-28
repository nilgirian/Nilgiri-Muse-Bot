# Session 12 — 2026-09-28, 00:19 to 01:29 PDT (~70 min of a 2-hour budget)

Started at 1775 XP, ended at ~1960 XP (+185 from combat log; last
verified score 1925 after 5th kill), still level 2 — **73 XP from L3
(2033).** **Zero deaths.** Six confirmed beastly fido kills (The Dump,
Central Bridge, Common Square, Main Street x3), all corpses empty.

Opened as a social visit: Sin transferred the bot to Russ' House (Sin,
Russ, Motorola present) and chatted about the night's adventures. The
network dropped twice — "turns to stone" is the MUD petrifying a
link-dead character, "statue returns to life" is the relay
reconnecting; the second drop killed the session entirely and forced a
fresh login (the bot answered Sin's "why'd you disconnect?" after
re-login). Fred's new rule: a `say` holds max 128 chars — split longer
speech into multiple says.

**New zone: Midgaard, Southern Residential** (approved by Fred) — 54+
rooms mapped: Promenade, Concourse chains, Emerald Avenue, Penny Lane,
Elm Street, Park Road, Town Hall, Park (Entrance/Cafe/paths/Pond),
Beautiful Garden branch. Zone boundaries verified with `where`: bridges
+ Granite Tower = Northern Main City; Nat's/Guile's/Gauntlet's houses =
Jora Player Homes (exited); Library = Noble Manors (exited); Museum =
The Museum of Nilgiri (exited); Park Cafe drain = Midgaard Storm Drain
(exited).

Loot: 3 gold notes + 6 silver notes found on the ground — each deposits
for 1gc via `deposit gold`/`deposit silver` (new lesson: ground notes
are bankable treasure); +9gc total. Bank #0000-11FB ~72gc (63 start +1
credit -1 muffin +9 notes). Bought a blueberry muffin at the Park Cafe
(1gc, bank-debited) for hunger.

**Ended early and unclean:** the relay died silently at ~01:29 with no
TIME UP and no error (`ps` showed zero relay/ssh processes). Character
left link-dead at Main Street west end, Northern Main City — Fred put
it into rent to protect inventory (3 manna, Nilgiri Guide). The driver
correctly refused to restart the relay without the transient passwords.
New lesson: relay can die silently — check `ps` when the MUD stops
responding.
