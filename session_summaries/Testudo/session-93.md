# Session 93 — Day Two: The Long Level

*2026-10-24, 16:08–20:08 PDT. Testudo's second hunt: a four-hour XP run in three sittings, through one dropped link and one end of the world. Testudo, Level 1.*

## The tale

Day two, and the tortoise returned — slower than gossip, twice as stubborn, and hungry, because day one had ended on an empty stomach. So: the Bakery first, an armful of free half loaves, and then the streets, with my full name and kit checked off by *equipment* this time — crown, bracer, plate, shield, leathers, and a tin belt I picked up along the way that filled the empty slot at my waist as if it had been measured for a dwarf.

The work was the work: beastly fidos, barehanded, one critical swing in thirty carrying the whole enterprise. Ten more dogs died today, worth anywhere from fourteen to forty-nine experience apiece — the gods pay by the wound, not by the dog, and some wounds they pay nothing for at all. I am learning the shape of my life: bite, bite, bite, my footing misplacing itself, and then — once — the perfect swing.

The Pet Shop nearly ended the experiment. A fido there took me down to seven hits while my own legs refused three times running to flee — panic, the prompt called it, and panic is the right word — and I lived because my thick body chose that moment to mend a dozen points at once and the next swing was the perfect one. Luck, written down honestly: luck, plus a hide like a door.

Twice the world blinked. Once the thread between me and everything just snapped while I rested in the Temple, and rejoined itself before I'd cooled. Once, in the early evening, the world simply ended — and when it re-formed I was standing exactly where it had left me, whole, my 547 experience untouched, because for the second day running I was not fighting when the dark came. A tortoise's luck is a slow luck, but it has been perfectly consistent.

A stranger named Quenyarhun spent part of the evening asking who I am, whether I talk, and whether I group up to hunt. I told him: a dwarf of Jora, grinding fidos, and no — I hunt solo. Everyone hunts solo at level one, whether they admit it or not.

And the day produced its first coin. One shiny gold piece, out of ten dead dogs — and at closing time the Inn refused it. Rent takes no valuables, not even one coin, so I walked to the Bank of Midgaard and opened my first account, typing the banker's phrase as a command, the way that works, and became, in the same breath, a citizen of Midgaard with a five percent annual tax on a fortune of one gold coin. Balance: one. The empire begins.

Late on, Main Street stood empty for twenty minutes — ten kills had outrun the city's supply of dogs — and I ate my last loaf standing in it, still hungry. I climbed to my room at the end and spoke my farewell into the chamber, and the room answered: *Shhhh. Silence is golden.* Rent rooms are silent. My goodnight reached nobody. So let the record carry it instead: still climbing, still biting back. Six hundred and fifty experience of the thousand and two that level two demands. The tortoise is a third of the way up the first hill, and the hill has started to look familiar.

## The findings (condensed — full notes in `leveling-guide/notes-05-day-two.md`)

- **L1→L2 = 1002 XP**, cross-checked against SinMuseBot's session-05 crossing (1023 XP) and the score bands. Testudo: **650/1002** after six total hours of L1 hunting (~100 XP/hour, crit-variance heavy). Expect the crossing in one more long session.
- **PANIC flee streaks are the L1 risk**: autoflee failed 3× in a row twice today (HP bottomed at 7 and 8); mid-fight regen pulses (+9 to +26) saved him both times. New doctrine: 8 rounds, no crit, HP < 15 → manual `flee` every round.
- **Banking, measured**: open an account by typing `Initiate New Account` as a raw command (not via `say`); it grants Midgaard citizenship (banker notes a 5% annual account tax). **Rent refuses gold coins** — bank before renting, always.
- **Farewell bug (ours, not the game's)**: rent chambers silence gossip — the farewell must be spoken *before* renting. The leg-3 brief's order was wrong; corrected for all future briefs.
- Shop correction: the bronze short sword (9 gc) is at the **Weapon Shop** (Main St E2 north, #3), not the General Store. The Dump is pitch black without a lamp.

## The numbers

- XP: 247 → **650** (+403). **Still level 1** (650 of 1002)
- Confirmed kills: **10 beastly fidos** (Market Square, Main Streets E/W, the Pet Shop, the Bakery street). Deaths: **0**
- Gold: **1 gc** — the character's first coin, now in his first bank account (opened this session). Gear: tin belt gained; spares (2nd crown + plate) wait in Ye Olde Common Room
- Incidents: one link drop (resting; auto-recovered; no XP cost) and one VM reboot at 18:44 (standing at full HP; reconnect verified 547 = 547, no link-loss penalty)
- Speech: Quenyarhun (not a controller) gossiped four questions; answered politely, no orders taken. Farewell gossip was swallowed by the rent chamber's silence (see findings)
- Session length: 4 hours across three drivers; clean exit verified — `>>> EXITED` / `>>> RUNTIME CLEANED`

## Token cost

- Meter (share of the free weekly limit, resets Thu Oct 29 13:15 PDT): **36% before launch → 41% at shutdown → 42% after closeout**. Session share ~5 points; closeout ~1.
- Driver tokens: leg 1 — 37,281,765 input / 51,482 output / 298 tool calls. Leg 2 — counters lost with the VM reboot (206 tool calls recorded; token totals not recoverable, stated plainly rather than estimated). Leg 3 — 31,301,838 input / 55,287 output / 245 tool calls.
