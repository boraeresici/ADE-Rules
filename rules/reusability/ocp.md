---
id: "ocp"
title: "Open/Closed Principle (OCP)"
description: "Code should be open for extension but closed for modification."
tags: ["solid", "design-principles", "reusability"]
severity: "high"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube"]
related_rules: ["srp", "lsp", "isp", "dip"]
---

- Code should be open for extension but closed for modification.
- Effectively use abstractions, interfaces, or inheritance.
- Clearly define and document extension points.

**Rationale:** OCP encourages designing systems that can be extended with new functionality without altering existing, tested code. This reduces the risk of introducing bugs into stable parts of the system.

**Automation Potential:** Design review and architectural analysis tools can help identify violations.
