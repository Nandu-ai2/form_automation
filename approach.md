# Approach Summary

## Step 1: Automate Form Filling
- Used Selenium WebDriver to open the Google Form.
- Identified input fields using CSS selectors (`input.whsOnd`).
- Filled all fields automatically using pre-defined data.
- For the CAPTCHA (last field), user input is required manually.
- After submission, took a screenshot of the confirmation page.

## Step 2: Automate Email Submission
- Used Python Flask to build a simple email-sending API.
- Integrated SMTP with Gmail App Password for secure sending.
- Attached confirmation screenshot, resume, and documentation.
- Email automatically sends to themedius.ai (TO + CC) with required info.

## Step 3: GitHub Repository
- Uploaded source code and documentation to GitHub.
