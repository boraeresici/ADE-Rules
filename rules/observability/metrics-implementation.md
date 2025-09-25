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

- Follow the Four Golden Signals (latency, traffic, errors, saturation).
- Use standard metric naming conventions.
- Implement custom business metrics.
- Create meaningful dashboards.
- Define SLIs, SLOs, and error budgets.

**Rationale:** Metrics provide quantitative data about system performance and health. The Four Golden Signals offer a comprehensive view of user experience. Custom business metrics align technical performance with business goals. SLIs/SLOs define acceptable performance levels.

**Automation Potential:** Monitoring tools (e.g., Prometheus, Grafana, Datadog) automate metric collection, visualization, and alerting.
