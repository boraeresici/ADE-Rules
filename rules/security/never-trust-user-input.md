---
id: "never-trust-user-input"
title: "Never Trust User Input"
description: "Treat all input from users or external systems as untrusted and validate/sanitize to prevent injection attacks."
tags: ["security", "input-validation", "xss", "sqli"]
severity: "critical"
applies_to: ["all"]
automation_potential: ["linter", "sast", "dast", "code-review"]
suggested_tools: ["OWASP ESAPI", "DOMPurify", "SAST tools"]
related_rules: ["least-privilege", "automate-vulnerability-management"]
---

**Description:** Treat all input from users or external systems as untrusted. All input must be validated and sanitized to prevent injection attacks (e.g., SQLi, XSS).

**Rationale:** Untrusted input is a primary vector for security attacks. Strict validation and sanitization at the point of entry are the first line of defense.

**Good Practice:**
- Use parameterized queries (prepared statements) for all database access.
- Use an allow-list approach for validation where possible.
- Sanitize data before rendering it in a UI to prevent XSS.
