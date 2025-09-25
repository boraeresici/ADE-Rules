---
id: "readability-clarity"
title: "Readability and Clarity"
description: "Code should be written to be easily understandable by other developers."
tags: ["code-quality", "readability", "clean-code"]
severity: "high"
applies_to: ["all"]
automation_potential: ["linter", "code-review"]
suggested_tools: ["ESLint", "Pylint", "Flake8", "SonarQube"]
related_rules: ["consistency", "simplicity-kiss", "commenting-documentation"]
---

# Rule: Readability and Clarity

**Description:** Code should be written to be easily understandable by other developers. Variable names, function names, and comments should be clear and descriptive. Avoid overly complex or "clever" code that is difficult to decipher.

**Rationale:** Readable code is easier to debug, maintain, and extend. It reduces the cognitive load on developers joining the project or revisiting the code after a period.

**Good Practice:**
```python
# Descriptive variable names
def calculate_discounted_price(price, discount_percentage):
    """Calculates the final price after applying a discount."""
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    return final_price
```

**Bad Practice:**
```python
# Cryptic names
def calc(p, d):
    # d is percentage
    da = p * (d / 100)
    fp = p - da
    return fp
```

---

**Automation Potential:** This rule can be partially automated through linters (e.g., ESLint, Pylint) that check for naming conventions and code complexity. Code reviews are essential for subjective aspects of readability.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
