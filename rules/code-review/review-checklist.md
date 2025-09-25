---
id: "review-checklist"
title: "Code Review Checklist"
description: "A comprehensive checklist for evaluating code quality, security, and functionality during a code review."
tags: ["code-review", "checklist", "quality", "security"]
severity: "high"
applies_to: ["project-management", "all"]
automation_potential: ["linter", "static-analysis", "code-review"]
suggested_tools: ["SonarQube", "ESLint", "Pylint", "SAST tools"]
related_rules: ["review-approach", "feedback-organization", "code-review-best-practices"]
---

- Is the code simple and readable?
- Are functions and variables well-named?
- Is there any repetitive code?
- Is appropriate error handling implemented?
- Are sensitive information or API keys exposed?
- Is input validation implemented?
- Is there good test coverage?
- Are performance considerations addressed?

**Rationale:** A comprehensive checklist ensures that all critical aspects of code quality, security, and functionality are evaluated during the review process.

**Automation Potential:** Many of these checks can be automated by linters, static analysis tools, and security scanners.
