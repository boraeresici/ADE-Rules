---
id: "performance-principles"
title: "Performance Principles"
description: "Fundamental guidelines for optimizing application performance, emphasizing measurement and critical path optimization."
tags: ["performance", "optimization", "principles"]
severity: "high"
applies_to: ["all"]
automation_potential: ["profiling", "static-analysis", "code-review"]
suggested_tools: ["Chrome DevTools", "Blackfire", "SonarQube"]
related_rules: ["algorithmic-optimization", "memory-optimization", "asynchronous-performance"]
---

- Measure before optimizing.
- Optimize the critical path first.
- Consider algorithmic complexity.
- Balance performance with readability.
- Cache costly operations.

**Rationale:** Premature optimization can lead to wasted effort and complex code. Focusing on critical paths yields the most significant performance gains. Algorithmic efficiency is fundamental. Balancing performance with readability ensures maintainability. Caching reduces redundant computations.

**Automation Potential:** Profiling tools (e.g., Chrome DevTools, Blackfire) help measure performance. Static analysis can identify some algorithmic inefficiencies.
