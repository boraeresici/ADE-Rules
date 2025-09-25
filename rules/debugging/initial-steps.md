---
id: "initial-steps"
title: "Debugging Initial Steps"
description: "First steps to take when encountering a software defect, focusing on error capture and reproduction."
tags: ["debugging", "troubleshooting", "errors"]
severity: "high"
applies_to: ["all"]
automation_potential: ["tool-integration", "manual-review"]
suggested_tools: ["IDE debuggers", "logging frameworks"]
related_rules: ["debugging-process", "reporting", "debugging-best-practices"]
---

1. Capture the error message and stack trace.
2. Identify reproduction steps.
3. Isolate the location where the error occurs.
4. Apply a minimal fix.
5. Verify that the solution works.

**Rationale:** A structured approach to debugging helps in quickly pinpointing the root cause of an issue. Reproduction steps are crucial for consistency, and isolating the problem area streamlines the investigation.

**Automation Potential:** Automated testing can help in identifying reproduction steps.
