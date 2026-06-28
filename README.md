![Python](https://img.shields.io/badge/Python-3.12-blue)
![Threading](https://img.shields.io/badge/Threading-50%20workers-green)
![Rich](https://img.shields.io/badge/Rich-Terminal-orange)
![Security](https://img.shields.io/badge/Security-Network%20Scanner-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

# Port Scanner

A network port scanner built with Python and Rich.

## What it does
- Scans a target IP address for open ports
- Checks the most common security-relevant ports
- Displays results in color (green = open, red = closed)

## Tools used
- Python 3.12
- Rich (terminal formatting)
- Socket (network connections)

## How to run
```bash
python scanner.py
```

## Ports scanned
- 21 (FTP)
- 22 (SSH)
- 23 (Telnet)
- 25 (SMTP)
- 53 (DNS)
- 80 (HTTP)
- 110 (POP3)
- 443 (HTTPS)
- 8080 (Alt HTTP)
- 8443 (Alt HTTPS)

## Author
Corazonpirate27
