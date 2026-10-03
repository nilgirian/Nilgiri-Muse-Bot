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

## Containers: the small bag (tested 2026-10-02, session 30)

The 5gc small bag works as a container.

- Correct syntax: `put <item> bag` (NO "in") — e.g. `put cake bag` →
  "You put a funnel cake into your bag."
- Retrieve: `get <item> from bag` — e.g. `get cake from bag` →
  "You get a funnel cake from your bag."
- **Parser bug (filed as [issue 011](issues/011-put-in-container-syntax.md)):**
  `put <item> in bag` FAILS with "A funnel cake will not contain
  anything." — the `in` form mis-parses and blames the wrong object.
  Always use the bare form until fixed.
- Capacity: untested beyond 1–2 items (used for food storage all
  session: `get loaf from bag` / `eat loaf` worked).
- Quirk: inventory shows "a small bag ..it is emitting light!" when it
  holds the lit oil lamp — the lamp shines from inside the bag.

## Scrolls: scroll of recall (tested 2026-10-02, session 30)

The 30gc scroll of recall is **unusable by SinMuseBot**:

- `recite scroll` → "Recite on what?"
- `recite scroll of recall` → "You do not know the first thing about
  reading a magic scroll."
- Not consumed; still carried. The character lacks whatever skill
  scroll-reading requires, and the game gives no hint what that is.
- Filed as [issue 012](issues/012-scroll-of-recall-unusable.md).
- Standing rule: do NOT buy scrolls until the requirement is known.

## Learning skills: `learn` (tested 2026-10-02, session 31)

Skills are taught player-to-player; there are no trainers and no gold
cost. The teacher must know the skill (immortals know every skill at
100%). The flow:

1. Student `follow`s the teacher (keep following — learning may not
   work otherwise).
2. Teacher types `apprentice <student>`, then `teach <student> <skill>`.
3. Student types `learn <N> <skill>` — each point costs one practice.
   From an immortal teacher each point gains ~3.5% (rolls 1–7%).

Mechanics learned the hard way:

- **Parent skills first:** a skill cannot be practiced while its parent
  is at 0% (martialism → weapon skills/kick; catechism → cure light /
  word of recall / create food).
- **Multi-word skill names need quotes:** `learn 4 word_of_recall`
  fails; `learn 4 "word of recall"` works.
- **`practice <skill>`** shows the qualifiers, the computed maximum
  from stats, and the full child-skill tree with current values —
  e.g. `practice martialism` printed `MARTIALISM [65/66]` and every
  child at `[00/65]`. Read this before spending.
- **Caps:** each skill has a stat-derived maximum (martialism capped at
  66 for SinMuseBot: `(50%x76str+30%x57dex+20%x57con) = 66`). Spending
  past the cap is wasted — `learn` stops at 65/66.
- **Weapon skills must match the wielded weapon:** slashes needs a
  slashing weapon. SinMuseBot's mace matched nothing, so Sin ordered a
  bronze short sword (9gc) to go with the slashes training.
- **`help <skill>`** documents every skill and spell (`help kick`,
  `help cure light wounds` — full name, no quotes needed).
