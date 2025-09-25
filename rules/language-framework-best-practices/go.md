---
id: "go"
title: "Go Best Practices"
description: "Guidelines for writing idiomatic, concurrent, and robust applications in Go."
tags: ["go", "backend", "concurrency"]
severity: "high"
applies_to: ["go", "backend"]
automation_potential: ["linter", "static-analysis", "code-review"]
suggested_tools: ["go vet", "golint", "staticcheck"]
related_rules: ["python-django", "javascript-typescript", "fastapi", "general-principles"]
---

- Use the `if err != nil` pattern for error handling.
- Effectively use interfaces.
- Appropriately use Go's built-in concurrency features (goroutines and channels).
- Design package structure logically and organized.

**Rationale:** Go's explicit error handling promotes robust applications. Interfaces enable flexible and testable designs. Goroutines and channels are fundamental for efficient concurrent programming in Go.

**Automation Potential:** `go vet` and `golint` can identify some issues.
