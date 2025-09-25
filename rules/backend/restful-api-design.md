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

# Rule: RESTful API Design

**Description:** This rule provides guidelines for designing intuitive, consistent, and efficient RESTful APIs. It covers best practices for using appropriate HTTP methods, consistent naming conventions, effective versioning strategies, and standardized error handling to ensure a positive developer experience and robust system integration.

**Rationale:** Well-designed RESTful APIs are intuitive, easy to consume, and promote efficient data exchange. Consistency and versioning are key for developer experience, maintainability, and the long-term evolution of the system. Adhering to these principles reduces integration friction and improves overall system reliability.

### Core Principles:
- **HTTP Methods:** Use appropriate HTTP methods (GET, POST, PUT, DELETE, PATCH) according to their semantic meaning.
- **Consistent Naming:** Implement consistent and understandable endpoint naming conventions (e.g., plural nouns for collections, kebab-case for paths).
- **API Versioning:** Implement API versioning (e.g., URL-based, header-based) to manage changes without breaking existing clients.
- **Standardized Error Handling:** Define a standard format for error codes and messages to provide clear feedback to clients.
- **Query Parameters:** Use query string parameters for pagination, filtering, and sorting of resources.

### Good Practice:
```http
GET /api/v1/users/123
Host: example.com
Accept: application/json

HTTP/1.1 200 OK
Content-Type: application/json
{
  "id": "123",
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Bad Practice:
```http
GET /api/get_user_by_id?id=123
Host: example.com

HTTP/1.1 200 OK
Content-Type: application/xml
<user>
  <id>123</id>
  <name>John Doe</name>
</user>
```

---

**Automation Potential:** API testing tools (e.g., Postman, Newman) can validate API responses and behavior. OpenAPI/Swagger specifications can be used for schema validation and linting API definitions. Code reviews are essential for ensuring design consistency and adherence to principles.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
