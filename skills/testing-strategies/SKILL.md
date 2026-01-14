---
name: testing-strategies
description: Guidelines for writing effective tests (unit, integration, e2e)
---

# Testing Strategies

## Unit Tests
- Test one thing at a time (single responsibility)
- Use descriptive test names that explain what is being tested
- Follow AAA pattern: Arrange, Act, Assert
- Mock external dependencies (databases, APIs, file system)
- Test edge cases: null values, empty collections, boundary conditions
- Keep tests fast and independent (no shared state)

## Integration Tests
- Test interactions between components
- Use test containers or in-memory databases when possible
- Test real data flows, not just mocks
- Focus on critical paths and user workflows
- Keep setup/teardown simple and fast

## End-to-End Tests
- Test complete user journeys
- Use realistic test data
- Test error scenarios and recovery paths
- Keep E2E tests minimal (they're slow and brittle)
- Use page object pattern for UI tests

## Test Quality
- Tests should be readable and maintainable
- Avoid test code duplication (use test helpers)
- Tests should fail for the right reason
- Keep test data close to the test
- Use factories/builders for complex test objects
