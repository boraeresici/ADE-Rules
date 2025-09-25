---
id: "nuxtjs"
title: "Nuxt.js Best Practices"
description: "Guidelines for building performant, SEO-friendly, and scalable Vue.js applications with Nuxt.js, covering data fetching, routing, and deployment."
tags: ["frontend", "nuxtjs", "vuejs", "ssr", "ssg"]
severity: "high"
applies_to: ["frontend", "nuxtjs", "vuejs", "javascript", "typescript"]
automation_potential: ["linter", "static-analysis", "code-review", "seo-audit"]
suggested_tools: ["ESLint-plugin-vue", "Nuxt.js CLI", "Lighthouse"]
related_rules: ["vuejs", "nextjs", "general-frontend-best-practices"]
---

### Data Fetching Strategies
- Use `asyncData` or `fetch` (Nuxt 2) for server-side rendering (SSR) or static site generation (SSG).
- Use `useAsyncData` or `useFetch` (Nuxt 3 Composition API) for data fetching.
- Understand when to use client-side fetching for dynamic content.

**Rationale:** Nuxt.js provides powerful data fetching hooks to optimize for performance, SEO, and user experience, allowing for flexible rendering strategies.

### Routing and Navigation
- Leverage Nuxt's file-system based routing for automatic route generation.
- Use `NuxtLink` for client-side navigation.
- Understand dynamic routes (`_slug.vue`) and nested routes.

**Rationale:** Nuxt's routing simplifies application structure and provides efficient client-side transitions.

### Server-Side Features
- Use Nuxt's server-side API routes for backend logic.
- Understand middleware for route protection or data manipulation.

**Rationale:** Nuxt allows you to build full-stack applications within a single framework, simplifying development and deployment.

### Performance Optimization
- Optimize images with `@nuxt/image` module.
- Lazy load components and routes.
- Use code splitting.
- Implement font optimization.

**Rationale:** Nuxt.js provides built-in optimizations and modules to ensure fast loading times and a high Lighthouse score.

### Deployment
- Deploy to platforms optimized for Nuxt.js (e.g., Vercel, Netlify).
- Understand different rendering modes: SSR, SSG (Generate), SPA.

**Rationale:** Choosing the right deployment strategy and platform ensures optimal performance and scalability for your Nuxt.js application.
