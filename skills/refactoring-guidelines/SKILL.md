---
name: refactoring-guidelines
description: Safe refactoring patterns and techniques
---

# Refactoring Guidelines

## When to Refactor
- Code smells: duplication, long methods, large classes
- Before adding new features (make it easy to add)
- When fixing bugs (improve structure)
- When code is hard to understand
- When performance needs improvement

## Refactoring Principles
- **Small steps**: Make one change at a time
- **Tests first**: Ensure you have tests before refactoring
- **Green tests**: Keep tests passing throughout
- **Commit often**: Small, incremental commits
- **Review changes**: Get feedback on refactoring

## Common Refactorings
- **Extract Method**: Break long methods into smaller ones
- **Extract Class**: Split large classes into focused ones
- **Rename**: Use clear, descriptive names
- **Move Method/Field**: Place code where it logically belongs
- **Replace Magic Numbers**: Use named constants
- **Introduce Parameter Object**: Group related parameters
- **Replace Conditional with Polymorphism**: Use inheritance/interfaces

## Safety Checklist
- [ ] All tests pass before starting
- [ ] Understand the code you're refactoring
- [ ] Make one change at a time
- [ ] Run tests after each change
- [ ] Commit working state frequently
- [ ] Review changes before merging
- [ ] Update documentation if needed

## Red Flags
- Don't refactor and add features in the same commit
- Don't refactor code you don't understand
- Don't skip tests "to save time"
- Don't refactor everything at once
- Don't ignore code review feedback
