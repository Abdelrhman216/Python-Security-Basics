#!/usr/bin/env python3
"""IPv4 validation utility."""
import ipaddress
import sys

if len(sys.argv) != 2:
    print("Usage: python3 ip_validator.py <IPv4>")
    raise SystemExit(1)

try:
    address = ipaddress.ip_address(sys.argv[1])
    print(f"Valid IP: {address}")
    print(f"Version: IPv{address.version}")
    print(f"Private: {address.is_private}")
except ValueError:
    print("Invalid IP address")
