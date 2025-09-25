---
id: "performance-optimization"
title: "Frontend Performance Optimization"
description: "Techniques for optimizing frontend performance, including memoization, lazy loading, and code splitting."
tags: ["performance", "frontend", "optimization", "ui"]
severity: "high"
applies_to: ["frontend", "ui-ux"]
automation_potential: ["performance-audit", "ci-cd-check", "code-review"]
suggested_tools: ["Lighthouse", "Chrome DevTools Profiler", "Webpack Bundle Analyzer"]
related_rules: ["ui-ux-fundamentals", "component-architecture-react", "state-management"]
---

- Use React.memo for costly components.
- Apply useMemo and useCallback appropriately.
- Use lazy loading and code splitting techniques for large components.
- Prevent unnecessary re-renders by managing dependencies correctly.
- Use React DevTools Profiler to identify performance bottlenecks.
- Aim for load times under 3 seconds.

**Rationale:** Optimizing frontend performance directly impacts user satisfaction and engagement. These techniques reduce load times and improve responsiveness.

**Automation Potential:** Build tools automate code splitting and lazy loading. Performance monitoring tools track load times and identify bottlenecks.
