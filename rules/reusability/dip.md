---
id: "dip"
title: "Dependency Inversion Principle (DIP)"
description: "High-level modules should depend on abstractions, not concrete implementations."
tags: ["solid", "design-principles", "reusability"]
severity: "high"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube", "Dependency Injection frameworks"]
related_rules: ["srp", "ocp", "lsp", "isp"]
---

# Rule: Dependency Inversion Principle (DIP)

**Description:** The Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules. Both should depend on abstractions. Additionally, abstractions should not depend on details; details should depend on abstractions. This principle promotes loose coupling and flexibility in software design.

**Rationale:** Adhering to DIP promotes loose coupling between modules, making systems more flexible, testable, and maintainable. By depending on abstractions rather than concrete implementations, it allows for easier swapping of implementations (e.g., changing a database or a logging mechanism) without affecting high-level business logic. This significantly improves the testability of components and facilitates parallel development.

### Core Principles:
- **Depend on Abstractions:** High-level modules should depend on abstractions (interfaces or abstract classes), not on concrete implementations of low-level modules.
- **Abstractions Own Details:** Abstractions should not depend on details; instead, details (concrete implementations) should depend on abstractions.
- **Dependency Injection/Inversion of Control:** Effectively use dependency injection (DI) or Inversion of Control (IoC) containers to manage dependencies and provide concrete implementations at runtime.

### Good Practice:
```python
# Good: High-level module depends on an abstraction (interface)
from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(MessageSender):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSSender(MessageSender):
    def send(self, message):
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)

# High-level NotificationService depends on MessageSender abstraction
email_service = NotificationService(EmailSender())
email_service.notify("Hello via Email!")

sms_service = NotificationService(SMSSender())
sms_service.notify("Hello via SMS!")
```

### Bad Practice:
```python
# Bad: High-level module depends on a concrete implementation
class EmailSender:
    def send(self, message):
        print(f"Sending email: {message}")

class NotificationService:
    def __init__(self):
        self.sender = EmailSender() # Direct dependency on concrete implementation

    def notify(self, message):
        self.sender.send(message)

# To change to SMSSender, NotificationService's code needs modification.
# This violates DIP.
```

---

**Automation Potential:** Static analysis tools can help identify direct dependencies on concrete implementations in high-level modules. Dependency Injection (DI) frameworks automate the management of dependencies, making it easier to adhere to DIP. Code reviews are essential for validating architectural adherence to DIP.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
