---
id: "managed-serverless-services"
title: "Use Managed and Serverless Services"
description: "Prefer managed and serverless cloud services over self-hosting to reduce operational overhead and improve reliability."
tags: ["cloud", "serverless", "managed-services", "aws", "gcp", "azure"]
severity: "high"
applies_to: ["devops", "cloud", "backend", "frontend"]
automation_potential: ["iac", "ci-cd-check"]
suggested_tools: ["AWS Fargate", "Google Cloud Run", "AWS RDS", "Azure Cosmos DB"]
related_rules: ["infrastructure-as-code", "system-scalability"]
---

**Description:** Prefer managed and serverless cloud services over self-hosting. This includes using services like AWS Fargate, Google Cloud Run, AWS RDS, and Azure Cosmos DB.

**Rationale:** Managed services reduce operational overhead, improve reliability and scalability, and allow development teams to focus on application logic instead of infrastructure management.

**Good Practice:**
- Use AWS Fargate or Google Cloud Run for serverless containers.
- Use managed databases like AWS RDS or Azure SQL.
- Use S3/CloudFront or equivalent for distributing static content.
