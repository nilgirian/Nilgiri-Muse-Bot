# Nilgiri MUD Login — Lessons Learned

Date: 2026-09-24 (generalized 2026-09-25)
Goal: SSH as `player@nilgiri.net`, log in as a MUD character, enter the game.

**Standing rule: `SinMuseBot` below is only an example from the first session. Always prompt the user for the character name and the character password at runtime. Never hardcode a name, email, or password.**

## 1. Network reality on this VM

- The VM is Ubuntu 24.04. Outbound traffic goes through an HTTP egress proxy (`hatch-egress-proxy:3128`, configured via `ALL_PROXY` / `HTTP_PROXY` env vars).
- Direct `ssh player@nilgiri.net` fails: `kex_exchange_identification: read: Connection reset by peer` / `Connection reset by <proxy-ip> port 3128`.
- `getent hosts nilgiri.net` returns `198.18.27.43` (benchmark range) from local DNS, but the proxy resolves it itself for CONNECT — don't rely on local DNS.
- Good news: the proxy **does** allow `CONNECT nilgiri.net:22` (returns `HTTP/1.1 200 Connection Established`). Many proxies only allow 443; this one allows 22.

## 2. How the tunnel works

HTTP `CONNECT` asks the proxy to open a raw TCP tunnel to `host:port`, then bytes are forwarded blindly. SSH runs inside that tunnel.

Flow:
1. Open TCP to proxy host:port from `ALL_PROXY`.
2. Send: `CONNECT nilgiri.net:22 HTTP/1.1` + `Host:` + `Proxy-Authorization: Basic base64(user:pass)` (user/pass parsed from `ALL_PROXY` at runtime).
3. Wait for `HTTP/1.1 200`. If not 200, abort.
4. Bidirectionally forward between the socket and ssh's stdin/stdout.

## 3. Scripts (persisted)

All in `~/workspace/nilgiri/` (not `/tmp`, which is ephemeral):

- `proxy_tunnel.py` — Python CONNECT tunnel for `ssh ProxyCommand`. Reads proxy URL from env (`ALL_PROXY` etc.), never hardcodes credentials. Uses threads for stdin↔socket and socket↔stdout forwarding.
  - Usage: `python3 ~/workspace/nilgiri/proxy_tunnel.py <host> <port>`
  - Earlier version used `select` with non-blocking stdin and silently died; thread-based version works.

- `ssh_via_proxy.sh` — wrapper:
  ```bash
  #!/bin/bash
  exec ssh -o ProxyCommand="python3 $HOME/workspace/nilgiri/proxy_tunnel.py %h %p" \
    -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null "$@"
  ```
  - Usage: `~/workspace/nilgiri/ssh_via_proxy.sh player@nilgiri.net`
  - Test key auth (expected to fail if key not yet authorized):
    `~/workspace/nilgiri/ssh_via_proxy.sh -o BatchMode=yes player@nilgiri.net echo ssh-ok`
  - Verify tunnel + banner manually:
    ```python
    # python3 -c with socket: CONNECT nilgiri.net:22, then recv banner
    # Expected banner: SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u10
    ```

## 4. SSH auth notes

- Key auth: `~/.ssh/id_ed25519.pub` is:
  `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINHmhYK0KyVVsNDzmY1l3MmL0quiIQwsx//yG22cF7s3 hatch`
  The user added this to `player@nilgiri.net:authorized_keys`, but the server still returned `Permission denied (publickey,password,keyboard-interactive)` when offering it. Key may not have propagated or was added to the wrong account. Fall back to password.
- Password auth: the shared MUD password is provided by the user at runtime (transient, never written to disk). Use `expect` with `MUD_PASS` env var, e.g.:
  ```
  MUD_PASS='<password-from-user>' timeout 30 expect /tmp/mud_login.exp
  ```
  Expect script spawns `/tmp/ssh_via_proxy.sh` (or the workspace version), expects `(P|p)assword:`, sends `$env(MUD_PASS)`.

## 5. MUD session flow (Nilgiri Gamma 5.0.2563)

After SSH auth succeeds:

1. `Nilgiri Gamma 5.0.2563 (nilgiri.net 8008) session 3400`
2. `Do you want text color (yes/no) ?` → `yes`
3. Welcome banner (ASCII art, "WELCOME TO the world of Rivin and Sin... NILGIRI")
4. `By what name do you wish to be known?` → the character name (prompt the user every time)
5. Branch on the name:
   - **Existing character** → goes directly to `What is the password?` (skips creation). Prompt the user for that character's password and enter it.
   - **Unknown name** → `Did I get that right, <name> (yes/no) ?` appears. This means the character does not exist yet. **Stop and ask the user whether they want to create it.** If yes, prompt for the email address that should receive the temp password (never default to a personal email), then run the creation flow in §10.
6. `WELCOME TO Nilgiri the Forgotten World` → `*** PRESS RETURN:` → send return
7. Menu appears:
   ```
   0) Exit from the Forgotten World.
   1) Enter the game.
   2) Change password.
       Make your choice:
   ```
   → send `1` to enter the game.
8. In game at `<>` prompt. Useful commands: `look` (describe room), `encamp` (save inventory and disconnect cleanly).
9. **Always leave with `encamp`, never `quit`** — `quit` drops all inventory; `encamp` saves it.
10. If the previous session didn't end cleanly, login shows `Reconnecting...` and goes directly to `<>` (skips the menu).

## 6. Expect automation notes

- `expect` is at `/usr/bin/expect`. `pexpect` 4.9.0 was installed via pip (for Python automation, but Tcl expect proved more reliable for MUD).
- `muse.exec` does NOT support `pty: true` — use `expect` for interactive sessions.
- Strip ANSI color codes when reading MUD output: `sed -e 's/\x1b\[[0-9;]*m//g'`.
- Watch for quoting hell: `ssh -o ProxyCommand="..."` inside `expect`'s `spawn` breaks Tcl quoting. Workaround: put the ssh invocation in a shell wrapper (`ssh_via_proxy.sh`) and `spawn` the wrapper.
- Generic `Send "\r"` to `Select your X:` prompts loops forever — always send a valid listed option.
- The MUD prompt `<>` may have ANSI codes; match with `-re "<>"` not `-re "<> "`.
- For password prompts, use `log_user 0` before sending and `log_user 1` after to avoid leaking passwords into logs.
- "What is the password?" prompt has trailing control chars (`?\x01`); match with `-re "What is the password"` not exact.

## 7. Security notes

- NEVER write the proxy password (from `ALL_PROXY`), the MUD shared SSH password, any character password, or any email address to files, logs, or chat. All of them are transient runtime input: SSH password via `MUD_PASS` env, character name via `CHAR_NAME` env (or a user prompt), character password via `/tmp/mud_password.txt` + `log_user 0`, email via `CHAR_EMAIL` env (or a user prompt).
- The earlier debug run leaked a proxy password into tool output via `expect`'s `spawn` echo — avoid `log_user` + command echo when credentials are in the command line. `proxy_tunnel.py` avoids this by reading credentials from env at runtime.
- `ssh_via_proxy.sh` uses `StrictHostKeyChecking=no` + `UserKnownHostsFile=/dev/null` for automation; fine for this throwaway MUD login, not for general use.
- No passwords or personal emails live in this repo. If one ever slips in, restart the repo fresh (delete + recreate) so it never appears in history — editing alone is not enough.

## 8. Quick resume commands

```bash
# Test tunnel + SSH banner (no auth)
/tmp/proxy_tunnel.py nilgiri.net 22  # then read banner, or use the python CONNECT snippet

# SSH via proxy (password prompt)
/workspace/nilgiri/ssh_via_proxy.sh player@nilgiri.net

# Expect-driven login to skin-complexion prompt (example)
/workspace/nilgiri/ssh_via_proxy.sh player@nilgiri.net  # wrapped by expect script
```

## 9. Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `Connection reset by peer` on direct ssh | Expected — use the proxy tunnel, not direct ssh |
| `Connection timed out during banner exchange` | Old `proxy_tunnel.py` (select-based) was broken; use thread-based version in workspace |
| `Permission denied (publickey,...)` | Key not authorized (yet); use password via expect |
| `Select your X:` loops forever | Sent invalid option; send one of the listed options exactly |
| `command-line line 0: invalid quotes` | Nested quotes in `ProxyCommand` inside expect; use the shell wrapper |

## 10. Character creation flow (discovered 2026-09-24)

Complete sequence. **Attributes are picked randomly** — `mud_wait_for_pass.exp`
chooses a random valid option at each prompt and logs the pick (values in
parentheses are the full option pools):

1. text color -> yes
2. name -> <character name> (prompt the user), then confirm `yes` at "Did I get that right"
3. email -> the email address the user gave for this character (entered twice; receives the temp password)
4. gender -> random (female, male)
5. race -> random (human, drow, dwarf, elf, giant, gnoll, gnome, goblin, halfling, ogre, orc, pixie, saurian), then confirm `yes` at "Do you wish to be <race>"
6. hair shape -> random (bald, cropped, straight, wavy, curly, spiked, mohawked, braided, dreadlocked)
7. hair length -> random (very short, short, medium, long, very long)
8. hair color -> random (black, brown, red, blond, platinum, gray)
9. skin complexion -> random (pale, light tan, tan, dark tan, dark)
10. eye color -> random (black, brown, blue, hazel, green)
11. eye shape -> random (almond, round, squinty, beady)
12. demeanor -> random (very young, young, adolescent, adult, mature, elderly, old, ancient)
13. height -> random (very short, short, average, tall, very tall)
14. weight -> random (very light, light, moderate, heavy, very heavy — NOTE: "average" is NOT valid here)
15. description confirm -> yes
16. homeland -> random (Jora, Argoceania)
17. stats reroll -> no (keep the server's roll, which is already random)
18. handedness -> random (right, left)
19. Then: "A password has been sent to you at: <email>" -> "What is the password?" -> enter the temp password from the email (see §11)

The example character `SinMuseBot` (2026-09-24) was rolled before
randomization: male human, straight short brown hair, tan, almond brown eyes,
adult, average height, moderate weight, Jora, right-handed.

## 11. Critical: Temp password is session-bound

- The temp password emailed is ONLY valid for the specific connected session sitting at "What is the password?" prompt.
- If you disconnect and reconnect, the old temp password is invalid. Each new creation run generates a NEW temp password.
- DO NOT use expect scripts that exit at the password prompt. You must keep the session alive.
- Working pattern: `mud_wait_for_pass.exp` goes through creation with `MUD_PASS`/`CHAR_NAME`/`CHAR_EMAIL` from env, then at "What is the password?" it waits (polls `/tmp/mud_password.txt` every 5s, up to 10 min) without disconnecting, and sends the password with `log_user 0` to avoid leaking it.
- After successful entry, the character is saved and that temp password becomes its permanent password until changed. Subsequent logins go directly to "What is the password?" (no recreation needed).
- Verified with the example character `SinMuseBot` on 2026-09-24: entered the game (saw WELCOME TO Nilgiri, then "*** PRESS RETURN:").

## 12. Example session: SinMuseBot (2026-09-24)

- Created as male human from Jora (values in §10 are this character's).
- Entered game, saw the Temple of Midgaard, then was transferred to Russ' House.
- Deities present: Russ, Motorola, Sin (Implementor). Sin said "the thing finally logged in".
- Test commands run: `look`, `smile motorola` ("You smile at Motorola."), then `encamp` to leave with inventory saved.
- Character persists; no recreation needed on next login.

## 13. Password lifecycle

- Temp password emailed during creation is session-bound (see §11).
- Once entered correctly, the character is saved AND that temp password becomes the character's permanent password until changed (verified with the example character on 2026-09-24).
- To change: choose option 2 at the menu after pressing return.
- Do NOT reuse old temp passwords from previous (disconnected) sessions.
- Never store character passwords in files or the repo — prompt the user at runtime.

## 14. Runtime prompt checklist (for the assistant)

Every MUD session, ask the user for:
1. **Character name** — which character to connect as.
2. **Character password** — that character's password (transient; never stored).
3. If the name turns out to be new (MUD asks "Did I get that right?"): **whether to create it**, and if yes, **which email** should receive the temp password.

Then follow §5. Nothing in this repo contains a name, email, or password.

## 15. Creating additional characters (for different jobs)

The flow in §5/§10 is reusable for any character name. Variables:
- `CHAR_NAME`: e.g. `SinScout`, `SinMage` (must be unique; case-sensitive)
- `CHAR_EMAIL`: **prompt the user for this each time** — do NOT default to a personal email. Each new character triggers a temp-password email.
- Appearance/race/class choices: pick per job.

To create a new character:
1. Confirm with the user that they want a new character, and ask which email should receive the temp password.
2. Run `mud_wait_for_pass.exp` with `MUD_PASS`, `CHAR_NAME`, `CHAR_EMAIL` set via env:
   ```
   MUD_PASS='<ssh-password>' CHAR_NAME='<name>' CHAR_EMAIL='<email>' \
     timeout 700 expect ~/workspace/nilgiri/mud_wait_for_pass.exp
   ```
3. At "What is the password?" the script waits; the user reads the temp password from the email and provides it (via `/tmp/mud_password.txt` or chat), and the script submits it in the still-connected session.
4. That temp password becomes the new character's permanent password.
5. Each character has its own password; never store them — prompt at runtime.

Notes:
- Same SSH login (`player@nilgiri.net`) hosts multiple characters; the "By what name" prompt selects which one.
- If name is new, the MUD asks "Did I get that right?" and goes through full creation (§10). If name exists, it goes directly to the password prompt.
- Character names are case-sensitive.

## 16. In-game communication (2026-09-25)

- Speech from others arrives as `<Name> says, "..."`, `<Name> asks, "..."`,
  `<Name> exclaims, "..."`, or `<Name> tells you, "..."`. Match all the verbs —
  a first version that only watched `says`/`tells you` missed Motorola's
  `asks`.
- To speak: the `say` command, e.g. `say hi` produces `You say, "hi"`.
- Bot etiquette that works: stay silent unless Sin, Motorola, or Russ address
  the bot directly; then reply with `say`. Keep replies short and lowercase,
  like a player would type them.
- Simple reply policy that held up in testing: greeting → greet back;
  question → `i'm just a bot, ask sin`; name mention → `that's me`;
  otherwise `ok`.
- Reference implementation: `scripts/mud_comms_test.exp` — logs in, idles
  N minutes answering only direct address from those three, then
  `say time to leave` + `encamp`.
- For live, agent-driven conversation: `scripts/mud_relay.py` — logs in and
  relays stdin/stdout so the agent reads the game and types replies itself.
  Flags speech as `>>> SPEECH name=... verb=... text=...`. Passwords are read
  from env (`MUD_PASS`, `CHAR_PASS`) and redacted from output.
