#!/bin/bash
# SSH via HTTP CONNECT proxy tunnel. Proxy credentials are read from env at runtime, never hardcoded.
# Keepalive tuning (2026-09-28): ServerAliveInterval=15 x ServerAliveCountMax=10
# means ssh waits ~165s of silence (15s idle + 10 unanswered keepalives)
# before aborting the connection itself
# ("Timeout, server nilgiri.net not responding."). The relay's own
# no-output stall detector (STALL_AFTER=150s) fires first and is the
# backstop for a truly dead connection. Note the 2026-09-29 root-cause
# fix: proxy_tunnel.py now clears the 15s setup timeout after CONNECT,
# so quiet-game stretches no longer one-way-kill the tunnel.
exec ssh -o ProxyCommand="python3 $HOME/workspace/nilgiri/proxy_tunnel.py %h %p" -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ServerAliveInterval=15 -o ServerAliveCountMax=10 "$@"
