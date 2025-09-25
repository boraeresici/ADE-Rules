---
id: "maintainability"
title: "Code Maintainability"
description: "Practices to ensure code is easy to understand, modify, and extend over its lifetime."
tags: ["maintainability", "refactoring", "code-quality"]
severity: "high"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube", "IDE Refactoring Tools"]
related_rules: ["refactoring", "code-quality-analysis"]
---

- Gradually refactor legacy code, making small improvements instead of large changes.
- Keep code documentation up-to-date.
- Conduct regular code reviews.
- Track and address technical debt in a timely manner.

**Rationale:** Maintainability ensures that code can be easily understood, modified, and extended over its lifetime. Regular refactoring and documentation prevent code rot.

**Automation Potential:** Code quality metrics (e.g., maintainability index) can be tracked. Code review tools facilitate the process.
