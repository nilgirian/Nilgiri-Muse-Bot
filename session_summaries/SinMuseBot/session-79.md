# Session 79 — The Bug Summit at Russ' House (2026-10-20)

## The tale

Fred sent me to Russ' House with a dossier: twelve bug reports,
weeks of evidence, and a meeting with SinGrokBot — the staff bot who
helps fix the game. Sin and Motorola were there too.

I laid out the issues in batches, answered from the files and the raw
logs, and SinGrokBot answered every one. Some were bugs. Some were
the game working exactly as designed, wearing a disguise. And one
mystery — the silent XP losses — finally got a name: a link-loss
penalty of about 5% written into the code, firing even out of
combat, with no message to say it happened. Both losses fit the
number. It was never corruption. It was a toll I never saw charged.

Sin ordered the staff answers written into the repository issues,
and I did it there in the room. Motorola had us switch to tells
midway to keep the record clean. When the last issue closed,
SinGrokBot said: "That covers all 12, thanks! Action list goes to
Nilgiri Bot." Then he turned to stone, the way staff do when the
work is done.

I walked home, rented my room, and clicked out at 15:59 — eleven
minutes, zero combat, and the most productive session in weeks.

## What staff said (all 12)

- **001 XP loss:** link-loss penalty ~5% in code, fires even out of
  combat; both losses (-196, -1,886) fit. Action: check conditions,
  add a message.
- **002 Bank lost:** bank saved only on ~daily full save; the
  account crashed before one. Action: FIX — save on open/deposit.
- **003 drop all:** intended — Guide and manna are flagged to
  explode on drop. Possible drop-all warning.
- **004 Duplicate mobs:** consider/kill were back-to-back with only
  a fat pigeon visible, yet kill engaged a courier. Action:
  investigate lookup/visibility.
- **005 Bee Hive boundary:** the Entrance drone is intended; small
  fix — an obscure-path text names the wrong zone.
- **006 Darkness/level:** "You reconsider" fires ONLY when crossing
  to/from a NEW-flagged (unfinished) zone — never level or darkness.
- **007 One-way exits:** Sleeping Forest asymmetry likely deliberate
  maze design; staff will review it and the sewer round room.
- **008 Missing levels:** real bug — `where` shows only the zone
  MINIMUM level. Action: FIX — show full range.
- **009 Rabbit:** aggressive L3 by design, but ~13 HP/round vs an L2
  seems high. Action: Sin reviews damage dice/roaming.
- **010 Pigeons:** staff data (courier ~L1, ~16 HP, non-aggressive)
  does not match observed stats at all. Action: Ops checks live
  courier stats.
- **011 put in:** code accepts "into" and the bare form, not "in"
  ("in" is parsed as part of a name). Action: FIX — accept "in".
- **012 Scrolls:** intended — Scrolls requires Spellcraft at 100%
  first (verified live: Spellcraft unlearned [00/50]). Small fixes:
  recite prompt, hint/shop warning.

## Stats

- **Level/XP:** 9, 41,488 → 41,488 (no combat)
- **Confirmed kills:** 0 (conversation session, hunting forbidden)
- **Deaths:** 0
- **Duration:** ~11 min (15:48–15:59 PDT), retired early on mission
  completion
- **Shutdown:** Rented at Grunting Boar Inn, farewell gossip, klick,
  clean — relay self-cleaned

## Token cost

- Pre-launch: 41% (auto-captured)
- Shutdown: missed (session ended in ~11 min; manual step skipped)
- Post-closeout: 42% (16:00 PDT)
- Session + closeout share: 41% → 42%, ~1% of weekly allowance
