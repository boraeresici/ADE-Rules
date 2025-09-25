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

# Rule: Backend Service Architecture

**Description:** This rule provides guidelines for making informed decisions about backend service architectures, including the choice between microservice and monolithic patterns. It also covers best practices for inter-service communication, implementing fault tolerance, and defining clear architectural outputs to ensure robust and scalable systems.

**Rationale:** The choice of architecture significantly impacts scalability, development speed, operational complexity, and system resilience. Robust inter-service communication and effective fault tolerance mechanisms are critical for maintaining stability and performance in distributed systems. Clearly defined architectural outputs ensure documentation and alignment with project goals.

### Core Principles:
- **Architecture Choice:** Make an informed choice between microservice and monolithic architectures based on project requirements, team size, and scalability needs.
- **Inter-Service Communication:** Choose appropriate protocols for inter-service communication (e.g., HTTP/REST, gRPC, message queues) considering latency, throughput, and reliability.
- **Service Discovery & Load Balancing:** Implement robust service discovery and load balancing mechanisms to ensure services can find each other and distribute traffic efficiently.
- **Fault Tolerance:** Utilize patterns like circuit breakers, retries, and bulkheads for fault tolerance and resilience in distributed systems.
- **Distributed Tracing:** Implement unique request IDs for distributed tracing to enable end-to-end visibility and easier debugging (referencing `distributed-tracing.md`).

### Good Practice:
```mermaid
graph TD
    A[Client] --> B(API Gateway)
    B --> C{User Service}
    B --> D{Product Service}
    B --> E{Order Service}
    C --> F[Database]
    D --> F
    E --> F
```
*Example: A microservices architecture with an API Gateway, demonstrating clear service boundaries.*

### Bad Practice:
```mermaid
graph TD
    A[Client] --> B(Monolithic App)
    B --> C(Database)
    B --> D(External Service)
    B -- Direct Call --> E(Another Monolithic App)
```
*Example: A monolithic application with tight coupling and direct calls to other large applications, leading to scalability and maintenance issues.*

---

**Automation Potential:** Container orchestration platforms (e.g., Kubernetes) automate service discovery and load balancing. Infrastructure as Code (IaC) tools can automate the deployment of architectural components. Code reviews are essential for validating architectural decisions and adherence to principles.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
