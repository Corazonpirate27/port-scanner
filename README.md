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
