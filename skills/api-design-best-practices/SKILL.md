---
name: api-design-best-practices
description: RESTful API design principles and conventions
---

# API Design Best Practices

## RESTful Principles
- Use nouns for resources, not verbs (e.g., `/users` not `/getUsers`)
- Use HTTP methods correctly: GET (read), POST (create), PUT (update), DELETE (remove)
- Use plural nouns for collections: `/users`, `/orders`
- Use hierarchical URLs: `/users/{id}/orders`
- Return appropriate HTTP status codes (200, 201, 400, 404, 500, etc.)

## URL Design
- Keep URLs simple and intuitive
- Use kebab-case for multi-word resources: `/user-profiles`
- Avoid deep nesting (max 2-3 levels)
- Use query parameters for filtering, sorting, pagination
- Version APIs: `/api/v1/users` or via headers

## Request/Response
- Use consistent JSON structure
- Include relevant metadata (pagination, timestamps)
- Use meaningful field names (avoid abbreviations)
- Support content negotiation (Accept header)
- Return error details in consistent format

## Security
- Use HTTPS for all endpoints
- Implement authentication (OAuth2, JWT)
- Validate and sanitize all inputs
- Rate limit to prevent abuse
- Don't expose sensitive data in URLs or error messages

## Documentation
- Document all endpoints with examples
- Include request/response schemas
- Document error codes and meanings
- Provide SDKs or code examples
- Keep documentation up to date
