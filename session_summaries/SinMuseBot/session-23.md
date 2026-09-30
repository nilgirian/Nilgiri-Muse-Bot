# Session 23 — SinMuseBot — 2026-09-30 (~08:57–10:07 PDT)

One-hour courier-pigeon combat probe (Fred), run in three segments because the
relay kept dying (see Technical below). Retired cleanly via rent + klick +
menu-0 at ~10:07 PDT.

## Results (audited from the full log)

- **Level:** L4 (no level-up)
- **XP:** 3412 → 3861 (**+449**)
- **Confirmed kills:** 7, all courier pigeons (R.I.P. lines only — XP events
  never counted)
- **Deaths:** 0
- **Loot:** a dull tin chest plate picked up at the Dump (segment 1). The bank
  refused it ("has no bank value"); it went into the rent-room vault.
- **Bank:** 4gc, unchanged. No gold looted (pigeon corpses are empty).

## Fights

1. Main Street (General Store): `consider` rated a FAT pigeon P2, but `kill
   pigeon` engaged a COURIER — target mismatch. 54→40 HP. R.I.P. +53.
2. Main Street (weapon shop): courier, considered P2. 54→33 HP, ~5 straight
   unwieldy misses (unhittable mode). Incapacitated +42; died off-record
   (corpse eaten by a fido, no R.I.P.). NOT counted.
3. Main Street (weapon shop): courier, considered P3 ("easy battle"). 54→38.
   R.I.P. +31.
4. Poor Alley: courier, considered P2. 54→33, condition flipped awful→wounds
   mid-fight. Mortally wounded +68 → R.I.P.
5. Alley at Levee (beastly fido, P3 easy): 54→52, incapacitated +13. Died
   off-record. NOT counted.
6. Market Square: courier, P3. 54→28, noflee auto-fled at 27 (backstop
   worked). Escaped to the bakery.
7. Market Square: courier, P2. 54→43, stunned +35, recovered → R.I.P.
8. Market Square: courier, P2. 54→43, mortally wounded +52 → R.I.P.
9. Market Square: courier, P2. 54→20. Heavy hits ("extremely hard" -5, "very
   hard" -6). noflee fired but FAILED twice ("PANIC! You could not escape!");
   manual `flee` worked. Mortally wounded +82 → R.I.P.
10. Temple Square: courier, P3. 54→43, mortally wounded +36 → R.I.P.
11. Common Square (segment 2): courier, considered P3/easy — nearly instantly
    destroyed. R.I.P. +19.

## Probe findings

- Courier pigeons are swingy but survivable with prompt-HP reads, `set
  noflee`, and manual-flee discipline.
- `consider`/`kill` can target different birds (fight 1, re-confirmed).
- Per-bird ratings vary: couriers rated both P2 and P3.
- Unhittable mode is real (~5+ straight misses at full HP, fight 2).
- Condition-line flips mid-fight (fight 4) fit the duplicate-mob explanation.
- Mortally-wounded deaths produce R.I.P. lines, usually delayed.
- Worst single round: 6 HP. "Extremely hard" hit was 5.
- **Autoflee is one flee attempt, not a guaranteed escape.** When it fires or
  fails, keep issuing `flee` until actually out. (Fight 9: noflee failed
  twice; manual flee saved the character at 20 HP.)

## Technical: relay LOGIN TIMEOUT death spiral (root-caused, fixed, verified)

- The relay's login state machine waited for a legacy `<>` prompt to declare
  IN GAME. Nilgiri now shows `<54h 106m 106v>`-style prompts.
- On linkdead reconnects the MUD skips the banner/menu and lands straight on
  the game prompt — the relay sat in login state while the character was
  visibly in-game, LOGIN TIMEOUT'd at 120s, killed SSH, reconnected. 13
  timeouts and two five-attempt give-ups this session. No VM reboot involved;
  one drop showed `client_loop: send disconnect: Broken pipe`.
- Fix (pushed to repo): `GAME_PROMPT_RE = re.compile(r"<\d+h \d+m \d+v[ >]")`
  with a global fallback — any game prompt outside the exit flow means IN
  GAME. The final relaunch logged `>>> IN GAME (game prompt detected)` with
  zero manual nudging.
- Operator's own bug, same session: restructuring the state machine left the
  steps-loop `break` misindented, so login checked only the first step and
  stuck at the color prompt. Fixed and pushed.

## Comms

- Answered Sin's "hi sinmusebot" and "what you doing this time SinMuseBot?"
  gossips. No controller orders beyond the mission.

## Token cost

- Driver segment 1: 19,949,214 in / 42,095 out (197 calls)
- Driver segment 2: 3,268,117 in / 24,089 out (54 calls)
- Driver segment 3 (retirement): ~5 min, count pending
- Session driver total: **23,217,331 in / 66,184 out (251 calls)** before segment 3
- Weekly free allowance: **94% → 95%** (resets Oct 1, 1:14 PM PDT) — the whole
  session (drivers + operator work) cost about **1% of the weekly allowance**.

## Shutdown

Bank attempt (plate refused, no gold), Grunting Boar Inn rent room, klick,
Return, atomic 0. MUD closed the connection (`>>> EXITED`). No relay
process, FIFO, or PID files remain. Character stored at full HP, fed,
quenched, with the tin plate in the rent vault.
