#!/usr/bin/env python3
"""Nilgiri session closeout — parse raw session logs into verified stats.

Usage:
    python3 scripts/closeout.py LOG [LOG ...] [--character SinMuseBot]

Feed it every log belonging to one session (multi-part sessions have one
log per relay launch). It prints a JSON stat extraction and writes a
draft summary in Fred's fixed format next to the stats, with the tale
left as a TODO for the operator to write from the log.

What it extracts (all from the raw logs, nothing invented):
- Window: first/last timestamps from log filenames + TIME UP markers
- XP: first score, last score + gains after it, gross gains, and ANY
  drop between consecutive scores (death or anomaly — flagged, never
  silently absorbed)
- Kills: R.I.P. lines only, counted per mob (XP never proves a kill)
- Bank: live "debited/credited" events (history listings carry an
  in-game date prefix and are ignored), Amount trajectory
- Speech: controller gossip lines from Sin / Motorola / Russ / Mandessa
- Disruptions: relay restarts, "Reconnecting...", TIME UP, clean exit
"""
import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

CONTROLLERS = ("Sin", "Motorola", "Russ", "Mandessa")


def read(path):
    return Path(path).read_text(errors="replace")


def xp_series(text):
    return [int(m) for m in re.findall(r"Experience points:\s*(\d+)", text)]


def gains(text):
    return [int(m) for m in re.findall(r"[Yy]ou gain (\d+) experience points", text)]


def kills(text):
    """R.I.P. lines only (XP never proves a kill). A kill is attributed
    to the player UNLESS the nearest preceding killing-blow line names
    another actor (e.g. "A deputy destroys a filthy street urchin...").
    Session 34: a deputy's urchin kill was wrongly credited to the bot."""
    def clean(name):
        return re.sub(r"^(A|An|The)\s+", "", name.strip())
    out = Counter()
    for m in re.finditer(r"(.+?) is dead! R\.I\.P\.", text):
        name = clean(m.group(1))
        prev = text[max(0, m.start() - 600):m.start()]
        blows = re.findall(
            r"^(.{0,80}?)(?:destroys?|kills?|annihilates?)\s+"
            r"(?:a|an|the)\s+" + re.escape(name) + r"\b",
            prev, re.M | re.I)
        if blows and not re.match(r"^(You|Your)\b", blows[-1].strip()):
            continue  # someone else dealt the killing blow
        out[name] += 1
    return out


def bank_events(text):
    """Live bank events only: history listings are prefixed with an
    in-game date like 00836/01/26-03:16:26:: and must not double-count."""
    debits, credits = [], []
    for line in text.splitlines():
        if re.match(r"^\d{5}/\d\d/\d\d-", line):
            continue
        m = re.search(r"debited (\d+)gc for purchase .* '(.+?)'", line)
        if m:
            debits.append((int(m.group(1)), m.group(2)))
        m = re.search(r"credited (\d+)gc", line)
        if m:
            credits.append(int(m.group(1)))
    amounts = [int(m) for m in re.findall(r"Amount:\s*(\d+)gc", text)]
    return debits, credits, amounts


def speech(text):
    out = []
    for name in CONTROLLERS:
        for m in re.finditer(rf'{name} gossips, "([^"]+)"', text):
            out.append((name, m.group(1)))
    for m in re.finditer(r'You gossip, "([^"]+)"', text):
        out.append(("BOT", m.group(1)))
    return out


def log_time(path):
    m = re.search(r"(\d{8})-(\d{6})", Path(path).name)
    if not m:
        return None
    return datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M%S")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("logs", nargs="+")
    ap.add_argument("--character", default="SinMuseBot")
    ap.add_argument("--session", type=int, default=None)
    args = ap.parse_args()

    texts = [(p, read(p)) for p in sorted(args.logs, key=lambda p: log_time(p) or datetime.min)]
    full = "\n".join(t for _, t in texts)

    # XP ledger
    series = xp_series(full)
    xp_start = series[0] if series else None
    last_score = series[-1] if series else None
    tail_gains = 0
    if series:
        idx = full.rfind(f"Experience points: {last_score}")
        tail_gains = sum(gains(full[idx:])) if idx >= 0 else 0
    xp_end = (last_score + tail_gains) if last_score is not None else None
    gross = sum(gains(full))
    drops = [
        (a, b, b - a) for a, b in zip(series, series[1:]) if b < a
    ]
    net = (xp_end - xp_start) if xp_start is not None and xp_end is not None else None

    # Kills / deaths / bank
    kk = kills(full)
    deb, cred, amounts = bank_events(full)
    deaths = len(re.findall(r"[Yy]ou have died|[Yy]ou are dead", full))

    # Disruptions / shutdown
    time_ups = len(re.findall(r">>> TIME UP", full))
    reboots = max(0, len(texts) - 1)
    clean_exit = "MUD closed the connection after menu exit" in full
    reconnects = len(re.findall(r"Reconnecting\.\.\.", full))

    times = [log_time(p) for p, _ in texts if log_time(p)]
    fmt = "%H:%M"
    window = (
        f"{times[0].strftime(fmt)}–{times[-1].strftime(fmt)}"
        if len(times) >= 2 else (times[0].strftime(fmt) if times else "?")
    )
    day = times[0].strftime("%Y-%m-%d") if times else "????-??-??"

    spent = sum(d for d, _ in deb)
    deposited = sum(cred)
    bank_end = amounts[-1] if amounts else None

    stats = {
        "character": args.character,
        "logs": [p for p, _ in texts],
        "xp": {
            "start": xp_start, "end": xp_end, "net": net,
            "gross_gains": gross, "drops_flagged": drops,
        },
        "kills": dict(kk), "kills_total": sum(kk.values()),
        "deaths": deaths,
        "bank": {
            "spent": spent, "deposited": deposited, "end": bank_end,
            "amount_trajectory": amounts, "purchases": deb,
        },
        "speech": speech(full),
        "disruptions": {
            "relay_launches": len(texts), "reboots": reboots,
            "reconnects": reconnects, "time_ups": time_ups,
        },
        "shutdown_clean": clean_exit,
    }
    print(json.dumps(stats, indent=1))

    if args.session:
        kills_line = ", ".join(f"{n} {k}" for k, n in sorted(kk.items(), key=lambda kv: -kv[1]))
        drop_note = ""
        if drops:
            drop_note = "; ".join(f"⚠️ XP drop {a} → {b} ({d}) between scores — investigate" for a, b, d in drops)
        draft = f"""# Session {args.session:02d} — {args.character} — {day} ({window})

## The tale

TODO — operator writes this from the log. Disruptions/speech below are
extracted; every line must trace to a log event.

## Stat block

- **Level:** ?
- **XP:** {xp_start} → {xp_end} (**{net:+d}** net; +{gross} gross gains{'; ' + drop_note if drop_note else ''})
- **Confirmed kills ({sum(kk.values())}):** {kills_line}
- **Deaths:** {deaths} recorded in logs
- **Bank:** +{deposited}gc deposited, −{spent}gc spent → **{bank_end}gc total**
- **Discoveries:** TODO
- **Disruptions:** {reboots} relay restart(s), {reconnects} reconnect(s); clean exit: {clean_exit}
- **Shutdown:** TODO

## Token cost

- Weekly allowance: TODO% → TODO% (driver-reported tokens unavailable
  unless the driver report came back with them)
"""
        out = Path(f"session_summaries/{args.character}/session-{args.session:02d}.md")
        out.parent.mkdir(parents=True, exist_ok=True)
        # Never clobber an existing published summary.
        if out.exists():
            out = out.with_suffix(".draft.md")
        out.write_text(draft)
        print(f"draft summary -> {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
