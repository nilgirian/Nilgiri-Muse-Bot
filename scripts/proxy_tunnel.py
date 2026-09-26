#!/usr/bin/env python3
"""Tunnel TCP via HTTP CONNECT proxy for ssh ProxyCommand. Reads proxy from env."""
import os, sys, socket, base64, threading
from urllib.parse import urlparse

def get_proxy():
    for k in ("ALL_PROXY", "all_proxy", "HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy"):
        v = os.environ.get(k)
        if v:
            return v
    return None

def forward(src, dst):
    try:
        while True:
            data = src.recv(16384)
            if not data:
                break
            dst.sendall(data)
    except Exception:
        pass
    try:
        dst.shutdown(socket.SHUT_WR)
    except OSError:
        pass

def main():
    if len(sys.argv) != 3:
        sys.stderr.write("usage: proxy_tunnel.py <host> <port>\n")
        sys.exit(1)
    dest_host, dest_port = sys.argv[1], sys.argv[2]
    proxy_url = get_proxy()
    if not proxy_url:
        sys.stderr.write("no proxy env\n")
        sys.exit(1)
    p = urlparse(proxy_url)
    proxy_host, proxy_port = p.hostname, p.port or 8080
    s = socket.create_connection((proxy_host, proxy_port), timeout=15)
    req = f"CONNECT {dest_host}:{dest_port} HTTP/1.1\r\nHost: {dest_host}:{dest_port}\r\n"
    if p.username:
        token = base64.b64encode(f"{p.username}:{p.password}".encode()).decode()
        req += f"Proxy-Authorization: Basic {token}\r\n"
    req += "\r\n"
    s.sendall(req.encode())
    resp = b""
    while b"\r\n\r\n" not in resp:
        chunk = s.recv(4096)
        if not chunk:
            break
        resp += chunk
    status = resp.split(b"\r\n", 1)[0].decode(errors="replace") if resp else ""
    if " 200 " not in status:
        sys.stderr.write(f"CONNECT failed: {status}\n")
        sys.exit(1)
    # Now s is the tunnel. Connect it to stdin/stdout.
    # Use socket pair for stdio forwarding via threads
    stdin_buf = sys.stdin.buffer.raw if hasattr(sys.stdin.buffer, 'raw') else sys.stdin.buffer
    stdout_buf = sys.stdout.buffer.raw if hasattr(sys.stdout.buffer, 'raw') else sys.stdout.buffer
    # We need file descriptors; use os.read/os.write with threads
    def stdin_to_sock():
        try:
            while True:
                data = os.read(0, 16384)
                if not data:
                    break
                s.sendall(data)
        except Exception:
            pass
        try:
            s.shutdown(socket.SHUT_WR)
        except OSError:
            pass
    def sock_to_stdout():
        try:
            while True:
                data = s.recv(16384)
                if not data:
                    break
                os.write(1, data)
        except Exception:
            pass
    t1 = threading.Thread(target=stdin_to_sock, daemon=True)
    t2 = threading.Thread(target=sock_to_stdout, daemon=True)
    t1.start(); t2.start()
    t1.join(); t2.join()

if __name__ == "__main__":
    main()
