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

- Use REST or gRPC for synchronous communication.
- Use message queues (RabbitMQ, Apache Kafka) for asynchronous communication.
- Implement the API Gateway pattern to manage client-service communication.

**Rationale:** Choosing the right communication pattern is vital for performance, resilience, and scalability in a distributed system. API Gateways centralize concerns like routing, authentication, and rate limiting.

**Automation Potential:** Service mesh technologies (e.g., Istio, Linkerd) automate many aspects of inter-service communication.

### Example (gRPC Service Definition):
```protobuf
syntax = "proto3";

package userservice;

service UserService {
  rpc GetUser (GetUserRequest) returns (User) {}
  rpc CreateUser (CreateUserRequest) returns (User) {}
  rpc UpdateUser (UpdateUserRequest) returns (User) {}
  rpc DeleteUser (DeleteUserRequest) returns (DeleteUserResponse) {}
}

message GetUserRequest {
  string user_id = 1;
}

message User {
  string user_id = 1;
  string name = 2;
  string email = 3;
}

// Other message definitions...
```
