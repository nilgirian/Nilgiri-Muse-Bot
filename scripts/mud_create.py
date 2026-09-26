#!/usr/bin/env python3
"""Persistent MUD character creation for Nilgiri.
Uses pexpect to drive ssh via proxy tunnel without disconnecting.
Reads MUD_PASS, CHAR_NAME, CHAR_EMAIL from env. Logs to /tmp/mud_session.log.
Exits with code 10 when temp-password prompt is reached (needs user input).

NOTE: experimental — broad prompt matching proved unreliable; prefer
mud_wait_for_pass.exp for real creation runs.
"""
import os, sys, re, time
import pexpect

LOG = "/tmp/mud_session.log"
EMAIL = os.environ.get("CHAR_EMAIL", "")
CHAR = os.environ.get("CHAR_NAME", "")
MUD_PASS = os.environ.get("MUD_PASS", "")
if not EMAIL or not CHAR:
    print("CHAR_NAME and CHAR_EMAIL must be set in env")
    sys.exit(4)

# Known answers in order; for Select prompts we pick these
answers = {
    "text color": "yes",
    "by what name": CHAR,
    "did i get that right": "yes",
    "please enter your e-mail": EMAIL,
    "confirm by retyping": EMAIL,
    "female or male": "male",
    "select your race": "human",
    "do you wish to be human": "yes",
    "hair shape": "straight",
    "hair length": "short",
    "hair color": "brown",
    "skin complexion": "tan",
    "eye color": "brown",
    "height": "average",
    "weight": "average",
    "select your class": "warrior",
    "select your alignment": "neutral",
}

def log(msg):
    with open(LOG, "a") as f:
        f.write(msg + "\n")
    print(msg, flush=True)

def main():
    # Clear log
    open(LOG, "w").write("")
    cmd = os.path.expanduser("~/workspace/nilgiri/ssh_via_proxy.sh")
    log(f"Spawning {cmd} player@nilgiri.net")
    child = pexpect.spawn(cmd, ["player@nilgiri.net"], encoding="utf-8", timeout=30)
    # Log all output to file as well
    child.logfile_read = open(LOG, "a")

    def expect_and_respond():
        # We loop, matching prompts
        while True:
            # Patterns to watch for
            idx = child.expect([
                r"(?i)password:\s*$",                    # 0 ssh password
                r"Do you want text color",              # 1 (ANSI-tolerant)
                r"By what name do you wish to be known", # 2
                r"Did I get that right",                # 3
                r"Please enter your e-mail address:",   # 4
                r"Confirm by retyping",                 # 5
                r"Are you female or male",              # 6
                r"Select your race:",                    # 7
                r"Do you wish to be human",              # 8
                r"Select your hair shape:",             # 9
                r"Select your hair length:",            # 10
                r"Select your hair color:",             # 11
                r"Select your skin complexion:",        # 12
                r"Select your eye color:",              # 13
                r"Select your eye shape:",              # 14 eye shape
                r"Select your class:",                  # 15
                r"Select your alignment:",             # 16
                r"(?i)temporary password.*:",           # 17 TEMP PASSWORD PROMPT - stop
                r"(?i)enter.*code.*:",                  # 18 alt code prompt
                r"\(yes/no\)",                          # 19 generic yes/no (ANSI-tolerant)
                r"\?",                                  # 20 generic "?" select prompt
                pexpect.TIMEOUT,
                pexpect.EOF,
            ])
            if idx == 0:
                log("[->] sending SSH password")
                child.sendline(MUD_PASS)
            elif idx == 1:
                child.sendline("yes")
            elif idx == 2:
                child.sendline(CHAR)
            elif idx == 3:
                child.sendline("yes")
            elif idx == 4:
                child.sendline(EMAIL)
            elif idx == 5:
                child.sendline(EMAIL)
            elif idx == 6:
                child.sendline("male")
            elif idx == 7:
                child.sendline("human")
            elif idx == 8:
                child.sendline("yes")
            elif idx == 9:
                child.sendline("straight")
            elif idx == 10:
                child.sendline("short")
            elif idx == 11:
                child.sendline("brown")
            elif idx == 12:
                child.sendline("tan")
            elif idx == 13:
                child.sendline("brown")
            elif idx == 14:
                child.sendline("almond")
            elif idx == 15:
                child.sendline("warrior")
            elif idx == 16:
                child.sendline("neutral")
            elif idx in (17, 18):
                log("[!!] TEMP PASSWORD PROMPT REACHED - need user input")
                # Leave session alive? For now exit 10 so orchestrator can ask user
                # Try to keep child alive in background? We'll just exit and let user know
                sys.exit(10)
            elif idx == 19:
                # Generic yes/no -> yes
                log("[->] generic yes/no -> yes")
                child.sendline("yes")
            elif idx == 20:
                # Generic select - try to extract options from before buffer
                before = child.before or ""
                # Find listed options (lines with 2+ spaces indent)
                opts = re.findall(r"^\s{2,}(\S[^\r\n]*)$", before, re.M)
                # Filter to last block of options
                log(f"[?] generic select prompt, options seen: {opts[-8:] if opts else 'none'}")
                # Try common defaults
                # Send the first option's first word if we have it
                if opts:
                    guess = opts[0].strip().split()[0]
                    log(f"[->] trying '{guess}'")
                    child.sendline(guess)
                else:
                    child.sendline("")
            elif idx == 21:  # TIMEOUT
                log(f"[timeout] before={repr((child.before or '')[-200:])}")
                # Continue waiting
                continue
            elif idx == 22:  # EOF
                log("[eof] session ended")
                break

    try:
        expect_and_respond()
    except Exception as e:
        log(f"[error] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
