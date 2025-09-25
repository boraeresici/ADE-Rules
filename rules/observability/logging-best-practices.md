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

# Rule: Logging Best Practices

**Description:** This rule provides guidelines for implementing structured and contextual logging across all applications. It covers essential practices such as using correlation IDs, defining appropriate log levels, avoiding sensitive information in logs, and centralizing log collection to enhance observability and facilitate debugging.

**Rationale:** Structured and contextual logging provides invaluable insights into application behavior, making it significantly easier to diagnose issues, understand system flow, and perform root cause analysis in complex distributed systems. Centralized logging further facilitates efficient analysis, alerting, and compliance, which are critical for maintaining system health and security.

### Core Principles:
- **Structured Logging:** Use structured logging formats (e.g., JSON) to make logs machine-readable and easily parsable by log management systems.
- **Correlation IDs:** Add unique correlation IDs to each request at the entry point and propagate them across all services to enable end-to-end tracing of requests (referencing `distributed-tracing.md`).
- **Appropriate Log Levels:** Log messages at appropriate levels (e.g., ERROR, WARN, INFO, DEBUG) to filter and prioritize information effectively.
- **Sensitive Data Exclusion:** Strictly avoid logging sensitive information such as passwords, credit card numbers, or Personally Identifiable Information (PII).
- **Centralized Log Collection:** Implement a centralized log collection and management system to aggregate logs from all services for unified analysis and monitoring.

### Good Practice:
```json
{
  "timestamp": "2023-10-27T10:30:00Z",
  "level": "INFO",
  "service": "user-service",
  "correlation_id": "abc-123-xyz",
  "message": "User login successful",
  "user_id": "user-123",
  "ip_address": "192.168.1.1"
}
```
*Example: A structured log entry in JSON format, including a correlation ID and relevant context.*

### Bad Practice:
```
2023-10-27 10:30:00 INFO User user-123 logged in from 192.168.1.1
2023-10-27 10:31:05 ERROR An error occurred: NullPointerException
```
*Example: Unstructured log entries that are difficult to parse automatically and lack consistent contextual information.*

---

**Automation Potential:** Logging libraries (e.g., Serilog, Log4j, Winston) automate structured logging. Log management platforms (e.g., ELK Stack, Splunk, Datadog) automate log collection, parsing, analysis, and alerting. Code reviews are essential for ensuring adherence to logging standards and preventing sensitive data leakage.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
