---
id: "cost-per-task"
title: "AI Cost per Task Monitoring"
description: "Measure and monitor the unit cost of AI tasks (inference, retrieval, orchestration) against baselines, and set alerts for significant cost increases, building on general metrics and alerting principles."
tags: ["ai-operations", "cost-management", "observability", "finops"]
severity: "high"
applies_to: ["ai", "llm", "ml"]
automation_potential: ["telemetry-collection", "alerting"]
suggested_tools: ["cloud cost management tools", "Prometheus", "Grafana"]
related_rules: ["monitoring-observability-ai", "performance-monitoring", "metrics-implementation", "alerting-strategy"]
---

**Note:** This rule applies the general principles of `metrics-implementation.md` for measurement and `alerting-strategy.md` for notifications, specifically to AI task costs.

### Core Principles for AI Cost per Task Monitoring:
- **Unit Cost Measurement:** Accurately measure the **unit cost per AI task**, encompassing inference, retrieval, and orchestration components.
- **Baseline Comparison:** Establish and regularly compare current unit costs against a defined **non-AI baseline cost** or historical AI cost baselines.
- **Alerting for Anomalies:** Configure alerts to trigger when the unit cost significantly deviates from the baseline (e.g., increases by >20%).
- **Regular Reporting:** Generate and review monthly cost reports to identify trends and optimization opportunities.

### Production Checklist:
- [ ] Unit cost (inference + retrieval + orchestration) is accurately measured for all AI tasks.  
- [ ] AI task unit costs are regularly compared against established baselines.  
- [ ] Alerts are configured to fire if unit cost exceeds predefined thresholds (e.g., > +20% baseline).  
- [ ] Monthly cost reports are generated, reviewed, and used for cost optimization efforts.  
