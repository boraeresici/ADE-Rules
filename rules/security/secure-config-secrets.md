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

# Rule: Secure Configuration and Secrets Management

**Description:** This rule emphasizes the critical importance of avoiding security misconfigurations and strictly prohibits storing sensitive information (secrets like API keys, database passwords, private keys) directly within source code. Instead, it mandates the use of dedicated, secure secrets management services.

**Rationale:** Security misconfigurations are a leading cause of data breaches, often resulting from default settings, incomplete configurations, or exposed interfaces. Storing secrets in source code is a severe vulnerability; if the code repository is compromised or accidentally exposed, all embedded secrets become immediately accessible to attackers, leading to widespread system compromise. Dedicated secrets management services provide a secure, centralized, and auditable way to handle sensitive credentials.

### Good Practice:
```yaml
# Example: Injecting secrets into a Kubernetes Pod via a Secret object
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  containers:
  - name: my-app-container
    image: my-app-image
    env:
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: my-db-secret
          key: password
```
*Example: Using Kubernetes Secrets to inject a database password as an environment variable at runtime, avoiding hardcoding in code.*

### Bad Practice:
```python
# Example: Hardcoding API keys directly in source code
API_KEY = "your_api_key_here"
DB_PASSWORD = "my_super_secret_password"

def make_api_call():
    # ... use API_KEY ...
    pass
```
*Example: Hardcoding sensitive API keys or passwords directly in source code, making them vulnerable if the code is exposed.*

---

**Automation Potential:** Static Application Security Testing (SAST) tools can detect hardcoded secrets in source code. Infrastructure as Code (IaC) tools can enforce secure configuration practices. CI/CD checks can validate that secrets are not committed to repositories. Dedicated secrets management services automate the secure storage and retrieval of credentials.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
