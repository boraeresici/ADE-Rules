---
id: "shadow-evals"
title: "AI Shadow Evaluations"
description: "Conduct shadow evaluations comparing new AI models against baselines using a golden dataset to track AI-specific performance (accuracy, drift) and regressions before deployment, building on general testing and metrics principles."
tags: ["ai-safety", "model-evaluation", "ci-cd", "quality-assurance"]
severity: "critical"
applies_to: ["ai", "llm", "ml"]
automation_potential: ["ci-cd-integration", "automated-testing"]
suggested_tools: ["MLflow", "DVC", "CI/CD platforms"]
related_rules: ["model-lifecycle-management", "comprehensive-multi-layered-testing", "metrics-implementation"]
---

**Note:** This rule extends the general testing practices defined in `comprehensive-multi-layered-testing.md` and leverages metric implementation guidelines from `metrics-implementation.md`.

### Core Principles for AI Shadow Evaluations:
- **Golden Dataset:** Maintain a **golden set** of representative test cases (e.g., 10–50 cases) that are versioned and regularly updated.
- **Baseline Comparison:** Run shadow evaluations by comparing the performance of new AI models against established baselines using the golden dataset.
- **AI-Specific Performance Tracking:** Track key AI performance indicators such as:
  - **Accuracy, Precision, Recall, F1-score** (relevant to the model's task).
  - **Latency** (inference time).
  - **Regressions** in performance compared to the baseline.
  - **Data/Concept Drift** (if applicable, referencing `monitoring-observability-ai.md`).

### Production Checklist:
- [ ] A versioned and maintained golden dataset is used for evaluations.  
- [ ] Shadow evaluations are run before every AI model release.  
- [ ] AI-specific performance metrics (accuracy, latency, regressions) are tracked against baselines.  
- [ ] Alerts are configured for performance degradation or regression thresholds.  
- [ ] Shadow evaluation results are integrated into CI/CD pipelines for automated gating.  
