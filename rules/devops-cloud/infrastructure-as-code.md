---
id: "infrastructure-as-code"
title: "Infrastructure as Code (IaC)"
description: "All cloud infrastructure should be defined and managed as code using tools like Terraform, AWS CloudFormation, or Azure Resource Manager."
tags: ["devops", "iac", "cloud", "automation"]
severity: "critical"
applies_to: ["devops", "cloud", "backend"]
automation_potential: ["ci-cd-check", "static-analysis", "code-review"]
suggested_tools: ["Terraform", "AWS CloudFormation", "Azure Resource Manager"]
related_rules: ["automate-deployments-ci-cd", "containerize-applications"]
---

**Description:** All cloud infrastructure should be defined and managed as code using tools like Terraform, AWS CloudFormation, or Azure Resource Manager. Do not create or modify infrastructure manually via a web console.

**Rationale:** IaC ensures infrastructure is provisioned consistently, repeatably, and in a version-controlled manner. It enables peer review of infrastructure changes and automates environment creation.

**Good Practice:**
```hcl
# Example Terraform for an S3 bucket
resource "aws_s3_bucket" "static_website" {
  bucket = "my-static-website-bucket"
  acl    = "public-read"

  website {
    index_document = "index.html"
  }
}
```
