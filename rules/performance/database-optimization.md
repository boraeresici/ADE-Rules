---
id: "database-optimization"
title: "Database Optimization"
description: "Best practices for optimizing database queries, indexing, and connection management."
tags: ["performance", "database", "sql"]
severity: "high"
applies_to: ["backend", "database"]
automation_potential: ["profiling", "static-analysis", "code-review"]
suggested_tools: ["ORM tools", "Database performance monitors"]
related_rules: ["performance-principles", "caching-strategies"]
---

- Optimize database queries, create necessary indexes.
- Avoid the N+1 query problem, fetch related data in a single query.
- Use connection pooling.

**Rationale:** Database interactions are often a major performance bottleneck. Optimized queries, proper indexing, and efficient connection management are critical for fast data retrieval.

**Automation Potential:** ORM tools can help mitigate N+1 issues. Database performance monitoring tools identify slow queries.
