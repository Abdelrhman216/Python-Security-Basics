#!/usr/bin/env python3
"""Extract IPv4 indicators from text."""
import re
import sys

IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

if len(sys.argv) != 2:
    print("Usage: python3 ioc_extractor.py <text_file>")
    raise SystemExit(1)

text = open(sys.argv[1], encoding="utf-8").read()
ips = sorted(set(IPV4.findall(text)))

for ip in ips:
    octets = ip.split(".")
    if all(0 <= int(o) <= 255 for o in octets):
        print(ip)
