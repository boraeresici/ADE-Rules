---
id: "algorithmic-optimization"
title: "Algorithmic Optimization"
description: "Guidelines for improving performance by choosing efficient algorithms and data structures."
tags: ["performance", "algorithms", "data-structures"]
severity: "high"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube", "profilers"]
related_rules: ["performance-principles", "memory-optimization"]
---

- Be aware of time complexity and use more efficient algorithms.
- Choose appropriate data structures (Map, Set, etc.).

**Rationale:** The choice of algorithm and data structure has a profound impact on performance, especially with large datasets. Understanding time complexity (e.g., O(n), O(log n)) is key.

**Automation Potential:** Some static analysis tools can flag inefficient patterns, but often requires manual review.
