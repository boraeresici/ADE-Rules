---
id: "react-specific"
title: "React Specific Best Practices"
description: "Guidelines for optimizing React component performance, organization, and reusability."
tags: ["react", "frontend", "performance"]
severity: "high"
applies_to: ["react", "frontend"]
automation_potential: ["linter", "static-analysis", "code-review"]
suggested_tools: ["ESLint-plugin-react", "React DevTools Profiler"]
related_rules: ["react", "general-frontend-best-practices"]
---

- Use `useMemo` and `useCallback` hooks to prevent unnecessary renders.
- Prefer functional components and hooks.
- Use Context API or state management libraries to avoid prop drilling.
- Design component structure logically and for reusability.

**Rationale:** These practices optimize React component performance, improve code organization, and enhance reusability, leading to more efficient and maintainable UIs.

**Automation Potential:** ESLint rules for React hooks and component patterns.
