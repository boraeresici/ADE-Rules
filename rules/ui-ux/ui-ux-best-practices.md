---
id: "ui-ux-best-practices"
title: "UI/UX Best Practices"
description: "Specific best practices for high-quality, accessible, and maintainable frontend code, addressing common pitfalls."
tags: ["ui-ux", "best-practices", "accessibility", "maintainability"]
severity: "high"
applies_to: ["frontend", "ui-ux"]
automation_potential: ["linter", "accessibility-check", "code-review"]
suggested_tools: ["ESLint", "axe DevTools", "Lighthouse"]
related_rules: ["ui-ux-fundamentals", "design-principles", "component-architecture-react"]
---

- Do not use class components unless absolutely necessary.
- Do not write components without appropriate TypeScript typings.
- Do not create components with more than 300 lines of code.
- Do not use `any` or `unknown` types for props.
- Do not skip error handling for asynchronous operations.
- Use semantic HTML and add appropriate ARIA attributes.
- Support keyboard navigation.

**Rationale:** These specific best practices address common pitfalls and promote high-quality, accessible, and maintainable frontend code.

**Automation Potential:** Linters and accessibility checkers can enforce many of these.
