---
id: "dip"
title: "Dependency Inversion Principle (DIP)"
description: "High-level modules should depend on abstractions, not concrete implementations."
tags: ["solid", "design-principles", "reusability"]
severity: "high"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube", "Dependency Injection frameworks"]
related_rules: ["srp", "ocp", "lsp", "isp"]
---

- Yüksek seviyeli modüller, somut uygulamalar yerine soyutlamalara bağımlı olmalı. (High-level modules should depend on abstractions, not concrete implementations.)
- Bağımlılık enjeksiyonu veya kontrol tersine çevirmeyi etkili bir şekilde kullan. (Effectively use dependency injection or inversion of control.)
- Bağımlılıklar açık olmalı, gizli olmamalı. (Dependencies should be explicit, not hidden.)

**Rationale:** DIP promotes loose coupling between modules, making systems more flexible, testable, and maintainable. It allows for easier swapping of implementations without affecting high-level logic.

**Automation Potential:** Dependency analysis tools can visualize dependencies and identify violations.
