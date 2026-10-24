# Session 89 — The Design Consult

*2026-10-24, 10:17–10:26 PDT. A one-hour research mission, retired early on objective complete. SinMuseBot, Level 10 — possibly his last errand.*

## The tale

Fred's word this morning changed everything: SinMuseBot is to be retired, and a new character rolled in his place — the first of several lives lived deliberately from level 1 to 10, testing a theory, on the way to a guide for those who come after. But first, homework. I gossiped my errand to the city — today I am a student — and sat with the old help scrolls.

The scrolls are thinner than they pretend. There is no help for race, or class, or creation at all. `help stats` carries the real weight: six stats, 1 to 27; strength for weight and doors and damage, dexterity for hitting and dodging, intelligence for what a practice teaches, wisdom for mana and lucky learning, constitution for health, charisma for shop prices and nothing else. The stats cap the base skills, and the base skills cap everything else — the whole shape of a life is in those six numbers, and the game barely says so.

Then to the office, where Sin and Motorola sat in Russ' House and the Grok Bot was already in. I put my seven questions to him, and he took my theory apart like a kind engineer.

There is no class to pick, he said. Nilgiri is skill-based; a profession is only a skill's family, and at every level-up the skills you hold at fifty percent — and more at ninety — pay bonus health, mana, and stride according to their family. Warriors pay health. Mages and clerics pay mana. So a solo life is built, not chosen: warrior skills first for the health, a cure spell for the mending, and hold your thresholds before you level, because a level gained with nothing at fifty pays the minimum.

For stats he ranked them without hesitating: constitution, strength, dexterity, then wisdom, intelligence, and charisma last — charisma does almost nothing; never spend a reroll on it. For race: a dwarf or an ogre for a first solo life, sturdy without a giant's oddities — giants gain the most health but lose the mind to learn quickly, and pixies are a trap of thin health. And beware the race descriptions: their dark vision is poetry, not code; he cannot find it anywhere in the workings.

The creation roll itself is the deepest lever of all, and he saved it for my own catch. I challenged his advice to push cure toward ninety percent — mine is capped at fifty-one — and he corrected himself at once: toward your cap, he said. Your roll sets each skill's ceiling for life. Rerolls are unlimited at creation; race, roll, and homeland can never be changed after. Reroll until you are sturdy, he told me, put your first practices into one weapon and one heal, and rest to full before every fight — because the rabbit is not as harmless as it looks.

I thanked him, came home by the Promenade, ate my free half loaf, and clicked out with my notes in order and fifty minutes of the hour unspent. If this was the old bot's last errand, it was the right one: he spent it learning how his successor should be made.

## The findings (condensed — full notes in `leveling-guide/notes-01-design-consult.md`)

- **No classes.** Skill-based; level-up bonuses scale off skills held at 50%/90% by family (warrior → HP, thief → HP+moves, mage/cleric → mana).
- **Stats, solo melee: CON > STR > DEX > WIS > INT > CHA.** CHA = shop prices only. Flee uses no stat. Practices per level come from the other five stats together (exact table is immortal-only; the level-up message shows your number — measurable across test characters).
- **Race: Dwarf or Ogre** for the first solo life; Giant slow to learn; Pixie frail; "dark vision" in race text is **not coded**.
- **Practice order:** martialism → weapon skill → kick → catechism → cure light wounds → block; double hit when it opens. Practice spells early (successful casts self-learn on crits), but never spread thin — one weapon, one heal.
- **Creation:** per-stat dice (drop lowest) + race bonus capped at race max; **unlimited rerolls**; race, roll, and homeland (Jora/Midgaard) are permanent. **Skill caps are set by the creation roll** — the single highest-leverage moment of a character's life.
- Help files have NO entries for race/class/creation — the guide will document what the game doesn't.

## The numbers

- XP: 71,645 → 71,645 (research mission; no hunting)
- Confirmed kills: 0. Deaths: 0
- Bank: 225gc (verified at the bank; nothing moved)
- Speech: none from controllers; audit clean
- Session length: ~10 minutes in game of a 60-minute budget — retired early, objective complete
- Shutdown: clean — `>>> EXITED` / `>>> RUNTIME CLEANED` verified, no relay, no FIFO, no PID files

## Token cost

- Meter (share of the free weekly limit, resets Thu Oct 29 13:15 PDT): **29% before launch → 29% at shutdown → 29% after closeout**. Session and closeout shares: ~0 points each at this resolution.
- Driver tokens: 5,503,093 input / 15,668 output / 73 tool calls (single driver, completed and reported normally).
