# Nilgiri Muse Bot

A basic MUD bot that lets **Muse AI** create characters and log them in to
**Nilgiri the Forgotten World** — http://nilgiri.net — a DikuMUD-based fantasy
MUD ("the world of Rivin and Sin").

It is meant as a starting point for players to build upon and tune
themselves: the connection plumbing, the login/creation flows, and the
hard-won lessons are all here. Automate one character or a roster of them,
give each a job, and extend from there.

## What's in here

- **[NILGIRI_LOGIN.md](NILGIRI_LOGIN.md)** — the full playbook: how the
  connection works, the complete character-creation flow, the login flow,
  Expect automation notes, and troubleshooting.
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

## How a session works

1. SSH as `player@nilgiri.net` through the proxy tunnel.
2. Answer the text-color prompt, then give the character's name.
3. **Existing character** → password prompt → `*** PRESS RETURN:` → menu →
   `1) Enter the game` → in-game prompt `<>`.
4. **New name** → the MUD asks "Did I get that right?" and starts character
   creation: gender, race, appearance, homeland, stats, handedness. A
   temporary password is emailed; it must be entered in the *same connected
   session*, then the character is saved and that password becomes its
   permanent one.

## Key lessons (details in NILGIRI_LOGIN.md)

- **Temp passwords are session-bound.** Disconnect and the emailed password
  is dead. The Expect script stays connected and polls for the password.
- **Leave with `encamp`, not `quit`.** `quit` drops all inventory;
  `encamp` saves it and disconnects cleanly.
- **Nothing secret lives in this repo.** Character names, passwords, and
  email addresses are prompted for at runtime and passed via environment
  variables — never written to disk.

## Build upon it

Ideas for where to take it: per-character job scripts (a scout, a mage, a
merchant), scheduled check-ins, inventory tracking, or mapping. The `<>`
prompt is yours — `look` around and start automating.
