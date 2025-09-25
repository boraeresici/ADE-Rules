---
id: "principled-error-handling"
title: "Principled Error Handling"
description: "Errors should be handled gracefully and explicitly. Never silently swallow errors."
tags: ["error-handling", "resilience", "logging"]
severity: "critical"
applies_to: ["all"]
automation_potential: ["linter", "code-review"]
suggested_tools: ["ESLint", "Pylint", "SonarQube"]
related_rules: ["semantic-custom-error-types", "resilient-recovery-strategies"]
---

**Description:** Errors should be handled gracefully and explicitly. Never silently swallow errors. Fail fast and provide clear, actionable error messages. Errors should be logged with appropriate context for debugging.

**Rationale:** Silently swallowing errors hides underlying problems and leads to unpredictable application behavior. A clear, fail-fast strategy makes bugs easier to detect, diagnose, and fix.

**Good Practice:**
- Use try-catch-finally blocks appropriately.
- Implement global error handlers to catch unhandled exceptions.
- Log errors with contextual information like request IDs, user IDs, and stack traces.

**Bad Practice:**
```javascript
try {
  // some operation that might fail
} catch (error) {
  // console.log(error) -> This is not enough
  // An empty catch block is worse
}
```
