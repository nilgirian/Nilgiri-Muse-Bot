#!/usr/bin/env python3
"""render_leg1_brief.py — assemble a leg-1 driver brief.

WHY (Fred approved 2026-10-22): leg-1 briefs grew 3.8x in six days
(2,276 chars on 2026-10-16 -> 8,588 for session 86) because the
operator hand-condensed the standard rules into every brief — slow
to compose and prone to copy-drift. This renderer takes the rule
sections of DRIVER_BRIEF_TEMPLATE.md VERBATIM and fills only the
session slots (mission, state, greeting, deadline, circuit). The
operator then reviews and adds session-specific notes only.

Usage:
  python3 scripts/render_leg1_brief.py \
    --session 87 --date 2026-10-23 --title "8-hour XP run" \
    --character SinMuseBot --level 9 --xp 60546 --bank 201 \
    --hp 96 --mana 116 --move 121 --noflee 48 \
    --skills "Catechism 51/51, Cure light wounds 51/51, ..." \
    --practices 0 \
    --log logs/session-20261023-1200-8h.log --seconds 28800 \
    --deadline "19:40 PDT" \
    --greeting "Morning, Nilgiri -- ..." \
    --mission-file run/mission-s87.txt \
    --circuit-file run/circuit-s87.txt \
    [--notes-file run/notes-s87.txt] [--farewell "..."] \
    [--teaching] [--out run/brief-...-leg1.md]

The render FAILS (exit 2) if any [BRACKETED] template placeholder
survives substitution — the operator must resolve it by hand.
Sections are extracted from the template by their ## headings, so
editing the template updates every future brief automatically.
"""
import argparse, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "DRIVER_BRIEF_TEMPLATE.md"

# Template sections emitted verbatim, in this order.
SECTIONS = [
    "## Comms — how you talk to the game",
    "## Authority order (hardcoded — never overridden)",
    "## Talking to people (standing rule)",
    "## Session greeting and farewell (Fred, 2026-10-02)",
    "## Rules",
    "## Retirement (at >>> TIME UP, or when the mission is done)",
    "## Time discipline (hard rule — three sessions ended early on bad time math)",
    "## Report back",
]
TEACHING_SECTION = "## Teaching protocol (proven L4-L7; improvised on 2026-10-16 and failed — Fred, 2026-10-16)"

DEFAULT_ZONES = ("Northern Midgaard, Hills and Plains, Midgaard "
                 "Southern Residential, the Bee Hive, Midgaard "
                 "Vineyard, Sleeping Forest, Tharen")
DEFAULT_HAZARDS = ("Market Square manhole -> Storm Drain "
                   "(OFF-LIMITS, open — do not go down); 'The heavy "
                   "jungle' north of the dense forest (OFF-LIMITS — "
                   "every exit loops back, never enter); Haon-Dor "
                   "Forest (dark, off-limits); Sleeping Forest D/E "
                   "stalker maze (off-limits)")
DEFAULT_BANK = ("Bank of Midgaard: `deposit gold` for coins "
                "(ONE coin per command — repeat until none left), "
                "`deposit` for gems/treasure, verify with `balance`")
DEFAULT_RENT = "the Grunting Boar Inn Reception"


def split_sections(text):
    """Split markdown into {heading_line: body} on ## headings."""
    parts, current, buf = {}, None, []
    for line in text.splitlines():
        if line.startswith("## "):
            if current is not None:
                parts[current] = "\n".join(buf).strip("\n")
            current, buf = line.rstrip(), []
        elif current is not None:
            buf.append(line)
    if current is not None:
        parts[current] = "\n".join(buf).strip("\n")
    return parts


def substitute(text, subs):
    for pattern, repl in subs:
        text = re.sub(pattern, lambda m, r=repl: r, text, flags=re.S)
    return text


def main():
    ap = argparse.ArgumentParser(description="Render a leg-1 driver brief")
    ap.add_argument("--session", required=True)
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--title", required=True, help='e.g. "8-hour XP run"')
    ap.add_argument("--character", default="SinMuseBot")
    ap.add_argument("--level", required=True)
    ap.add_argument("--xp", required=True)
    ap.add_argument("--bank", required=True, help="bank balance in gc")
    ap.add_argument("--hp", required=True)
    ap.add_argument("--mana", required=True)
    ap.add_argument("--move", required=True)
    ap.add_argument("--noflee", required=True)
    ap.add_argument("--skills", required=True)
    ap.add_argument("--practices", default="0")
    ap.add_argument("--log", required=True, help="session log path")
    ap.add_argument("--seconds", required=True, help="total session budget seconds")
    ap.add_argument("--deadline", required=True,
                    help='leg-1 wall-clock deadline, e.g. "13:35 PDT"')
    ap.add_argument("--greeting", required=True)
    ap.add_argument("--farewell", default=None,
                    help="only for single-login sessions (the exit leg carries it otherwise)")
    ap.add_argument("--mission-file", required=True)
    ap.add_argument("--circuit-file", default=None)
    ap.add_argument("--notes-file", default=None)
    ap.add_argument("--report-extra-file", default=None)
    ap.add_argument("--zones", default=DEFAULT_ZONES)
    ap.add_argument("--hazards", default=DEFAULT_HAZARDS)
    ap.add_argument("--teaching", action="store_true")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    template = TEMPLATE.read_text()
    sections = split_sections(template)
    wanted = list(SECTIONS)
    if args.teaching:
        wanted.insert(5, TEACHING_SECTION)
    missing = [h for h in wanted if h not in sections]
    if missing:
        sys.exit("template sections not found: %s" % "; ".join(missing))

    log_rel = args.log
    subs = [
        (r"\[NILGIRI DIR\]", "~/workspace/nilgiri"),
        (r"\[LOG PATH\]", log_rel),
        (r"\[CHARACTER NAME\]", args.character),
        (r"\[LIST, e\.g\. Northern Main City, Southern Residential\]",
         args.zones),
        (r"\[LIST, e\.g\. Market Square manhole.*?\]",
         args.hazards),
        (r"\[BANK PROCEDURE, e\.g\..*?\]",
         DEFAULT_BANK),
        (r"\[RENT LOCATION, e\.g\. the Grunting Boar Inn Reception\]",
         DEFAULT_RENT),
    ]

    def read_slot(path):
        return Path(path).read_text().strip("\n") if path else None

    mission = read_slot(args.mission_file)
    circuit = read_slot(args.circuit_file)
    notes = read_slot(args.notes_file)
    report_extra = read_slot(args.report_extra_file)

    out = []
    out.append("# Driver brief — %s %s, SESSION %s LEG 1 (%s)"
               % (args.character, args.title, args.session, args.date))
    out.append("")
    out.append("## Mission")
    out.append(mission)
    out.append("")
    out.append("## Session parameters")
    out.append("- Character: %s (Level %s, XP %s, bank %sgc)"
               % (args.character, args.level, args.xp, args.bank))
    out.append("- HP %s / mana %s / move %s; noflee %s"
               % (args.hp, args.mana, args.move, args.noflee))
    out.append("- Skills: %s; %s practices banked"
               % (args.skills, args.practices))
    out.append("- Session log: `%s`" % log_rel)
    out.append("- Command FIFO: `/tmp/mud_cmd`")
    out.append("- Time box: %s seconds of game time. The relay "
               "announces `>>> TIME UP` at the end of the FULL "
               "session budget." % args.seconds)
    out.append("- LEG DEADLINE: retire no later than **%s wall "
               "clock** — check `date` every ~20 min (session 86 "
               "saw both an overrun and an early retirement on "
               "bad clock discipline). At the deadline: bank gold "
               "and valuables, rent a private room at the "
               "Grunting Boar Inn, and STOP there — do NOT klick, "
               "do NOT farewell-gossip unless this is the final "
               "leg (the operator relaunches the next leg from "
               "the rent room)." % args.deadline)
    out.append("")
    out.append("## [SESSION GREETING]")
    out.append("gossip %s" % args.greeting)
    if args.farewell:
        out.append("")
        out.append("## [SESSION FAREWELL]")
        out.append("gossip %s" % args.farewell)
    if circuit:
        out.append("")
        out.append("## Session plan (operator)")
        out.append(circuit)

    for heading in wanted:
        body = sections[heading]
        if heading.startswith("## Session greeting and farewell"):
            # drop the template's bracketed example lines; the real
            # greeting/farewell live in the slots above
            body = "\n".join(
                l for l in body.splitlines()
                if not l.strip().startswith("[SESSION "))
        if heading == "## Rules":
            # cut the template's bracketed HUNT SESSIONS block: its
            # circuit text is stale by design — the operator's
            # current circuit rides in the Session plan slot above
            lines = body.splitlines()
            cut, kept = None, []
            for i, l in enumerate(lines):
                if "[HUNT SESSIONS:" in l:
                    cut = i
                    break
                kept.append(l)
            if cut is not None:
                j = cut
                while j < len(lines) and "danger zone alone.]" not in lines[j]:
                    j += 1
                kept.extend(lines[j + 1:])
                body = "\n".join(kept)
        body = substitute(body, subs)
        out.append("")
        out.append(heading)
        out.append(body.strip("\n"))

    if notes:
        out.append("")
        out.append("## Session-specific notes (operator)")
        out.append(notes)

    out.append("")
    out.append("## Leg report must include")
    out.append("- XP start/end (your first and last `score`), "
               "confirmed kills with locations, deaths")
    out.append("- Spell usage: attempts vs lands per spell; "
               "food/water state at handover")
    out.append("- Any rabbit contact, verbatim, and whether rabbit "
               "country is now exiled for the session")
    out.append("- BLOCK tally if you used blocking waits: calls, "
               "wake reasons, probes ignored, seconds blocked")
    out.append("- Bank balance at handover (verbatim read) and "
               "where you left the character")
    out.append("- Token usage (input/output tokens, tool calls)")
    if report_extra:
        out.append(report_extra)

    text = "\n".join(out) + "\n"

    # Safety net: greeting/farewell become literal game commands, so
    # they must be pure US-ASCII (standing ASCII-only rule — the
    # relay strips non-ASCII outbound as a safety net, but a brief
    # should never rely on that).
    for label, value in (("greeting", args.greeting),
                         ("farewell", args.farewell)):
        if value is not None:
            try:
                value.encode("ascii")
            except UnicodeEncodeError:
                bad = sorted(set(c for c in value if ord(c) > 127))
                sys.stderr.write(
                    "NON-ASCII in --%s — brief NOT written: %s\n"
                    % (label, "".join(bad)))
                sys.exit(2)

    # Safety net: no unresolved [BRACKETED] placeholder may ship.
    # The two slot headings below are intentional (house style).
    INTENTIONAL = {"[SESSION GREETING]", "[SESSION FAREWELL]"}
    leftovers = []
    for i, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"\[[A-Z][A-Z0-9 ,/()—-]{4,}\]", line):
            if m.group(0) not in INTENTIONAL:
                leftovers.append("line %d: %s" % (i, m.group(0)))
    if leftovers:
        sys.stderr.write("UNRESOLVED PLACEHOLDERS — brief NOT written:\n")
        sys.stderr.write("\n".join(leftovers) + "\n")
        sys.exit(2)

    if args.out:
        Path(args.out).write_text(text)
        print("wrote %s (%d chars)" % (args.out, len(text)))
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
