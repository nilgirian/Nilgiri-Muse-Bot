#!/bin/bash
# launch_relay.sh — start the MUD relay fully detached from this shell.
#
# Why: relays started with `nohup ... &` from an exec session have died
# silently ~60-70 minutes after the launching shell exited (sessions 4
# and 12), with no error in the log — consistent with the execution
# environment reaping the process tree of the finished shell. This
# launcher puts the relay (and its FIFO holder) in their OWN session via
# setsid, so nothing that reaps the launching shell's tree can reach it.
#
# Usage:
#   SESSION_SECONDS=7200 MUD_PASS=... CHAR_PASS=... ./launch_relay.sh [logfile]
# Passwords travel in the environment (inherited by the detached child),
# never on a command line. CHAR_NAME defaults to SinMuseBot.
#
# Layout:
#   run/relay.pid        PID of the relay (kill this exact PID at cleanup)
#   run/fifo_holder.pid  PID of the FIFO writer (kill at cleanup too)
#   run/heartbeat        touched by the relay every 60s; a heartbeat older
#                        than ~2 minutes means the relay process is gone
#   /tmp/mud_cmd         the command FIFO (send commands by writing lines)
#
# Cleanup after a clean exit OR a dead relay:
#   kill "$(cat run/relay.pid)" "$(cat run/fifo_holder.pid)" 2>/dev/null
#   rm -f /tmp/mud_cmd
# Forensics after a silent death: `stat -c %y run/heartbeat` is the last
# minute the relay was alive; the session log's last line shows what it
# was doing.
set -u
cd "$(dirname "$0")"
mkdir -p run logs

if [ -f run/relay.pid ]; then
    OLD_PID="$(cat run/relay.pid)"
    if kill -0 "$OLD_PID" 2>/dev/null; then
        echo "A relay is already running as PID $OLD_PID; kill it first." >&2
        exit 1
    fi
fi

LOG="${1:-logs/session-$(date +%Y%m%d-%H%M%S).log}"
rm -f /tmp/mud_cmd
mkfifo /tmp/mud_cmd

# setsid(1): run the child in a brand-new session, detached from this
# shell's process group and controlling terminal. The trailing & plus the
# immediate exit of this script reparents everything to init.
setsid bash -c '
    cd "$0"
    # FIFO holder: keeps the relay'"'"'s stdin open for the whole session.
    # 12h outlasts any session budget; the session ends when the relay
    # itself exits, not when this holder goes away.
    sleep 43200 > /tmp/mud_cmd &
    echo "$!" > run/fifo_holder.pid
    # The relay. Env (MUD_PASS/CHAR_PASS/SESSION_SECONDS/CHAR_NAME) is
    # inherited through setsid — never placed on a command line.
    python3 -u mud_relay.py < /tmp/mud_cmd >> "$1" 2>&1 &
    echo "$!" > run/relay.pid
    echo "launched relay=$(cat run/relay.pid) holder=$(cat run/fifo_holder.pid) log=$1"
' "$(pwd)" "$LOG" > run/launch.out 2>&1 &
sleep 2
cat run/launch.out
echo "Verify: ps -p $(cat run/relay.pid 2>/dev/null) -o pid,pgid,sid,etime,args"
ps -p "$(cat run/relay.pid 2>/dev/null)" -o pid,pgid,sid,etime,args 2>/dev/null || echo "WARNING: relay did not start"
