---
id: "go-microservices"
title: "Go Microservices Best Practices"
description: "Guidelines for building robust and scalable microservices with Go."
tags: ["go", "microservices", "architecture"]
severity: "high"
applies_to: ["backend", "microservices"]
automation_potential: ["code-review"]
suggested_tools: ["Go Micro", "gRPC"]
related_rules: ["go-best-practices", "microservices-best-practices"]
---

### Core Principles:
- Design services with clear boundaries and APIs.
- Implement robust error handling and observability.
- Utilize Go's concurrency features for performance.

### Production Checklist:
- [ ] Service APIs are well-defined and versioned.
- [ ] Observability (logging, metrics, tracing) is integrated.
- [ ] Concurrency patterns are used safely.
