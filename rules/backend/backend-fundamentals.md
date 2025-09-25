---
id: "backend-fundamentals"
title: "Backend Fundamentals"
description: "Core focus areas and structured approach for designing and implementing robust, scalable, and secure backend architectures."
tags: ["backend", "architecture", "fundamentals"]
severity: "high"
applies_to: ["backend", "architecture"]
automation_potential: ["manual-review"]
suggested_tools: []
related_rules: ["restful-api-design", "service-architecture", "database-design"]
---

### Focus Areas
- RESTful API design (with appropriate versioning and error handling)
- Defining service boundaries and inter-service communication
- Database schema design (normalization, indexes, sharding)
- Caching strategies and performance optimization
- Basic security patterns (authentication, rate limiting)

**Rationale:** These focus areas represent the core pillars of backend development, directly impacting data integrity, system performance, security, and maintainability.

### Approach
1. Start with clear service boundaries.
2. Design APIs contract-first.
3. Consider data consistency requirements.
4. Plan for horizontal scalability from the outset.
5. Keep it simple - avoid premature optimization.

**Rationale:** A structured approach ensures that the backend is well-organized, extensible, and capable of meeting current and future demands.
