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

# Rule: Database Design

**Description:** This rule outlines best practices for designing robust and scalable databases. It covers critical aspects such as selecting the appropriate database type, schema normalization, effective indexing strategies, and implementing sharding for large datasets to ensure optimal performance and scalability.

**Rationale:** Database design directly impacts data integrity, query performance, and the overall scalability of an application. Selecting the right database type and optimizing its schema are fundamental steps to prevent bottlenecks, ensure data consistency, and support future growth.

### Core Principles:
- **Database Type Selection:** Choose the appropriate database type (relational, NoSQL, NewSQL) based on data structure, access patterns, and scalability requirements.
- **Schema Design:** Apply schema normalization principles and strategically denormalize when necessary for performance optimization.
- **Indexing:** Create appropriate and efficient indexes to accelerate query performance without excessive overhead.
- **Sharding/Partitioning:** Implement sharding or partitioning strategies for large datasets to distribute load and improve scalability.
- **Connection Pooling:** Utilize connection pooling to efficiently manage database connections and reduce overhead.

### Good Practice:
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
*Example: A normalized user table with appropriate indexes for common lookup fields.*

### Bad Practice:
```sql
CREATE TABLE orders (
  order_id UUID PRIMARY KEY,
  user_id UUID NOT NULL,
  user_name VARCHAR(255), -- Denormalized without clear rationale
  user_email VARCHAR(255), -- Denormalized without clear rationale
  product_details JSONB, -- Storing complex data without schema
  created_at TIMESTAMP
);
```
*Example: Excessive denormalization or storing unstructured data without clear benefits, leading to data redundancy and potential inconsistencies.*

---

**Automation Potential:** ORM (Object-Relational Mapping) tools can assist in schema management and migrations. Database performance monitoring tools can identify query bottlenecks and suggest index improvements. Static analysis tools can check for common schema design anti-patterns.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
