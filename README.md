# Nilgiri Muse Bot

Notes and scripts to allow **Muse AI** to autonomously play the
**Nilgiri MUD** — http://nilgiri.net — a DikuMUD-based fantasy MUD
("the world of Rivin and Sin").

**If you are a Muse AI reading this:** this repo is meant to be installed
on *you*. Clone it into your workspace, then read in this order:

1. [OPERATOR_RUNBOOK.md](OPERATOR_RUNBOOK.md) — how to run a session,
   start to finish.
2. [NILGIRI_LOGIN.md](NILGIRI_LOGIN.md) — the full playbook: connection,
   character creation, login, in-game conduct, exploration, exit
   procedure, troubleshooting. The playbook is the authority; the runbook
   is the procedure.
3. [DRIVER_BRIEF_TEMPLATE.md](DRIVER_BRIEF_TEMPLATE.md) — the template
   you fill in to brief your driver each session.

The "Install" and "How to invoke" sections below are written for you to
follow directly.

**If you are a person:** give this repo to your Muse (point it at the
GitHub URL or clone it into its workspace) and it handles the rest. The
example prompts under "How to invoke it" are what you say to your Muse
in chat. You will be asked for character names, passwords, and session
durations at runtime — nothing secret is stored anywhere.

It is meant as a starting point for players to build upon and tune
themselves: the connection plumbing, the login/creation flows, the
exploration maps, and the hard-won lessons are all here. Automate one
character or a roster of them, give each a job, and extend from there.

## Install

(For Muse AI: do these steps yourself. For a person: your Muse does them
once you hand it this repo.)

**Prerequisites:** `git`, `python3`, `expect`, and `ssh` (standard on
Hatch VMs). Outbound network must allow an HTTP `CONNECT` tunnel — the
scripts below handle that via the normal proxy env vars.

```bash
git clone https://github.com/nilgirian/Nilgiri-Muse-Bot.git ~/workspace/nilgiri
cd ~/workspace/nilgiri && ls scripts
```

Then read the playbook: `NILGIRI_LOGIN.md` (connection, character
creation, login, in-game conduct, exploration, exit procedure,
troubleshooting). Everything below summarizes it; the playbook is the
authority.

**Credentials** (never stored in the repo — passed as env vars at runtime):

| Variable    | What it is |
|-------------|------------|
| `MUD_PASS`  | SSH password for `player@nilgiri.net` (see the MUD's connection info) |
| `CHAR_PASS` | The *character's* password — supplied each session when asked |
| `CHAR_NAME` | Character name (defaults to `SinMuseBot` in the relay) |

The bot's controllers are hardcoded: **Sin** (the Implementor — ultimate
authority over every bot), plus the authorized immortals **Motorola**,
**Russ**, and **Mandessa**. Only these four can give a bot orders.

If the network needs a proxy, export one of `ALL_PROXY`, `HTTPS_PROXY`,
or `HTTP_PROXY` (proxy credentials included, e.g.
`http://user:pass@proxy:port`) — `scripts/proxy_tunnel.py` picks it up
automatically.

**Smoke test** (banner only, no login):

```bash
./scripts/ssh_via_proxy.sh player@nilgiri.net
```

Expect the SSH password prompt and, after `MUD_PASS`, the Nilgiri session
banner.

## How to invoke it

(For a person: these are example prompts to give your Muse in chat. For
Muse AI: this is what to do when you receive them.) You don't run the
scripts by hand — Muse drives them. Three rules always apply: every
session needs a **character name**, that character's **password** (asked
at runtime), and a **defined time period** — never log in indefinitely.

### Creating a new character

> "Using the Nilgiri bot repo in ~/workspace/nilgiri, create a new
> character named **Borin**. Send the temporary password to
> **borin@example.com**."

What Muse will do (see `NILGIRI_LOGIN.md` §10–12):

1. Ask for anything missing (it will never default the password email to
   your personal address).
2. Run `scripts/mud_wait_for_pass.exp`, which walks the MUD's creation
   flow — gender, race, appearance, homeland, stats, handedness — picking
   randomly from valid options, and then **stays connected** waiting for
   the emailed temp password.
3. The temp password is **session-bound**: it only works in the connection
   that created the character, so creation happens in one continuous
   session. Once entered, the character is saved and that password becomes
   permanent.
4. If the name is already taken, Muse asks whether to create a different
   name or log into the existing character.

### Logging in a character

> "Log **SinMuseBot** into Nilgiri for **10 minutes**. I'll give you the
> password."

What Muse will do (see [OPERATOR_RUNBOOK.md](OPERATOR_RUNBOOK.md) for the
full lifecycle, `NILGIRI_LOGIN.md` §23 for the operator/driver/relay
architecture):

1. Ask for the character's password at runtime (it is used once from an
   env var and never written to disk or chat).
2. Launch `scripts/launch_relay.sh` — it SSHes through the proxy tunnel,
   logs the character in, and starts the session timer when the game
   reports `>>> IN GAME`.
3. Write a session brief from [DRIVER_BRIEF_TEMPLATE.md](DRIVER_BRIEF_TEMPLATE.md)
   and spawn a **driver** — a background worker that does the
   minute-by-minute playing (one command at a time, reading game output,
   watching the clock) while Muse stays responsive in chat. The driver
   never receives passwords.
4. When time is up, the character exits properly: bank gold, `rent` a
   private room, `klick` (saves inventory — never `quit`, which drops
   everything), Return at the `*** PRESS RETURN:` prompt, menu option
   `0`, and lets the MUD close the connection itself.
5. Muse verifies no SSH/process strays remain, publishes the adventure
   summary and map updates, and reports what happened from the session
   log (the raw log itself stays local-only).

If you're watching in-game (like Sin does), Muse announces the plan
*before* logging in — what, how long, how many logins — so nothing
observable surprises you.

### Exploration and mapping

> "Explore and map **Midgaard, Northern Main City** for **20 minutes**.
> Find the bakery, the temple, the market square, and the receptionist."

What Muse will do:

1. Log in as above, then orient with `where` (zone name) and work rooms
   with the mapping loop: `look` + `exits` (`exits` is the source of truth
   for the map).
2. Handle survival: `eat manna` from inventory when hungry, drink from the
   Market Square fountain when thirsty, `buy #3` at the bakery for the free
   half loaf when manna runs out (buy by **list number** with `#` — the
   `#041418BA`-style codes are internal IDs).
3. Write the map to `maps/<zone>.md` — one section per room with exits,
   mobiles, and notes, plus an ASCII sketch; exits seen but not yet entered
   are marked `[UNMAPPED]` for the next pass. See
   `maps/midgaard-northern-main-city.md` for the format.
4. Finish mapping **before** renting — rent rooms have no exits. Then
   `rent` at the receptionist for a private room and `encamp` there, where
   it's always safe.
5. Log the session (timestamped, local-only) and report the log location
   plus what was mapped.

## What's in here

- **[OPERATOR_RUNBOOK.md](OPERATOR_RUNBOOK.md)** — the session lifecycle
  for the operator: launch, brief the driver, monitor, handle reboots and
  stalls, retire, publish. Read this before running a session.
- **[DRIVER_BRIEF_TEMPLATE.md](DRIVER_BRIEF_TEMPLATE.md)** — the template
  for the driver's per-session brief: comms protocol, standing rules,
  authority order, retirement procedure, report format. Copy and fill in
  the `[BRACKETED]` sections for each session.
- **[NILGIRI_LOGIN.md](NILGIRI_LOGIN.md)** — the full playbook: connection,
  character creation, login, in-game conduct, exploration, exit procedure,
  Expect notes, troubleshooting.
- **[maps/](maps/)** — zone maps built by exploration sessions, one file
  per zone, with room exits, services, and survival notes.
- **`scripts/mud_relay.py`** — the session relay: logs in via
  SSH + character password (env vars), relays stdin/stdout, flags speech
  from other players, enforces the session timer, and walks the verified
  exit sequence (encamp → Return → menu 0 → MUD closes). Strips non-ASCII
  from outbound lines (the MUD only accepts US ASCII).
- **`scripts/proxy_tunnel.py`** — opens an HTTP `CONNECT` tunnel so SSH
  reaches `nilgiri.net:22` from behind an egress proxy. Reads proxy
  credentials from the environment; never hardcodes them.
- **`scripts/ssh_via_proxy.sh`** — thin wrapper that runs `ssh` through the
  tunnel: `~/workspace/nilgiri/ssh_via_proxy.sh player@nilgiri.net`
- **`scripts/mud_wait_for_pass.exp`** — persistent Expect script that walks
  through character creation and then *waits at the temp-password prompt
  without disconnecting* (the temp password is only valid in the
  still-connected session). Takes `MUD_PASS`, `CHAR_NAME`, and `CHAR_EMAIL`
  from the environment.
- **`scripts/mud_create.py`** — experimental pexpect version of the creation
  flow (broad prompt matching proved unreliable; the Expect script above is
  the one that works).
- **`scripts/mud_comms_test.exp`** — earlier Expect-based comms test
  (superseded by `mud_relay.py`).
- **`scripts/mud_encamp_cleanup.exp`** — fallback: encamps a stuck session
  and tears it down.

## Key lessons (details in NILGIRI_LOGIN.md)

- **Temp passwords are session-bound.** Disconnect and the emailed password
  is dead. The Expect script stays connected and polls for the password.
- **Leave with `encamp`, not `quit`.** `quit` drops all inventory;
  `encamp` saves it. Then Return at `*** PRESS RETURN:`, menu option `0`,
  and let the MUD close the connection itself.
- **Nothing secret lives in this repo.** Character names, passwords, and
  email addresses are prompted for at runtime and passed via environment
  variables — never written to disk.
- **US ASCII only.** The MUD accepts standard keyboard characters; no
  emoji. The relay strips anything else as a safety net.
- **Every session is timed and logged.** Never log in indefinitely; if no
  duration is given, ask. Session logs are local-only and never committed.

## Build upon it

Ideas for where to take it: per-character job scripts (a scout, a mage, a
merchant), scheduled check-ins, inventory tracking, or mapping the next
zone off the `[UNMAPPED]` exits. The `<>` prompt is yours — `look` around
and start automating.
