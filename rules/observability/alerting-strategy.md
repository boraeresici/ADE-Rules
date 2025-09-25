---
id: "alerting-strategy"
title: "Alerting Strategy"
description: "Guidelines for effective alerting, focusing on symptoms, clear escalation policies, and avoiding alert fatigue."
tags: ["observability", "alerting", "incident-response"]
severity: "critical"
applies_to: ["devops", "all"]
automation_potential: ["tool-integration", "ci-cd-check"]
suggested_tools: ["PagerDuty", "Opsgenie", "Prometheus Alertmanager"]
related_rules: ["logging-best-practices", "metrics-implementation", "performance-monitoring"]
---

# Rule: Alerting Strategy

**Description:** This rule provides guidelines for developing an effective alerting strategy that focuses on symptoms rather than causes, defines clear escalation policies, and aims to minimize alert fatigue. The goal is to ensure that critical issues are detected promptly and addressed efficiently.

**Rationale:** Effective alerting is crucial for maintaining the reliability and availability of systems. Alerting on symptoms (user-facing impact) is generally more effective than alerting on causes (internal system state) as it directly reflects the user experience. Clear escalation policies and strategies to avoid alert fatigue streamline incident response, reduce mean time to resolution (MTTR), and prevent engineers from becoming desensitized to alerts.

### Core Principles:
- **Alert on Symptoms, Not Causes:** Configure alerts to trigger based on user-facing symptoms (e.g., increased latency, error rates) rather than internal system metrics that might not directly impact users.
- **Clear Escalation Policies:** Define clear, well-documented escalation policies that specify who is responsible for responding to different types of alerts and how they should be notified.
- **Avoid Alert Fatigue:** Implement strategies to minimize alert fatigue, such as setting appropriate thresholds, grouping related alerts, and using different notification channels for varying severities.
- **Include Runbooks:** Provide runbooks or clear instructions within alert descriptions to guide responders on initial troubleshooting steps and actions.
- **Regularly Test Alerts:** Periodically test alerts and the entire incident response process to ensure they function as expected and remain effective.

### Good Practice:
```yaml
# Example: Prometheus Alertmanager configuration for a critical alert
alert:
  - alertname: HighServiceLatency
    expr: histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m])) > 0.5
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "High latency detected for HTTP requests"
      description: "The 99th percentile of HTTP request duration has been above 0.5 seconds for 5 minutes. Check service health and logs. Runbook: go/service-latency-runbook"
```

### Bad Practice:
```yaml
# Example: Alerting on a non-critical internal metric without user impact
alert:
  - alertname: HighCPULoad
    expr: node_cpu_seconds_total{mode="idle"} < 0.1
    for: 10m
    labels:
      severity: warning
    annotations:
      summary: "CPU load is high"
      description: "CPU idle time is below 10% for 10 minutes. This might not indicate a user-facing issue."
```

---

**Automation Potential:** Alerting platforms (e.g., PagerDuty, Opsgenie, Prometheus Alertmanager) automate alert routing, escalation, and notification. CI/CD checks can ensure that new services include appropriate alerting configurations. Code reviews are essential for validating alert definitions and runbook quality.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
