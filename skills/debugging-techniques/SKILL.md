---
name: debugging-techniques
description: Systematic approaches to debugging code issues
---

# Debugging Techniques

## Systematic Approach
1. **Reproduce the issue** - Can you consistently reproduce it?
2. **Isolate the problem** - Narrow down to the smallest failing case
3. **Check assumptions** - Verify your understanding of how the code should work
4. **Read error messages carefully** - They often point to the exact issue
5. **Use logging strategically** - Add logs at key decision points

## Debugging Tools
- Use breakpoints and step through code
- Inspect variable values at runtime
- Use conditional breakpoints for specific scenarios
- Check call stack to understand execution flow
- Use profilers to identify performance bottlenecks

## Common Issues
- **Null pointer exceptions**: Check for null before dereferencing
- **Off-by-one errors**: Verify loop boundaries and array indices
- **Race conditions**: Check for thread safety issues
- **Memory leaks**: Verify resources are properly closed
- **Logic errors**: Trace through the code with sample data

## Best Practices
- Add logging before debugging, remove after fixing
- Write a failing test that reproduces the bug
- Fix the root cause, not just the symptom
- Document the fix and why it works
- Consider if the bug reveals a design issue
