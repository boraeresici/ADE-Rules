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

# Rule: Single Responsibility Principle (SRP)

**Description:** The Single Responsibility Principle (SRP) states that each class, module, or function should have only one reason to change, meaning it should have only one responsibility. This principle promotes high cohesion and loose coupling within a software system.

**Rationale:** Adhering to SRP makes components easier to understand, test, and maintain. When a component has only one responsibility, changes related to that responsibility do not affect other unrelated functionalities, thus reducing the risk of introducing bugs and simplifying future modifications. It also improves code readability and reusability.

### Core Principles:
- **One Reason to Change:** A component should have only one reason to change, meaning it should encapsulate a single, well-defined responsibility.
- **Separation of Concerns:** Different concerns (e.g., UI logic, business logic, data access, logging) should be properly separated into distinct components.
- **High Cohesion:** Components should be highly cohesive, meaning their internal elements are closely related and focused on a single purpose.

### Good Practice:
```python
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
*Example: Separating user data, persistence, and email sending into distinct classes, each with a single responsibility.*

### Bad Practice:
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
```
*Example: A `User` class handling both its own data, database persistence, and email communication, violating SRP.*

---

**Automation Potential:** Static analysis tools (e.g., SonarQube, ESLint, Pylint) can sometimes identify classes or functions with too many responsibilities (e.g., high cyclomatic complexity combined with many dependencies). Code reviews are essential for enforcing SRP and ensuring proper separation of concerns.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
