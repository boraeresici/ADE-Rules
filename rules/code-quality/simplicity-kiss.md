---
id: "simplicity-kiss"
title: "Simplicity and Conciseness (KISS)"
description: "Prefer simple, straightforward solutions over complex ones."
tags: ["code-quality", "simplicity", "kiss-principle"]
severity: "high"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube", "ESLint", "Pylint"]
related_rules: ["readability-clarity", "refactoring", "srp"]
---

**Description:** Keep It Simple, Stupid (KISS). Prefer simple, straightforward solutions over complex ones. Each function and class should have a single, well-defined responsibility.

**Rationale:** Simple code is less prone to bugs and easier to understand. Over-engineering can lead to unnecessary complexity, making the system harder to manage.

**Good Practice:**
```javascript
// Simple function for a single task
function isUserActive(user) {
  return user.status === 'active';
}
```

**Bad Practice:**
```javascript
// Overly complex function trying to do too much
function processUserData(user) {
  if (user.status === 'active' && user.profile.isComplete) {
    // ... logic to process data
    // ... then more logic to send an email
    return true; // Also returns a boolean, mixing concerns
  }
  return false;
}
```
