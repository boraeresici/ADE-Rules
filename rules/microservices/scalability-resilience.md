---
id: "scalability-resilience"
title: "Microservice Scalability and Resilience"
description: "Principles for designing independently scalable services and implementing resilience patterns like Circuit Breaker."
tags: ["microservices", "scalability", "resilience", "circuit-breaker"]
severity: "high"
applies_to: ["backend", "microservices", "architecture"]
automation_potential: ["tool-integration", "ci-cd-check"]
suggested_tools: ["Kubernetes", "Circuit Breaker libraries"]
related_rules: ["defining-service-boundaries", "inter-service-communication", "system-scalability"]
---

- Design each service to be independently scalable.
- Implement the Circuit Breaker pattern to isolate service failures.
- Add health check endpoints to monitor service health.

**Rationale:** Microservices enable independent scaling of components, optimizing resource utilization. Resilience patterns like Circuit Breaker prevent cascading failures and improve overall system stability.

**Automation Potential:** Container orchestration platforms (e.g., Kubernetes) automate scaling and health checks.
