# MUD_TOOLS.md

Useful Nilgiri MUD-side commands and settings discovered during bot
operation. These live in the game, not in our scripts — the driver
invokes them in-session. This is a living list; add new finds with the
date and who found them.

## Automatic flee: `set noflee`

Found 2026-09-30 (Fred).

- `set noflee` — show the current value.
- `set noflee <number>` — turn it on. The character flees automatically
  once its hit points fall BELOW that number.
- `set noflee reset` — turn it off.
- When it is 0, it is off and the character never flees on its own.

Standing rule: arm it at every session start. The number is provisional
at half max HP, rounded down (SinMuseBot at 54 max: `set noflee 27`),
until prompt-HP fight logs yield real damage-per-round data. The
threshold must sit ABOVE the worst single round a mob can deal — a
number one bad round can vault clean over never fires. Recompute after
every level-up.

It is a backstop for the gaps between driver wakes and for stalls, not
a replacement for manual fleeing: flee attempts can FAIL (session 21's
courier pigeon: "You were unable to flee!"), so the 50%-HP manual flee
rule still applies.

## Prompt HP/move/mana display: `environment displ_*`

Found 2026-09-30 (Fred).

- `environment displ_hits on` — show hit points on every prompt.
- `environment displ_move on` — show movement on every prompt.
- `environment displ_mana on` — show mana on every prompt.
- `environment exits_long on` — `look` also shows the room exits
  automatically (found 2026-09-30, Fred).
- `environment` alone — list all settings.

The prompt then reads like `45h 88v>` (`h` = HP, `v` = move, `m` =
mana). Standing rule: enable all three at session start and read HP
from the prompt before every `consider` and throughout every fight,
instead of spamming `score`. This keeps HP-at-engagement on the log
record (which post-session forensics needs) and saves a command each
time.
