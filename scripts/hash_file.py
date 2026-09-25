#!/usr/bin/env python3
"""Calculate SHA-256 hash for a file."""
import hashlib
import sys

if len(sys.argv) != 2:
    print("Usage: python3 hash_file.py <file>")
    raise SystemExit(1)

sha256 = hashlib.sha256()
with open(sys.argv[1], "rb") as handle:
    for chunk in iter(lambda: handle.read(8192), b""):
        sha256.update(chunk)

print(f"SHA-256: {sha256.hexdigest()}")
