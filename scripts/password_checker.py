#!/usr/bin/env python3
"""Basic password-strength characteristics checker."""
import getpass
import string

password = getpass.getpass("Password: ")

checks = {
    "Length >= 12": len(password) >= 12,
    "Uppercase": any(c.isupper() for c in password),
    "Lowercase": any(c.islower() for c in password),
    "Digit": any(c.isdigit() for c in password),
    "Special character": any(c in string.punctuation for c in password),
}

for name, passed in checks.items():
    print(f"[{'OK' if passed else 'MISSING'}] {name}")

score = sum(checks.values())
print(f"Score: {score}/{len(checks)}")
