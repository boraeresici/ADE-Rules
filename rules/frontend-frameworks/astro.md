---
id: "astro"
title: "Astro Best Practices"
description: "Guidelines for building fast, content-focused websites with Astro, leveraging its island architecture and framework-agnostic approach."
tags: ["frontend", "astro", "ssg", "mpa"]
severity: "high"
applies_to: ["frontend", "astro", "javascript", "typescript"]
automation_potential: ["linter", "static-analysis", "code-review", "seo-audit"]
suggested_tools: ["ESLint", "Lighthouse"]
related_rules: ["nextjs", "nuxtjs", "general-frontend-best-practices"]
---

### Island Architecture
- Understand Astro's island architecture, where JavaScript is isolated to small, interactive components (islands) on an otherwise static HTML page.
- Prefer static HTML where interactivity is not needed.

**Rationale:** Astro's island architecture delivers highly performant websites by sending minimal JavaScript to the client, resulting in faster page loads and better Core Web Vitals.

### Framework Agnostic
- Use your favorite UI frameworks (React, Vue, Svelte, etc.) within Astro components.
- Understand when to hydrate components (`client:load`, `client:idle`, etc.).

**Rationale:** Astro allows developers to use the best tool for the job, integrating multiple UI frameworks seamlessly while maintaining performance benefits.

### Content-Focused
- Astro is ideal for content-heavy websites, blogs, and marketing sites.
- Leverage Markdown and MDX for content creation.

**Rationale:** Astro's focus on static content and minimal JavaScript makes it perfect for sites where content delivery and SEO are paramount.

### Performance Optimization
- Astro is inherently performant due to its static output and island architecture.
- Optimize images and assets.
- Use built-in optimizations for CSS and JavaScript.

**Rationale:** Astro's design prioritizes speed and efficiency, delivering excellent performance out of the box.

### Accessibility
- Use semantic HTML.
- Ensure keyboard navigation.
- Provide ARIA attributes where necessary.

**Rationale:** Accessible applications cater to a broader audience and improve overall usability.

### Testing
- Write unit tests for individual components.
- Write end-to-end tests for critical user flows.

**Rationale:** Comprehensive testing ensures application reliability and prevents regressions.
