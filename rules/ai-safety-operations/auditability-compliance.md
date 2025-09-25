---
id: "auditability-compliance"
title: "AI Auditability and Compliance"
description: "Ensure full audit trails for AI systems (prompt, output, decision logs) and compliance with relevant regulations (GDPR, HIPAA, ISO), building on general data privacy, secure logging, and ethical development principles."
tags: ["ai-safety", "compliance", "audit", "security", "ethics"]
severity: "critical"
applies_to: ["ai", "llm", "ml"]
automation_potential: ["logging", "data-governance-tools"]
suggested_tools: ["SIEM systems", "data governance platforms"]
related_rules: ["data-privacy", "secure-logging-monitoring", "ethical-software-development"]
---

**Note:** This rule extends the principles of `data-privacy.md` for data handling, `secure-logging-monitoring.md` for logging practices, and `ethical-software-development.md` for overall ethical considerations, specifically for AI systems.

### Core Principles for AI Auditability and Compliance:
- **Comprehensive Audit Trails:** Implement full audit trails for AI systems, capturing critical events such as:
  - **Prompts:** User inputs to the AI model.
  - **Outputs:** AI model responses.
  - **Decision Logs:** Internal reasoning or confidence scores leading to AI decisions.
  - **Human Interventions:** Records of human overrides or modifications (referencing `human-in-the-loop.md`).
- **Regulatory Compliance:** Map AI system functionalities and data flows to relevant regulations (e.g., GDPR, HIPAA, ISO) and ensure compliance.
- **Data Retention:** Retain logs and audit trails according to legal and regulatory requirements.
- **Explainability:** Provide explainability features for high-risk AI outputs to support auditability and transparency.

### Production Checklist:
- [ ] Full audit trails (prompt, output, decision logs, human interventions) are implemented for all AI systems.  
- [ ] AI system compliance with relevant regulations (GDPR, HIPAA, ISO) is documented and regularly reviewed.  
- [ ] Logs and audit trails are retained according to defined legal and regulatory requirements.  
- [ ] Explainability features are provided for AI outputs, especially in high-risk scenarios.  
