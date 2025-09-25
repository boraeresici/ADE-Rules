---
id: "database-design"
title: "Database Design"
description: "Best practices for choosing database types, schema normalization, indexing, and sharding for performance and scalability."
tags: ["backend", "database", "sql", "nosql"]
severity: "high"
applies_to: ["backend", "database"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["ORM tools", "Database performance monitors"]
related_rules: ["backend-fundamentals", "performance-optimization"]
---

- Choose the appropriate database type (relational, NoSQL, NewSQL).
- Normalize database schemas and denormalize when necessary.
- Create appropriate indexes for performance.
- Implement sharding strategies for large datasets.
- Pool database connections (connection pooling).

**Rationale:** Database design directly impacts data integrity, query performance, and scalability. Selecting the right database type and optimizing its schema are fundamental.

**Automation Potential:** ORM tools assist in schema management. Database performance monitoring tools identify bottlenecks.

### Database Schema Example:
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);
```
