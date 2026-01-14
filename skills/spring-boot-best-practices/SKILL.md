---
name: spring-boot-best-practices
description: Framework-specific patterns and conventions for Spring Boot
---

# Spring Boot Best Practices

## Project Structure
- Follow standard Maven/Gradle layout
- Group by feature, not by layer (optional but recommended)
- Keep controllers thin (delegate to services)
- Use service layer for business logic
- Use repository layer for data access
- Keep configuration in `@Configuration` classes

## Dependency Injection
- Prefer constructor injection over field injection
- Use `@RequiredArgsConstructor` (Lombok) for cleaner code
- Avoid circular dependencies
- Use `@Qualifier` when multiple beans of same type
- Prefer interfaces over concrete classes

## Configuration
- Use `application.yml` or `application.properties`
- Use profiles for environment-specific config (`application-dev.yml`)
- Use `@ConfigurationProperties` for type-safe configuration
- Externalize configuration (don't hardcode)
- Use environment variables for secrets

## REST Controllers
- Use `@RestController` for REST APIs
- Use appropriate HTTP methods and status codes
- Validate inputs with `@Valid` and Bean Validation
- Use DTOs for request/response (don't expose entities)
- Handle exceptions with `@ControllerAdvice`
- Use `@CrossOrigin` appropriately

## Data Access
- Use Spring Data JPA repositories
- Use `@Transactional` appropriately (services, not controllers)
- Avoid N+1 queries (use `@EntityGraph` or fetch joins)
- Use pagination for large datasets
- Use `@Query` for complex queries
- Consider using DTO projections

## Testing
- Use `@SpringBootTest` for integration tests
- Use `@WebMvcTest` for controller tests
- Use `@DataJpaTest` for repository tests
- Use `@MockBean` for mocking dependencies
- Use Testcontainers for database tests
- Keep tests fast and independent

## Security
- Use Spring Security for authentication/authorization
- Don't store passwords in plain text (use BCrypt)
- Use HTTPS in production
- Validate and sanitize inputs
- Use CSRF protection for state-changing operations
- Keep dependencies updated

## Performance
- Use connection pooling (HikariCP default)
- Enable caching with `@Cacheable`
- Use async methods with `@Async` for long-running tasks
- Monitor with Actuator endpoints
- Use `@Profile` to exclude dev-only beans in production
