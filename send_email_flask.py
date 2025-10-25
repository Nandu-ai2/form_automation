# send_email.py
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

SENDER_EMAIL = os.environ.get("SMTP_USER")
SENDER_PASSWORD = os.environ.get("SMTP_PASSWORD")
TO_EMAIL = "tech@themedius.ai"
CC_EMAIL = "hr@themedius.ai"
SUBJECT = "Python (Selenium) Assignment - K.R.S.S Manikanta"

if not SENDER_EMAIL or not SENDER_PASSWORD:
    raise SystemExit("Set SMTP_USER and SMTP_PASSWORD environment variables before running.")

msg = EmailMessage()
msg["From"] = SENDER_EMAIL
msg["To"] = TO_EMAIL
msg["Cc"] = CC_EMAIL
msg["Subject"] = SUBJECT

body = """Dear Team,
Please find attached my completed assignment for the Python (Selenium) task.

Included items:
1. Screenshot of the Google Form confirmation page.
2. Source code (GitHub link below).
3. Brief documentation of my approach.
4. My updated resume.
5. Links to previous projects/work samples.
6. I confirm I am available full time (10 AM – 7 PM) for the next 3–6 months.

GitHub Repository: https://github.com/Nandu-ai2/form_automation.git

Best regards,
K.R.S.S Manikanta
"""
msg.set_content(body)

attachments = [
    "confirmation.png",
    "KRSSManikanta_job_resume.pdf",
    "My Past Projects and its links.pdf",
    "README.md",
    "approach.md"
]

for file in attachments:
    path = Path(file)
    if path.exists():
        msg.add_attachment(path.read_bytes(), maintype="application", subtype="octet-stream", filename=path.name)
    else:
        print(f"Warning: {file} not found")

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)
    print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Failed to send email:", e)
