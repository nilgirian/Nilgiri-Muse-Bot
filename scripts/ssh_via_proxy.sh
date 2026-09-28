#!/bin/bash
# SSH via HTTP CONNECT proxy tunnel. Proxy credentials are read from env at runtime, never hardcoded.
# Keepalive tuning (2026-09-28): ServerAliveInterval=15 x ServerAliveCountMax=10
# means ssh waits up to 150s of silence before aborting the connection itself
# ("Timeout, server nilgiri.net not responding."). The MUD game was never down
# during those stalls — the break is in the VM -> proxy -> nilgiri.net path —
# so riding through transient stalls beats dropping and re-logging. The relay's
# own no-output stall detector (STALL_AFTER=150s) is the backstop for a truly
# dead connection.
exec ssh -o ProxyCommand="python3 $HOME/workspace/nilgiri/proxy_tunnel.py %h %p" -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ServerAliveInterval=15 -o ServerAliveCountMax=10 "$@"
