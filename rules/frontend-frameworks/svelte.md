---
id: "svelte"
title: "Svelte Best Practices"
description: "Guidelines for building reactive and efficient web applications with Svelte, focusing on its compiler-driven approach and reactivity model."
tags: ["frontend", "svelte", "javascript", "ui"]
severity: "high"
applies_to: ["frontend", "svelte", "javascript", "typescript"]
automation_potential: ["linter", "static-analysis", "code-review"]
suggested_tools: ["ESLint-plugin-svelte", "Svelte Testing Library", "Cypress"]
related_rules: ["react", "vuejs", "general-frontend-best-practices"]
---

### Component Design
- Use Svelte's `.svelte` single-file components.
- Keep components small and focused.
- Use props for parent-to-child communication and events for child-to-parent.
- Leverage Svelte's built-in reactivity (`$:`).

**Rationale:** Svelte's compiler-driven approach means less boilerplate and highly optimized vanilla JavaScript output. Small components are easier to manage and test. Clear communication patterns prevent unexpected side effects.

### State Management
- Use Svelte stores (`writable`, `readable`, `derived`) for shared state.
- For simple component-local state, use `let` declarations.
- Understand the auto-subscriptions (`$`) for stores.

**Rationale:** Svelte stores provide a simple yet powerful way to manage global state without the overhead of larger frameworks. Its reactivity system is highly efficient.

### Performance Optimization
- Svelte compiles to highly optimized JavaScript, often requiring less manual optimization.
- Use `{#each}` blocks with `key` attributes for efficient list rendering.
- Optimize image loading and asset delivery.

**Rationale:** Svelte's compile-time approach inherently leads to performant applications, but good practices still enhance the user experience.

### Accessibility
- Use semantic HTML.
- Ensure keyboard navigation.
- Provide ARIA attributes where necessary.

**Rationale:** Accessible applications cater to a broader audience and improve overall usability.

### Testing
- Write unit tests for components (e.g., using Svelte Testing Library).
- Write end-to-end tests for critical user flows.

**Rationale:** Comprehensive testing ensures component reliability and prevents regressions.
