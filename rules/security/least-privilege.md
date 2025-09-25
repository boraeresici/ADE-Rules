---
id: "least-privilege"
title: "Enforce the Principle of Least Privilege"
description: "Every user, service, or process should only have the minimum permissions necessary to perform its function."
tags: ["security", "access-control", "rbac"]
severity: "critical"
applies_to: ["all"]
automation_potential: ["iac", "code-review"]
suggested_tools: ["IAM policies", "RBAC systems"]
related_rules: ["never-trust-user-input", "secure-config-secrets"]
---

**Description:** Every user, service, or process should only have the minimum permissions necessary to perform its function. Deny access by default.

**Rationale:** This principle minimizes the potential damage from a security breach. If an account is compromised, its access is already limited, containing the blast radius of the attack.

**Good Practice:**
- Implement Role-Based Access Control (RBAC).
- Check authorization for every single request.
- For CI/CD pipelines, grant the `GITHUB_TOKEN` minimal permissions.
