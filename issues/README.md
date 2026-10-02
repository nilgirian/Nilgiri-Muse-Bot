# Issues — Nilgiri MUD bugs and playability notes

Candidate bugs and playability issues found while playing Nilgiri with the
SinMuseBot character (started 2026-09-25). Each issue is one file so it can
be tracked, updated, and closed independently. Every issue ends with a
**Staff response** section, reserved for the Nilgiri Grok Bot (which runs
the MUD code) to answer in place — more issues will be added as play
continues.

Raw session logs are **local-only and never published**; evidence below
points at the published per-session summaries and the repo docs that
describe the events.

## Open issues

| ID | Title | Kind | Status |
|----|-------|------|--------|
| [001](001-xp-loss-without-death.md) | XP lost (−196) with no death in the logs | Suspected bug | Open — needs staff adjudication |
| [002](002-bank-account-lost-after-crash.md) | Bank account vanished after a MUD crash | Suspected bug | Open — needs staff check |
| [003](003-drop-all-destroyed-items.md) | `drop all` destroyed the Nilgiri Guide and 2 manna | Suspected bug / needs clarification | Open — is this intended? |
| [004](004-duplicate-mobs-and-targeting.md) | Duplicate same-keyword mobs join fights; `consider X` / `kill X` can target different mobs | Mechanics / playability | Open — design feedback |
| [005](005-invisible-zone-boundary-bee-hive.md) | Invisible zone boundary: Hills-looking path is Bee Hive zone | Playability | Open |
| [006](006-night-darkness-reads-as-level-gate.md) | Night darkness reads as a level restriction | Playability | Open |
| [007](007-one-way-exits-undocumented.md) | One-way / asymmetric exits are undocumented | Playability | Open |
| [008](008-missing-recommended-levels.md) | `where` shows no recommended level for several zones | Playability | Open |
| [009](009-ferocious-rabbit-ambush.md) | Ferocious rabbit ambushes on sight in neutral leveling zones | Playability | Open |
| [010](010-courier-pigeon-danger.md) | Courier pigeons in the city center far tougher than they look | Playability | Open |

## Fixed (client-side, tracked in LESSONS_LEARNED.md)

These were bugs in the bot's own relay/tooling, not in the MUD. All fixed
and documented in [LESSONS_LEARNED.md](../LESSONS_LEARNED.md):

- SSH tunnel `timeout=15` never cleared after setup — first quiet 15s
  killed the download thread silently; commands executed unseen.
  Fixed in `scripts/proxy_tunnel.py`.
- Reconnect budget counted total drops, not consecutive ones — 6
  recoverable drops across a session exhausted it. Fixed in
  `scripts/mud_relay.py`.
- `game_start` reset on every reconnect, so the session TIME UP timer
  could never fire. Fixed in `scripts/mud_relay.py`.
- Relay stdin EOF killed the whole session. Now detaches instead.
  Fixed in `scripts/mud_relay.py`.
