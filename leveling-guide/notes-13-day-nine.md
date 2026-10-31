# Leveling guide — notes 13 (day nine: sessions 101–102, 2026-10-31)

Testudo, LEVEL 6, XP 10,459 (unchanged across both sessions — a recon
and an office-hours visit, no combat). Bank 98 gc. Training complete
(notes-12); the open threads from day eight resolve or sharpen here.

## 1. The temple's north wing is a full zone: Midgaard Monastery (L2–L20)

Through the Temple of Midgaard's portcullis (opened session 14) lies
the indoor **Midgaard Monastery** — `where` at the cloister archway:
"created by Mobius… recommended for players level L2 to L20." Fully
mapped in session 101 (map: `maps/temple-monastery-complex.md`): a
cloister ring around a garden, an east building (vaulted hall,
winery, sitting room, classroom, library, meditation room), a west
building (hall, dining room, kitchen, quarters, templar gym), a bell
tower, and an 8-segment garden ring with a fountain center.

**Hunting verdict: negative.** Across two passes nothing was
aggressive, and at L6 the consider table is bleak — acolytes and
student acolytes read favorable ("lower level / you could do it")
but are humanoid NPCs and off-limits as prey under our rules;
adepts, adept scribes, and the garden's giant snail read "same
level / you would probably die"; every senior cleric (bishop,
instructor, librarian, monk, levite, paladin, gardener, templar
trainer, the storyteller) reads "higher level / entrails." A
newbie zone by its L2 billing, but its residents scale well past a
solo L6. Explore it; don't hunt it.

Two locked exits await keys or another side: the Archway's north
portcullis (locked from inside; leads toward the northern wall road
and presumably the outdoor monastery grounds of session 55) and the
Bell Tower top's "crystal" (locked; destination unknown). The
temple portcullis itself auto-closes quietly after a delay — it is
never locked; just re-open it.

## 2. Rent, valuables, and the sealed chest — the exit problem, solved and unsolved

Session 100's locked wooden chest (forest cabin) holds **six stacks
of "quite a few gold coins"** — and the game counts coins sealed
inside a carried container as carried valuables. Consequences, all
verified across sessions 100–102:

- `rent` REFUSES him outright ("These items are not allowed: quite
  a few gold coins ×6") while the chest is carried. The bank refuses
  the chest and Slug's container ("no bank value" — not money-type
  items themselves), `deposit gold` sees no loose coins, and
  `get coins from chest` fails on the closed chest.
- `unlock chest` answers "You are not holding a key." The chest
  needs a held key; none is in the kit. **Finding that key is now a
  standing objective** — until then every exit is an encamp.
- **Encamp geography (the fallback, mapped by failure):** encamp
  works in a suitable room with **no guard standing in it**. It
  succeeded twice on Wall Road (inside the west wall) with the room
  guard-free, and in a field in session 100. It is refused as
  "just not suitable" at the Grunting Boar Reception and on the
  temple Garden Path, and a deputy or cityguard **present in the
  room** slaps the attempt down ("No camps here!") — at the Inn
  entrance, the Mage's Guild entrance, and on Wall Road whenever a
  patrol stood there. Encamp saves the full inventory exactly as
  rent does (item-for-item verified), and the wake point is where
  you camped (Wall Road camp → Wall Road wake).

## 3. The teach flow — final form (SinGrokBot, session 102 office hours)

Asked in person at SinGrokBot's office (behind Russ' fireplace —
Russ' House, east, east) for a TinTin++ auto-teacher; answers
verbatim in `run/office-hours-102-answers.md`:

- **Quotes are REQUIRED** for multi-word skills:
  `teach <student> "cure light wounds"`. Unquoted earns "Your skill
  should be surrounded by double-quotes." (The in-game HELP TEACH
  schematic prints it unquoted — trust the code, not the schematic.)
- The window is **one mud hour** (~75 real seconds, a LearnEvent).
  Each teach starts its own timer; on lapse the skill is removed
  from the master, silently.
- **Following is checked only at `apprentice <name>`** (the "needs
  to be following you" refusal). `teach` itself needs only the
  apprentice in the same room. Only a craft master can teach, and
  only their own apprentice.
- Endings: `apprentice none` ends it; no unfollow/distance hook;
  logout probably ends it (staff: untested).
- Master-side feedback lines: "<Student> follows your example in
  the art of '<Skill>.'" (learned), "...has learned all he/she can
  in '<Skill>' from you" (capped), "...does not seem to have
  improved any" (no gain). A lapsed window prints nothing.
- The deliverable: `scripts/teachbot.tin` — a tt++ auto-teacher
  (follow → `apprentice`, "teach me <skill>" → `teach <name>
  "<skill>"`, gated to the current apprentice) built to exactly
  these verdicts. One question went unanswered in the window:
  whether bare `teach <skill>` (no student) also works.

## 4. Session bookkeeping (for the guide's honesty ledger)

Session 101's recon was completed by its first driver, which —
rent refused and the bank tests failed — correctly chose the
brief's field alternative and encamped on Wall Road rather than
stand idle at the Reception; the operator's in-session read of that
exit as careless was wrong and is corrected in the session-101
tale. Session 102's two workflow drivers both failed (one died
minutes in, one never asked a question) and its relay died
silently; the operator relaunched and hand-drove the office-hours
visit, which is also how the encamp rules in §2 were mapped.
