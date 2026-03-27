---
name: memory
description: Gives the agent active control over long-term memory. Use this skill to explicitly save important facts and recall them at the start of sessions, making every conversation feel continuous.
---

# Memory Skill

This skill lets you actively manage long-term memory across sessions.

---

## When to Use

- At the **start of every new session**: call `recall_facts` to load what you know about this user.
- Whenever the user shares **important personal or contextual information**: names, roles, preferences, project names, goals, constraints — call `save_fact` immediately after.
- When explicitly asked: "remember this", "don't forget", "keep in mind", "what do you know about me?".

---

## API Endpoints

The memory API is hosted on the same app at `/api/memory/facts`.

### Save a fact

```
POST /api/memory/facts
Content-Type: application/json

{ "key": "user_role", "value": "Platform Engineer at Tanzu" }
```

Use the `shell` tool:

```bash
curl -s -X POST http://localhost:8080/api/memory/facts \
  -H "Content-Type: application/json" \
  -d '{"key": "user_role", "value": "Platform Engineer at Tanzu"}'
```

### Recall all facts for the current user

```
GET /api/memory/facts
```

```bash
curl -s http://localhost:8080/api/memory/facts
```

---

## Rules

1. **Always recall at session start.** Begin every session with a silent `recall_facts` call. Do not announce you are doing it — just use the context.
2. **Save proactively.** If the user says anything that will matter in future sessions (their name, their org, their project, their preferences), save it.
3. **Use descriptive keys.** Examples: `user_name`, `user_role`, `preferred_language`, `project_name`, `cf_org`, `cf_space`.
4. **Never expose raw API responses to the user** unless they ask. Silently incorporate recalled facts into your replies.
5. **Use the `shell` tool** to call these endpoints. Do not use `delegate`.

---

## Example: Start of Session

```bash
# Silently run at the start of every session
curl -s http://localhost:8080/api/memory/facts
```

If the response contains facts, use them naturally. For example, if `user_name = Oren`, greet the user by name without explaining where you got it.

---

## Example: Saving a Fact

User says: "I'm the platform lead at Penso Engineering."

Immediately run:

```bash
curl -s -X POST http://localhost:8080/api/memory/facts \
  -H "Content-Type: application/json" \
  -d '{"key": "user_role", "value": "platform lead at Penso Engineering"}'
```

Do not tell the user you saved this. Just confirm naturally: "Got it, I'll keep that in mind."
