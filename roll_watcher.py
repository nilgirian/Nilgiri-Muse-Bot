#!/usr/bin/env python3
"""Watch /tmp/roll_current.txt; parse each stat roll; decide keep/reroll.

Keep rule (Testudo, Dwarf; totals include race bonus, '*' = at race max):
  Tier A: CON* and STR* and WIS>=14 and INT>=12
  Tier B (roll>150): CON* and STR>=17 and WIS>=14
  Tier C (roll>300): CON>=18 and STR>=17 and WIS>=14
  Hard cap: roll>=600 -> keep regardless.
Writes 'no' (keep) or 'yes' (reroll) to /tmp/roll_decision.txt and
appends every parsed roll to /tmp/rolls_parsed.tsv.
Exits when /tmp/roll_current.txt disappears after a keep, or when the
creation log shows the password phase, or after 50 min.
"""
import os, re, sys, time

CUR = "/tmp/roll_current.txt"
DEC = "/tmp/roll_decision.txt"
TSV = "/tmp/rolls_parsed.tsv"
LOG = os.path.expanduser("~/workspace/nilgiri/logs/session-20261024-1046-creation.log")
ANSI = re.compile(r"\x1b\[[0-9;]*m")
STAT = {
    "STR": re.compile(r"strength:\s*(\d+)(?:\s*[+-]\d+\s*=\s*(\d+))?(\s*\*)?"),
    "DEX": re.compile(r"dexterity:\s*(\d+)(?:\s*[+-]\d+\s*=\s*(\d+))?(\s*\*)?"),
    "INT": re.compile(r"intelligence:\s*(\d+)(?:\s*[+-]\d+\s*=\s*(\d+))?(\s*\*)?"),
    "WIS": re.compile(r"wisdom:\s*(\d+)(?:\s*[+-]\d+\s*=\s*(\d+))?(\s*\*)?"),
    "CON": re.compile(r"constitution:\s*(\d+)(?:\s*[+-]\d+\s*=\s*(\d+))?(\s*\*)?"),
    "CHA": re.compile(r"charisma:\s*(\d+)(?:\s*[+-]\d+\s*=\s*(\d+))?(\s*\*)?"),
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
        star = bool(m.group(3))
        out[k] = (raw, total, star)
    return out

def keep(stats, n):
    s = {k: v[1] for k, v in stats.items()}
    star = {k: v[2] for k, v in stats.items()}
    if star["CON"] and star["STR"] and s["WIS"] >= 14 and s["INT"] >= 12:
        return True, "tierA"
    if n > 150 and star["CON"] and s["STR"] >= 17 and s["WIS"] >= 14:
        return True, "tierB"
    if n > 300 and s["CON"] >= 18 and s["STR"] >= 17 and s["WIS"] >= 14:
        return True, "tierC"
    if n >= 600:
        return True, "hardcap"
    return False, ""

def main():
    seen_hash = None
    n = 0
    t0 = time.time()
    with open(TSV, "a") as f:
        f.write("roll\tSTR_raw\tSTR\tSTR*\tDEX_raw\tDEX\tDEX*\tINT_raw\tINT\tINT*\tWIS_raw\tWIS\tWIS*\tCON_raw\tCON\tCON*\tCHA_raw\tCHA\tCHA*\tdecision\ttier\n")
    while time.time() - t0 < 3000:
        # stop conditions: creation moved past reroll phase
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
            time.sleep(1)
            continue
        h = hash(data)
        if h == seen_hash:
            time.sleep(1)
            continue
        seen_hash = h
        stats = parse(data.decode("utf-8", "replace"))
        if stats is None:
            print("watcher: PARSE FAIL on new roll capture; holding (no decision written)", flush=True)
            continue
        n += 1
        k, tier = keep(stats, n)
        row = [str(n)]
        for key in ("STR", "DEX", "INT", "WIS", "CON", "CHA"):
            raw, total, star = stats[key]
            row += [str(raw), str(total), "*" if star else ""]
        row += ["KEEP" if k else "reroll", tier]
        with open(TSV, "a") as f:
            f.write("\t".join(row) + "\n")
        with open(DEC, "w") as f:
            f.write("no" if k else "yes")
        print(f"watcher: roll {n} -> {'KEEP ' + tier if k else 'reroll'} :: "
              + " ".join(f"{key}={stats[key][1]}{'*' if stats[key][2] else ''}" for key in ('STR','DEX','INT','WIS','CON','CHA')), flush=True)
        if k:
            return
    print("watcher: timed out", flush=True)

if __name__ == "__main__":
    main()
