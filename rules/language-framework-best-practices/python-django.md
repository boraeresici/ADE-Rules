---
id: "python-django"
title: "Python and Django Best Practices"
description: "Guidelines for writing idiomatic, efficient, and maintainable Python code within the Django framework."
tags: ["python", "django", "backend", "web"]
severity: "high"
applies_to: ["python", "django", "backend"]
automation_potential: ["linter", "static-analysis", "code-review"]
suggested_tools: ["Flake8", "Pylint", "Django check", "pytest-django"]
related_rules: ["javascript-typescript", "go", "fastapi", "general-principles"]
---

- Use list comprehensions and generator expressions where appropriate.
- Utilize Django's built-in features and tools as much as possible.
- Ensure PEP 8 compliance and follow Django's coding style guide.
- Use Class-Based Views (CBV) for complex views and Function-Based Views (FBV) for simple logic.
- Use Django ORM for database interactions; avoid raw SQL queries unless performance is critical.
- Strictly adhere to the MVT (Model-View-Template) pattern.
- Use Django's built-in testing tools (unittest and pytest-django).

**Rationale:** Following Python's PEP 8 and Django's conventions promotes readable and maintainable code. Leveraging built-in features and ORM ensures efficient and secure development.

**Automation Potential:** Linters (e.g., Flake8, Pylint) and Django's `check` command can enforce many of these rules.
