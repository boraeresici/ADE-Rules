---
id: "reusability"
title: "Code Reusability"
description: "Practices to enhance code reusability by extracting common logic and using dependency injection."
tags: ["reusability", "design-patterns"]
severity: "high"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube", "IDE Refactoring Tools"]
related_rules: ["srp", "maintainability"]
---

- Extract repetitive code blocks into functions or classes.
- Use the Dependency Injection pattern to reduce dependencies.
- Create utility classes or modules for frequently used functionalities.
- Organize code snippets into modules.

**Rationale:** Reusability reduces development time, improves consistency, and minimizes the risk of bugs by centralizing common logic.

**Automation Potential:** Static analysis tools can detect code duplication.
