Requirements

Python 3.9+

An email account with SMTP support (e.g., Gmail – with an App Password)

Note: No extra dependencies are required since only standard libraries are used (csv, os, datetime, smtplib, random).

Configuration
Inside alarm_sistemi.py:

Thresholds: MIN_TEMP and MAX_TEMP (e.g., 800–900°C)

Email: SMTP server, port, sender/receiver addresses

If using Gmail, enable 2FA and create an App Password to use here.

Run

(Optional) Create a virtual environment:

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
