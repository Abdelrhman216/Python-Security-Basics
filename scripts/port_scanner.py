#!/usr/bin/env python3
"""Basic TCP port scanner for authorized lab systems.
Author: Abdelrhman Ali Saleh
"""
import socket
import sys

def scan(host, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            result = sock.connect_ex((host, port))
            state = "OPEN" if result == 0 else "CLOSED/FILTERED"
            print(f"{host}:{port} -> {state}")
        except socket.gaierror:
            print(f"Unable to resolve host: {host}")
            break
        finally:
            sock.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 port_scanner.py <host> <port> [port ...]")
        raise SystemExit(1)
    scan(sys.argv[1], [int(p) for p in sys.argv[2:]])
