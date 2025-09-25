---
id: "incident-path"
title: "AI Incident Management"
description: "Define clear incident response procedures, roles (incident commander), reporting channels, and SLAs for AI system failures, building on general alerting and monitoring strategies."
tags: ["ai-operations", "incident-response", "devops", "reliability"]
severity: "critical"
applies_to: ["ai", "llm", "ml"]
automation_potential: ["alerting", "communication-tools"]
suggested_tools: ["PagerDuty", "Opsgenie", "Slack", "Jira"]
related_rules: ["alerting-strategy", "rollback-plan", "comprehensive-monitoring-logging"]
---

**Note:** This rule extends the general `alerting-strategy.md` and relies on the comprehensive monitoring and logging practices defined in `comprehensive-monitoring-logging.md`.

### Core Principles for AI Incident Management:
- **Incident Commander:** Clearly define the role of an **incident commander** responsible for leading the response during AI system failures.
- **Reporting Channels:** Establish clear and accessible reporting channels (e.g., Slack, PagerDuty, Jira) for users and automated systems to report AI-related issues.
- **Service Level Agreements (SLAs):** Define specific SLAs for acknowledging and responding to AI incidents (e.g., acknowledge < 30m, resolve < 2h).
- **AI-Specific Playbooks:** Develop and regularly test incident playbooks tailored to common AI failure modes (e.g., model drift, unexpected outputs, performance degradation).

### Production Checklist:
- [ ] An incident commander role is assigned, and on-call rotations are documented.  
- [ ] Clear channels for reporting AI-related issues are established and communicated.  
- [ ] SLAs for AI incident acknowledgment and resolution are defined and tracked.  
- [ ] AI-specific incident playbooks are developed and tested quarterly.  
- [ ] Post-incident reviews are conducted to identify root causes and implement preventative measures.  
