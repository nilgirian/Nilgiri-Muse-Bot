#!/bin/bash
# SSH via HTTP CONNECT proxy tunnel. Proxy credentials are read from env at runtime, never hardcoded.
exec ssh -o ProxyCommand="python3 $HOME/workspace/nilgiri/proxy_tunnel.py %h %p" -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null "$@"
