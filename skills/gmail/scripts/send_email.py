#!/usr/bin/env python3
"""Send HTML emails via Gmail SMTP using an App Password."""

import argparse
import os
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


def send_email(
    recipients: str,
    subject: str,
    html_body: str,
    gmail_address: str,
    app_password: str,
) -> None:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = gmail_address
    msg["To"] = recipients
    msg.attach(MIMEText(html_body, "html"))

    recipient_list = [r.strip() for r in recipients.split(",")]

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(gmail_address, app_password)
        smtp.sendmail(gmail_address, recipient_list, msg.as_string())

    print(f"Email sent successfully to {recipients}.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Send HTML emails via Gmail SMTP")
    parser.add_argument("recipients", help="Single email or comma-separated list")
    parser.add_argument("subject", help="Email subject line")
    parser.add_argument("html_body", help="Email body in HTML format")
    args = parser.parse_args()

    gmail_address = os.environ.get("GMAIL_ADDRESS")
    app_password = os.environ.get("GMAIL_APP_PASSWORD")

    if not gmail_address:
        print(
            "Error: GMAIL_ADDRESS environment variable is required.",
            file=sys.stderr,
        )
        sys.exit(1)

    if not app_password:
        print(
            "Error: GMAIL_APP_PASSWORD environment variable is required.",
            file=sys.stderr,
        )
        sys.exit(1)

    send_email(args.recipients, args.subject, args.html_body, gmail_address, app_password)


if __name__ == "__main__":
    main()
