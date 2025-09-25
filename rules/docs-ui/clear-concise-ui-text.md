---
id: "clear-concise-ui-text"
title: "Clear and Concise UI Text"
description: "All user interface texts, including labels, buttons, and messages, should be clear, concise, and action-oriented."
tags: ["ui", "ux", "copywriting", "readability"]
severity: "high"
applies_to: ["frontend", "ui-ux"]
automation_potential: ["linter", "manual-review"]
suggested_tools: ["Grammarly", "Stylelint"]
related_rules: ["user-centric-guiding-language", "consistency-terminology-style"]
---

**Description:** All user interface texts, including labels, buttons, and messages, should be clear, concise, and action-oriented. Avoid marketing language and unnecessary words.

**Rationale:** Clear language in the UI improves user experience, reduces errors, and builds trust. Action-oriented text guides users effectively and helps them complete tasks efficiently.

**Good Practice:**
```
# Button Text
Good: "Deploy H100 GPU Cluster"
Bad: "Unleash the power of GPUs."

# Status Message
Good: "Your cluster is ready."
Bad: "Your cluster setup is complete and you can now start using it."
```
