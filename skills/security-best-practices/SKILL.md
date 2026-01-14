---
name: security-best-practices
description: Common security patterns and vulnerabilities to avoid
---

# Security Best Practices

## Input Validation
- Validate all user inputs (client-side and server-side)
- Sanitize inputs to prevent injection attacks
- Use parameterized queries for databases
- Validate file uploads (type, size, content)
- Escape output to prevent XSS attacks

## Authentication & Authorization
- Use strong password requirements
- Implement proper session management
- Use secure password hashing (bcrypt, Argon2)
- Implement multi-factor authentication where appropriate
- Follow principle of least privilege
- Validate permissions on every request

## Common Vulnerabilities
- **SQL Injection**: Use parameterized queries, ORMs
- **XSS (Cross-Site Scripting)**: Escape output, use CSP headers
- **CSRF (Cross-Site Request Forgery)**: Use CSRF tokens
- **Insecure Deserialization**: Validate serialized data
- **Sensitive Data Exposure**: Encrypt sensitive data at rest and in transit
- **Broken Authentication**: Secure session management
- **Security Misconfiguration**: Keep dependencies updated, secure defaults

## Secrets Management
- Never commit secrets to version control
- Use environment variables or secret management services
- Rotate secrets regularly
- Use different secrets for different environments
- Don't log sensitive information

## Dependencies
- Keep dependencies updated
- Scan for known vulnerabilities
- Use dependency management tools
- Review third-party code before including
- Prefer well-maintained libraries
