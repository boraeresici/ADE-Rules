---
id: "qwik"
title: "Qwik Best Practices"
description: "Guidelines for building instantly interactive web applications with Qwik, focusing on its resumability and fine-grained lazy loading."
tags: ["frontend", "qwik", "javascript", "ui"]
severity: "high"
applies_to: ["frontend", "qwik", "javascript", "typescript"]
automation_potential: ["linter", "static-analysis", "code-review"]
suggested_tools: ["ESLint", "Qwik Testing Library"]
related_rules: ["react", "vuejs", "general-frontend-best-practices"]
---

### Resumability
- Understand Qwik's core concept of resumability, where HTML and JavaScript are paused on the server and resumed on the client.
- Avoid hydration; Qwik doesn't re-execute JavaScript on the client.

**Rationale:** Qwik aims for instant interactivity by delivering minimal JavaScript to the client and only executing code when absolutely necessary, leading to superior performance metrics like Time to Interactive (TTI).

### Component Design
- Use JSX for templating.
- Leverage Qwik's `$` syntax for lazy-loading event handlers and functions.
- Keep components small and focused.

**Rationale:** Qwik's component model is designed around lazy loading and resumability, ensuring that only the code needed for interaction is downloaded and executed.

### Performance Optimization
- Qwik's architecture is inherently optimized for performance through resumability and fine-grained lazy loading.
- Focus on efficient asset delivery and image optimization.

**Rationale:** Qwik's primary goal is to achieve 0ms TTI, making performance a core part of its design.

### Accessibility
- Use semantic HTML.
- Ensure keyboard navigation.
- Provide ARIA attributes where necessary.

**Rationale:** Accessible applications cater to a broader audience and improve overall usability.

### Testing
- Write unit tests for components and Qwik primitives.
- Write end-to-end tests for critical user flows.

**Rationale:** Comprehensive testing ensures application reliability and prevents regressions.
