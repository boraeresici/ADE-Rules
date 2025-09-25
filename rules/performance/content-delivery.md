---
id: "content-delivery"
title: "Content Delivery Optimization"
description: "Techniques for optimizing static content delivery using CDNs and lazy loading."
tags: ["performance", "cdn", "lazy-loading"]
severity: "medium"
applies_to: ["frontend", "devops"]
automation_potential: ["ci-cd-check", "tool-integration"]
suggested_tools: ["CDN providers", "Webpack", "Vite"]
related_rules: ["performance-principles", "caching-strategies"]
---

- Optimize static content delivery using CDN.
- Implement lazy loading techniques.

**Rationale:** CDNs reduce latency for static assets by serving them from geographically closer edge locations. Lazy loading improves initial page load times by deferring the loading of non-critical resources.

**Automation Potential:** Build tools and web servers can automate lazy loading.
