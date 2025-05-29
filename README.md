🚀 DigitalOcean Serverless Function (Python + SendGrid) – Windows 11 Setup
🧩 Overview
This project sets up and deploys a serverless function on DigitalOcean Functions that sends emails via SendGrid, using Python 3.11+. Deployment is triggered over HTTP and is managed via the doctl CLI on Windows 11 (PowerShell) using remote build.

📁 Project Structure
bot-sendmail/
│
├── project.yml
├── packages/
│   └── sample/
│       └── email/
│           ├── __main__.py
│           ├── requirements.txt
│           └── build.sh


📦 Key Files
__main__.py
Main handler for sending emails using the sendgrid package. It reads environment variables for API key and sender email using os.environ.
requirements.txt
sendgrid

build.sh
Linux-compatible build script for packaging dependencies:
#!/bin/bash
set -e

virtualenv --no-download virtualenv
pip install --upgrade pip
pip install -r requirements.txt --target virtualenv/lib/python3.11/site-packages

📝 Adjust python3.11 if needed based on your selected Python runtime.
✅ project.yml
name: bot-sendmail
packages:
  sample:
    functions:
      email:
        runtime: python:3.11
        web: true
        env:
          SENDGRID_API_KEY: your-actual-sendgrid-api-key
          VERIFIED_SENDER: your-verified-sender@example.com

🔐 Best Practice: Use environment variables instead of hardcoding secrets in __main__.py.
In your Python code:
import os
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
FROM_EMAIL = os.environ.get("VERIFIED_SENDER")


🛠️ Deployment Steps (Windows 11 – PowerShell)
Download and install doctl manually:
 https://docs.digitalocean.com/reference/doctl/how-to/install/


Add doctl.exe to PATH and test with:

 doctl version


Authenticate:

 doctl auth init


Enable serverless support:

 doctl serverless install


Deploy the function:

 doctl serverless deploy . --remote-build



🧪 Test via HTTP
curl -X POST https://<your-cloud-url>/api/v1/web/sample/email \
  -H "Content-Type: application/json" \
  -d '{
    "to": "recipient@example.com",
    "subject": "Hello from DO",
    "body": "This is a test email sent from a serverless function."
  }'


🧠 Notes
build.cmd is ignored — always use build.sh.


Environment variables are declared in project.yml, not .env files.


Functions are stateless — use env vars or external storage for persistence.


Use os.environ.get("KEY") to safely fetch config in Python.



Let me know if you'd like this exported as a Markdown or PDF file for your records.

