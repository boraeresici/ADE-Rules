---
id: "logging-best-practices"
title: "Logging Best Practices"
description: "Guidelines for structured and contextual logging, including correlation IDs and appropriate log levels."
tags: ["observability", "logging", "best-practices"]
severity: "high"
applies_to: ["all"]
automation_potential: ["tool-integration", "code-review"]
suggested_tools: ["ELK Stack", "Splunk", "Datadog", "Winston", "Log4j"]
related_rules: ["metrics-implementation", "distributed-tracing", "alerting-strategy"]
---

- Use structured logging (JSON format).
- Add correlation IDs for request tracing.
- Log at appropriate levels (ERROR, WARN, INFO, DEBUG).
- Avoid logging sensitive information.
- Implement log collection and centralization.

**Rationale:** Structured and contextual logging provides valuable insights into application behavior, making it easier to diagnose issues and understand system flow. Centralized logging facilitates analysis and alerting.

**Automation Potential:** Logging libraries (e.g., Serilog, Log4j, Winston) and log management platforms (e.g., ELK Stack, Splunk) automate these practices.
