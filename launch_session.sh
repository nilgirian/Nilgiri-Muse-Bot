#!/bin/bash
# launch_session.sh — single source of truth for session timing.
# Usage: ./launch_session.sh <session#> <budget_minutes> <logfile>
# Sets the relay's SESSION_SECONDS and writes session_active.json from
# the SAME budget, so the driver and relay can never disagree.
# The workflow must then be launched with session_seconds = budget*60.
set -e
cd "$(dirname "$0")"

# --verify mode (Fred approved 2026-10-22): read-only launch checks,
# no launch performed. Folds the mechanical verifications that used
# to be separate manual steps into one command:
#   ./launch_session.sh --verify [logfile]
# Checks: command FIFO is a real FIFO; relay process alive (pidfile
# + pgrep agree); the relay's stdout fd points at the intended log
# (the session-85 "23921" check — a relaunch once wrote a whole leg
# to a file named "23921"); heartbeat fresh (<150s); a PRE-LAUNCH
# meter line for this log exists in run/meter.log; the log's relay
# markers (last IN GAME / EXITED state); session_active.json status.
# Exit 0 = all checks pass, 1 = at least one failure.
if [ "${1:-}" = "--verify" ]; then
  VLOG="${2:-$(ls -t logs/session-*.log 2>/dev/null | head -1)}"
  FAILS=0
  vpass() { echo "VERIFY $1: PASS — $2"; }
  vfail() { echo "VERIFY $1: FAIL — $2"; FAILS=$((FAILS + 1)); }
  echo "VERIFY log: ${VLOG:-<none found>}"
  if [ -p /tmp/mud_cmd ]; then
    vpass "fifo" "/tmp/mud_cmd is a FIFO"
  else
    vfail "fifo" "/tmp/mud_cmd is missing or not a FIFO"
  fi
  RPID=""
  [ -f run/relay.pid ] && RPID="$(cat run/relay.pid 2>/dev/null || true)"
  if [ -n "$RPID" ] && kill -0 "$RPID" 2>/dev/null; then
    vpass "relay-process" "relay alive, pid $RPID"
  else
    vfail "relay-process" "no live relay (pidfile: ${RPID:-none})"
  fi
  PG="$(pgrep -f '[m]ud_relay' | head -1 || true)"
  if [ -n "$RPID" ] && [ -n "$PG" ] && [ "$PG" = "$RPID" ]; then
    vpass "relay-pgrep" "pgrep agrees with pidfile ($RPID)"
  else
    vfail "relay-pgrep" "pgrep found '${PG:-none}', pidfile says '${RPID:-none}'"
  fi
  if [ -n "$RPID" ] && [ -d "/proc/$RPID/fd" ] && [ -n "$VLOG" ]; then
    FD1="$(readlink "/proc/$RPID/fd/1" 2>/dev/null || true)"
    WANT="$(readlink -f "$VLOG" 2>/dev/null || true)"
    if [ -n "$FD1" ] && [ "$FD1" = "$WANT" ]; then
      vpass "relay-fd" "relay stdout -> $VLOG"
    else
      vfail "relay-fd" "relay stdout -> '${FD1:-?}', want '${WANT:-?}'"
    fi
  else
    vfail "relay-fd" "cannot check (relay down or no log given)"
  fi
  if [ -f run/heartbeat ]; then
    AGE=$(( $(date +%s) - $(stat -c %Y run/heartbeat) ))
    if [ "$AGE" -lt 150 ]; then
      vpass "heartbeat" "age ${AGE}s (<150s)"
    else
      vfail "heartbeat" "age ${AGE}s (>=150s — relay presumed dead)"
    fi
  else
    vfail "heartbeat" "run/heartbeat missing"
  fi
  if [ -n "$VLOG" ] && grep -qF "PRE-LAUNCH log=$VLOG" run/meter.log 2>/dev/null; then
    vpass "meter" "PRE-LAUNCH line for $VLOG in run/meter.log"
  else
    vfail "meter" "no PRE-LAUNCH line for ${VLOG:-<none>} in run/meter.log"
  fi
  if [ -n "$VLOG" ] && [ -f "$VLOG" ]; then
    LASTMARK="$(grep -a '>>> ' "$VLOG" | tail -1 || true)"
    echo "VERIFY log-markers: last marker: ${LASTMARK:-<none>}"
    if grep -aq '>>> EXITED' "$VLOG" && \
       [ "$(grep -an '>>> EXITED' "$VLOG" | tail -1 | cut -d: -f1)" -gt \
         "$(grep -an '>>> IN GAME' "$VLOG" | tail -1 | cut -d: -f1 || echo 0)" ]; then
      echo "VERIFY log-markers: NOTE — last EXITED is after last IN GAME (session already closed)"
    fi
  else
    vfail "log-markers" "log file ${VLOG:-<none>} not found"
  fi
  if [ -f run/session_active.json ]; then
    echo "VERIFY session-json: $(python3 -c "import json;d=json.load(open('run/session_active.json'));print('session',d.get('session'),'status',d.get('status'),'budget_end',d.get('budget_end'))" 2>/dev/null || echo 'unreadable')"
  fi
  if [ "$FAILS" -eq 0 ]; then
    echo "VERIFY RESULT: PASS"
    exit 0
  fi
  echo "VERIFY RESULT: FAIL ($FAILS check(s) failed)"
  exit 1
fi

SESSION="$1"; MINUTES="$2"; LOG="$3"
if [ -z "$SESSION" ] || [ -z "$MINUTES" ] || [ -z "$LOG" ]; then
  echo "usage: $0 <session#> <budget_minutes> <logfile>" >&2; exit 1
fi
BUDGET_SECONDS=$((MINUTES * 60))
# Relay and driver share the SAME budget. The driver is told that
# >>> TIME UP is the only retirement trigger — its own clock is
# approximate and must never cause an early stop.
RELAY_SECONDS=$BUDGET_SECONDS
rm -f run/relay.pid
SESSION_SECONDS=$RELAY_SECONDS MUD_PASS="$MUD_PASS" CHAR_PASS="$CHAR_PASS" \
  ./launch_relay.sh "$LOG" 2>&1 | tail -2
python3 - "$SESSION" "$MINUTES" <<'EOF'
import json, sys
from datetime import datetime, timedelta, timezone
pdt = timezone(timedelta(hours=-7))
start = datetime.now(pdt).replace(microsecond=0)
s = {
  "session": int(sys.argv[1]),
  "status": "active",
  "started": start.strftime("%Y-%m-%d %H:%M %Z"),
  "budget_min": int(sys.argv[2]),
  "budget_end": (start + timedelta(minutes=int(sys.argv[2]))).isoformat(),
  "relay_seconds": int(sys.argv[2]) * 60,
  "mission": "",
}
json.dump(s, open("run/session_active.json", "w"), indent=2)
print("session %s active, budget %s min, relay %ss" % (sys.argv[1], sys.argv[2], int(sys.argv[2]) * 60))
EOF
cat > run/driver_inbox.md <<'EOF'
# Driver inbox — FRESH
Operator notes land here; the driver reads this every wake.
EOF
echo "inbox reset; launch the workflow with session_seconds=$BUDGET_SECONDS"
