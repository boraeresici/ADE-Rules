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

# Rule: Enforce the Principle of Least Privilege

**Description:** This rule mandates that every user, service, or process within a system should be granted only the absolute minimum permissions and access rights necessary to perform its intended function. Access should be denied by default, and privileges should be granted only when explicitly required.

**Rationale:** The Principle of Least Privilege (PoLP) is a fundamental security concept that significantly reduces the attack surface and limits the potential damage from security breaches. By restricting access, it minimizes the impact of compromised accounts or vulnerabilities, making it harder for attackers to move laterally or escalate privileges within a system. It helps contain the blast radius of an attack.

### Core Principles:
- **Just-Enough Access:** Grant users, services, and processes only the permissions required for their specific tasks, and no more. Deny access by default.
- **Just-in-Time Access:** Provide elevated privileges only when they are needed, and revoke them as soon as the task is completed.
- **Role-Based Access Control (RBAC):** Implement RBAC to define roles with specific permissions and assign users/services to these roles, rather than granting permissions directly.
- **Regular Review:** Periodically review and audit assigned permissions to ensure they remain appropriate and remove any unnecessary access.

### Good Practice:
```yaml
# Example: AWS IAM policy granting only necessary S3 read access
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-app-bucket/*",
        "arn:aws:s3:::my-app-bucket"
      ]
    }
  ]
}
```
*Example: An IAM policy granting only read access to a specific S3 bucket, adhering to PoLP.*

### Bad Practice:
```yaml
# Example: AWS IAM policy granting overly broad S3 access
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:*", # Grants all S3 actions
      "Resource": "*"    # Grants access to all S3 resources
    }
  ]
}
```
*Example: An IAM policy granting full access to all S3 resources, violating PoLP and creating a significant security risk.*

---

**Automation Potential:** Infrastructure as Code (IaC) tools (e.g., Terraform, CloudFormation) can define and enforce permissions programmatically. RBAC systems automate permission assignment based on roles. Code reviews are essential for validating permission configurations.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
