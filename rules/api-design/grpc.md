---
id: "grpc"
title: "gRPC Design"
description: "Best practices for designing high-performance, low-latency APIs using gRPC, Protocol Buffers, and HTTP/2 streaming."
tags: ["api", "grpc", "rpc", "protobuf"]
severity: "high"
applies_to: ["backend", "microservices", "api"]
automation_potential: ["code-generation", "code-review"]
suggested_tools: ["Protocol Buffers compiler", "gRPC frameworks"]
related_rules: ["restful-api", "graphql", "api-selection-process"]
---

gRPC is a high-performance, low-latency RPC (Remote Procedure Call) framework developed by Google.

### Core Principles:
1. Data serialization using Protocol Buffers.
2. Bi-directional streaming built on HTTP/2.
3. Providing strong type safety.
4. Rapid development with code generation.
5. Multi-language support.

**Rationale:** gRPC is ideal for high-performance, inter-service communication in microservices architectures due to its efficient binary serialization and HTTP/2 streaming capabilities. Code generation simplifies client and server implementation.

**Automation Potential:** Protocol Buffer compilers automate code generation.

### Example (Protocol Buffers):
```protobuf
syntax = "proto3";

service UserService {
  rpc GetUser (UserRequest) returns (User) {}
  rpc ListUsers (UserListRequest) returns (stream User) {}
}

message UserRequest {
  string user_id = 1;
}

message UserListRequest {
  int32 page_size = 1;
  string page_token = 2;
}

message User {
  string user_id = 1;
  string name = 2;
  string email = 3;
}
```

### When to Use:
- For microservices architectures.
- When high performance and low latency are required.
- In inter-service communication, especially in internal systems.
- In real-time streaming applications.
