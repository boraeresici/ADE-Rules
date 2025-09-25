---
id: "zuplo-deployment-gitops"
title: "Zuplo Deployment with GitOps"
description: "Guidelines for deploying Zuplo API Gateway using GitOps principles."
tags: ["zuplo", "deployment", "gitops", "ci-cd"]
severity: "high"
applies_to: ["devops", "api"]
automation_potential: ["ci-cd-integration"]
suggested_tools: ["GitHub Actions", "GitLab CI"]
related_rules: ["zuplo-api-gateway-setup", "automate-deployments-ci-cd"]
---

### Core Principles:
- Manage Zuplo configuration in a Git repository.
- Automate deployments via CI/CD pipelines.
- Ensure declarative configuration for infrastructure.

### Production Checklist:
- [ ] Zuplo config is version-controlled.
- [ ] CI/CD pipeline automates Zuplo deployments.
- [ ] Rollback procedures are defined.
