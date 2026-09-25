# Usage Guide

## 1. Port Scanner

Use only against systems you own or are explicitly authorized to test.

```bash
python3 scripts/port_scanner.py 127.0.0.1 22 80 443
```

## 2. Log Parser

```bash
python3 scripts/log_parser.py samples/auth_sample.log
```

## 3. Password Checker

```bash
python3 scripts/password_checker.py
```

The checker reports characteristics only; it does not store the password.

## 4. IP Validator

```bash
python3 scripts/ip_validator.py 10.0.0.1
```

## 5. File Hashing

```bash
python3 scripts/hash_file.py README.md
```

## 6. IOC Extraction

```bash
python3 scripts/ioc_extractor.py samples/auth_sample.log
```
