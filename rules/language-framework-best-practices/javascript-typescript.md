---
id: "javascript-typescript"
title: "JavaScript/TypeScript Best Practices"
description: "Guidelines for writing robust, type-safe, and maintainable JavaScript and TypeScript code."
tags: ["javascript", "typescript", "frontend", "backend"]
severity: "high"
applies_to: ["javascript", "typescript", "frontend", "backend"]
automation_potential: ["linter", "type-checker", "static-analysis", "code-review"]
suggested_tools: ["ESLint", "Prettier", "TypeScript compiler"]
related_rules: ["python-django", "go", "fastapi", "general-principles"]
---

- Use async/await for asynchronous operations.
- Prefer TypeScript for type safety.
- Standardize code style using tools like ESLint and Prettier.
- Organize code using the module system (ES6 modules).

**Rationale:** Async/await simplifies asynchronous code, improving readability and error handling. TypeScript enhances code quality and maintainability through static typing. Consistent tooling ensures a unified codebase.

**Automation Potential:** ESLint and Prettier automate code style enforcement. TypeScript compiler enforces type safety.
