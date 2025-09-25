---
id: "general-frontend-best-practices"
title: "General Frontend Best Practices"
description: "Overarching guidelines applicable across all frontend frameworks for building high-quality, performant, and maintainable web applications."
tags: ["frontend", "best-practices", "performance", "accessibility", "security"]
severity: "high"
applies_to: ["frontend", "all"]
automation_potential: ["linter", "static-analysis", "code-review", "seo-audit", "performance-audit"]
suggested_tools: ["ESLint", "Prettier", "Lighthouse", "WebPageTest"]
related_rules: ["react", "vuejs", "angular", "svelte", "nextjs", "nuxtjs", "gatsby", "solidjs", "qwik", "astro", "web-components"]
---

### Performance
- Optimize image and video assets (compression, responsive images, lazy loading).
- Minimize CSS and JavaScript (minification, tree-shaking).
- Implement code splitting.
- Leverage browser caching.
- Monitor Core Web Vitals.

**Rationale:** Fast loading times and smooth interactions are critical for user experience and SEO. Optimizing assets and code reduces bandwidth usage and improves perceived performance.

### Accessibility (A11y)
- Use semantic HTML elements.
- Ensure keyboard navigability for all interactive elements.
- Provide sufficient color contrast.
- Add `alt` text for images and ARIA attributes where necessary.
- Test with screen readers.

**Rationale:** Accessible websites are usable by everyone, including people with disabilities, expanding your audience and often improving overall usability.

### Security
- Prevent Cross-Site Scripting (XSS) by sanitizing user input and output.
- Implement Content Security Policy (CSP).
- Secure API calls (HTTPS, authentication tokens).
- Keep dependencies updated to avoid known vulnerabilities.

**Rationale:** Frontend security is crucial to protect users from malicious attacks and ensure data integrity. Proactive measures prevent common web vulnerabilities.

### Maintainability and Readability
- Follow consistent coding styles (linters, formatters).
- Write clean, self-documenting code.
- Break down complex logic into smaller, testable functions/components.
- Write comprehensive tests (unit, integration, E2E).

**Rationale:** Maintainable code is easier to understand, debug, and extend, reducing long-term development costs and improving team collaboration.

### SEO (Search Engine Optimization)
- Use semantic HTML and proper heading structures.
- Ensure meta tags (title, description) are accurate and unique.
- Optimize for mobile devices.
- Ensure fast page load times.
- Use sitemaps.

**Rationale:** Good SEO practices improve visibility in search engine results, driving organic traffic to your application.
