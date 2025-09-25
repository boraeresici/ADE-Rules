---
id: "observability-best-practices"
title: "Observability Best Practices"
description: "Overarching practices to ensure observability is a first-class citizen in the development lifecycle."
tags: ["observability", "best-practices"]
severity: "high"
applies_to: ["all"]
automation_potential: ["tool-integration", "code-review"]
suggested_tools: ["Prometheus", "Grafana", "ELK Stack", "OpenTelemetry"]
related_rules: ["logging-best-practices", "metrics-implementation", "distributed-tracing", "alerting-strategy", "performance-monitoring"]
---

- Implement observability from the start.
- Use consistent naming across metrics, logs, and traces.
- Document your observability strategy.
- Regularly review and update dashboards.
- Implement and practice incident response procedures.

**Rationale:** These overarching practices ensure that observability is a first-class citizen in the development lifecycle, leading to more resilient systems and effective incident management.

**Automation Potential:** Observability platforms integrate these components.
