---
id: "service-architecture"
title: "Backend Service Architecture"
description: "Guidelines for choosing between microservice and monolithic architectures, inter-service communication, and fault tolerance, including output definitions."
tags: ["backend", "architecture", "microservices", "monolith"]
severity: "high"
applies_to: ["backend", "architecture", "microservices"]
automation_potential: ["tool-integration", "code-review"]
suggested_tools: ["Kubernetes", "Istio", "Linkerd"]
related_rules: ["backend-fundamentals", "restful-api-design", "database-design"]
---

- Make an informed choice between microservice and monolithic architecture.
- Choose appropriate protocols for inter-service communication (HTTP, gRPC, message queues).
- Implement service discovery and load balancing mechanisms.
- Use the circuit breaker pattern for fault tolerance and resilience.
- Use unique request IDs for distributed tracing.

**Rationale:** The choice of architecture impacts scalability, development speed, and operational complexity. Robust inter-service communication and fault tolerance are critical in distributed systems.

**Automation Potential:** Container orchestration platforms (e.g., Kubernetes) automate service discovery and load balancing.

### Service Architecture Example (ASCII Diagram):
```
+------------+     +-------------+     +--------------+
|            |     |             |     |              |
|   User     |     |   Product   |     |    Order     |
|  Service   |     |   Service   |     |   Service    |
|            |     |             |     |              |
+------------+     +-------------+     +--------------+
       |                  |                   |
       |                  |                   |
       v                  v                   v
+---------------------------------------------+
|                                             |
|              API Gateway                    |
|                                             |
+---------------------------------------------+
                    |
                    |
                    v
        +------------------------+
        |                        |
        |      Load Balancer     |
        |                        |
        +------------------------+
                    |
                    |
                    v
        +------------------------+
        |                        |
        |       Client Apps      |
        |                        |
        +------------------------+
```

### Output
- API endpoint definitions (with example requests and responses).
- Service architecture diagram (mermaid or ASCII).
- Database schema with key relationships.
- List of technology recommendations with brief justifications.
- Potential bottlenecks and scaling measures.

**Rationale:** Clearly defined outputs ensure that the backend development process is well-documented, transparent, and aligned with architectural goals.
