---
id: "gatsby"
title: "Gatsby Best Practices"
description: "Guidelines for building fast, secure, and scalable static sites and applications with Gatsby, focusing on data sourcing, plugins, and performance."
tags: ["frontend", "gatsby", "react", "ssg", "graphql"]
severity: "high"
applies_to: ["frontend", "gatsby", "react", "javascript", "typescript"]
automation_potential: ["linter", "static-analysis", "code-review", "seo-audit"]
suggested_tools: ["ESLint-plugin-react", "Gatsby CLI", "Lighthouse"]
related_rules: ["react", "nextjs", "general-frontend-best-practices"]
---

### Data Sourcing
- Use Gatsby's GraphQL layer to query data from various sources (CMS, Markdown, APIs).
- Leverage source plugins to pull data into Gatsby's data layer.

**Rationale:** Gatsby's data layer unifies data from disparate sources, allowing you to query everything with GraphQL and build a single, cohesive application.

### Plugin Ecosystem
- Utilize Gatsby's rich plugin ecosystem for functionalities like image optimization, SEO, and analytics.
- Understand when to create custom plugins for specific needs.

**Rationale:** Plugins extend Gatsby's capabilities, simplifying common tasks and adding advanced features without writing extensive custom code.

### Performance Optimization
- Gatsby is inherently fast due to its static site generation and built-in optimizations.
- Optimize images with `gatsby-plugin-image`.
- Lazy load components and routes.
- Use code splitting.

**Rationale:** Gatsby's architecture focuses on delivering highly performant websites by default, pre-rendering content and optimizing assets.

### Accessibility
- Use semantic HTML.
- Ensure keyboard navigation.
- Provide ARIA attributes where necessary.

**Rationale:** Accessible applications cater to a broader audience and improve overall usability.

### Deployment
- Deploy to static site hosting platforms (e.g., Netlify, Vercel, GitHub Pages).
- Understand incremental builds for faster deployment times.

**Rationale:** Gatsby's output is static, making it highly suitable for cost-effective and performant static site hosting.
