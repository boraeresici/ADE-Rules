---
id: "isp"
title: "Interface Segregation Principle (ISP)"
description: "Interfaces should be client-specific, not general-purpose."
tags: ["solid", "design-principles", "reusability"]
severity: "high"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube"]
related_rules: ["srp", "ocp", "lsp", "dip"]
---

- Arayüzler istemciye özel olmalı, genel amaçlı olmamalı. (Interfaces should be client-specific, not general-purpose.)
- Arayüzler odaklı ve minimal olmalı. (Interfaces should be focused and minimal.)
- Şişman arayüzleri daha küçük parçalara böl. (Break down fat interfaces into smaller parts.)

**Rationale:** ISP prevents clients from depending on methods they don't use, reducing coupling and making interfaces more manageable. It leads to more robust and flexible designs.

**Automation Potential:** Static analysis tools can identify interfaces with many methods that are not used by all implementers.
