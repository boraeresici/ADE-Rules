---
id: "secure-config-secrets"
title: "Secure Configuration and Secrets Management"
description: "Avoid security misconfigurations and never store secrets in source code; use a dedicated secrets management service."
tags: ["security", "configuration", "secrets-management"]
severity: "critical"
applies_to: ["all"]
automation_potential: ["ci-cd-check", "static-analysis", "iac"]
suggested_tools: ["AWS Secrets Manager", "Azure Key Vault", "HashiCorp Vault", "SAST tools"]
related_rules: ["least-privilege", "strong-auth-crypto"]
---

**Description:** Avoid security misconfigurations by using hardened base images and automated validation. Never store secrets (API keys, passwords) in source code. Use a dedicated secrets management service.

**Rationale:** Misconfigurations are a common cause of breaches. Storing secrets in code is a critical vulnerability that can be easily exploited if the code is leaked.

**Good Practice:**
- Remove or disable unnecessary features and components.
- Use AWS Secrets Manager, Azure Key Vault, or HashiCorp Vault for secrets.
- Inject secrets into the application environment at runtime.
