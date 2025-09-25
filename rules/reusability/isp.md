---
id: "isp"
title: "Interface Segregation Principle (ISP)"
description: "Clients should not be forced to depend on interfaces they do not use."
tags: ["solid", "design-principles", "reusability"]
severity: "high"
applies_to: ["all"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube"]
related_rules: ["srp", "ocp", "lsp", "dip"]
---

# Rule: Interface Segregation Principle (ISP)

**Description:** The Interface Segregation Principle (ISP) states that clients should not be forced to depend on interfaces they do not use. Instead of one large, general-purpose interface, it is better to have many small, client-specific interfaces.

**Rationale:** Adhering to ISP promotes loose coupling and improves the maintainability and flexibility of a system. When clients depend only on the methods they actually use, changes to unused parts of a large interface do not force clients to recompile or redeploy, reducing the impact of modifications and simplifying development. It also leads to more focused and cohesive interfaces.

### Core Principles:
- **Client-Specific Interfaces:** Design interfaces that are specific to the needs of individual clients or client groups.
- **Avoid Fat Interfaces:** Do not create large, monolithic interfaces that force clients to implement methods they do not need.
- **Loose Coupling:** Promote loose coupling by ensuring clients depend only on the minimal set of functionalities they require.

### Good Practice:
```python
# Good: Segregated interfaces for different client needs
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class SimplePrinter(Printer):
    def print_document(self):
        print("Printing...")

class MultiFunctionDevice(Printer, Scanner):
    def print_document(self):
        print("Printing from MFD...")
    def scan_document(self):
        print("Scanning from MFD...")

def use_printer(device: Printer):
    device.print_document()

def use_scanner(device: Scanner):
    device.scan_document()

# Clients only depend on the interfaces they use.
use_printer(SimplePrinter())
use_scanner(MultiFunctionDevice())
```

### Bad Practice:
```python
# Bad: A single, fat interface forcing clients to implement unused methods
from abc import ABC, abstractmethod

class IMultiFunctionDevice(ABC):
    @abstractmethod
    def print_document(self):
        pass
    @abstractmethod
    def scan_document(self):
        pass
    @abstractmethod
    def fax_document(self):
        pass

class SimplePrinter(IMultiFunctionDevice):
    def print_document(self):
        print("Printing...")
    def scan_document(self):
        raise NotImplementedError("Scan not supported") # Forced to implement unused method
    def fax_document(self):
        raise NotImplementedError("Fax not supported") # Forced to implement unused method
```

---

**Automation Potential:** Static analysis tools can help identify interfaces with many methods that are frequently left unimplemented or throw `NotImplementedError` in client classes. Code reviews are essential for designing well-segregated interfaces.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
