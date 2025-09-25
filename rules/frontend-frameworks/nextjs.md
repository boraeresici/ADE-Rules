---
id: "nextjs"
title: "Next.js Best Practices"
description: "Guidelines for building performant, SEO-friendly, and scalable React applications with Next.js, covering data fetching, routing, and deployment."
tags: ["frontend", "nextjs", "react", "ssr", "ssg"]
severity: "high"
applies_to: ["frontend", "nextjs", "react", "javascript", "typescript"]
automation_potential: ["linter", "static-analysis", "code-review", "seo-audit"]
suggested_tools: ["ESLint-config-next", "Next.js CLI", "Lighthouse"]
related_rules: ["react", "nuxtjs", "general-frontend-best-practices"]
---

### Data Fetching Strategies
- Use `getServerSideProps` for server-side rendering (SSR) when data needs to be fresh on every request.
- Use `getStaticProps` for static site generation (SSG) when data can be pre-rendered at build time.
- Use `getStaticPaths` with `getStaticProps` for dynamic SSG routes.
- Use `useSWR` or `React Query` for client-side data fetching and caching.

**Rationale:** Choosing the correct data fetching strategy is crucial for performance, SEO, and user experience. Next.js offers flexible options to optimize for different use cases.

### Routing and Navigation
- Use the `next/router` for client-side navigation.
- Understand dynamic routes (`[param].js`) and catch-all routes (`[[...param]].js`).
- Use `next/link` for client-side transitions between pages.

**Rationale:** Efficient routing and navigation contribute to a smooth and fast user experience.

### API Routes
- Use API Routes for building your backend API within a Next.js project.
- Keep API Routes focused on single responsibilities.
- Secure API Routes with authentication and authorization.

**Rationale:** API Routes provide a convenient way to build serverless functions as part of your frontend project, ideal for handling form submissions, database interactions, or external API calls.

### Performance Optimization
- Optimize images with `next/image`.
- Lazy load components with `next/dynamic`.
- Use `next/script` for third-party scripts.
- Implement font optimization.

**Rationale:** Next.js provides built-in optimizations to ensure fast loading times and a high Lighthouse score.

### Deployment
- Deploy to Vercel for seamless integration and optimal performance.
- Understand serverless functions and edge functions for global distribution.

**Rationale:** Vercel is optimized for Next.js deployments, offering features like automatic scaling, global CDN, and serverless functions.
