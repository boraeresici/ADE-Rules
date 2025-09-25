---
id: "state-management"
title: "State Management in UI/UX"
description: "Guidelines for effective state management in frontend applications, from local component state to global state libraries."
tags: ["state-management", "react", "vue", "angular", "ui"]
severity: "high"
applies_to: ["frontend", "ui-ux"]
automation_potential: ["code-review"]
suggested_tools: ["Redux DevTools", "Zustand DevTools"]
related_rules: ["component-architecture-react", "performance-optimization"]
---

- Use useState for local component state.
- Use useReducer for complex state logic.
- Use Context API for sharing state between components.
- Consider state management libraries (Redux, Zustand) for large applications.
- Keep state as close as possible to where it's needed.

**Rationale:** Effective state management is crucial for predictable application behavior and maintainability. Choosing the right tool depends on the complexity and scope of the application.

**Automation Potential:** State management libraries often provide developer tools for debugging.
