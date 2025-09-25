---
id: "vuejs"
title: "Vue.js Best Practices"
description: "Guidelines for developing efficient, maintainable, and scalable applications with Vue.js, covering component design, state management, and reactivity."
tags: ["frontend", "vuejs", "javascript", "ui"]
severity: "high"
applies_to: ["frontend", "vuejs", "javascript", "typescript"]
automation_potential: ["linter", "static-analysis", "code-review"]
suggested_tools: ["ESLint-plugin-vue", "Vue Test Utils", "Cypress"]
related_rules: ["react", "angular", "nuxtjs", "general-frontend-best-practices"]
---

### Component Design
- Use Single File Components (SFCs).
- Keep components small and focused.
- Use props for parent-to-child communication and events for child-to-parent.
- Follow a consistent naming convention for components (e.g., PascalCase).

**Rationale:** SFCs provide a clear separation of concerns (template, script, style). Small components are easier to manage and test. Clear communication patterns prevent unexpected side effects.

### Reactivity and State Management
- Understand Vue's reactivity system (e.g., `ref`, `reactive`).
- For simple global state, use Vue's provide/inject or a simple reactive object.
- For complex global state, use Pinia (recommended for Vue 3) or Vuex (for Vue 2).

**Rationale:** Proper use of reactivity ensures efficient updates. Centralized state management simplifies data flow in larger applications.

### Performance Optimization
- Use `v-if` vs `v-show` appropriately.
- Optimize `v-for` lists with unique `key` attributes.
- Lazy load components and routes.
- Use `keep-alive` for frequently toggled components.

**Rationale:** Performance optimizations are crucial for a smooth user experience, especially in data-intensive applications.

### Accessibility
- Use semantic HTML.
- Ensure keyboard navigation.
- Provide ARIA attributes where necessary.

**Rationale:** Accessible applications cater to a broader audience and improve overall usability.

### Testing
- Write unit tests for components (e.g., using Vue Test Utils).
- Write end-to-end tests for critical user flows.

**Rationale:** Comprehensive testing ensures component reliability and prevents regressions.
