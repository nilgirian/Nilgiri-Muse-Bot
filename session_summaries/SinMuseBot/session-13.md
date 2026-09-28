# Session 13 — 2026-09-28, 09:21 to 10:06 PDT (~44 min of a 2-hour budget)

Started at 1960 XP, ended at **2348 XP (+388)** — **LEVEL 3 reached** in
the Dark Alley. Level gains: 38 -> 47 max HP (+9), 102 -> 104 mana
(+2), 96 -> 101 move (+5), +14 practice sessions, +4% Spy. **Zero
deaths.** 15 confirmed beastly fido kills, all in Northern Main City:
Main Street x1, Temple Square x1, Inn entrance x1, Dark Alley x6,
eastern Wall Road x1, Common Square x2, Poor Alley x1, western Wall
Road x1, northern Wall Road x1. All corpses looted promptly.

The level was announced with `shout Level!` — this happened BEFORE
Fred's mid-session correction (2026-09-28) that `gossip` out-reaches
`shout` (gossip = whole game, shout = zone, yell = a few rooms, say =
room). The gossip rule is absorbed for all future level-ups.

Loot: a tiny diamond ring (equipped, right finger) and **2 shiny gold
coins** (carried, never banked — the Bank was not visited this
session; account #0000-11FB unverified, ~72gc expected). Hunger was
managed with manna (3 -> 1 remaining).

Social: Sin gossiped asking the distance to next level; the bot
answered truthfully from `level` output — 1084 XP to level 4
(L3 = 2033-3243, L4 at 3244).

**Ended early: the entire VM rebooted at ~10:06 PDT**, ~44 minutes in.
This was NOT the historical silent relay death — the new detached
relay (own session via `setsid`, heartbeat every 60s) was healthy
until the reboot: heartbeat age 2-68s the whole time, last beat 44
seconds before the machine went down. No bank deposit, no
rent/klick/menu-0 retirement was possible. The character is **link-dead
at the Common Square** — Fred needs to put it into rent to protect
inventory: 2 gold coins, 1 manna, Nilgiri Guide, worn diamond ring.

**Diagnostic verdict: inconclusive.** The relay never reached the
historical 60-70 minute silent-death window, so the shell-tree reaping
theory (sessions 4/12) remains untested. The setsid hardening cannot be
judged from this session. The next diagnostic run needs the relay to
survive past ~70 minutes without a VM reboot to actually test the fix.

Session log (local-only):
`logs/session-20260928-092100.log` (98,019 bytes, frozen at 10:06).
