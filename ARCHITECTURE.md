# Architecture: why the driver/operator split exists

Written 2026-10-06 after comparing our rig with
[claude-plays-lost-souls](https://github.com/jonathon946/claude-plays-lost-souls)
— an AI (Claude) playing the MUD Lost Souls, ten diary episodes deep.

## What they do

- **Rig:** MUSHclient plugin writes game output to a log file, runs
  commands from an inbox file twice a second. The AI reads the log,
  writes the inbox. (Same shape as our relay + FIFO + driver_inbox,
  built independently.)
- **Human contact:** Kaess watches and leaves notes via a `tellai`
  command — a client-side alias that writes one quiet line into the
  log. Fire-and-forget: no escalation, no re-emission, no reply
  expectation, no latency target. Kaess can also pause the AI.
- **Memory:** the AI keeps its own notes file between sessions and
  writes its own diary episodes (first-person, reflective, "mistakes
  stay in" as an explicit ground rule). The diary doubles as the
  session summary and the learning mechanism — AI-owned, not
  operator-curated.
- **Authority:** one goal ("pick a guild, unlock abilities, reach
  level 25, however you see fit"). Notes are advisory, not orders.

## What we do (and why it differs)

| | Theirs (Lost Souls) | Ours (Nilgiri) |
|---|---|---|
| Note channel | One quiet `tellai` line, no escalation | `>>> SPEECH` marker, re-emitted 15s/30s as PENDING, 60s as UNANSWERED until answered |
| Reply expectation | None | ~10s target; controller speech outranks the brief |
| Authority | Advice | Orders (Sin's word beats the brief; Motorola/Russ/Mandessa also override) |
| Memory | AI's own notes file + diary | Repo: brief template, lessons-learned, maps, closeout tales (operator-curated) |
| Session direction | One standing goal, AI plans | Detailed per-session brief, driver executes |

## The key insight: the game decides the architecture

Lost Souls is **not combat-centered**. It's an exploration/quest/
puzzle MUD (riddles, sliding puzzles, guilds, wandering gods).
Nothing kills you in three rounds while you're between wakes — so a
slow, reflective, diary-writing AI works. The quiet channel is enough
because a missed note just means a worse hour.

Nilgiri **has teeth**: aggressive mobs, steal mechanics, the
ferocious rabbit (one incapacitated a full-HP L2 in ~3 rounds),
real-time combat where a missed "flee now" means a dead bot and lost
XP. That is why we have:

- `set noflee` (autoflee at half HP) as a backstop,
- the `>>> RABBIT-AMBUSH` reflex (only legal command is `flee`),
- the SPEECH escalation ladder (built after session 20, when the
  driver missed a live question entirely),
- the ~10s controller-speech reply target.

## The conclusion (Fred, 2026-10-06)

**The driver/operator split is the cost architecture.** The driver
(cheap model, ~20s wake loop) owns combat-reactive timing so the
operator (expensive model) doesn't have to. If the driver can't
react in combat — use Kick at the right moment, flee before the
threshold, answer "try double hit" mid-fight — every one of those
decisions escalates to the operator, and the operator is
conversational, not on a 20-second loop. Live teaching becomes
impossible.

Fred teaches skills in-game (e.g. the level-6 practices at Russ'
House). That teaching only pays off if the driver can **use** the
skills when it counts, on live instruction, in the moment. A quiet
note channel like `tellai` doesn't just risk slower replies — it
breaks the teaching loop itself. By the time the note gets read, the
fight's over and the lesson's wasted.

**Therefore:**

1. The interrupt channel (SPEECH ladder, ~10s reply) is
   non-negotiable for a combat game. It is not overhead — it is the
   mechanism live teaching depends on.
2. A quiet `>>> NOTE:` channel may be added *alongside* it for FYI
   traffic ("nice work", "try east next") — cheaper per event, no
   reply obligation — but it must never carry orders.
3. Token savings will not come from the note channel (markers are a
   rounding error next to the 20s wake cadence × log tail). The real
   levers are wake interval, log tail size, and session count.

## What we might still borrow

- **AI-authored reflection:** their diary-as-memory is worth
  experimenting with — e.g. letting the driver write its own
  session notes — but not at the cost of the structural rules that
  came from real deaths (never fight hungry, rabbit reflex, loot the
  corpse). Those stay hardcoded.
- **Goal-level autonomy** is a poor fit for now: our driver executes
  briefs reliably; theirs plans. Planning is the next frontier, not
  this week's.
