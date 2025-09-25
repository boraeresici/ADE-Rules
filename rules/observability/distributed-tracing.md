---
id: "distributed-tracing"
title: "Distributed Tracing"
description: "Guidelines for implementing end-to-end visibility into requests using OpenTelemetry for complex microservices architectures."
tags: ["observability", "tracing", "opentelemetry"]
severity: "high"
applies_to: ["backend", "microservices"]
automation_potential: ["tool-integration", "ci-cd-check"]
suggested_tools: ["OpenTelemetry", "Jaeger", "Zipkin"]
related_rules: ["logging-best-practices", "metrics-implementation", "alerting-strategy"]
---

- Implement OpenTelemetry for vendor-agnostic tracing.
- Add spans for critical operations.
- Include relevant context in span attributes.
- Sample traces appropriately for performance.
- Correlate traces with logs and metrics.

**Rationale:** Distributed tracing provides end-to-end visibility into requests as they flow through complex microservices architectures, enabling rapid identification of performance bottlenecks and error sources.

**Automation Potential:** OpenTelemetry SDKs and tracing platforms automate trace collection and visualization.
