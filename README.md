# Nilgiri Muse Bot

Notes and scripts for logging into and playing the Nilgiri MUD.

- [NILGIRI_LOGIN.md](NILGIRI_LOGIN.md) — full write-up: SSH-over-proxy tunnel setup, character creation flow, login flow, and game commands.
- [scripts/](scripts/) — `proxy_tunnel.py` (HTTP CONNECT tunnel), `ssh_via_proxy.sh` (SSH wrapper), `mud_wait_for_pass.exp` (persistent character-creation script), `mud_create.py` (experimental).

No names, emails, or passwords are stored in this repo — the assistant prompts for the character name and password at runtime.
