---
id: "project-structure"
title: "Project Structure and Code Quality"
description: "Principles for maintaining a modular, scalable, and high-quality codebase through refactoring and static analysis."
tags: ["architecture", "code-quality", "refactoring"]
severity: "high"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube", "ESLint", "Pylint"]
related_rules: ["refactoring", "code-quality-analysis"]
---

- Keep the project structure modular and scalable.
- Regularly address technical debt and refactor.
- Use static code analysis tools to maintain code quality.

**Rationale:** A modular and scalable project structure simplifies development, maintenance, and onboarding. Proactively managing technical debt prevents it from hindering future development. Static analysis helps enforce coding standards and identify potential issues early.

**Automation Potential:** Linters and static analysis tools (e.g., SonarQube, ESLint) automate code quality checks.