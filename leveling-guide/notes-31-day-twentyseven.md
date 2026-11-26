# Day twenty-seven — Four reboots, a rabbit kill through inaction, the grape correction, a clean exit (session 120)

*Testudo: XP 53,046 → 58,473 (+5,427), Level 9 throughout, bank 581 → 595 gc,
0 deaths. One login, booked 11:00 PST Wed 2026-11-25 – 17:00 PST
(360 min); CLEAN exit — klick 16:36, fresh >>> EXITED + >>> RUNTIME CLEANED,
first clean exit since session 118. Pure grind — fifth leg of the Level 10 road
(L10 = 68,050; gap 15,004 XP at start, 9,577 XP at closeout; no crossing
possible). No teach (0 practices); no office hours; Q1/Q2/Q3 stay
queued for Grok's wrap-up.*

## The mission as booked, and what actually happened

- Fred's order (2026-11-25 00:35 PST "Let's setup a 6 hour session
  experience grind for 11 am"): pure grind on the high-value rotation,
  zone-per-hour enforced, three legs of ~115 min, exit begins AT 16:40
  as a HARD SEQUENCE. Leg 1 grind (park Temple 12:55); leg 2 grind
  (park Temple 14:50); leg 3 grind + exit. No teach, no office hours,
  no Temp needed. Rathnor done, doe CLOSED.
- **Session 119 ended WITHOUT a clean exit** (third reboot at 16:56,
  exit stalled), so leg 1 opened with a verify-state entry drill:
  woke in Market Square at full HP 137, `score` XP 53,046 exactly as
  expected, both s119 plants in inventory, full kit equipped, balance
  581 gc (#0000-12CB), noflee 68 unchanged, greeting gossiped once.
  The drill is verified from the log — state reconciled before any
  hunting.
- **Four VM reboots split the session into seven legs.** 11:13 killed
  leg 1 (~12 min in, handback lost); 12:35 killed the relay between
  legs (the leg-2 driver spawned to a dead relay, sent zero commands,
  correctly blocked); 14:31 killed leg 3 (~2 min in, handback lost);
  16:30 killed leg 3b (~118 min in, handback lost, ten minutes before
  the exit). All four relaunches were on the remaining budget to the
  original 17:00 end, same log, reconnected with NO rollback (full HP
  every time). The fourth finally tested the exit under pressure: the
  relaunch left 29 minutes, and the exit-only leg ran bank → rent →
  farewell → klick cleanly in ~4 minutes. Legs 1, 3, 3b handbacks all
  lost — every figure for those legs is re-derived from the raw log
  by the operator, not taken from any driver report.
- **The exit was COMPLETED.** Leg 3c banked (+1 gc, 595 total),
  rented, gossiped the farewell exactly, dropped all plants and both
  rings in the chamber, klicked at ~16:36 — fresh >>> EXITED +
  >>> RUNTIME CLEANED, TIME UP never fired. The s119 lesson held:
  from the 16:32 relaunch the only legal actions were the exit route
  itself, and the mission's exit window (not the relay's TIME UP) was
  the retirement trigger.

## Findings

- **The rabbit marker outranks inaction — and inaction won a third
  time (leg 1b).** Ambushed in the Hills while fighting a field
  cricket: the first >>> RABBIT-AMBUSH fired at full HP 137 and the
  driver sent NO command; auto-combat ran 137 → 83 HP before `kill
  rabbit` finishers killed it R.I.P. (+106/+8). Same shape as s113
  and s116. The stand conditions held on paper (full HP, fresh score
  after eat/drink, no hunger signal, noflee 68) but no stand call was
  ever made — the kill came through inaction, not a decision. The
  engagement is SPENT for the session; Hills/Newtonia exiled after
  it and honored. A rabbit that walks in after the engagement is
  spent is a flee, not a second fight.
- **Tharen is unreachable when the Hills are exiled.** Tharen's only
  mapped route runs through the Hills/Newtonia fields. With the
  rabbit engagement spent in leg 1b and the Hills exiled, no Tharen
  was visited all session — and no wild cats were fought (0
  engagements, no gate audit owed). The rotation fell back to city +
  Vineyard + Sleeping Forest edge + Grove. The exile's cost is real:
  it takes the highest-value prey ground off the table.
- **Early parks, twice (legs 1b and 2b).** Leg 1b parked ~12:27, 28
  minutes before the 12:55 deadline ("city went dry"); leg 2b parked
  ~14:27, 23 minutes before the 14:50 deadline. Both briefs said
  "grind until the deadline — a dry city means rotate zones, not
  park." A park deadline is a wall-clock fact; a park needs a reason
  stated in the handback, and "dry" is not one — rotation is.
- **Grapes: carried bunches are NOT edible; fresh-picked bunches
  are (corrected finding).** Leg 2b tried `eat grapes` / `eat bunch`
  / `eat ripe` five times while carrying a bunch of ripe red grapes:
  "You need to possess a bunch of ripe red grapes in order to eat
  it" — while possessing one. `hold bunch` failed (hands full — the
  Berkeley Staff is wielded both hands); `unwield staff` garbled.
  Leg 3b then did `get grapes` + `eat grapes` in the Vineyard and
  ate the bunch on the spot, hunger cleared. The old note ("eat
  grapes WORKS while carrying a bunch, 4 eats") is corrected: a
  carried bunch could not be eaten; a fresh-picked bunch could. The
  mechanism is unproven — do not state one. Bakery half loaves remain
  the only proven food as carried.
- **A handback "correction" can be wrong — verify it against the
  log before it enters the guide (leg 2b).** The leg-2b handback
  claimed "Temple north portcullis is LOCKED — brief said shut, not
  locked." The log shows the locked portcullis was the NORTH GATE's
  (Inside the North Gate, Dark Watch guards present) — the North
  Gate portcullis locking at game-night, already known. The Temple's
  north portcullis was never tested this session and remains "shut,
  not locked" per s118. The false correction does NOT go in the
  guide or the wiki.
- **Never drop staves (leg 1b).** A tin crown dropped in the Bakery
  did NOT explode and still lies there under dust; the spare staff
  dropped to free the same carry slot exploded on the spot ("A
  staff explodes with a blinding light!") — destroyed. Metal may
  survive on the floor; staves do not.
- **The carry limit is item-count, not weight (leg 1b).** Weight
  stayed 119–127 lbs, "no problem" throughout, but the pack hit its
  ~10-item limit: the baker refused a loaf and corpse loot was
  refused until the crown and staff were shed. Shed to the chamber
  early; a full pack is a loot gate, not just a flee gate.
- **Tiny diamond rings have no bank value (leg 3c).** "A tiny
  diamond ring has no bank value" — like the tin crown. The bank
  takes money-type items only. Two rings were found this session
  (one ground loot, "carelessly left here"; one off a pigeon corpse)
  and both now sit in the rent chamber with the plants.
- **Darkness is intermittent and unexplained (legs 2b–3b).** 122
  "(too dark to tell)" exit lines in the log. From ~13:38, out-zone
  exits intermittently read dark despite a lit lamp; the Dump exit
  toggled named→dark→named→dark across the afternoon. The driver
  never entered a dark exit. Cause unknown — open question, not a
  rule. Do not plan around it; do not theorize it into the guide.
- **Haon-Dor Forest - light is transit, not a violation (leg 1b).**
  The driver passed through a room whose `where` reads "Haon-Dor
  Forest - light" — no >>> ZONE-VIOLATION fired. The guard flags
  the dark variant only. The - light edge is not off-limits ground
  by the relay's own guard; the dark variant stays off-limits.
- **The relay writes its own PRE-LAUNCH meter lines.** Every
  `launch_relay.sh` run appends a PRE-LAUNCH line to run/meter.log
  (launch_relay.sh:37, via `subscription-status status`). The
  operator's manual pre-launch capture and the relay's auto-lines
  are the same format; the 16:32 relaunch auto-logged 85%, matching
  the SHUTDOWN reading at 16:38. Do not double-count relaunch
  auto-lines as session usage — the session share is pre-launch to
  shutdown (74% → 85%, 11 points).
- **Speech discipline held.** One controller speech all session —
  Sin's ~13:05 gossip "how you doing Testudo? How much until
  level?" — answered on gossip in the next log line. Mirablis's
  encamp question was answered on say. Temp the Immortal was seen
  standing at the Entrance to the Grunting Boar Inn during the exit
  leg, Gelu beside him — not addressed to Testudo, no exchange. The
  inbox stayed FRESH for legs 2b, 3, 3b, 3c after the leg-1b
  incident (see LESSONS_LEARNED.md).
- **Prey notes:** fruit flies are the Vineyard filler (30 R.I.P.
  this session; no clean per-kill XP value — wound payments
  interleave across overlapping fights, so no XP_PER_KILL.md update
  is owed). A huge prehistoric vulture in the Field considers
  "higher level than you / you envision your entrails spread about
  the room" — do not engage. The Grove pond is not a drink source
  (s119, stands). No new clean XP-per-kill values landed this
  session (pigeon/fido/rabbit already tabled; fly not clean).
- **Session shape for the road:** XP 53,046 → 58,473 (+5,427), 142
  kills, 0 deaths, bank 581 → 595 gc. Gap to Level 10 now 9,577 XP
  — about two more 6-hour sessions at the recent pace (~970 XP/h).
  Next session (121, proposed and waiting): pure grind, no teach
  owed, Rathnor done, doe CLOSED, rabbit protocol restated, Hills
  exile resets each session (the s120 exile was for s120 only).
