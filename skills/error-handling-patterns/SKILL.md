---
name: error-handling-patterns
description: Best practices for error handling and exception management
---

# Error Handling Patterns

## Exception Types
- **Checked Exceptions**: For recoverable errors (file not found, network issues)
- **Unchecked Exceptions**: For programming errors (null pointer, illegal argument)
- **Custom Exceptions**: For domain-specific errors
- **Error**: For serious system errors (out of memory)

## Best Practices
- Fail fast: Detect errors as early as possible
- Don't swallow exceptions: Log or handle appropriately
- Use specific exception types: Don't catch generic Exception
- Provide meaningful error messages: Include context
- Log exceptions with stack traces: Help debugging
- Don't expose internal details: Sanitize error messages for users

## Error Handling Strategies
- **Retry**: For transient failures (network, temporary locks)
- **Fallback**: Provide default behavior when possible
- **Circuit Breaker**: Stop calling failing services
- **Graceful Degradation**: Reduce functionality instead of failing
- **Fail Fast**: Stop immediately on critical errors

## Logging Errors
- Log at appropriate level (ERROR for exceptions, WARN for recoverable issues)
- Include context: user ID, request ID, operation being performed
- Don't log sensitive information (passwords, tokens, PII)
- Use structured logging (JSON format)
- Include stack traces for debugging

## API Error Responses
- Return appropriate HTTP status codes
- Provide consistent error response format
- Include error code, message, and details
- Don't expose stack traces in production
- Include request ID for tracking

## Recovery Patterns
- Validate inputs early to prevent errors
- Use transactions for atomic operations
- Implement idempotency for retries
- Handle timeouts appropriately
- Clean up resources in finally blocks
