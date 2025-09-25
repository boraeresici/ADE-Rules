---
id: "commenting-documentation"
title: "Commenting and Documentation"
description: "Write comments to explain the \"why,\" not the \"what.\" Document complex algorithms, business logic, and API contracts."
tags: ["code-quality", "comments", "documentation"]
severity: "medium"
applies_to: ["all"]
automation_potential: ["linter", "code-review"]
suggested_tools: ["ESLint", "Pylint", "JSDoc", "Sphinx"]
related_rules: ["readability-clarity"]
---

**Description:** Write comments to explain the "why," not the "what." Document complex algorithms, business logic, and API contracts. Avoid obvious comments.

**Rationale:** Good comments provide context that is not available in the code itself. They help other developers understand the intent behind a piece of logic.

**Good Practice:**
```java
// Calculate the interest rate based on the user's credit score tier.
// This is a temporary simplification of a business rule that is expected to change next quarter.
float interestRate = getRateForTier(user.getCreditScore());
```

**Bad Practice:**
```java
// This is a loop
for (int i = 0; i < 10; i++) {
  // Increment i
  i++;
}
```

```