---
name: gmail
description: Send HTML emails via Gmail using SMTP. Use when the user requests to send an email, notify someone via email, or compose and deliver email messages to recipients. Supports single or multiple recipients with dynamically generated subjects and HTML content based on context.
---

# Gmail Email Sender

Send HTML emails through Gmail SMTP with context-aware subject and body generation. All emails are sent as HTML for rich formatting support.

## Configuration

- **SMTP Host**: `smtp.gmail.com:587` (STARTTLS)
- **Authentication**: Gmail address and App Password required via `GMAIL_ADDRESS` and `GMAIL_APP_PASSWORD` environment variables
- **Sender**: The value of `GMAIL_ADDRESS` (e.g. `you@gmail.com`)

> **Note**: `GMAIL_APP_PASSWORD` is a 16-character Google App Password, not your regular Gmail password.
> Generate one at https://myaccount.google.com/apppasswords (requires 2-Step Verification enabled).

## Workflow

When the user requests sending an email:

1. **Identify recipients**: Extract email addresses from the request
2. **Generate content**: Create an appropriate subject line and email body based on context
3. **Execute script**: Use `scripts/send_email.py` to send the email

## Script Usage

The bundled `send_email.py` script handles all Gmail SMTP communication and sends HTML emails:

```bash
python3 scripts/send_email.py <recipients> <subject> <html_body>
```

### Arguments

- `recipients`: Single email or comma-separated list (e.g., `user@example.com` or `user1@example.com,user2@example.com`)
- `subject`: Email subject line
- `html_body`: Email body in HTML format (supports full HTML markup)

## Examples

### Single Recipient

User request: *"Send an email to alice@example.com about the Q4 architecture review meeting tomorrow at 2pm"*

```bash
python3 scripts/send_email.py \
  "alice@example.com" \
  "Reminder: Q4 Architecture Review Tomorrow" \
  "<html>
<body>
<p>Hi Alice,</p>

<p>This is a reminder about our <strong>Q4 Architecture Review</strong> meeting scheduled for tomorrow at <strong>2:00 PM</strong>.</p>

<p>We'll be covering:</p>
<ul>
  <li>Current platform architecture</li>
  <li>Proposed improvements</li>
  <li>Migration strategy</li>
  <li>Q&amp;A session</li>
</ul>

<p>Looking forward to seeing you there!</p>

<p>Best regards,<br>
Goose Agent</p>
</body>
</html>"
```

### Multiple Recipients

User request: *"Email the team about the deployment being complete"*

```bash
python3 scripts/send_email.py \
  "alice@example.com,bob@example.com" \
  "Deployment Complete: Production Environment" \
  "<html>
<body>
<p>Hi Team,</p>

<p>The production deployment has been completed successfully. All services are running normally.</p>

<p>Best regards,<br>
Goose Agent</p>
</body>
</html>"
```

## Content Generation Guidelines

**Subject Lines:**
- Keep concise (under 60 characters)
- Make purpose immediately clear
- Professional but friendly tone
- Examples: "Meeting Reminder: Q4 Planning", "Update: Deployment Status"

**HTML Email Body:**
- Always wrap content in `<html>...<body>...</body></html>` tags
- Use `<p>` tags for paragraphs
- Use `<strong>` for bold and `<em>` for italic text
- Use `<ul>` and `<li>` for bullet lists, `<ol>` for numbered lists
- Use `<br>` for line breaks within paragraphs
- Use `<a href="...">` for hyperlinks
- Escape special characters (e.g., `&amp;` for &)
- Start with appropriate greeting
- State purpose clearly upfront
- Include relevant context from the user's request
- Close professionally

## Notes

- Script uses Python standard library only (`smtplib`, `email`) — no pip install required
- Script handles single recipients or comma-separated lists
- Sender address is read from `GMAIL_ADDRESS` environment variable
- Script outputs success/failure status
