# Getting Started — Play Nilgiri the Forgotten World with Nilgiri-Muse-Bot

**Nilgiri** (http://nilgiri.net) is a DikuMUD-based fantasy MUD — "the
world of Rivin and Sin," also called *the Forgotten World*. You play by
typing text commands: you explore rooms, fight monsters, gain
experience, level up, and collect treasure. This repository is a
complete kit for playing it — connection plumbing, maps, hard-won
lessons, and an AI driver that can play a character for you.

There are two ways to use this repo: **play yourself**, or **have Muse
play for you**. Both start the same way.

## 1. Connect to the game

Nilgiri lives at `nilgiri.net`. The entry account is `player`:

```bash
git clone https://github.com/nilgirian/Nilgiri-Muse-Bot.git ~/workspace/nilgiri
cd ~/workspace/nilgiri
```

The connection goes through an SSH tunnel (the `player` account is
shared; its password is published on Nilgiri's connect page at
https://nilgiri.net/doku.php?id=nilgiri:connect). This repo handles the
tunnel for you:

```bash
./ssh_via_proxy.sh player@nilgiri.net
```

What you'll see (verified live — server is currently Gamma 5.0.2738):

```
Nilgiri Gamma 5.0.2738 (nilgiri.net 8008)
Do you want text color (yes/no) ?  → yes
By what name do you wish to be known?  → your character's name
```

If the name exists, you'll be asked for that character's password. If
it doesn't, you'll be offered character creation (see below). Then:

```
WELCOME TO Nilgiri the Forgotten World
*** PRESS RETURN:
0) Exit from the Forgotten World.
1) Enter the game.
2) Change password.
    Make your choice:  → 1
```

You're in. The full connection playbook — tunnel details,
troubleshooting, the works — is in [NILGIRI_LOGIN.md](NILGIRI_LOGIN.md).

## 2. Create your character

Pick a name at the "By what name" prompt. If it's new, the MUD asks
`Did I get that right, <name> (yes/no)?` — say yes, and give an **email
address** when asked. The MUD emails you a temporary password for the
character. (Each character has its own password — keep them private and
never commit them anywhere.)

You'll start at the Temple of Midgaard. Read the starting room, then:

## 3. Your first commands

MUDs reward the curious. These will carry you through your first hour:

| Command | What it does |
|---|---|
| `look` | Describe the room you're in |
| `exits` | List obvious exits (or set `environment exits_long on` to see them with every `look`) |
| `north/south/east/west/up/down` | Move |
| `where` | Show your zone ("exploring the depths of …") and who's nearby — use it in every new room |
| `score` | Your level, XP, HP, hunger/thirst |
| `inventory` / `equipment` | What you're carrying / wearing |
| `consider <target>` | Judge whether you can beat it — **always consider before attacking** |
| `kill <target>` | Attack |
| `flee` | Run from a fight going badly |
| `get all from corpse` | Loot what you killed (note: "from" — `get all corpse` doesn't work) |
| `say <text>` / `gossip <text>` | Talk (room / whole game) |

**Try exits the description mentions, not just the obvious ones.** If a
room says "the path continues northeast" but northeast isn't listed —
try `northeast` anyway. Hidden exits guard the best secrets.

## 4. Surviving your first session

- **Eat and drink.** Hunger and thirst weaken you — never fight hungry.
  Buy food in the city; drink from fountains.
- **Consider everything.** If `consider` says it's too strong, believe
  it. Some things that look harmless (rabbits, mosquitoes in swarms)
  are not.
- **Bank your gold.** The Bank of Midgaard takes deposits — gold left on
  your corpse is gold lost. `rent` a room at an inn to save safely.
- **Learn the map.** Start in [Northern Midgaard](maps/midgaard-northern-main-city.md),
  then the [Hills and Plains](maps/hills-and-plains.md) for hunting.
  Every map has an ASCII sketch; `{{Name}}` markers show where areas
  connect.

When you're done: bank valuables, `rent` a room, and exit cleanly —
never just close the connection mid-adventure if you can avoid it.

## 5. Have Muse play for you (the bot path)

This repo's real power: a Muse AI can drive a character autonomously —
exploring, hunting, mapping, and reporting back with a story of the
adventure.

**Give the repo to your Muse** (point it at the GitHub URL or clone it
into its workspace). Your Muse can **create a character for you** — no
ready-made character needed:

> "Create a new Nilgiri character named *<name>* for me."

It runs the full creation flow (appearance randomized, temp password
emailed to an address you provide), and that password becomes the
character's permanent one. The complete creation playbook is
[NILGIRI_LOGIN.md](NILGIRI_LOGIN.md) §10–11.

Already have a character? Say something like:

> "Log into Nilgiri as *<character>* for one hour and go hunting in the
> Hills and Plains."

Your Muse will ask for the character password at runtime (transient —
never stored), run the session, and hand you an adventure debrief: what
happened, XP gained, kills, loot, and how it ended. The operator's
procedure is [OPERATOR_RUNBOOK.md](OPERATOR_RUNBOOK.md); the full
playbook is [NILGIRI_LOGIN.md](NILGIRI_LOGIN.md).

While the bot plays, you can watch from your own character and even
give it live orders — it answers its masters within seconds.

## 6. Go deeper

- [NILGIRI_LOGIN.md](NILGIRI_LOGIN.md) — the complete playbook:
  connection, creation, conduct, exit, troubleshooting
- [OPERATOR_RUNBOOK.md](OPERATOR_RUNBOOK.md) — running bot sessions
- [MUD_TOOLS.md](MUD_TOOLS.md) — in-game mechanics (`consider`,
  `noflee`, prompt HP display, banking, rent)
- [LESSONS_LEARNED.md](LESSONS_LEARNED.md) — every hard lesson, so you
  don't pay for them yourself
- [maps/](maps/) — player-made maps with ASCII sketches
- [session_summaries/](session_summaries/) — actual play reports, told
  as stories

Welcome to the Forgotten World. Watch out for rabbits.
