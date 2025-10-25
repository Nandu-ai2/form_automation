# Python (Selenium) Assignment - TheMedius.ai

## Overview
This project automates filling a Google Form using Selenium and then emails the results automatically using Flask.

## Files
- **form_filler.py** — Fills out and submits the Google Form.
- **send_email_flask.py** — Sends email submission with attachments.
- **approach.md** — Documentation of how the code works.
- **confirmation.png** — Screenshot of confirmation page.

## Usage
1. Run `pip install selenium flask`
2. Run `python form_filler.py`
3. After form submission, run `python send_email_flask.py`
4. Visit http://127.0.0.1:5000 to send your email automatically.

## Notes
- CAPTCHA field must be filled manually.
- Use a Gmail App Password to send emails securely.
