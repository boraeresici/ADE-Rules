---
id: "reusability"
title: "Code Reusability"
description: "Practices to enhance code reusability by extracting common logic and using dependency injection."
tags: ["reusability", "design-patterns"]
severity: "high"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube", "IDE Refactoring Tools"]
related_rules: ["srp", "maintainability"]
---

# Rule: Code Reusability

**Description:** This rule outlines practices designed to enhance code reusability within a project. It focuses on strategies such as extracting common logic into shared components, effectively utilizing dependency injection, and organizing code into modular units to minimize duplication and improve development efficiency.

**Rationale:** Code reusability significantly reduces development time, improves consistency across the codebase, and minimizes the risk of bugs by centralizing common logic. By promoting the reuse of well-tested components, it leads to more robust, maintainable, and scalable software systems. It also fosters a more efficient development process and reduces technical debt.

### Core Principles:
- **Extract Common Logic:** Identify and extract repetitive code blocks or functionalities into dedicated functions, classes, or modules.
- **Dependency Injection:** Use Dependency Injection (DI) patterns to reduce tight coupling between components, making them more independent and reusable (referencing `dip.md`).
- **Utility Components:** Create utility classes, modules, or libraries for frequently used functionalities that are generic and applicable across different parts of the application.
- **Modular Design:** Organize code into well-defined, modular units that encapsulate specific responsibilities, making them easier to reuse.

### Good Practice:
```python
# Good: Extracting common validation logic into a reusable function
def validate_email(email):
    if not isinstance(email, str) or "@" not in email:
        raise ValueError("Invalid email format")
    # ... more validation logic ...
    return True

class UserRegistration:
    def register(self, email, password):
        validate_email(email)
        # ... rest of registration logic ...

class NewsletterSubscription:
    def subscribe(self, email):
        validate_email(email)
        # ... rest of subscription logic ...
```

### Bad Practice:
```python
# Bad: Duplicating validation logic across multiple parts of the application
class UserRegistration:
    def register(self, email, password):
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("Invalid email format")
        # ... rest of registration logic ...

class NewsletterSubscription:
    def subscribe(self, email):
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("Invalid email format")
        # ... rest of subscription logic ...
```

---

**Automation Potential:** Static analysis tools (e.g., SonarQube) can detect code duplication, suggesting areas for refactoring and reuse. IDEs offer refactoring tools to extract methods or classes. Code reviews are essential for identifying opportunities for reuse and ensuring the quality of shared components.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
