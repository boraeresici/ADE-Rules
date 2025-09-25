---
id: "lsp"
title: "Liskov Substitution Principle (LSP)"
description: "Subtypes must be substitutable for their base types without altering the correctness of the program."
tags: ["solid", "design-principles", "reusability"]
severity: "high"
applies_to: ["all"]
automation_potential: ["type-checker", "static-analysis", "code-review"]
suggested_tools: ["SonarQube", "TypeScript compiler"]
related_rules: ["srp", "ocp", "isp", "dip"]
---

# Rule: Liskov Substitution Principle (LSP)

**Description:** The Liskov Substitution Principle (LSP) states that subtypes must be substitutable for their base types without altering the correctness of the program. This means that if a program module uses a base class, it should be able to use any derived class without knowing it, and the program should still function correctly.

**Rationale:** LSP ensures that derived classes behave consistently with their base classes, preventing unexpected behavior when substituting objects. This is crucial for maintaining type safety, predictable system behavior, and enabling polymorphism to work as intended. Violations of LSP can lead to fragile designs, unexpected bugs, and difficulties in extending the system.

### Core Principles:
- **Substitutability:** Subtypes must be substitutable for their base types without altering the correctness of the program.
- **Behavioral Guarantees:** Derived classes should maintain the same behavioral guarantees (preconditions, postconditions, invariants) as their base classes.
- **No Unexpected Behavior:** Derived classes should not introduce unexpected side effects or throw new types of exceptions that are not part of the base class's contract.

### Good Practice:
```python
# Good: Square is a subtype of Rectangle, and can be substituted
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def area(self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self._width = self._height = width

    def set_height(self, height):
        self._width = self._height = height

def get_area(shape: Rectangle):
    return shape.area()

rect = Rectangle(2, 3)
sq = Square(4)

print(get_area(rect)) # Works
print(get_area(sq))   # Works, Square is substitutable
```

### Bad Practice:
```python
# Bad: Square is NOT a true subtype of Rectangle if set_width/set_height change both dimensions
# (This is a classic example where LSP is often violated if Square overrides set_width/set_height incorrectly)
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def area(self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self._width = self._height = width # Modifies height too

    def set_height(self, height):
        self._width = self._height = height # Modifies width too

def increase_width(rect: Rectangle):
    rect.set_width(rect._width + 1)
    # If rect is a Square, its height also changes, which is unexpected for a Rectangle client.

rect = Rectangle(2, 3)
increase_width(rect) # rect becomes (3, 3)

sq = Square(2)
increase_width(sq) # sq becomes (3, 3) - but expected (3, 2) if it were a Rectangle
```

---

**Automation Potential:** Type checkers and some static analysis tools can detect certain LSP violations, especially those related to method signatures and return types. Code reviews are crucial for identifying behavioral violations that are harder for automated tools to catch.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
