---
id: "semantic-custom-error-types"
title: "Semantic and Custom Error Types"
description: "Define and use custom error types to convey semantic meaning for precise programmatic responses."
tags: ["error-handling", "types", "custom-errors"]
severity: "high"
applies_to: ["all"]
automation_potential: ["linter", "type-checker", "code-review"]
suggested_tools: ["TypeScript", "ESLint", "Pylint"]
related_rules: ["principled-error-handling"]
---

**Description:** Define and use custom error types to convey semantic meaning. This allows for more precise programmatic responses to different error conditions.

**Rationale:** Differentiating between error types (e.g., `ValidationError`, `AuthenticationError`, `NotFoundError`) allows the application to handle them differently, such as returning a 400 vs. a 404 status code, or triggering different recovery logic.

**Good Practice:**
```typescript
class ValidationError extends Error {
    constructor(message: string, public field?: string) {
        super(message);
        this.name = 'ValidationError';
    }
}

// in application logic
if (!isValid(input)) {
  throw new ValidationError("Invalid input provided.", "username");
}
```
