---
id: "consistency"
title: "Consistency"
description: "Follow a consistent coding style, naming convention, and architectural pattern throughout the project."
tags: ["code-quality", "consistency", "coding-standards"]
severity: "high"
applies_to: ["all"]
automation_potential: ["linter", "formatter", "code-review"]
suggested_tools: ["ESLint", "Prettier", "Black", "isort", "gofmt"]
related_rules: ["readability-clarity"]
---

**Description:** Follow a consistent coding style, naming convention, and architectural pattern throughout the project. Use linters and formatters to enforce this automatically.

**Rationale:** Consistency makes the codebase predictable and easier to navigate. It allows developers to focus on the logic rather than deciphering different styles in different parts of the application.

**Good Practice:**
```javascript
// Consistent naming (e.g., camelCase for variables)
const firstName = "John";
const lastName = "Doe";

function getUserProfile() {
  // ...
}
```

**Bad Practice:**
```javascript
// Inconsistent naming
const first_name = "John";
const lastName = "Doe";

function Get_User_Profile() {
  // ...
}
```
