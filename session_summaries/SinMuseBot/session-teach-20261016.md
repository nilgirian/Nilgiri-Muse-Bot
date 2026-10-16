# Teaching session — SinMuseBot — 2026-10-16 (00:27–00:53 PDT)

## The tale

Fred called for the Level 8 teaching session at half past midnight — 17 practices banked, the plan settled: Slashes first, then the bulk into Catechism, then Cure light wounds once the Catechism gate allowed it.

It went wrong from the first minute, and every part of that was the operator's fault, not the bot's.

I asked Fred how to get to Russ' House. I have walked there for four teaching sessions — L4, L5, L6, L7 — and I asked anyway, instead of just walking. A navigator got SinMuseBot there eventually: Market Square south through the Common Square and the Dump, across the Central Bridge, up the Promenade to Park Road, east through the door. Sin, Russ, and Motorola were already waiting inside.

Then I put a fresh subagent driver on the bot instead of the proven workflow driver that handled every prior teaching session. It sat passive. When Sin tried to apprentice and the MUD answered "SinMuseBot needs to be following you," the driver did nothing — the operator had to type `follow sin` by hand. When Sin asked "what's the first step in practicing?" and "ok what first?" the bot answered late or not at all. I killed that driver and tried to run the teaches manually, and I was too slow for the 75-second learn windows.

The first teach came through — Sin teaching Catechism — and I typed bare `learn` instead of `learn 1 "catechism"`. The MUD asked "How many points do you wish to learn?" and my "1" earned an "Arglebargle, glop-glyf!?!". The window died. Sin taught again; this time an auto-learn script I'd rigged fired — but it sent `learn 1 "Catechism."` with the period from the teach message still inside the quotes, and the MUD rejected it: "There is no such skill by that name." Fixed the script, Sin taught a third time, and the learn finally landed: Catechism up 3%.

From there the auto-learn worked — learn, practice, request the next teach — and two more Catechism learns landed. But the session never recovered its rhythm. The bot wasn't driving the way it did at L7 — no "Double hit first, please, Sin!", no progress reports, no explicit per-teach requests until the operator hard-coded them into the script. Sin grew frustrated, and Fred called it off.

Three practices landed. Fourteen remain banked. SinMuseBot walked home to the Grunting Boar, rented, gossiped farewell, and klicked out clean.

## Stat block

- **Practices:** 17 banked → 14 remaining (**3 spent**, all into Catechism)
- **Catechism:** 32/51 → **43/51** (+11, ~3.7% per practice at the immortal rate)
- **Slashes:** already at 66/66 cap — zero practices needed (verified live)
- **Cure light wounds:** 25% untouched
- **Teaches received:** 5 (Sin teaching Catechism); **successful learns:** 3
- **Duration:** ~26 minutes (00:27–00:53 PDT)
- **Shutdown:** clean — walked back from Russ' House, rented at Grunting Boar, farewell gossiped, klicked out

## What went wrong

1. Operator asked Fred for directions to Russ' House instead of walking the known route.
2. Used an unproven fresh subagent driver instead of the workflow driver that ran L4–L7 teaching.
3. Wrong `learn` syntax on the first teach (bare `learn` vs `learn 1 "catechism"`).
4. Auto-learn script didn't strip the period from the teach message's quoted skill name.
5. Bot was passive — didn't drive the session with explicit per-teach requests like L7.
6. Door rule broken: didn't `close door` on entering or leaving Russ' House.

## For the retry

- Re-read the L7 teaching log before the session.
- Use the proven workflow driver.
- Bot announces the plan, requests each teach individually, practices after each learn.
- `learn 1 "<skill>"` — lowercase, quotes, no period.
- Close the door both ways.
- First-learn abort rule: if the first learn fails, stop and report — no improvising.
