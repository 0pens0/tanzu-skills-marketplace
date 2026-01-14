---
name: performance-optimization
description: Techniques for improving code performance
---

# Performance Optimization

## Measurement First
- Profile before optimizing (measure, don't guess)
- Identify bottlenecks with profiling tools
- Set performance goals and measure against them
- Monitor production performance metrics

## Database Optimization
- Use indexes on frequently queried columns
- Avoid N+1 queries (use eager loading, batch loading)
- Use pagination for large result sets
- Cache frequently accessed data
- Optimize queries (avoid SELECT *, use appropriate joins)
- Consider read replicas for read-heavy workloads

## Code Optimization
- Avoid premature optimization
- Use appropriate data structures (HashMap vs List)
- Minimize object creation in loops
- Use lazy loading where appropriate
- Cache expensive computations
- Use connection pooling for databases

## Caching Strategies
- Cache at multiple levels (application, database, CDN)
- Set appropriate cache expiration times
- Invalidate cache when data changes
- Use cache keys that include version/context
- Consider cache warming for critical paths

## Concurrency
- Use async/await for I/O operations
- Parallelize independent operations
- Use thread pools appropriately
- Avoid blocking operations in async code
- Consider message queues for decoupling

## Memory Management
- Avoid memory leaks (close resources, clear references)
- Use object pooling for frequently created objects
- Monitor memory usage
- Set appropriate heap sizes
- Consider garbage collection tuning if needed
