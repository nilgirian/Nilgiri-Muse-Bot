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

| Mob | Where | Probe protocol |
|-----|-------|----------------|
| Courier pigeon | Main Street / Market Square (city) | `consider` first (expect "you think you could do it"); engage ONLY at full HP, fed and watered, noflee armed |
| Large elk | Hills and Plains, "Field (field)" | `consider` first (expect "you think you could do it"); engage ONLY at full HP, fed and watered, noflee armed |
| Small green lizard | Hills and Plains | `consider` first (expect "easy battle"); engage ONLY at full HP, fed and watered, noflee armed |

Probe rules for all three: read HP from the prompt every round and keep
the damage-per-round record in the session report; manual flee at 50%
HP no matter what the mob's condition line says; noflee is the backstop
for failed/never-issued flees. One probe per mob per session unless the
first probe clearly clears it — do not chain rematches while wounded.
A clean kill (R.I.P. or corpse) moves the mob to Cleared with the level;
another loss keeps it listed AND goes in the report as data.

## Currently too strong

| Mob | Where | What happened | Level when listed |
|-----|-------|---------------|-------------------|
| Angry drone bee | Bee Hive entrance | Killed the bot | L2 (session 9, 2026-09-27) |
| Fluffy the baby dragon | Inside the West Gate; the Field | `consider` (L4): "higher level than you / envision your entrails spread about the room" | L4 (session 20, 2026-09-29) |
| Ferocious rabbit | Hills and Plains AND Newtonia fields (Large grassy field through Open field) — it is NOT confined to Newtonia; attacked an L3 in the Hills and Plains ~09:14 PDT session 20 | Incapacitated a full-HP L2 in ~3 rounds | L2 (session 10, 2026-09-27). Session 19: an L3 counterattack left one mortally wounded ("will die soon") but the driver fled with no R.I.P./corpse — UNCONFIRMED, stays listed |
| Brown bear | Heavy jungle | Killed the bot | L2 (session 9, 2026-09-27) |
| Tarantulas | Heavy jungle | Killed the bot | L2 (session 9, 2026-09-27) |
| Three-point horned stag | Hills and Plains (forest edge) | `consider` read too strong; left alone, never fought | L2 (session 7, 2026-09-27) |
| Small green lizard | Hills and Plains | `consider` said "easy battle" but it dodged nearly everything and landed ~10 hard bites; fled at 27/47 HP | L3 (session 16, 2026-09-28) |
| HUGE prehistoric vulture | Grassy plain (Hills and Plains) | `consider`: "higher level than you. You envision your entrails spread about the room." Never fought | L3 (session 18, 2026-09-28) |
| Mosquito (swarm) | Muddy park, Newtonia | NOT weak — swarmed and killed a full-HP L3 in ~8 rounds (session 18b). The session-18a "aggressive but weak" note was wrong. **Session 26 (Sin authorized "try the mosquito be careful"): killable 1v1 at L4 (12-33 XP each, "bite barely hits you") BUT they swarm and reinforce ("comes to the assistance of a mosquito") — 3-4 at once forced repeated noflee autoflees at 54→20s HP. Motorola's heals kept the char up. Survivable with autoflee + full HP + willingness to retreat, but the pond area is a meat grinder, not a hunt spot** | L3 (session 18, 2026-09-28) |
| Sir Issac | Newton's Lab, Newtonia | `consider`: higher level, "entrails" — never fought | L3 (session 18, 2026-09-28) |
| Large elk | Hills and Plains, "Field (field)" — large grassy field east of the hills, city walls to the east | `consider` (L4): "lower level than you / you think you could do it" — but it took a full-HP L4 from 54 to incapacitated then mortally wounded in ~75s; the driver died link-dead when the VM rebooted mid-fight. `consider` LIED again (like the small green lizard) | L4 (session 21, 2026-09-29) |
| Courier pigeon | Main Street / Market Square (city) | `consider` (L4): "She is a lower level than you / you judge it to be an easy battle" — but it dealt "hard" → "very hard" → "extremely hard" bites, taking a full-HP full-tin L4 to mortally wounded; `flee` failed ("no state of coinciousness"). KILLED THE BOT twice (session 21 Market Square, session 21b Main Street). The 89-XP reward was the tell (fidos pay ~16): high XP = high danger, whatever `consider` says. `consider` LIED — liar #3 after the small green lizard and the elk. **Session-22 probe (Fred 2026-09-30): 4 confirmed courier kills, 0 deaths — but one fight reproduced the unhittable death-spiral (~9 straight misses, 54→26 HP) and only the new `set noflee 27` backstop saved the char. Second pigeon flew in mid-fight (duplicates confirmed); `consider`/`kill` targeted different birds (fat vs courier). Dangerous but survivable with autoflee + 50% flee discipline — stays listed until a no-near-loss session** | L4 (sessions 21/21b, 2026-09-29) |
| Shambling mound | Demuryn Ruins entrance (below "Behind the avalanche", Newtonia chapel corridor boulder passage) | "hits you extremely hard" — took a full-HP L4 (54 HP, full tin) to 20 HP in ONE round, alongside 2 newt shades. Driver fled via noflee. Do not engage at L4 | L4 (session 26, 2026-09-30) |
| Newt shade | Demuryn Ruins entrance (same room as shambling mound) | "rips you up badly", "hits you hard" — 2 of them with the mound; part of the 54→20 round. Do not engage at L4 | L4 (session 26, 2026-09-30) |
| Giant cricket | In the cricket pen, Newtonia Fishing Village (also roams slick paths, bridge, hills, pond) | `consider` (session 28): "It is a higher level than you. You envision your entrails spread about the room." Never fought. Do not engage at L4 | L4 (session 28, 2026-10-01) |
| Crawfish | In a shallow pond, Newtonia Fishing Village | `consider` (session 28): "It is a higher level than you. You would probably die..." Never fought. Do not engage at L4 — the village pond's tempting prey is a death sentence | L4 (session 28, 2026-10-01) |

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
| *(none yet — the session-19 rabbit "kill" was reverted: the rabbit was left mortally wounded and the driver fled with no R.I.P. or corpse, so per the kill-confirmation rule it does not count)* | | |

## Do-not-engage for other reasons

Avoided by rule, not by level — never "clear" these:

- Ugly troll, Shargugh the Forest Brownie, John the Lumberjack, gnome,
  Intrepid, knight templar — ambiguous identity (could be an NPC or a
  player). The creature-only rule requires `look <name>` first; they
  were left alone.
