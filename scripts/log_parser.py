#!/usr/bin/env python3
"""Extract failed authentication events from a text log."""
import re
import sys
from collections import Counter

PATTERN = re.compile(
    r"Failed password for (?:invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)"
)

if len(sys.argv) != 2:
    print("Usage: python3 log_parser.py <log_file>")
    raise SystemExit(1)

counts = Counter()
with open(sys.argv[1], encoding="utf-8") as handle:
    for line in handle:
        match = PATTERN.search(line)
        if match:
            user, ip = match.groups()
            counts[ip] += 1
            print(f"FAILED_LOGIN user={user} source_ip={ip}")

print("\nFailed attempts by source IP:")
for ip, count in counts.most_common():
    print(f"{ip}: {count}")
