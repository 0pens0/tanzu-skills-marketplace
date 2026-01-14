# Goose Skills Marketplace

A centralized repository for reusable Goose AI agent skills. This marketplace provides curated, production-ready skills that enhance Goose's capabilities across various development domains.

## Overview

This marketplace provides Goose skills for enhancing development workflows, code quality, and best practices. Skills are organized by domain and can be easily integrated into any Goose configuration.

## Available Skills

### Development Best Practices

- **code-review** - Comprehensive code review checklist covering functionality, quality, and testing
- **testing-strategies** - Guidelines for writing effective tests (unit, integration, e2e)
- **debugging-techniques** - Systematic approaches to debugging code issues
- **refactoring-guidelines** - Safe refactoring patterns and techniques
- **error-handling-patterns** - Best practices for error handling and exception management

### API & Architecture

- **api-design-best-practices** - RESTful API design principles and conventions
- **documentation-writing** - Guidelines for writing clear, maintainable documentation

### Security & Performance

- **security-best-practices** - Common security patterns and vulnerabilities to avoid
- **performance-optimization** - Techniques for improving code performance

### Workflow & Framework

- **git-workflow-best-practices** - Commit message conventions and branching strategies
- **spring-boot-best-practices** - Framework-specific patterns and conventions for Spring Boot

## 🚀 Quick Start

### Using Skills in Your Goose Configuration

Add skills from this repository to your `.goose-config.yml`:

```yaml
skills:
  # Reference skills from this Git repository
  - name: code-review
    source: https://github.com/your-org/goose-skills-marketplace.git
    branch: main
    path: skills/code-review

  - name: testing-strategies
    source: https://github.com/your-org/goose-skills-marketplace.git
    branch: main
    path: skills/testing-strategies

  - name: spring-boot-best-practices
    source: https://github.com/your-org/goose-skills-marketplace.git
    branch: main
    path: skills/spring-boot-best-practices
```

### Using All Skills

To use all skills from this marketplace, add them individually or use a script to generate the configuration:

```yaml
skills:
  - name: code-review
    source: https://github.com/your-org/goose-skills-marketplace.git
    branch: main
    path: skills/code-review
  - name: testing-strategies
    source: https://github.com/your-org/goose-skills-marketplace.git
    branch: main
    path: skills/testing-strategies
  # ... add all skills
```

## Skill Structure

Each skill follows the Goose Skills format with YAML frontmatter:

```markdown
---
name: skill-name
description: Brief description of what this skill teaches
---

# Skill Content

The actual skill content in Markdown format...
```

## How Skills Work

Skills are reusable instruction sets that teach Goose how to perform specific tasks. When a skill is loaded:

1. Goose reads the skill's `SKILL.md` file
2. The skill's instructions are integrated into Goose's context
3. Goose can apply the skill's knowledge when relevant to user requests

Skills seamlessly integrate into your Goose workflow, requiring no special syntax once configured.

## 🔧 For Skill Contributors

### Repository Structure

```
goose-skills-marketplace/
├── skills/
│   ├── code-review/
│   │   └── SKILL.md          # Skill definition with frontmatter
│   ├── testing-strategies/
│   │   └── SKILL.md
│   └── ...
└── README.md
```

### Adding a New Skill

1. Create a new directory under `skills/` with a descriptive name (kebab-case)
2. Create a `SKILL.md` file with:
   - YAML frontmatter containing `name` and `description`
   - Markdown content with the skill's instructions
3. Update this README.md to include the new skill
4. Submit a pull request

### Skill Format Requirements

- **Name**: Must be unique, kebab-case (e.g., `api-design-best-practices`)
- **Description**: One-line description of what the skill teaches
- **Content**: Markdown-formatted instructions, guidelines, or checklists
- **File**: Must be named `SKILL.md` and placed in the skill's directory

### Example Skill Structure

```markdown
---
name: my-new-skill
description: What this skill teaches Goose
---

# My New Skill

## Introduction
This skill teaches Goose about...

## Key Concepts
- Concept 1
- Concept 2

## Best Practices
1. Practice 1
2. Practice 2
```

## Use Cases

**Code Quality:**
- Ensure consistent code review standards across teams
- Apply testing best practices automatically
- Follow refactoring safety guidelines

**Development Workflow:**
- Enforce Git workflow conventions
- Apply framework-specific best practices (Spring Boot, etc.)
- Maintain consistent documentation standards

**Security & Performance:**
- Identify security vulnerabilities
- Optimize code performance
- Follow secure coding practices

## 📋 Skill Management

### Updating Skills

Skills can be updated by:
1. Making changes to the `SKILL.md` file
2. Committing and pushing to the repository
3. Goose will automatically use the latest version from the specified branch

### Versioning

- Use Git branches or tags for versioning if needed
- Default to `main` branch for latest stable skills
- Create version-specific branches for breaking changes

## 🔗 Resources

- [Goose Documentation](https://block.github.io/goose/docs/)
- [Goose Skills Guide](https://block.github.io/goose/docs/guides/context-engineering/using-skills)
- [Goose Configuration Files](https://block.github.io/goose/docs/guides/configuration-files/)

## 📄 License

MIT License - See LICENSE file for details

## 👤 Maintainers

**Tanzu Platform Team**

---

**Built for Goose AI Agent** - Extend your AI development experience with curated best practices!
