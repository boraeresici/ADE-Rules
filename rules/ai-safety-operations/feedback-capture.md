---
id: "feedback-capture"
title: "AI Feedback Capture"
description: "Implement mechanisms for capturing user feedback, raw prompts/outputs, and AI-specific telemetry to continuously improve AI model performance and safety, building on general observability and process improvement principles."
tags: ["ai-safety", "feedback", "telemetry", "continuous-improvement"]
severity: "high"
applies_to: ["ai", "llm", "ml"]
automation_potential: ["ui-integration", "analytics-pipeline"]
suggested_tools: ["feedback forms", "analytics platforms"]
related_rules: ["monitoring-observability-ai", "development-process-improvements", "metrics-implementation", "logging-best-practices"]
---

**Note:** This rule leverages the foundational telemetry collection practices defined in `metrics-implementation.md` and `logging-best-practices.md`, and contributes to the continuous improvement goals of `development-process-improvements.md`.

### Core Principles for AI Feedback Capture:
- **User Feedback Mechanisms:** Provide easy-to-use, one-click feedback options (e.g., `/+why`, thumbs up/down, error tagging) within the AI interface.
- **Raw Data Capture:** Allow users to securely attach or provide **raw prompts and model outputs** for detailed debugging and analysis.
- **AI-Specific Telemetry:** Collect telemetry relevant to AI model performance and safety, such as:
  - Success/failure rates of AI tasks.
  - Latency and time-to-response for AI inferences.
  - Error codes and types specific to AI model failures.
  - User engagement metrics with AI features.

### Production Checklist:
- [ ] One-click feedback mechanisms are integrated into AI interfaces.  
- [ ] Secure methods for users to attach raw prompts/outputs are implemented.  
- [ ] AI-specific telemetry (success/failure, latency, error codes) is collected and analyzed.  
- [ ] Feedback data is anonymized and processed in a privacy-compliant manner.  
- [ ] Feedback and telemetry data are regularly reviewed to inform AI model improvements.  
