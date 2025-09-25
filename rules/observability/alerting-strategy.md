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

- Alert on symptoms, not causes.
- Define clear escalation policies.
- Avoid alert fatigue with appropriate thresholds.
- Include runbooks in alert descriptions.
- Regularly test alerts.

**Rationale:** Effective alerting ensures that critical issues are detected and addressed promptly. Alerting on symptoms (user-facing impact) is more effective than alerting on causes (internal system state). Clear policies and runbooks streamline incident response.

**Automation Potential:** Alerting platforms (e.g., PagerDuty, Opsgenie) automate escalation and notification.
