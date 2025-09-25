---
id: "serverless-framework-usage"
title: "Serverless Framework Usage Rules"
description: "Best practices for defining, deploying, and managing serverless applications using the Serverless Framework."
tags: ["serverless", "framework", "deployment", "devops"]
severity: "medium"
applies_to: ["devops", "backend"]
automation_potential: ["ci-cd-check"]
suggested_tools: ["Serverless Framework"]
related_rules: ["aws-lambda-function-optimization", "azure-functions-best-practices"]
---

### Core Principles:
- Use declarative configuration for serverless resources.
- Automate deployments via CI/CD pipelines.
- Manage environment variables securely.

### Production Checklist:
- [ ] Serverless config is version-controlled.
- [ ] CI/CD pipeline automates deployments.
- [ ] Environment variables are secure.
