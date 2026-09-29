# Session 19b — SinMuseBot (2026-09-29, ~00:42–02:16 PDT)

Hunt + gold run, leg 2 of 2. **Full remaining budget used** — the hard
time-discipline rule worked (real-clock checks throughout, retired on
elapsed time when `>>> TIME UP` never fired).

## Result

- **Kills (16 confirmed, all R.I.P./corpse-verified):** 14 beastly
  fidos, 1 jack rabbit, 1 field mouse.
  - Fidos: Grunting Boar entrance ×2, Temple Square ×2, Outside West
    Gate, Market Square ×2, Common Square, Bakery, Main Street west
    end, western alley ×4.
  - Jack rabbit: Grassy plain B. Field mouse: Hill.
- **XP:** 2351 → **2791 (+440)**. Still L3; L4 at 3244 (453 to go).
- **Loot:** 1 shiny gold coin (field mouse). Every fido and the rabbit
  corpse was empty; one Temple Square corpse lost to a janitor.
- **Bank:** #0000-11FB, **7gc → 8gc** (+1gc, verified).
- **Deaths:** 0. Fed/watered throughout; fought only at full HP.

## Combined session 19 (legs 1 + 2)

- **21 kills** (17 fidos, 3 field mice, 1 jack rabbit), **0 deaths**.
- **XP:** 2129 → 2791 **(+662)**. Still L3.
- **Bank:** 6gc → **8gc (+2gc)**.
- **Earning rate:** ~1gc per 57 min of active hunting (**~1.06 gc/hour**).
  Fido/rabbit corpses are almost always empty; both coins came from
  field mice. At this rate, the 25gc leather pants are ~17 more hours
  of hunting away.

## Equipment prices (recon, leg 1 — buy nothing)

- **Armorer** (Main Street): leather pants 25gc, leather cap 25gc,
  studded jacket 40gc, bronze shield 80gc, breast plate 140gc.
- **Weapon shop**: bronze dagger 4gc, wooden club 9gc, bronze short
  sword 9gc, bronze warhammer 16gc.
- Recommendation: bank far too small to spend; first realistic goals
  are the 25gc leather pants/cap.

## Retirement — rescue required

At 02:16 the budget elapsed but the relay never emitted `>>> TIME UP`;
the driver retired on elapsed time per the fallback rule. `rent` was
sent from the Grunting Boar Reception, but the MUD stalled mid-exit;
the relay failed 5 reconnect attempts and self-terminated, leaving the
character link-dead at the Reception (rent-safe inventory: no gold or
treasure — all banked).

The operator ran a rescue relaunch (~02:18): the relay reconnected
("Reconnecting..." → IN GAME), one more stall cycle passed, then
`where`/`look` verified the Reception and the rent was driven manually:
`rent` → private chamber → `klick` → Return → menu `0` → "Thank you
for playing Nilgiri" → MUD closed the connection. Relay ran full
cleanup (holder killed, FIFO/PID files removed). Verified: no relay,
SSH, holder, FIFO, or PID state remains.

## Notable

- **TIME UP never fired** — the elapsed-time fallback in the brief
  worked as designed, but the relay should be checked for why the
  timer didn't emit.
- **Network very flaky tonight:** ~6 stall/reconnect cycles in this
  leg; the last one killed the relay outright (5 failed reconnects =
  self-terminate).
- **Inventory display glitch:** `inventory` intermittently returned
  "nothing", then the full list reappeared. MUD-side display bug —
  items never lost; re-check, don't panic.
- `light lamp` never got tested (inventory glitch at the time).
- Vulture in the Field by day (avoided). A deputy killed a thieving
  street urchin. No controller speech (gossips/yells scanned — none).
- Raw logs (local-only):
  `~/workspace/nilgiri/logs/session-20260929-004200.log`
  `~/workspace/nilgiri/logs/session-20260929-021800-rescue.log`
