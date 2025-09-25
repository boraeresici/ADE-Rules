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

# Rule: Performance Monitoring

**Description:** This rule provides guidelines for implementing comprehensive performance monitoring across all layers of an application, encompassing Application Performance Monitoring (APM), Real User Monitoring (RUM), and synthetic monitoring. The goal is to gain a holistic view of application health, from backend services to the end-user experience.

**Rationale:** Comprehensive performance monitoring is critical for ensuring a high-quality user experience, maintaining system stability, and optimizing resource utilization. Proactive monitoring helps identify and resolve performance bottlenecks, slow response times, and other issues before they significantly impact users or lead to service degradation. It provides the data necessary for informed decision-making regarding scaling and optimization efforts.

### Core Principles:
- **Application Performance Monitoring (APM):** Monitor key application performance metrics (e.g., request rates, error rates, response times, transaction traces) for backend services and APIs (referencing `metrics-implementation.md`).
- **Database Performance Monitoring:** Track database query performance, connection pool usage, and resource utilization to identify and optimize database-related bottlenecks.
- **Real User Monitoring (RUM):** Implement RUM to collect performance data directly from end-users' browsers or devices, providing insights into actual user experience.
- **Third-Party Service Monitoring:** Monitor the performance and availability of all third-party services and APIs that the application depends on.
- **Synthetic Monitoring:** Set up synthetic monitoring for critical user paths and business transactions to proactively detect performance issues and ensure service availability.

### Good Practice:
```yaml
# Example: APM dashboard showing key metrics for a service
# (Visual representation, not code)

# Example: Synthetic monitoring script for a login flow
# (Pseudocode for a synthetic test)
script:
  - navigate: "https://myapp.com/login"
  - type: "#username", "testuser"
  - type: "#password", "testpass"
  - click: "#loginButton"
  - assert: "#dashboardElement", "visible"
```

### Bad Practice:
```yaml
# Example: Relying solely on server-side metrics without understanding user experience
# (Visual representation, not code)

# Example: Not monitoring third-party APIs, leading to outages when dependencies fail silently
```

---

**Automation Potential:** APM tools (e.g., New Relic, Dynatrace, Datadog), RUM tools, and synthetic monitoring services automate data collection, analysis, and reporting. CI/CD checks can ensure that new features include appropriate instrumentation for performance monitoring. Code reviews are essential for validating monitoring strategies and ensuring comprehensive coverage.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
