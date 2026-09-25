# 🐍 Python Security Basics

**Author:** Abdelrhman Ali Saleh  
**Focus:** Cybersecurity Automation • Python • Network Security • SOC Tier 1

## Overview

A practical collection of beginner-friendly Python security utilities designed around common SOC and security tasks.

## Tools

| Tool | Purpose |
|---|---|
| `port_scanner.py` | Check TCP connectivity to selected ports |
| `log_parser.py` | Extract failed authentication events from logs |
| `password_checker.py` | Evaluate basic password characteristics |
| `ip_validator.py` | Validate IPv4 addresses |
| `hash_file.py` | Calculate SHA-256 file hashes |
| `ioc_extractor.py` | Extract IPv4 addresses from text |

## Project Structure

```text
Python-Security-Basics/
├── README.md
├── LICENSE
├── .gitignore
├── scripts/
│   ├── port_scanner.py
│   ├── log_parser.py
│   ├── password_checker.py
│   ├── ip_validator.py
│   ├── hash_file.py
│   └── ioc_extractor.py
├── samples/
│   └── auth_sample.log
├── documentation/
│   └── usage.md
└── tests/
    └── test_security_utils.py
```

## Examples

```bash
python3 scripts/port_scanner.py 127.0.0.1 22 80 443
python3 scripts/log_parser.py samples/auth_sample.log
python3 scripts/password_checker.py
python3 scripts/ip_validator.py 192.168.1.10
python3 scripts/hash_file.py README.md
python3 scripts/ioc_extractor.py samples/auth_sample.log
```

## Security Notes

These tools are for authorized systems and training environments. The port scanner performs basic TCP connection checks and does not attempt exploitation.

## Author

**Abdelrhman Ali Saleh**

GitHub: https://github.com/Abdelrhman216  
LinkedIn: https://www.linkedin.com/in/abdelrhmanalii/
