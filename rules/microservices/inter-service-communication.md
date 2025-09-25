---
id: "inter-service-communication"
title: "Inter-Service Communication"
description: "Guidelines for choosing appropriate communication patterns (REST, gRPC, message queues) and implementing API Gateways."
tags: ["microservices", "communication", "api-gateway"]
severity: "high"
applies_to: ["backend", "microservices", "architecture"]
automation_potential: ["tool-integration", "code-review"]
suggested_tools: ["Istio", "Linkerd", "RabbitMQ", "Apache Kafka"]
related_rules: ["defining-service-boundaries", "data-consistency-strategies", "distributed-tracing"]
---

# Rule: Inter-Service Communication

**Description:** This rule provides guidelines for selecting and implementing appropriate communication patterns within a microservices architecture. It covers synchronous communication methods like REST and gRPC, asynchronous patterns using message queues, and the strategic use of API Gateways to manage client-service interactions.

**Rationale:** Choosing the right communication pattern is vital for the performance, resilience, and scalability of a distributed system. Effective inter-service communication minimizes latency, ensures data consistency, and simplifies the management of complex service interactions. API Gateways centralize concerns like routing, authentication, and rate limiting, improving overall system manageability.

### Core Principles:
- **Synchronous Communication:** Use REST or gRPC for synchronous, request-response communication where immediate feedback is required (referencing `restful-api-design.md` or `grpc.md`).
- **Asynchronous Communication:** Employ message queues (e.g., RabbitMQ, Apache Kafka) for asynchronous communication, event-driven architectures, and decoupling services.
- **API Gateway Pattern:** Implement an API Gateway to centralize concerns such as routing, authentication, authorization, rate limiting, and caching for client-service communication.
- **Service Mesh:** Consider using a service mesh (e.g., Istio, Linkerd) to automate many aspects of inter-service communication, including traffic management, security, and observability.

### Good Practice:
```protobuf
syntax = "proto3";

package userservice;

service UserService {
  rpc GetUser (GetUserRequest) returns (User) {}
  rpc CreateUser (CreateUserRequest) returns (User) {}
}

message GetUserRequest {
  string user_id = 1;
}

message User {
  string user_id = 1;
  string name = 2;
  string email = 3;
}
```
*Example: A well-defined gRPC service using Protocol Buffers for efficient, type-safe synchronous communication.*

### Bad Practice:
```json
// Example: Direct HTTP calls between microservices without service discovery or proper error handling
// Service A making a direct call to Service B's hardcoded IP/port
// This leads to tight coupling, brittle systems, and difficult maintenance.
{
  "serviceA": {
    "dependency": "http://192.168.1.100:8080/api/serviceB"
  }
}
```
*Example: Tightly coupled services communicating directly via hardcoded endpoints, lacking resilience and flexibility.*

---

**Automation Potential:** Service mesh technologies (e.g., Istio, Linkerd) automate many aspects of inter-service communication, including traffic management, security, and observability. API Gateway solutions automate routing and policy enforcement. Code reviews are essential for validating communication patterns and protocol choices.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
