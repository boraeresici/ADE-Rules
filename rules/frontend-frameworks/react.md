---
id: "react"
title: "React Best Practices"
description: "Guidelines for building robust, scalable, and maintainable applications with React, focusing on component architecture, state management, and performance."
tags: ["frontend", "react", "javascript", "ui"]
severity: "high"
applies_to: ["frontend", "react", "javascript", "typescript"]
automation_potential: ["linter", "static-analysis", "code-review"]
suggested_tools: ["ESLint-plugin-react", "React Testing Library", "Cypress"]
related_rules: ["vuejs", "angular", "nextjs", "general-frontend-best-practices"]
---

### Component Architecture
- Use functional components with Hooks.
- Keep components small and focused (Single Responsibility Principle).
- Separate presentational and container components.
- Use a consistent folder structure (e.g., feature-based).

**Rationale:** Functional components with Hooks simplify stateful logic. Small, focused components are easier to test and maintain. Separating concerns improves reusability and readability.

### State Management
- Prefer local state for simple component-specific data.
- Use Context API for global state that doesn't change frequently.
- For complex global state, use libraries like Redux, Zustand, or Recoil.

**Rationale:** Choosing the right state management strategy prevents prop drilling and ensures efficient data flow. Over-reliance on global state can lead to complexity.

### Performance Optimization
- Use `React.memo` for functional components and `PureComponent` for class components to prevent unnecessary re-renders.
- Virtualize long lists with libraries like `react-window` or `react-virtualized`.
- Lazy load components and routes using `React.lazy` and `Suspense`.

**Rationale:** Optimizing rendering performance is crucial for a smooth user experience, especially in large applications.

### Accessibility
- Use semantic HTML elements.
- Provide `alt` attributes for images.
- Ensure keyboard navigation is fully functional.
- Manage focus effectively for dynamic content.

**Rationale:** Accessible applications are usable by a wider audience, including those with disabilities, and often improve overall usability for everyone.

### Testing
- Write unit tests for individual components (e.g., using React Testing Library).
- Write integration tests for component interactions.
- Use end-to-end tests for critical user flows.

**Rationale:** Comprehensive testing ensures component reliability, prevents regressions, and provides confidence in deployments.
