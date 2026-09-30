#!/bin/bash
# session_check.sh — one combined per-wake check for the Nilgiri driver.
#
# Usage: session_check.sh <log_path> <offset_file> [inbox_path]
#
# Prints everything the driver needs for one wake in a single compact
# block, then advances its cursor:
#   1. New log bytes since the last check (cursor in <offset_file>).
#   2. Any >>> relay markers inside the new bytes (SPEECH, TIME UP,
#      STALL, RECONNECTING...). Markers are extracted BEFORE output is
#      truncated, so they are never lost.
#   3. Relay heartbeat age in seconds.
#   4. Operator inbox contents (when inbox_path is given).
#
# This replaces three separate per-wake tool calls (tail, grep, stat)
# with one — fewer round trips, far less re-reading. On the very first
# run the cursor starts at end-of-file (no backlog dump); the driver's
# opening verification (score/inventory/where) covers state separately.
#
# Empty NEW LOG section = nothing happened since last wake. Normal.

set -u

LOG="$1"
OFFSET_FILE="$2"
INBOX="${3:-}"
HEARTBEAT="$HOME/workspace/nilgiri/run/heartbeat"

size=$(stat -c %s "$LOG" 2>/dev/null || echo 0)

if [ -f "$OFFSET_FILE" ]; then
    offset=$(cat "$OFFSET_FILE")
    # The log never rotates mid-session; if it shrank, restart the cursor.
    [ "$size" -lt "$offset" ] && offset=0
else
    offset=$size
    echo "$size" > "$OFFSET_FILE"
    echo "=== NEW LOG (cursor initialized at byte $size, no backlog) ==="
    echo "=== MARKERS ==="
    echo "=== HEARTBEAT ==="
    if [ -f "$HEARTBEAT" ]; then
        echo "age=$(( $(date +%s) - $(stat -c %Y "$HEARTBEAT") ))s"
    else
        echo "age=NO_HEARTBEAT_FILE"
    fi
    [ -n "$INBOX" ] && [ -f "$INBOX" ] && { echo "=== INBOX ==="; cat "$INBOX"; }
    exit 0
fi

newbytes=""
if [ "$size" -gt "$offset" ]; then
    newbytes=$(tail -c +$((offset + 1)) "$LOG" 2>/dev/null | tr -d '\000')
fi
echo "$size" > "$OFFSET_FILE"

echo "=== NEW LOG (bytes $offset-$size) ==="
[ -n "$newbytes" ] && printf '%s\n' "$newbytes" | tail -c 1500

echo "=== MARKERS ==="
if [ -n "$newbytes" ]; then
    printf '%s\n' "$newbytes" | grep -a ">>> " | tail -5
fi

echo "=== HEARTBEAT ==="
if [ -f "$HEARTBEAT" ]; then
    echo "age=$(( $(date +%s) - $(stat -c %Y "$HEARTBEAT") ))s"
else
    echo "age=NO_HEARTBEAT_FILE"
fi

if [ -n "$INBOX" ] && [ -f "$INBOX" ]; then
    echo "=== INBOX ==="
    cat "$INBOX"
fi
