---
id: "srp"
title: "Single Responsibility Principle (SRP)"
description: "Each class or function should have only one responsibility and one reason to change."
tags: ["solid", "design-principles", "reusability"]
severity: "high"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube", "ESLint", "Pylint"]
related_rules: ["ocp", "lsp", "isp", "dip", "simplicity-kiss"]
---

- Each class or function should have only one responsibility and only one reason to change.
- Different concerns (UI, business logic, data access) should be properly separated.

**Rationale:** SRP promotes high cohesion and loose coupling, making components easier to understand, test, and maintain. Changes to one responsibility do not affect others.

**Automation Potential:** Static analysis tools can sometimes identify classes with too many responsibilities (e.g., high cyclomatic complexity combined with many dependencies).

### Example (Single Responsibility Principle):
```python
# Bad: Class with multiple responsibilities
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        # Save user to database
        pass

    def send_email(self, message):
        # Send email to user
        pass

# Good: Responsibilities separated
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        # Save user to database
        pass

class EmailService:
    def send_email(self, user, message):
        # Send email to user
        pass
```
