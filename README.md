# Form Automation Assignment (Python + Selenium + Flask)

## Introduction

This project automates the process of filling out a Google Form, taking a screenshot of the confirmation page, and sending all the required submission files automatically through email.

It was created as part of the **Python (Selenium) Assignment** for *The Medius AI*.

The project uses **Selenium** for browser automation and **Flask** (along with SMTP) for sending the email.

---

## What the Project Does

1. Opens a Google Form automatically using Selenium.
2. Fills out all required fields with pre-defined answers.
3. Submits the form and saves a screenshot of the confirmation page.
4. Sends an email (via Flask) with the screenshot, source code, documentation, and resume attached.
5. Uses permanent environment variables for secure Gmail credentials.

---

## Technologies Used

* **Python 3.11+**
* **Selenium**
* **Flask**
* **smtplib**
* **dotenv / environment variables**

---

## Folder Structure

```
form_automation/
│
├── form_fill.py               # Automates Google Form filling
├── send_email_flask.py        # Sends the final email with attachments
├── requirements.txt           # Dependencies list
├── screenshots/               # Folder where screenshots are saved
└── README.md                  # Project documentation
```

---

## Step-by-Step Setup Guide

### Step 1: Open the Project

Extract the ZIP file or open the project folder `form_automation` on your system.

---

### Step 2: Create and Activate Virtual Environment

Open PowerShell or VS Code terminal in the project folder and run:

```bash
python -m venv venv
.\venv\Scripts\activate
```

---

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### Step 4: Set Permanent Environment Variables (Gmail Setup)

We use environment variables to store your Gmail and app password securely.

1. Open:
   **Control Panel → System → Advanced system settings → Environment Variables**
2. Under **User variables for [your username]**, click **New**.
3. Add the following:

   * **Variable name:** `SMTP_USER`
     **Value:** `your_email@gmail.com`
   * **Variable name:** `SMTP_PASSWORD`
     **Value:** `your_app_password`
     *(Use a Google App Password — generated from your Gmail account security settings.)*
4. Click **OK** to save both variables.
5. Close and reopen your terminal to apply the changes.

---

### Step 5: Run the Form Automation

Run the script to fill out the Google Form automatically:

```bash
python form_fill.py
```

This will:

* Launch Chrome,
* Fill the form,
* Submit it,
* And save a confirmation screenshot inside `/screenshots/`.

---

### Step 6: Send the Submission Email

Now send the final email using Flask:

```bash
python send_email_flask.py
```

If everything is configured properly, you’ll see:

```
✅ Email sent successfully!
```

The email will automatically include:

1. Screenshot of the form submission
2. GitHub link or source code
3. This README file
4. Your resume
5. Work sample/project links
6. Confirmation of availability (10 AM – 7 PM for 3–6 months)

---

## Common Issues & Fixes

| Issue                                                                   | Fix                                                                                       |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `Set SMTP_USER and SMTP_PASSWORD environment variables before running.` | Add them permanently using Windows Environment Variables (not temporary PowerShell ones). |
| Chrome not opening                                                      | Check if ChromeDriver matches your Chrome version.                                        |
| Email not sent                                                          | Use a valid App Password and check internet connectivity.                                 |
| Screenshot missing                                                      | Ensure `/screenshots/` folder exists and has write permissions.                           |

---

## Final Deliverables

Once complete, submit the following to **[tech@themedius.ai](mailto:tech@themedius.ai)** (CC: **[hr@themedius.ai](mailto:hr@themedius.ai)**):

1. Screenshot (PDF/PNG/JPG) of form confirmation page
2. Source code (GitHub or ZIP)
3. Documentation (this file)
4. Resume
5. Work samples/links
6. Availability confirmation

---

## Author

**Name:** K.R.S.S Manikanta
**Email:** [kesireddynandu004@gmail.com](mailto:kesireddynandu004@gmail.com)
**Availability:** Full-time (10 AM – 7 PM) for 3–6 months

---

### Notes

* Do not share your Gmail app password publicly.
* Always close Chrome properly after Selenium runs.
* This project is for learning and demonstration purposes only.
