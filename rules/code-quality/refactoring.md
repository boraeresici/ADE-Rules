---
id: "refactoring"
title: "Refactoring"
description: "Regularly refactor code to improve its structure, readability, and performance without changing its external behavior."
tags: ["code-quality", "refactoring", "technical-debt"]
severity: "medium"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube", "IDE Refactoring Tools"]
related_rules: ["simplicity-kiss", "srp", "ocp"]
---

**Description:** Regularly refactor code to improve its structure, readability, and performance without changing its external behavior. Address technical debt proactively.

**Rationale:** Codebases evolve, and what was a good solution yesterday might not be optimal today. Refactoring prevents code decay and keeps the system healthy.

**Good Practice:**
- Breaking down a large function into smaller, more manageable ones.
- Removing duplicate code by extracting it into a shared utility.
- Improving the names of variables and functions to be more descriptive.
