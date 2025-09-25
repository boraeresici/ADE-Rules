---
id: "model-lifecycle-management"
title: "AI Model Lifecycle Management"
description: "Manage the lifecycle of AI models, including versioning, release notes, planned deprecation, and automated evaluation in CI/CD pipelines, building on general CI/CD and version control principles."
tags: ["ai-operations", "mlops", "ci-cd", "model-management"]
severity: "high"
applies_to: ["ai", "llm", "ml"]
automation_potential: ["ci-cd-integration", "model-registry"]
suggested_tools: ["MLflow", "DVC", "Kubeflow", "CI/CD platforms"]
related_rules: ["shadow-evals", "automate-deployments-ci-cd", "version-control"]
---

**Note:** This rule extends the general `automate-deployments-ci-cd.md` for deployment automation and `version-control.md` for artifact management, specifically for AI models.

### Core Principles for AI Model Lifecycle Management:
- **Model Versioning:** Implement robust versioning for all AI models, datasets, and associated code, typically using a model registry.
- **Release Management:** Define clear processes for releasing new model versions, including release notes and impact assessments.
- **Planned Deprecation:** Establish a strategy for the planned deprecation and archiving of old model versions.
- **Automated Evaluation in CI/CD:** Integrate automated model evaluation (e.g., `shadow-evals.md`) into CI/CD pipelines to ensure quality and prevent regressions before deployment.

### Production Checklist:
- [ ] All AI models are versioned and managed in a dedicated model registry.  
- [ ] Release notes are created for every new model version, detailing changes and expected impact.  
- [ ] A clear process for planned deprecation and archiving of old models is in place.  
- [ ] CI/CD pipelines include automated evaluation steps for AI models before deployment.  
- [ ] Model lineage (data, code, hyperparameters) is tracked for reproducibility and auditability.  
