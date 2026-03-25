#!/usr/bin/env python3
"""Post messages to Google Chat Spaces via the Google Chat API."""

import json
import os
import sys

import requests


GOOGLE_CHAT_API = "https://chat.googleapis.com/v1/spaces/{space_id}/messages"


def get_spaces_config() -> dict:
    raw = os.environ.get("GOOGLE_CHAT_SPACES", "")
    if not raw:
        print(
            "Error: GOOGLE_CHAT_SPACES environment variable is not set.",
            file=sys.stderr,
        )
        sys.exit(1)
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"Error: GOOGLE_CHAT_SPACES contains invalid JSON: {exc}", file=sys.stderr)
        sys.exit(1)


def post_message(space_name: str, message_text: str) -> None:
    spaces = get_spaces_config()

    if space_name not in spaces:
        available = ", ".join(sorted(spaces.keys()))
        print(
            f"Error: Space '{space_name}' not found in configuration.\n"
            f"Available spaces: {available}",
            file=sys.stderr,
        )
        sys.exit(1)

    config = spaces[space_name]
    space_id = config["space_id"]
    key = config["key"]
    token = config["token"]

    # Convert literal \n sequences to real newlines
    text = message_text.replace("\\n", "\n")

    url = GOOGLE_CHAT_API.format(space_id=space_id)
    params = {"key": key, "token": token}
    payload = {"text": text}

    response = requests.post(url, params=params, json=payload)

    if response.status_code == 200:
        print(f"Message posted successfully to '{space_name}'.")
    else:
        print(
            f"Failed to post message. Status: {response.status_code}, "
            f"Response: {response.text}",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    if len(sys.argv) != 3:
        print(
            f"Usage: {sys.argv[0]} <space_name> <message_text>",
            file=sys.stderr,
        )
        sys.exit(1)

    space_name = sys.argv[1]
    message_text = sys.argv[2]
    post_message(space_name, message_text)


if __name__ == "__main__":
    main()
