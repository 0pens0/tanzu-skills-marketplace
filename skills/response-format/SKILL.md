---
name: response-format
description: Output formatting guidelines for multi-step tasks. Apply these rules to all responses involving more than one action so output is structured, scannable, and easy to follow.
---

# Response Formatting Guidelines

Apply these rules whenever you execute a task that involves more than one action (creating files, running commands, calling APIs, deploying apps, etc.).

## Before You Start

Open with a short execution plan as a numbered list:

**Plan:**
1. Brief description of step one
2. Brief description of step two
3. …

## During Execution

Use a level-2 heading for each step as you begin it:

```
## Step 1: Create the repository
```

End each step with a one-line status indicator:
- `✅ Done — <brief result, e.g. repo created at https://...>`
- `❌ Failed — <brief reason and what you will try next>`
- `⚠️ Warning — <non-fatal issue noted>`

Keep prose inside a step to one or two short sentences maximum. Prefer bullet points over paragraphs for listing details, outputs, or options.

Use fenced code blocks for all commands, file paths, URLs, and terminal output — never inline these in prose.

## After Completion

Always close with a `## Summary` section that lists every step and its outcome:

```markdown
## Summary
- ✅ Step 1: Created GitHub repo at https://github.com/org/repo
- ✅ Step 2: Built the JAR — 4.2 MB
- ✅ Step 3: Pushed to CF — running at https://app.example.com
- ❌ Step 4: Smoke test failed — HTTP 502, check CF logs
```

## General Rules

- **Never** run multiple completed steps together into one paragraph.
- **Never** repeat information already shown in a previous step.
- If a step produces important output (URLs, IDs, error messages), show it in a code block, not inline.
- Keep the overall tone concise. Assume the reader will scan, not read word-by-word.
