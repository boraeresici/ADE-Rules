---
id: "guardrails"
title: "AI Guardrails"
description: "Implement mechanisms to prevent AI models from generating harmful, biased, or out-of-policy content, focusing on AI-specific controls and referencing general security/ethics rules."
tags: ["ai-safety", "guardrails", "security", "ethics"]
severity: "critical"
applies_to: ["ai", "llm", "ml"]
automation_potential: ["content-filtering", "red-teaming", "ci-cd-check"]
suggested_tools: ["DLP solutions", "prompt red-teaming tools"]
related_rules: ["data-privacy", "algorithmic-bias", "never-trust-user-input"]
---

**Note:** This rule builds upon general security and ethical principles. Refer to `data-privacy.md` for sensitive data handling, `algorithmic-bias.md` for bias mitigation, and `never-trust-user-input.md` for input validation.

### Core Principles for AI Guardrails:
- **Sensitive Data Protection:** Implement AI-specific mechanisms to block or mask PII/PHI and sensitive documents before model input/output, aligning with `data-privacy.md`.
- **Bias Mitigation:** Design and implement controls to prevent AI models from generating biased content, in line with `algorithmic-bias.md`.
- **Adversarial Input Handling (Red-Teaming):** Maintain a **prompt red-teaming** checklist for jailbreak attempts and adversarial inputs, extending the principles of `never-trust-user-input.md` to AI prompts.
- **Policy Adherence:** Provide clear refusal templates (e.g., "I cannot provide [X] because it violates policy.") for out-of-policy content.
- **Auditing:** Log blocked/refused requests for auditing and continuous improvement.

### Production Checklist:
- [ ] AI-specific sensitive data detection in place (regex, classifiers, DLP) for model inputs/outputs.  
- [ ] Refusal prompts tested with adversarial inputs and included in CI/CD pipelines.  
- [ ] Logs of blocked/refused requests stored securely with masked user data.  
- [ ] Content filters enabled for both input and output of AI models.  
- [ ] Guardrail tests (including bias and adversarial input tests) included in CI/CD pipelines.  
