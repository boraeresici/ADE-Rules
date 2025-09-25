---
id: "unique-rule-identifier" # Required: A unique, kebab-case identifier for the rule (e.g., "readability-clarity")
title: "Descriptive Rule Title" # Required: A clear, concise title for the rule (e.g., "Code Readability and Clarity")
description: "A brief summary of what this rule is about and its purpose." # Required: A short description of the rule.
tags: ["tag1", "tag2", "category"] # Required: An array of relevant tags for categorization and filtering.

# Optional fields for enhanced AI/ADE consumption (refer to docs/metadata-glossary.md for definitions)
severity: "medium" # Optional: The criticality of the rule (e.g., "critical", "high", "medium", "low", "suggestion"). See [Metadata Glossary](docs/metadata-glossary.md#1-severity).
applies_to: ["language", "framework"] # Optional: An array of specific technologies/domains. See [Metadata Glossary](docs/metadata-glossary.md#2-applies_to).
automation_potential: ["linter", "manual-review"] # Optional: How this rule can be automated. See [Metadata Glossary](docs/metadata-glossary.md#3-automation_potential).
suggested_tools: ["ESLint", "SonarQube"] # Optional: Specific tools that can help enforce or check this rule. See [Metadata Glossary](docs/metadata-glossary.md#4-suggested_tools).
related_rules: ["related-rule-id-1", "related-rule-id-2"] # Optional: An array of IDs of other related rules. See [Metadata Glossary](docs/metadata-glossary.md#5-related_rules).
---

# Rule: [Descriptive Rule Title]

**Description:** [Provide a detailed explanation of the rule. What does it mean? What does it aim to achieve? Be clear and comprehensive.]

**Rationale:** [Explain the "why" behind this rule. What problems does it solve? What benefits does it bring (e.g., maintainability, performance, security)?]

**Good Practice:**
```[language]
# Provide a clear example of code that adheres to this rule.
# Include comments to explain key aspects if necessary.
# Example:
# def calculate_sum(a, b):
#     return a + b
```

**Bad Practice:**
```[language]
# Provide a clear example of code that violates this rule.
# Explain why it's considered bad practice.
# Example:
# def s(a, b): # Cryptic name
#     return a + b
```

# Optional: Structured Examples (for advanced AI/ADE parsing)

# If using structured examples, they would replace the Good/Bad Practice sections above.
# This is a more advanced concept from iyilestirme.md.
# good_example:
#   language: python
#   code: |
#     def calculate_discounted_price(price, discount_percentage):
#         """Calculates the final price after applying a discount."""
#         discount_amount = price * (discount_percentage / 100)
#         final_price = price - discount_amount
#         return final_price
# bad_example:
#   language: python
#   code: |
#     def calc(p, d):
#         # d is percentage
#         da = p * (d / 100)
#         fp = p - da
#         return fp

---

**Automation Potential:** [Briefly describe how this rule can be automated or checked by tools. Refer to `suggested_tools` if applicable.]

**Further Reading:** [Provide links to external resources, articles, or documentation related to this rule. This section should contain actual, clickable resources to enrich the rule's context.]
