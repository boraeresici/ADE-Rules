---
id: "ocp"
title: "Open/Closed Principle (OCP)"
description: "Code should be open for extension but closed for modification."
tags: ["solid", "design-principles", "reusability"]
severity: "high"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube"]
related_rules: ["srp", "lsp", "isp", "dip"]
---

# Rule: Open/Closed Principle (OCP)

**Description:** The Open/Closed Principle (OCP) states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means that new functionality should be added by extending existing code, rather than by altering it.

**Rationale:** OCP encourages designing systems that can be extended with new functionality without altering existing, tested, and stable code. This significantly reduces the risk of introducing bugs into stable parts of the system, improves maintainability, and facilitates the evolution of the software over time. It promotes a more robust and flexible architecture.

### Core Principles:
- **Open for Extension:** The behavior of a module can be extended to meet new requirements.
- **Closed for Modification:** The source code of a module should not be modified once it has been developed and tested.
- **Abstractions:** Effectively use abstractions, interfaces, or inheritance to define stable extension points.
- **Extension Points:** Clearly define and document the extension points within the system.

### Good Practice:
```python
# Good: Using an interface (abstract base class) for extensibility
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class Order:
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor

    def checkout(self, amount):
        self.processor.process_payment(amount)

# New payment methods can be added without modifying the Order class.
order1 = Order(CreditCardProcessor())
order1.checkout(100)
order2 = Order(PayPalProcessor())
order2.checkout(50)
```

### Bad Practice:
```python
# Bad: Modifying existing code to add new functionality
class Order:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def checkout(self, amount):
        if self.payment_method == "credit_card":
            print(f"Processing credit card payment of ${amount}")
        elif self.payment_method == "paypal":
            print(f"Processing PayPal payment of ${amount}")
        # To add a new payment method, this method needs to be modified.
        # This violates OCP.
```

---

**Automation Potential:** Static analysis tools can sometimes identify violations of OCP by detecting frequent modifications to stable modules when new features are added. Design reviews and architectural analysis tools can help enforce OCP principles.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
