---
id: "angular"
title: "Angular Best Practices"
description: "Guidelines for building robust, scalable, and maintainable applications with Angular, focusing on module organization, component communication, and change detection."
tags: ["frontend", "angular", "typescript", "ui"]
severity: "high"
applies_to: ["frontend", "angular", "typescript"]
automation_potential: ["linter", "static-analysis", "code-review"]
suggested_tools: ["ESLint-plugin-angular", "Angular CLI", "Cypress"]
related_rules: ["react", "vuejs", "general-frontend-best-practices"]
---

### Module and Component Organization
- Use feature modules to organize application logic.
- Keep components focused and reusable.
- Use smart (container) and dumb (presentational) components.
- Follow the Angular Style Guide for naming conventions and file structure.

**Rationale:** Feature modules improve scalability and lazy loading. Focused components are easier to test and maintain. Consistent styling enhances readability and collaboration.

### State Management and Data Flow
- Use RxJS Observables for asynchronous data streams.
- For global state, consider NgRx or Akita.
- Use `@Input()` for parent-to-child and `@Output()` for child-to-parent communication.

**Rationale:** RxJS provides powerful tools for reactive programming. Centralized state management simplifies data flow in complex applications. Clear communication patterns prevent unexpected side effects.

### Change Detection Strategy
- Prefer `OnPush` change detection strategy for performance.
- Understand how `OnPush` works with immutable data.

**Rationale:** `OnPush` significantly improves performance by reducing the number of change detection cycles, especially in large applications.

### Performance Optimization
- Lazy load modules and routes.
- Use `trackBy` with `*ngFor` for better rendering performance.
- Optimize image loading.
- Use Ahead-of-Time (AOT) compilation.

**Rationale:** Performance optimizations are crucial for a smooth user experience and efficient resource usage.

### Accessibility
- Use semantic HTML.
- Ensure keyboard navigation.
- Provide ARIA attributes where necessary.

**Rationale:** Accessible applications cater to a broader audience and improve overall usability.

### Testing
- Write unit tests for services and components.
- Write integration tests for module interactions.
- Use end-to-end tests for critical user flows.

**Rationale:** Comprehensive testing ensures application reliability and prevents regressions.
