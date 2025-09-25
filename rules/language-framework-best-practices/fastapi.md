---
id: "fastapi"
title: "FastAPI Best Practices"
description: "Guidelines for building reliable, testable, and high-performance APIs with FastAPI."
tags: ["fastapi", "python", "backend", "api"]
severity: "high"
applies_to: ["fastapi", "python", "backend", "api"]
automation_potential: ["linter", "static-analysis", "code-review", "api-testing"]
suggested_tools: ["Pydantic", "FastAPI CLI", "pytest"]
related_rules: ["python-django", "api-design", "general-principles"]
---

- Define request and response schemas using Pydantic models.
- Effectively use the Dependency Injection system.
- Use asynchronous functions where appropriate.
- Leverage FastAPI's OpenAPI features to automatically generate API documentation.

**Rationale:** Pydantic models provide data validation and serialization, improving API reliability. Dependency Injection enhances testability and modularity. Asynchronous functions improve performance for I/O-bound operations.

**Automation Potential:** FastAPI automatically generates OpenAPI documentation.
