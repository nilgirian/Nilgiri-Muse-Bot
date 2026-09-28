# Session 15 — Northern Midgaard finish attempt (SinMuseBot)

**Date:** 2026-09-28, ~14:15–14:21 PDT (~6 min of a 1-hour budget — ENDED EARLY: VM rebooted)
**Character:** SinMuseBot, Level 3 (2348 XP, unchanged)
**Result:** Mapping resumed; 2.5 rooms recorded before the machine rebooted. Character almost certainly link-dead at the Swordsmen Guild entrance hall.

## What happened

Fred's mission: finish mapping Northern Midgaard (7 remaining gaps), then
spot-check Southern Residential; plus a diagnosis of the connection drops.
The relay logged in cleanly at ~14:15 and the driver began on the guild
entrances. At ~14:21 the entire VM rebooted (third spontaneous reboot of the
day: 10:06, 13:37, 14:21 — all confirmed via `who -b`), killing relay, FIFO
holder, SSH, and driver instantly. No TIME UP, no exit markers, no traceback —
the relay never knew what hit it.

Rooms recorded before the reboot:

- **Entrance to Cleric's Guild** (W of Temple Square) — modest entrance hall,
  knight templar guard. Exits verified: N -> Cleric's Bar **[BLOCKED — templar
  grabs intruders: "YOU may not enter here!"]**, E -> The Temple Square,
  Up -> The Hospital.
- **The Hospital** — clean room, rows of beds, friendly doctor, sign on wall.
  Exit verified: Down -> Entrance to Cleric's Guild.
- **Entrance Hall to the Guild of Swordsmen** (S of Main Street east-2) —
  "a place where one has to be careful not to say something wrong (or
  right)"; knight guarding. Description gives E -> bar, N -> Main Street, but
  the `exits` command never ran before the reboot — verify next visit.

Social: the bot answered Sin's "welcome back" / "keep up the good work" and
Motorola's "are you having fun" naturally via gossip — the respond-to-the-crew
rule held this time.

Still unmapped (Northern): Todai Food Outlet, East/West Gate interiors, Steak
House interior, Grunting Boar bar, plus Swordsmen hall exit verification.
Southern Residential spot-check never started.

## Connection diagnosis (confirmed this session)

Two separate failure modes, now cleanly distinguished:

1. **VM reboots — the "silent deaths."** Sessions 13 and 15 both ended in full
   machine reboots. Relay + holder + SSH die together with zero log markers;
   the heartbeat file (in `~/workspace`, survives reboots) just goes stale.
   The historical session 4/12 silent deaths at ~60–70 min match this signature
   exactly — they were almost certainly VM reboots too, not a relay bug. The
   session-13 setsid/detachment hardening was aimed at the wrong cause: **no
   process detachment survives the machine rebooting.** Check `who -b` first
   whenever a relay dies silently.
2. **SSH keepalive drops — recoverable.** "Timeout, server nilgiri.net
   not responding." is OpenSSH's own client message (`ServerAliveInterval=15`
   x `ServerAliveCountMax=3` = 45s of unanswered keepalives, then ssh aborts
   itself). The stall is in the VM -> proxy -> nilgiri.net path, not the MUD
   (Fred confirms the game never went down). The relay's reconnect logic
   recovered all 3 such drops in session 14. A background probe this session
   logged the proxy path healthy (0.2–0.4s handshecks) right up to the reboot.

New trap: after a reboot `/tmp` is wiped, so `printf > /tmp/mud_cmd` silently
creates a regular file instead of reaching a relay. Always verify
`/tmp/mud_cmd` is a FIFO (`test -p`) and the relay process exists before
sending commands.

## Character state

Likely link-dead at the Entrance Hall to the Guild of Swordsmen. Session
start: L3, 2348 XP, 47/47 HP, inventory = 1 manna + Nilgiri Guide, no gold
carried, bank #0000-11FB = 69gc. A fresh login should recover it.

Map file `maps/midgaard-northern-main-city.md` updated (Cleric's entrance,
Hospital, Swordsmen hall); 5 markers remain.

## Resumed run (~14:30–15:19 PDT, 54 min — the remaining budget)

Per Fred's rule (reboot → note it, relaunch with remaining time, resume the
mission), the relay was relaunched with SESSION_SECONDS=3240 and the
ServerAliveCountMax=10 tuning live. The MUD handed the link-dead character
straight back at the Swordsmen Guild entrance hall.

**Northern Midgaard is now FULLY MAPPED.** All remaining gaps closed, exits
`exits`-verified and `where`-checked:

- Entrance Hall to the Guild of Swordsmen — exits verified: N -> Main
  Street, E -> The Bar of Swordsmen (not entered)
- The Todai Food Outlet (N of east-3) — chef, popular hangout; S -> Main St
- Inside the East Gate of Midgaard — two towers, footbridge, 5 Dark Watch
  guards; N/S -> Wall Road, E -> outside (gate), W -> Main Street
- Steak House interior (S of west-2) — chef; N -> Main Street
- Inside the West Gate of Midgaard — blood-stained gate, 5 Dark Watch
  guards, Gelu the God of Thalodia -Truth- (left alone); N/S -> Wall Road,
  E -> Main Street, W -> outside (gate)
- The Grunting Boar (bar, E of inn entrance) — bartender; E -> Gambling
  Den, W -> inn entrance
- The Gambling Den of Midgaard (bonus room, E of the bar) — circular
  dark-oak room, big blackened table; W -> The Grunting Boar

**Southern Residential spot-check: 18 rooms, zero discrepancies.** Promenade,
park paths, Emerald Avenue, concourse chain, Park Road, Elm Street — every
room matched the map exactly (name, description, exits). Pond not
exit-verified (pitch black at night); off-limits doors not entered.

**Combat (per Sin's live instruction "go gain experience, try to level"):**
3 beastly fidos killed, all one-hit, no damage taken. +22 XP: 2348 -> 2370,
still Level 3 (L4 needs 3244 — 874 away, not reachable in the time left).
Lesson learned: the driver's brief said "mapping pass, not a hunt", and it
obeyed the brief over Fred's live order after 2 kills. New standing rule:
a direct instruction from Fred overrides the brief.

**Connection:** one ssh keepalive drop mid-session (~14:52); relay
reconnected automatically in ~40s. No VM reboot this run.

**End state:** Level 3, 2370 XP, 47/47 HP. Bank #0000-11FB = 69gc
unchanged. Exit inventory: Nilgiri Guide only (manna eaten). Retired by
direct drive: rent + klick + menu-0, MUD closed cleanly, no strays.
