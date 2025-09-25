---
id: "strong-auth-crypto"
title: "Use Strong Authentication and Cryptography"
description: "Implement strong authentication mechanisms and encrypt all sensitive data using strong, modern algorithms."
tags: ["security", "authentication", "cryptography", "mfa"]
severity: "critical"
applies_to: ["all"]
automation_potential: ["sast", "code-review"]
suggested_tools: ["OWASP ZAP", "SAST tools", "cryptography libraries"]
related_rules: ["secure-config-secrets", "automate-vulnerability-management"]
---

**Description:** Implement strong authentication mechanisms, including multi-factor authentication (MFA). All sensitive data, both in transit and at rest, must be encrypted using strong, modern algorithms.

**Rationale:** Weak authentication can be easily bypassed, and unencrypted data is vulnerable to theft. Strong crypto and MFA are fundamental to protecting accounts and data.

**Good Practice:**
- Enforce strong password policies.
- Use standard, well-vetted authentication libraries (e.g., Passport.js, Django Auth).
- Use HTTPS for all traffic. Use AES-256 for data at rest.
