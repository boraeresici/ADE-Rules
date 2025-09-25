---
id: "performance-monitoring"
title: "Performance Monitoring"
description: "Guidelines for comprehensive performance monitoring, including APM, RUM, and synthetic monitoring."
tags: ["observability", "performance", "monitoring"]
severity: "high"
applies_to: ["all"]
automation_potential: ["tool-integration", "ci-cd-check"]
suggested_tools: ["New Relic", "Dynatrace", "Datadog", "Lighthouse"]
related_rules: ["metrics-implementation", "alerting-strategy", "system-scalability"]
---

- Monitor application performance metrics (APM).
- Track database query performance.
- Implement real user monitoring (RUM).
- Monitor third-party service dependencies.
- Set up synthetic monitoring for critical paths.

**Rationale:** Comprehensive performance monitoring provides a holistic view of application health, from backend services to user experience. Proactive monitoring helps identify and resolve issues before they impact users.

**Automation Potential:** APM tools (e.g., New Relic, Dynatrace), RUM tools, and synthetic monitoring services automate data collection and reporting.
