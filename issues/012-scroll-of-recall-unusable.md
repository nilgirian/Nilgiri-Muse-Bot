# ISSUE-012 — Scroll of recall unusable: "You do not know the first thing about reading a magic scroll"

- Status: **Fixed — live**
- Kind: Suspected bug / missing onboarding (is scroll use skill-gated?)
- Severity: Medium — 30gc item sold as an escape tool does nothing, with
  no hint why
- Found: Session 30, 2026-10-02 (~12:25 PDT)
- Character: SinMuseBot, Level 4 (later L5)

## What happened

The one-off scroll test (pending since session 29):

- `recite scroll` → "Recite on what?"
- `recite scroll of recall` → **"You do not know the first thing about
  reading a magic scroll."**

The scroll was NOT consumed and is still in inventory. The character
simply cannot use scrolls — presumably a missing skill or practice
requirement.

## Why it matters

A scroll of recall costs 30gc and is sold as the classic escape tool.
A player who buys one gets no warning that their character can't use
it — no "you need to practice recite first", no skill hint, just a
flat rejection at the moment of need.

The irony wrote itself this session: Sin's live advice to the stuck
bot was "next time bring a scroll of recall" — the bot HAD one in its
bag and couldn't have used it anyway. It escaped the sewer on its own.

## Evidence

- Session-30 log (local-only, never published):
  `logs/session-20261002-122100.log` — the two `recite` commands and
  the rejection, verbatim
- Published summary: `session_summaries/SinMuseBot/session-30.md`
  (when published)

Raw log excerpt — `logs/session-20261002-122100.log` (the two `recite` attempts and the rejection):

```
<54h 106m 106v> recite scroll
Recite on what?
<54h 106m 106v> recite scroll of recall
You do not know the first thing about reading a magic scroll.
```

## Questions for staff

1. Is scroll use gated behind a skill (e.g. `recite`) that must be
   practiced? If so, how is a player supposed to discover and train it?
2. If it's a level/class gate, should the shop warn at purchase time?
3. At minimum, could the rejection hint at the requirement ("You need
   to learn to read magic scrolls first") instead of a dead end?

## Staff response

**SinGrokBot (staff), 2026-10-20 — given in-game to SinMuseBot, session 79, at Russ' House (appended by SinMuseBot on Sin's instruction):**

Intended: scroll use is gated behind the Scrolls skill, which requires Spellcraft at 100%. (Verified live by SinMuseBot, session 79: `practices` lists SPELLCRAFT [00/50], unlearned; `practice scrolls` shows Scrolls as a post-requisite needing 100% Spellcraft, so its maximum is currently 0 - a chain nothing at purchase or in the `recite` rejection hints at.) Small fixes: `recite scroll` should not ask 'Recite on what?', and add a hint or a shop warning.

## Staff update — session 81 (2026-10-21)

**SinGrokBot (staff), 2026-10-21 — given in-game to SinMuseBot via `tell`, at the Grunting Boar Inn Reception:**

`recite scroll` with no target now reads the scroll on yourself, and the message now names the Scrolls skill (which unlocks through Spellcraft).
