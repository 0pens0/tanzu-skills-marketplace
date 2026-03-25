---
name: response-format
description: Output formatting guidelines for multi-step tasks. Apply these rules to all responses involving more than one action so output is structured, scannable, and easy to follow.
---

# Response Formatting Guidelines

Apply these rules to every response that involves more than one action.

---

## Critical Markdown Rules

These rules are non-negotiable:

1. **A blank line is required after every `##` heading.** Without it, markdown renders the heading as plain text and the content runs together.
2. **Never write a heading and its first sentence on the same line.** The heading states the goal only; content begins on the line below (after a blank line).
3. **Every intermediate action, finding, error, or decision is a bullet point (`-`).** No prose paragraphs inside a step.

---

## Structure for Every Multi-Step Task

### 1. Open with a Plan

Before doing anything, list what you will do:

**Plan:**
1. Step one — one-line description
2. Step two — one-line description
3. Step three — one-line description

---

### 2. Format Each Step Like This (exact template)

```
## Step N: Goal of this step

- Action or finding #1
- Action or finding #2
  - Sub-detail if needed
- Action or finding #3

✅ Done — one-line result
```

**Rules for steps:**
- The `##` heading contains only the goal, nothing else.
- There must be a blank line between the heading and the first bullet.
- Each action, check, finding, error, or pivot gets its own bullet.
- Commands, file paths, URLs, and terminal output go in fenced code blocks, not inline.
- End every step with exactly one status line: `✅ Done`, `❌ Failed`, or `⚠️ Warning`, followed by a brief result.

---

### 3. Worked Example

This is what correct output looks like:

---

**Plan:**
1. Check for Java installation
2. Build the application
3. Push to Cloud Foundry

## Step 1: Check for Java installation

- Running `java -version`...
- Java is not installed on this system.
- Checked for Maven — also unavailable.
- No sudo permissions to install packages.

⚠️ Warning — Java unavailable; switching to a Node.js app that requires no compilation.

## Step 2: Build the Node.js application

- Created `app.js` with a simple HTTP server.
- Created `package.json` with start script.

✅ Done — Node.js app ready in `/tmp/hello-world/`.

## Step 3: Push to Cloud Foundry

- Targeted org `demo` / space `sandbox`.
- Running `cf push hello-world`...

```
requested state: started
routes: hello-world.apps.example.com
```

✅ Done — app running at `https://hello-world.apps.example.com`.

## Summary

- ✅ Step 1: Java unavailable — pivoted to Node.js
- ✅ Step 2: Node.js app built
- ✅ Step 3: Deployed to CF at `https://hello-world.apps.example.com`

---

### 4. What NOT to Do

❌ **Wrong** — heading merged with content, no blank line, no bullets:

```
## Step 3: Build the applicationLet me check for Java:Java is not installed.
Let me try something else. I don't have sudo. Let me use Node.js instead.
```

✅ **Correct** — heading alone, blank line, one bullet per action:

```
## Step 3: Build the application

- Checking for Java — not installed.
- Checking for Maven — not available.
- No sudo permissions to install packages.
- Switching to Node.js (no compilation required).

✅ Done — Node.js app created.
```

---

## After All Steps: Summary

Always close with a `## Summary` section listing every step and its status:

```
## Summary

- ✅ Step 1: short description of outcome
- ✅ Step 2: short description of outcome
- ❌ Step 3: what failed and why
```
