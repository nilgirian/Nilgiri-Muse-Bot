# Session 21 — SinMuseBot, 8th VM reboot + first death

**Real time:** 2026-09-29, 13:20 → ~13:54 PDT (~34 min of the 120-min
budget). Killed by **VM reboot #8** mid-fight. Watchdog fired and paged
Fred; Fred supplied the password in ~1 min and session 21b relaunched
~14:04.

## What happened

- Logged straight back in at the Grunting Boar Reception (20d's clean
  retirement). Verified state: L4, 3960 XP, full tin, bank 8gc.
- Early kills: pigeon, mouse, cricket (+40 → 4000 XP).
- **First death (~13:3x): courier pigeon in Market Square.** `consider`
  said "lower level / easy battle". The driver went incapacitated →
  mortally wounded; "Sorry, you are dead." Respawned at the Temple,
  3581 XP (**-419 XP**). Re-entered via the death menu (walked
  automatically or manually — unclear from the log).
- Sin gossipped live: "SinMuseBot, what were you fighting before you
  died?" and "were you at full hp when you attacked it?" — driver
  answered both ("A courier pigeon in Market Square... it hit much
  harder than its consider rating suggested" / "Yes, 54 of 54. It still
  beat me down."). Motorola's tease ("you're a full grown man fighting
  a tiny pigeon") went unanswered (nag fired, no reply sent).
- Recovered, re-equipped, went to the Hills. Engaged a **large elk** in
  "Field (field)": `consider` said "lower level than you / you think
  you could do it" — it LIED. The elk dealt "very hard" → "extremely
  hard", took a full-HP full-tin L4 to incapacitated then mortally
  wounded in ~75s.
- Sin gossipped "did you attempt to flee?" — driver answered ("Yes,
  but it said the pain was too great to flee").
- **VM reboot #8 hit (~13:54) while mortally wounded.** Nobody could
  aid; the character died link-dead. Corpse with the full tin set
  (crown, chest plate, belt, boots), 2 oil lamps, Nilgiri Guide in the
  Hills "Field (field)". XP at death 3605 → respawn 3233 (**-372 XP**).

## Lessons (verified from the log)

- **Death costs XP** — 419 and 372 lost this session (~400 per death).
  The brief's "death should not cost XP" assumption was wrong.
- **"The weapon feels unwieldy" is NOT the anomaly.** It appeared 40x
  in the clean 9-kill session 20d and 27x here — a normal miss message,
  not a debuff.
- **The XP reward is the tell.** The pigeon paid 89 XP (vs ~16 for a
  fido) — ~5x the XP means ~5x the danger, whatever `consider` says.
- `consider` compares LEVELS, not damage dice. Elk and pigeon are both
  low-level mobs with brutal damage tables.
