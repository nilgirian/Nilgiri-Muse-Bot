# Too-Strong Mobs — running list

Mobs SinMuseBot could not defeat at its level. **Check this list before
engaging anything unfamiliar**, and re-`consider` everything on it after
every level-up (Fred's rule, 2026-09-28) — a new level may make an old
killer killable. When a mob becomes safely killable, move it to
[Cleared](#cleared-killable-as-of) with the level that cleared it.

The point of this file is the head start: a future new character using
this repository reads it on day one and knows what to avoid at low
levels without dying to learn it.

Drivers: update the local copy of this file during the session (new
entries, cleared entries); the operator publishes it to the repo.

## Re-test queue (Fred, 2026-09-30)

Fred's decision after the `consider` audit: treat `consider` as fairly
accurate and put the three "liars" back in the ring, with the new tools
(`set noflee` autoflee, prompt HP display) armed. These are CONTROLLED
PROBES, not grudges — the point is data: damage per round from the
prompt, whether the sim's numbers or the live disaster was right, and
whether anything (bug, target-switching, duplicate mobs) explains the
session-21 results.

All three "liars" resolved: courier pigeon cleared L5 (session 30),
small green lizard cleared L6 (session 42), large elk cleared L8
(session 75). No open probes. Probe protocol kept in
LESSONS_LEARNED.md in case a new `consider` liar appears.

## Currently too strong

| Mob | Where | What happened | Level when listed |
|-----|-------|---------------|-------------------|
| Angry drone bee | Bee Hive entrance | Killed the bot | L2 (session 9, 2026-09-27) |
| Fluffy the baby dragon | Inside the West Gate; the Field | `consider` (L4): "higher level than you / envision your entrails spread about the room" | L4 (session 20, 2026-09-29) |
| Brown bear | Heavy jungle | Killed the bot | L2 (session 9, 2026-09-27) |
| Tarantulas | Heavy jungle | Killed the bot | L2 (session 9, 2026-09-27) |
| Three-point horned stag | Hills and Plains (forest edge) | `consider` read too strong; left alone, never fought | L2 (session 7, 2026-09-27) |
| HUGE prehistoric vulture | Grassy plain (Hills and Plains) | `consider`: "higher level than you. You envision your entrails spread about the room." Never fought | L3 (session 18, 2026-09-28) |
| Mosquito (swarm) | Muddy park, Newtonia | NOT weak — swarmed and killed a full-HP L3 in ~8 rounds (session 18b). The session-18a "aggressive but weak" note was wrong. **Session 26 (Sin authorized "try the mosquito be careful"): killable 1v1 at L4 (12-33 XP each, "bite barely hits you") BUT they swarm and reinforce ("comes to the assistance of a mosquito") — 3-4 at once forced repeated noflee autoflees at 54→20s HP. Motorola's heals kept the char up. Survivable with autoflee + full HP + willingness to retreat, but the pond area is a meat grinder, not a hunt spot** | L3 (session 18, 2026-09-28) |
| Sir Issac | Newton's Lab, Newtonia | `consider`: higher level, "entrails" — never fought | L3 (session 18, 2026-09-28) |
| Shambling mound | Demuryn Ruins entrance (below "Behind the avalanche", Newtonia chapel corridor boulder passage) | "hits you extremely hard" — took a full-HP L4 (54 HP, full tin) to 20 HP in ONE round, alongside 2 newt shades. Driver fled via noflee. Do not engage at L4 | L4 (session 26, 2026-09-30) |
| Newt shade | Demuryn Ruins entrance (same room as shambling mound) | "rips you up badly", "hits you hard" — 2 of them with the mound; part of the 54→20 round. Do not engage at L4 | L4 (session 26, 2026-09-30) |
| Giant cricket | In the cricket pen, Newtonia Fishing Village (also roams slick paths, bridge, hills, pond) | `consider` (session 28): "It is a higher level than you. You envision your entrails spread about the room." Never fought. Do not engage at L4 | L4 (session 28, 2026-10-01) |
| Crawfish | In a shallow pond, Newtonia Fishing Village | `consider` (session 28): "It is a higher level than you. You would probably die..." Never fought. Do not engage at L4 — the village pond's tempting prey is a death sentence | L4 (session 28, 2026-10-01) |
| Skunk | Peaceful Grove | `consider` is a LIAR: reads P2 ("lower level / you think you could do it"), but session 86 leg 1c's fight went 96→43 HP (~55% of max) while the skunk stayed barely wounded — ~10+ dodges, "bites you very hard"; noflee autoflee tripped at 43 HP (one PANIC fail, then fled at 49). No kill. One session-85 kill (~71 XP) stands, but DO NOT ENGAGE at L9. n=1 disaster — single-encounter caveat. **L10 re-probe (session 87 leg 6, 2026-10-23): `consider` at full HP still reads "lower level than you / you think you could do it" — unchanged; not engaged per probe protocol. Stays DO NOT ENGAGE pending Fred.** | L9 (session 86, 2026-10-22); L10 probe (session 87) |
| Black crow | Roams Midgaard (found on Main Street, session 98 — NOT reliably at Temple Square) | Testudo `consider` at L5: "He is the same level as you. You would probably die..." Never fought. Re-consider at L6+ still open | L5 (session 98, 2026-10-28) |
| Stray cat | Midgaard / fringe | Testudo `consider` at L5: "very tough battle." Never fought | L5 (session 98, 2026-10-28) |
| Wild mustang | Hills and Plains fringe | Testudo: considered too tough at L5 (leg-1 driver judgment, session 98); never fought by Testudo | L5 (session 98, 2026-10-28) |
| Big horned doe | Hills and Plains fringe | Testudo: considered too tough at L5 (session 98); was prey for the higher-level SinMuseBot (~65 XP on its table) — level-dependent, retest for Testudo at L7+ | L5 (session 98, 2026-10-28) |

Notes:

- "Rabbit" covers both prey and predator: `consider` every rabbit-class
  mob before engaging. Jack rabbits were safe L2 prey; the ferocious
  rabbit is the killer.
- The small green lizard is a `consider` liar — treat its rating as
  unreliable even after it clears; verify with actual combat before
  trusting it.

## Cleared (killable as of)

| Mob | Cleared at level | Date |
|-----|------------------|------|
| Courier pigeon | L5 (2026-10-02, session 30) | 5 R.I.P. kills, 0 deaths, at full HP with probe discipline (solo, noflee armed, manual flee at 50% — one disciplined flee at 37/61 HP, no near-loss). The L4 deaths look increasingly like the duplicate-mob/targeting confusion, not the bird alone. Keep probe discipline anyway: bites still land hard/very-hard. |
| Small green lizard | L5 (2026-10-02, session 30) | 1 R.I.P. kill, 0 deaths (thin data — one kill; treat as provisionally cleared, re-confirm next session). **Confirmed L6 (2026-10-04, session 42):** second clean R.I.P. kill — fully cleared. |
| Large elk | L8 (2026-10-16, session 75) | First kill: "A large elk is dead! R.I.P." at full HP with probe discipline (noflee armed, manual flee at 50%). ~76 XP per kill (n=1, provisional) on the re-ranked XP-per-kill list. Listed L4 (session 21, 2026-09-29): the L4 loss was link-death mid-fight when the VM rebooted, not a fair defeat. |
| Ferocious rabbit | L8 (2026-10-17, graduated by Fred) | Killed session 58 (101 XP, 2026-10-08) and bled out session 72 (2026-10-14) — no longer "too strong." **The ambush protocol stays in full force:** default flee on RABBIT-AMBUSH; stand and fight ONLY at full HP, fed/watered, noflee armed, zero prior engagements that session; manual flee at 50% HP; one engagement per session max. Stays OFF the XP-per-kill ranked list (~78 XP, n=8, for reference only) — it is not a hunt target. **Session 87 range note: now also ranges the Grassy plain south of Large grassy field, and follows a fleeing player room-to-room — transit out needs several consecutive moves.** **Session 98 (Testudo L4–L6): killed once at L4 under audited flee-first conditions (auto-round crits incapacitated it, flee PANIC-failed, downed rabbit finished) — and it RESPAWNED the same day: four ambush events in one session, including a room-to-room pursuit (Testudo to 15 HP) and an attack on a SLEEPING player. Never sleep in the fringe; never re-enter the ambusher's room; flee-first, always.** |

## Do-not-engage for other reasons

Avoided by rule, not by level — never "clear" these:

- Ugly troll, Shargugh the Forest Brownie, John the Lumberjack, gnome,
  Intrepid, knight templar — ambiguous identity (could be an NPC or a
  player). The creature-only rule requires `look <name>` first; they
  were left alone.
