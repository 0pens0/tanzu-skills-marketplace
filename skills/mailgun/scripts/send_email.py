#!/usr/bin/env python3
"""Send HTML emails via the Mailgun API."""

import argparse
import os
import sys

import requests


MAILGUN_API_URL = "https://api.mailgun.net/v3/mail.corby.page/messages"
SENDER = "Tanzu Agent <postmaster@corby.page>"


def send_email(recipients: str, subject: str, html_body: str, api_key: str) -> None:
    bcc = os.environ.get("MAILGUN_BCC_ADDRESS", "")

    data: dict[str, str] = {
        "from": SENDER,
        "to": recipients,
        "subject": subject,
        "html": html_body,
    }
    if bcc:
        data["bcc"] = bcc

    response = requests.post(
        MAILGUN_API_URL,
        auth=("api", api_key),
        data=data,
    )

    if response.status_code == 200:
        message_id = response.json().get("id", "unknown")
        print(f"Email sent successfully. Message ID: {message_id}")
    else:
        print(
            f"Failed to send email. Status: {response.status_code}, "
            f"Response: {response.text}",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Send HTML emails via Mailgun API")
    parser.add_argument("recipients", help="Single email or comma-separated list")
    parser.add_argument("subject", help="Email subject line")
    parser.add_argument("html_body", help="Email body in HTML format")
    parser.add_argument(
        "--api-key",
        default=os.environ.get("MAILGUN_API_KEY"),
        help="Mailgun API key (defaults to MAILGUN_API_KEY env var)",
    )
    args = parser.parse_args()

    if not args.api_key:
        print(
            "Error: Mailgun API key required. Set MAILGUN_API_KEY env var or use --api-key.",
            file=sys.stderr,
        )
        sys.exit(1)

    send_email(args.recipients, args.subject, args.html_body, args.api_key)


if __name__ == "__main__":
    main()
