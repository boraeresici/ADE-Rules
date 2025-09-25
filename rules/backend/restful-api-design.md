---
id: "restful-api-design"
title: "RESTful API Design"
description: "Guidelines for designing intuitive, consistent, and efficient RESTful APIs with proper HTTP methods, naming, and versioning."
tags: ["backend", "api", "rest", "design"]
severity: "high"
applies_to: ["backend", "api"]
automation_potential: ["api-testing", "openapi-validation", "code-review"]
suggested_tools: ["Postman", "Swagger UI", "OpenAPI linters"]
related_rules: ["backend-fundamentals", "service-architecture", "api-design"]
---

- Use appropriate HTTP methods (GET, POST, PUT, DELETE, etc.).
- Use consistent and understandable endpoint naming.
- Implement API versioning (URL or header-based).
- Define a standard format for error codes and messages.
- Use querystring parameters for pagination, filtering, and sorting.

**Rationale:** Well-designed RESTful APIs are intuitive, easy to consume, and promote efficient data exchange. Consistency and versioning are key for developer experience and maintainability.

**Automation Potential:** OpenAPI/Swagger specifications can be used to document and validate API design.

### Example (API Endpoint Definition):
```yaml
POST /api/v1/users
Description: Creates a new user
Request Body:
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
Response:
  201 Created:
    {
      "id": "uuid",
      "username": "string",
      "email": "string",
      "createdAt": "timestamp"
    }
  400 Bad Request:
    {
      "error": "string",
      "details": ["string"]
    }
```
