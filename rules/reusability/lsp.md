---
id: "lsp"
title: "Liskov Substitution Principle (LSP)"
description: "Subtypes must be substitutable for their base types without altering the correctness of the program."
tags: ["solid", "design-principles", "reusability"]
severity: "high"
applies_to: ["all"]
automation_potential: ["type-checker", "static-analysis", "code-review"]
suggested_tools: ["SonarQube", "TypeScript compiler"]
related_rules: ["srp", "ocp", "isp", "dip"]
---

- Alt tipler, program doğruluğunu etkilemeden temel tiplerin yerine geçebilmeli. (Subtypes must be substitutable for their base types without altering the correctness of the program.)
- Türetilmiş sınıflar, temel sınıfların kullanıldığı her yerde kullanılabilmeli. (Derived classes should be usable wherever base classes are used.)
- Geçersiz kılınan metodlar aynı davranış garantilerini korumalı. (Overridden methods must maintain the same behavioral guarantees.)

**Rationale:** LSP ensures that derived classes behave consistently with their base classes, preventing unexpected behavior when substituting objects. This is crucial for maintaining type safety and predictable system behavior.

**Automation Potential:** Type checkers and some static analysis tools can detect certain LSP violations.
