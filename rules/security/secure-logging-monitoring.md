---
id: "secure-logging-monitoring"
title: "Implement Secure Logging and Monitoring"
description: "Log all security-relevant events, centralize logs, and monitor for suspicious activity to enable incident response."
tags: ["security", "logging", "monitoring", "observability"]
severity: "critical"
applies_to: ["all"]
automation_potential: ["tool-integration", "ci-cd-check"]
suggested_tools: ["SIEM systems", "ELK Stack", "Splunk"]
related_rules: ["automate-vulnerability-management", "observability-best-practices"]
---

**Description:** Log all security-relevant events, such as login attempts (successful and failed), access control failures, and significant server-side errors. Centralize logs and monitor them for suspicious activity.

**Rationale:** Without proper logging and monitoring, detecting and responding to a security incident is nearly impossible. Logs are essential for forensic analysis and threat detection.

**Good Practice:**
- Do not log sensitive data like passwords or credit card numbers.
- Use a SIEM (Security Information and Event Management) system to aggregate and analyze logs.
- Create alerts for anomalous activity (e.g., multiple failed logins from one IP).
