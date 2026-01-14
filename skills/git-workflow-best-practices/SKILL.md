---
name: git-workflow-best-practices
description: Commit message conventions and branching strategies
---

# Git Workflow Best Practices

## Commit Messages
- Use present tense: "Add feature" not "Added feature"
- Use imperative mood: "Fix bug" not "Fixes bug"
- Keep first line under 50 characters
- Add detailed explanation if needed (blank line, then details)
- Reference issues: "Fix #123" or "Closes #456"
- Be specific: "Fix null pointer in user service" not "Fix bug"

## Commit Structure
```
Short summary (50 chars or less)

More detailed explanation if needed. Wrap at 72 characters.
Explain what and why, not how.

- Bullet points are okay
- Use them for multiple changes

Fixes #123
```

## Branching Strategy
- **main/master**: Production-ready code
- **develop**: Integration branch for features
- **feature/**: New features (e.g., `feature/user-authentication`)
- **bugfix/**: Bug fixes (e.g., `bugfix/login-error`)
- **hotfix/**: Urgent production fixes
- **release/**: Preparing releases

## Branch Naming
- Use descriptive names: `feature/add-payment-gateway`
- Use kebab-case: lowercase with hyphens
- Include issue number if applicable: `feature/123-user-profile`
- Keep names concise but clear

## Commit Frequency
- Commit often: Small, logical units of work
- Commit working code: Don't commit broken code
- One logical change per commit
- Don't mix unrelated changes
- Commit before leaving work (save progress)

## Pull Request Best Practices
- Keep PRs small and focused
- Write clear PR descriptions
- Link related issues
- Request specific reviewers
- Address review feedback promptly
- Keep PRs up to date with base branch
- Delete branches after merge
