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
    # newline="": no universal-newline translation, so line numbers match
    # `grep -n` (the MUD logs use lone \r for prompt redraws, which text-mode
    # translation would otherwise count as extra lines).
    with open(path, encoding="utf-8", errors="replace", newline="") as f:
        return f.read()


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


QUESTION_RE = re.compile(
    r'^(Sin|Motorola|Russ|Mandessa) (?:gossips?|says?|shouts?|tells you),?\s*"([^"]*\?[^"]*)"')
# Relay markers: >>> SPEECH name=Sin verb=gossips text=...
SPEECH_MARKER_RE = re.compile(
    r'>>> SPEECH name=(\w+) verb=(\w+) text=(.+)$')
ESCALATION_RE = re.compile(
    r'>>> SPEECH-(PENDING|UNANSWERED) \((\d+)s(?: unanswered)?\): (\w+) (?:gossips|says): (.+)$')
# Replies go out over gossip (controller questions arrive as gossip; the
# driver's fixed exit script uses `say`, which is never a reply).
BOT_SPEECH_RE = re.compile(
    r'^You (?:gossips?|tells? [^,]+),?\s*"')


def norm(t):
    return re.sub(r"\s+", " ", t.strip().lower().rstrip("?"))


def speech_audit(texts):
    """Controller questions (any controller speech containing '?') and whether
    the bot ever spoke after them. The relay re-emits unacknowledged speech as
    >>> SPEECH-PENDING (15s/30s) then >>> SPEECH-UNANSWERED (60s); escalations
    are matched back to the question and reported as evidence of how long the
    question stood. Each question gets a verdict:
      'prompt'    — a bot gossip/tell followed before the 60s escalation
      'late'      — the question escalated to SPEECH-UNANSWERED (the driver
                    sent nothing for 60s+) but the bot did speak before the
                    rent-room farewell (session 32: Sin's skills question)
      'unanswered'— no bot gossip/tell between the question and the farewell
                    (session 37: Sin's 'how is the warhammer, SinMuseBot?')
    There is no semantic matching: a reply verdict means the driver at least
    spoke; the operator still judges whether the reply actually answered the
    question. The debrief flags every 'late' and 'unanswered' question with
    its log location and escalation level.
    """
    # Gather ordered events across all logs (already chronological).
    questions = []   # (global_order, name, question, where)
    bot_speech = []  # global_order of each bot speech line
    escalations = {}  # norm(question text) -> highest escalation label
    seen_q = set()     # norm(question text) already recorded (dedupes the
                       # relay's >>> SPEECH marker against the gossip line)
    order = 0
    for path, text in texts:
        fname = Path(path).name
        # split("\n") (not splitlines): matches grep -n numbering, since the
        # MUD logs contain bare \r prompt redraws that splitlines would count.
        for i, raw in enumerate(text.split("\n"), 1):
            line = raw.strip()
            order += 1
            qm = QUESTION_RE.match(line)
            if qm and qm.group(1) in CONTROLLERS:
                key = norm(qm.group(2))
                if key not in seen_q:
                    seen_q.add(key)
                    questions.append((order, qm.group(1), qm.group(2), f"{fname}:{i}"))
                continue
            sm = SPEECH_MARKER_RE.search(line)
            if sm and sm.group(1) in CONTROLLERS and "?" in sm.group(3):
                key = norm(sm.group(3))
                if key not in seen_q:
                    seen_q.add(key)
                    questions.append((order, sm.group(1), sm.group(3).strip(), f"{fname}:{i}"))
                continue
            em = ESCALATION_RE.search(line)
            if em:
                label = {"PENDING": f"PENDING-{em.group(2)}s",
                         "UNANSWERED": "UNANSWERED-60s"}[em.group(1)]
                key = norm(em.group(4))
                rank = {"SPEECH": 1, "PENDING-15s": 2,
                        "PENDING-30s": 3, "UNANSWERED-60s": 4}
                prev = escalations.get(key, "")
                if rank[label] > rank.get(prev, 0):
                    escalations[key] = label
                continue
            if BOT_SPEECH_RE.match(line):
                bot_speech.append(order)
    # The session's last bot gossip is the fixed farewell in the rent room;
    # everything after it is exit script (klick, 'no place like home', menu).
    # Only a gossip/tell between the question and the farewell can be a reply.
    farewell = bot_speech[-1] if bot_speech else None
    results = []
    for qorder, name, question, where in questions:
        esc = escalations.get(norm(question), "SPEECH")
        replied = (farewell is not None and qorder < farewell
                   and any(qorder < b < farewell for b in bot_speech))
        if not replied:
            verdict = "unanswered"
        elif esc == "UNANSWERED-60s":
            verdict = "late"  # the driver said something eventually, but the
                              # question still stood a full 60s+ (session 32)
        else:
            verdict = "prompt"
        results.append({
            "controller": name,
            "question": question,
            "where": where,
            "escalation": esc,
            "verdict": verdict,
        })
    return results


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
        "speech_audit": speech_audit(texts),
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
        audit = speech_audit(texts)
        bad = [q for q in audit if q["verdict"] != "prompt"]
        if not audit:
            speech_line = "no controller questions this session"
        elif not bad:
            speech_line = f"all {len(audit)} controller question(s) answered promptly"
        else:
            bits = "; ".join(
                f"⚠️ {q['verdict'].upper()}: {q['controller']} — \"{q['question']}\" "
                f"({q['where']}, escalated to {q['escalation']})"
                for q in bad)
            speech_line = f"{len(bad)}/{len(audit)} flagged: {bits}"
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
- **Speech audit:** {speech_line}
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
