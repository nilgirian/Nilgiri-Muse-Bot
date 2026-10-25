#!/usr/bin/env python3
"""Watcher v2 — totals-based keep rule (no stars: 0 asterisks in 303
rolls on this build's roll screen; raw dice cap empirically 18).

Dwarf total ceilings: STR 19, DEX 17, INT 17, WIS 18, CON 19, CHA 17.
Phased keep rule (by rolling time):
  P1 (0-90m):  (CON>=18 & STR>=17 & WIS>=15 & INT>=11) or
               (CON==19 & STR>=16 & WIS>=14 & INT>=10)
  P2 (90-150m): CON>=18 & STR>=16 & WIS>=14 & INT>=10
  P3 (>150m):   CON>=17 & STR>=16 & WIS>=14 & INT>=10
Continues numbering from the existing TSV. Tracks best-so-far.
"""
import os, re, time

CUR = "/tmp/roll_current.txt"
DEC = "/tmp/roll_decision.txt"
TSV = "/tmp/rolls_parsed.tsv"
LOG = os.path.expanduser("~/workspace/nilgiri/logs/session-20261024-1120-creation2.log")
ANSI = re.compile(r"\x1b\[[0-9;]*m")
STAT = {
    "STR": re.compile(r"strength:\s*(\d+)(?:\s*[+-]\d+\s*=\s*(\d+))?"),
    "DEX": re.compile(r"dexterity:\s*(\d+)(?:\s*[+-]\d+\s*=\s*(\d+))?"),
    "INT": re.compile(r"intelligence:\s*(\d+)(?:\s*[+-]\d+\s*=\s*(\d+))?"),
    "WIS": re.compile(r"wisdom:\s*(\d+)(?:\s*[+-]\d+\s*=\s*(\d+))?"),
    "CON": re.compile(r"constitution:\s*(\d+)(?:\s*[+-]\d+\s*=\s*(\d+))?"),
    "CHA": re.compile(r"charisma:\s*(\d+)(?:\s*[+-]\d+\s*=\s*(\d+))?"),
}

def parse(text):
    text = ANSI.sub("", text)
    out = {}
    for k, rx in STAT.items():
        m = rx.search(text)
        if not m:
            return None
        raw = int(m.group(1))
        total = int(m.group(2)) if m.group(2) else raw
        out[k] = (raw, total)
    return out

def decide(s, mins):
    if mins < 90:
        if (s["CON"] >= 18 and s["STR"] >= 17 and s["WIS"] >= 15 and s["INT"] >= 11) or \
           (s["CON"] == 19 and s["STR"] >= 16 and s["WIS"] >= 14 and s["INT"] >= 10):
            return "P1"
    elif mins < 150:
        if s["CON"] >= 18 and s["STR"] >= 16 and s["WIS"] >= 14 and s["INT"] >= 10:
            return "P2"
    else:
        if s["CON"] >= 17 and s["STR"] >= 16 and s["WIS"] >= 14 and s["INT"] >= 10:
            return "P3"
    return ""

def main():
    n = 0
    if os.path.exists(TSV):
        with open(TSV) as f:
            n = max(0, sum(1 for _ in f) - 1)
    print(f"watcher v2: resuming at roll {n}", flush=True)
    seen_hash = None
    t0 = time.time()
    best = None
    while time.time() - t0 < 14400:
        try:
            with open(LOG, "rb") as fh:
                tail = fh.read()[-200000:].decode("utf-8", "replace")
            if "---ROLL KEPT---" in tail or "---AT_PASSWORD_PROMPT---" in tail:
                print("watcher: creation moved on; exiting", flush=True)
                return
        except OSError:
            pass
        try:
            with open(CUR, "rb") as fh:
                data = fh.read()
        except OSError:
            time.sleep(1); continue
        h = hash(data)
        if h == seen_hash:
            time.sleep(1); continue
        seen_hash = h
        stats = parse(data.decode("utf-8", "replace"))
        if stats is None:
            print("watcher: PARSE FAIL; holding", flush=True)
            continue
        n += 1
        s = {k: v[1] for k, v in stats.items()}
        mins = (time.time() - t0) / 60.0
        tier = decide(s, mins)
        score = s["CON"]*4 + s["STR"]*3 + s["WIS"]*3 + s["INT"]*2 + s["DEX"]
        if best is None or score > best[0]:
            best = (score, n, dict(s))
        row = [str(n)]
        for key in ("STR", "DEX", "INT", "WIS", "CON", "CHA"):
            row += [str(stats[key][0]), str(stats[key][1]), ""]
        row += ["KEEP" if tier else "reroll", tier]
        with open(TSV, "a") as f:
            f.write("\t".join(row) + "\n")
        with open(DEC, "w") as f:
            f.write("no" if tier else "yes")
        print(f"watcher: roll {n} -> {'KEEP ' + tier if tier else 'reroll'} :: "
              + " ".join(f"{k}={s[k]}" for k in ('STR','DEX','INT','WIS','CON','CHA'))
              + f" | best #{best[1]}: " + " ".join(f"{k}={best[2][k]}" for k in ('STR','DEX','INT','WIS','CON','CHA')), flush=True)
        if tier:
            return
    print("watcher: timed out", flush=True)

if __name__ == "__main__":
    main()
