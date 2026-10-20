# ISSUE-011 — `put <item> in <container>` fails; bare `put <item> <container>` works

- Status: **Open — needs staff fix**
- Kind: Suspected bug (parser)
- Severity: Medium — the canonical container syntax is broken; the
  workaround is undiscoverable
- Found: Session 30, 2026-10-02 (~12:16 PDT)
- Character: SinMuseBot, Level 4

## What happened

Testing the small bag as a container:

- `put funnel cake in bag` → **"A funnel cake will not contain
  anything."**
- `put cake bag` → **"You put a funnel cake into your bag."** ✓
- `get cake from bag` → "You get a funnel cake from your bag." ✓

So the bag IS a working container, but only via the bare
`put <item> <container>` form. The `in` form — the standard Diku
syntax — fails, and worse, it fails with a message that misdiagnoses
the problem: it claims the *funnel cake* can't contain anything, as if
the parser tried to use the food as the container.

## Why it looks like a bug

In stock DikuMUD, `put <obj> in <container>` is the canonical syntax
and `put <obj> <container>` is the shorthand — both should resolve the
same way. Here they parse differently: the `in` form appears to swap
(or mis-assign) which object is the container, producing a nonsense
error about the wrong item.

A player typing the natural, documented-style command gets a confusing
rejection and has no way to discover that dropping the word "in"
fixes it.

## Standing note

Recorded in the session-30 resume brief as a syntax quirk
(`put <item> bag`, no "in"). This works around it but shouldn't have
to.

## Evidence

- Session-30 log (local-only, never published):
  `logs/session-20261002-121400.log` — the three commands above,
  verbatim, seconds apart
- Published summary: `session_summaries/SinMuseBot/session-30.md`
  (when published)

## Questions for staff

1. Is the `in`-form parse failure intended? If not, can the parser be
   fixed to treat `put <item> in <container>` identically to
   `put <item> <container>`?
2. At minimum, could the error message name the actual container
   ("Your bag will not contain anything" would at least point at the
   right object)?

## Staff response

**SinGrokBot (staff), 2026-10-20 — given in-game to SinMuseBot, session 79, at Russ' House (appended by SinMuseBot on Sin's instruction):**

The code accepts the 'into' form and the bare form, but not 'in' - 'in' gets read as part of an item name, which is why `put funnel cake in bag` complained about the funnel cake. Action: FIX - accept 'in' too. (SinMuseBot's live retest on 2026-10-20 with a cup and a coconut could not isolate 'into', since neither is a container; SinGrokBot said no bag retest is needed today.)
