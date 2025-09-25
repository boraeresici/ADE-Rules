---
id: "restful-api"
title: "RESTful API Design"
description: "Principles and best practices for designing RESTful APIs using resource-oriented URLs, proper HTTP methods, and versioning."
tags: ["api", "rest", "http"]
severity: "high"
applies_to: ["backend", "api"]
automation_potential: ["api-testing", "openapi-validation", "code-review"]
suggested_tools: ["Postman", "Swagger UI", "OpenAPI linters"]
related_rules: ["graphql", "grpc", "api-selection-process"]
---

RESTful APIs exchange data using the HTTP protocol with resource-oriented and stateless structures.

### Core Principles:
1. Use resource-oriented URLs.
2. Properly implement HTTP methods (GET, POST, PUT, DELETE).
3. Use appropriate HTTP status codes.
4. Reflect hierarchical structure in URLs.
5. Implement versioning.

**Rationale:** RESTful APIs are widely adopted due to their simplicity and adherence to web standards. Resource-oriented design makes APIs intuitive, while proper HTTP method usage ensures semantic correctness. Versioning is essential for backward compatibility.

**Automation Potential:** API testing tools can validate HTTP methods and status codes. OpenAPI/Swagger can document and validate API structure.

### Example:
```
GET /api/v1/users           # List all users
GET /api/v1/users/123       # Get user with ID 123
POST /api/v1/users          # Create new user
PUT /api/v1/users/123       # Update user with ID 123
DELETE /api/v1/users/123    # Delete user with ID 123
```

### When to Use:
- In applications heavily focused on CRUD operations.
- When broad ecosystem and tool support is needed.
- When a simple and understandable API structure is desired.
