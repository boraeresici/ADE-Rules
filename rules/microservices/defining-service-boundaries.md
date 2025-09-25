---
id: "defining-service-boundaries"
title: "Defining Microservice Boundaries"
description: "Guidelines for establishing clear and independent service boundaries using Domain-Driven Design principles."
tags: ["microservices", "architecture", "ddd"]
severity: "high"
applies_to: ["backend", "microservices", "architecture"]
automation_potential: ["static-analysis", "code-review"]
suggested_tools: ["SonarQube"]
related_rules: ["inter-service-communication", "data-consistency-strategies", "scalability-resilience"]
---

- Ensure each service has a single business responsibility (Single Responsibility Principle).
- Define bounded contexts using Domain-Driven Design (DDD) principles.
- Ensure services can be developed, tested, and deployed independently of each other.

**Rationale:** Well-defined service boundaries are crucial for realizing the benefits of microservices. They promote loose coupling, high cohesion, and independent evolution of services.

**Automation Potential:** Architectural analysis tools can help visualize service dependencies.
