#!/bin/bash
# session_check.sh — one combined per-wake check for the Nilgiri driver.
#
# Usage: session_check.sh [--block <seconds>] <log_path> <offset_file> [inbox_path]
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
#
# --block <seconds> (added 2026-10-21, adapted from SinGrokBot's sg-next):
# before doing the normal check, wait IN SHELL (no model cost) until
# something worth a wake happens, up to <seconds> (clamped 10-240).
# Wake triggers, checked once per second against new log bytes:
#   - any >>> relay marker (speech, TIME UP, RABBIT-AMBUSH, ...)
#   - a corpse (R.I.P. line), combat onset ("fighting" in a prompt),
#     raw speech lines, or ANY other new game output (ACTIVITY)
#   - relay heartbeat going stale (>150s) or vanishing (RELAY-STALE)
# Probe refinement (2026-10-22, Fred approved): the relay's routine
# health probe (">>> PROBE: ... path alive ... probing MUD with
# look", every ~75s of MUD silence) does NOT wake the block — the
# marker and the look output it produces are swallowed so a quiet
# wait can run the full cap. The trouble probe variants (SSH
# PROCESS DEAD, TRANSPORT FAILURE) and every other marker still
# wake immediately, as do corpse/combat/speech lines arriving
# inside or after probe output. Swallowed bytes stay unconsumed:
# the normal check below still prints them after the block ends.
# The block NEVER runs when there is already unread data, when the
# last prompt shows "fighting" (combat keeps the fast loop), or when
# no cursor exists yet. It never advances the cursor itself — the
# normal check below consumes the bytes and prints them as usual.
# A "=== BLOCK ===" line reports how long it waited and why it woke.

set -u

BLOCK=0
if [ "${1:-}" = "--block" ]; then
    BLOCK="${2:-120}"
    shift 2
    case "$BLOCK" in *[!0-9]*|"") BLOCK=120 ;; esac
    [ "$BLOCK" -lt 10 ] && BLOCK=10
    [ "$BLOCK" -gt 240 ] && BLOCK=240
fi

LOG="$1"
OFFSET_FILE="$2"
INBOX="${3:-}"
HEARTBEAT="$HOME/workspace/nilgiri/run/heartbeat"

size=$(stat -c %s "$LOG" 2>/dev/null || echo 0)

# ---- blocking wait (optional; see header) ----
if [ "$BLOCK" -gt 0 ]; then
    if [ ! -f "$OFFSET_FILE" ]; then
        echo "=== BLOCK === SKIPPED (no cursor yet)"
    else
        boffset=$(cat "$OFFSET_FILE")
        [ "$size" -lt "$boffset" ] && boffset=0
        if [ "$size" -gt "$boffset" ]; then
            echo "=== BLOCK === SKIPPED (pending data)"
        elif [ "$(tail -c 600 "$LOG" 2>/dev/null | grep -a -o -E '<[0-9]+h[^>]*>' | tail -1 | grep -c fighting)" = "1" ]; then
            echo "=== BLOCK === SKIPPED (fighting - fast loop stays)"
        else
            bstart=$(date +%s)
            wake="TIMEOUT"
            bmark="$size"
            probe_pending=0
            probes_ignored=0
            routine_probe='>>> PROBE: no MUD output for [0-9]+s; path alive'
            while :; do
                bnow=$(date +%s)
                [ $((bnow - bstart)) -ge "$BLOCK" ] && break
                if [ -f "$HEARTBEAT" ]; then
                    hbage=$(( bnow - $(stat -c %Y "$HEARTBEAT") ))
                    if [ "$hbage" -gt 150 ]; then
                        wake="RELAY-STALE (heartbeat age ${hbage}s)"
                        break
                    fi
                else
                    wake="RELAY-STALE (no heartbeat file)"
                    break
                fi
                cursize=$(stat -c %s "$LOG" 2>/dev/null || echo 0)
                if [ "$cursize" -lt "$bmark" ]; then
                    wake="ACTIVITY (log shrank)"
                    break
                fi
                if [ "$cursize" -gt "$bmark" ]; then
                    peek=$(tail -c +$((bmark + 1)) "$LOG" 2>/dev/null \
                        | head -c $((cursize - bmark)) | tr -d '\000')
                    nonprobe=$(printf '%s\n' "$peek" | grep -a '>>> ' \
                        | grep -a -v -E "$routine_probe" | head -1)
                    if [ -n "$nonprobe" ]; then
                        wake="MARKER: $(printf '%s' "$nonprobe" | cut -c1-120)"
                        break
                    elif printf '%s' "$peek" | grep -a -q "is dead! R.I.P."; then
                        wake="CORPSE"
                        break
                    elif printf '%s' "$peek" | grep -a -q "fighting"; then
                        wake="COMBAT"
                        break
                    elif printf '%s' "$peek" | grep -a -E -q "(says|asks|exclaims|shouts|yells|whispers)( to you)?,? \"|tells you,? \""; then
                        wake="SPEECH"
                        break
                    elif printf '%s' "$peek" | grep -a -q -E "$routine_probe"; then
                        # Routine health probe: swallow this delta. Its
                        # look output may ride along (pending clears if a
                        # prompt already follows the marker) or arrive in
                        # the next delta (pending stays set).
                        probes_ignored=$((probes_ignored + 1))
                        after=$(printf '%s\n' "$peek" \
                            | sed -n '/>>> PROBE: no MUD output for/,$p' \
                            | tail -n +2)
                        if printf '%s' "$after" | grep -a -q -E '<[0-9]+h[^>]*>'; then
                            probe_pending=0
                        else
                            probe_pending=1
                        fi
                        bmark="$cursize"
                    elif [ "$probe_pending" = "1" ]; then
                        # The probe's look output: trigger-free (checked
                        # above), so swallow it too. Pending clears once
                        # a prompt shows the look is complete.
                        if printf '%s' "$peek" | grep -a -q -E '<[0-9]+h[^>]*>'; then
                            probe_pending=0
                        fi
                        bmark="$cursize"
                    else
                        wake="ACTIVITY"
                        break
                    fi
                fi
                sleep 1
            done
            psuffix=""
            [ "$probes_ignored" -gt 0 ] && psuffix=", probes ignored: $probes_ignored"
            echo "=== BLOCK === waited $(( $(date +%s) - bstart ))s of ${BLOCK}s max, wake: $wake$psuffix"
            size=$(stat -c %s "$LOG" 2>/dev/null || echo 0)
        fi
    fi
fi
# ---- end blocking wait ----

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
    # Corpse-loot trigger: any R.I.P. line means something died in the
    # room — fair game, loot it. Fires for the bot's own kills too (the
    # driver already loots those); the point is to catch kills by
    # deputies, guards, other players, or other mobs.
    printf '%s\n' "$newbytes" | grep -a "is dead! R.I.P." | tail -2 | \
        while IFS= read -r line; do
            echo ">>> CORPSE-LOOT: $line — run 'get all from corpse' NOW"
        done
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
