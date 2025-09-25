---
id: "metrics-implementation"
title: "Metrics Implementation"
description: "Guidelines for implementing and visualizing metrics, including the Four Golden Signals and custom business metrics."
tags: ["observability", "metrics", "monitoring"]
severity: "high"
applies_to: ["all"]
automation_potential: ["tool-integration", "ci-cd-check"]
suggested_tools: ["Prometheus", "Grafana", "Datadog"]
related_rules: ["logging-best-practices", "distributed-tracing", "alerting-strategy"]
---

# Rule: Metrics Implementation

**Description:** This rule provides guidelines for the effective implementation and visualization of metrics to monitor system performance and health. It covers the adoption of the Four Golden Signals (Latency, Traffic, Errors, Saturation) and the creation of custom business metrics, along with defining Service Level Indicators (SLIs) and Service Level Objectives (SLOs).

**Rationale:** Metrics provide quantitative data essential for understanding system behavior, identifying performance bottlenecks, and proactively detecting issues. The Four Golden Signals offer a comprehensive, user-centric view of system health, while custom business metrics align technical performance with business goals. Clearly defined SLIs and SLOs establish acceptable performance levels and guide operational efforts.

### Core Principles:
- **Four Golden Signals:** Monitor the Four Golden Signals (Latency, Traffic, Errors, Saturation) as primary indicators of system health and user experience.
- **Standard Naming Conventions:** Use consistent and standard metric naming conventions to ensure clarity and ease of querying.
- **Custom Business Metrics:** Implement custom business metrics that reflect the unique value and performance indicators of the application.
- **Meaningful Dashboards:** Create meaningful and actionable dashboards that visualize key metrics, providing quick insights into system status.
- **SLIs, SLOs, and Error Budgets:** Define Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets to establish performance targets and manage reliability.

### Good Practice:
```yaml
# Example: Prometheus metric definition for request duration
http_request_duration_seconds_bucket{
  le="0.005",
  method="GET",
  path="/api/users",
  status="200"
} 1234

# Example: Grafana dashboard showing latency, errors, and traffic for a service
# (Visual representation, not code)
```

### Bad Practice:
```yaml
# Example: Generic, untagged metrics or metrics without clear units
requests_total 5000

# Example: Dashboards with too many metrics, making it hard to identify critical issues
# (Visual representation, not code)
```

---

**Automation Potential:** Monitoring tools (e.g., Prometheus, Grafana, Datadog) automate metric collection, storage, visualization, and alerting. CI/CD checks can ensure that new code includes appropriate instrumentation for metrics. Code reviews are essential for validating metric design and naming conventions.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
