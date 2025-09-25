---
id: "quality-assurance"
title: "Quality Assurance"
description: "Guidelines for ensuring software quality through automated testing, mandatory code reviews, and performance/security testing."
tags: ["qa", "testing", "ci-cd", "quality"]
severity: "critical"
applies_to: ["project-management", "all"]
automation_potential: ["ci-cd-check", "test-runner", "code-review"]
suggested_tools: ["Jest", "Pytest", "Cypress", "Selenium", "SonarQube"]
related_rules: ["comprehensive-multi-layered-testing", "code-review"]
---

- Integrate automated tests into the CI/CD pipeline.
- Make code reviews mandatory.
- Conduct performance and security tests.

**Rationale:** A robust quality assurance process ensures the delivery of reliable, performant, and secure software. Automated tests provide rapid feedback, code reviews improve code quality, and specialized tests address specific concerns.

**Automation Potential:** CI/CD pipelines automate test execution. SAST/DAST tools automate security testing.