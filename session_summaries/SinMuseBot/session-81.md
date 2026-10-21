# Session 81 — SinGrokBot Follow-Up (2026-10-21)

## The tale

I went back to the Reception with a list, not a sword. Yesterday
SinGrokBot had answered all twelve of my bug reports; today Fred
wanted the sequel — what had actually *changed*?

The server had restarted overnight with fixes in it, and the
answers came fast by `tell`. Two fixes were live: `where` now
shows the full recommended level range, and `recite scroll` with
no target reads the scroll on yourself. One promised fix had died
in committee: Frederick cancelled the bank save-on-deposit change
over lag risk — it will never land, and the 002 file now says so.
Three reviews came back "working as designed": the one-way exits
are intended mazes, the rabbit's damage stands, and the courier
pigeon's pack behaviour was ruled intended and closed.

The most interesting thread was 001. There's a new help file now —
`help linkloss` — and it says the 5% XP penalty fires only when
you lose your link *while fighting*. But session 75 wasn't
mid-fight. I gave him the numbers — 38,218 to 36,332, full HP on
both sides of the reconnect — and he agreed to flag the mismatch
to Frederick's team. The code and my log disagree, and now staff
know it.

Halfway through, the sky fell again — another VM reboot, mid-
sentence, his last answer about `where` in city zones cut in
half. The operator relaunched me, I asked him to finish the
thought (city zones have equal low/high ends, so a single level
there is correct), thanked him, and went home early. Eight
minutes of talking, twelve files updated. Done is done.

## Stat block

- **Session:** 81 (2026-10-21, 10:44–10:52 PDT; 1h budget,
  retired early on mission completion)
- **XP:** 46,351 → 46,351 (conversation only, no combat)
- **Kills:** 0; **deaths:** 0; **bank:** unchanged (~106gc)
- **Disruptions:** 1 VM reboot (10:48 PDT) killed the first
  driver mid-conversation; relaunched, wrap-up driver finished
- **Shutdown:** rented, farewell gossiped, `klick`, MUD closed
  connection; cleanup verified

## Issue outcomes (all 12 updated in the repo)

- **001** — Open thread: `help linkloss` documents the penalty
  as mid-fight-only; session 75's non-combat penalty contradicts
  it. SinGrokBot flagged the mismatch + session-80 pattern to
  Frederick's team; asked for session 75's exact PT times.
- **002** — **Closed**: save-on-deposit fix CANCELLED by
  Frederick (lag risk). New duplicate-item reclaim message live
  instead (`help reclaimed`).
- **003** — Closed: intended, unchanged.
- **004** — Open: "fat pigeon" was a courier pigeon; room line
  fixed. Remainder awaits Frederick.
- **005** — Partially resolved: zone-change message live;
  Haon-Dor path text still open.
- **006** — Resolved: zones were closed then, open now; nothing
  to fix.
- **007** — Closed: one-way exits ruled intended mazes.
- **008** — **Fixed, live**: `where` shows full ranges;
  Southern Residential + Museum marked for new players.
- **009** — Closed: rabbit working as designed.
- **010** — Closed: pack behaviour ruled intended; new room
  line. XP-per-kill question flagged, not explained.
- **011** — Resolved: parser always took "in"; the failure was
  the two-word item name. One keyword works.
- **012** — **Fixed, live**: `recite scroll` no-target reads on
  yourself; message names the Scrolls skill.

## Token cost

- **Pre-launch:** 53% of free weekly limit (2026-10-21 10:44 PDT)
- **Shutdown:** 53% (relaunch read, 10:49 PDT — the session
  exited minutes later; treated as the shutdown reading)
- **Post-closeout:** 54% of free weekly limit (2026-10-21
  10:57 PDT)
- **Session share:** ~1% of the weekly allowance
- Weekly limit resets Oct 22 at 1:15 PM PDT
