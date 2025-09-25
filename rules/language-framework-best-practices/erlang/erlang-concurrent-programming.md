---
id: "erlang-concurrent-programming"
title: "Erlang Concurrent Programming"
description: "Guidelines for effective concurrent programming in Erlang using Actors and message passing."
tags: ["erlang", "concurrency", "actors"]
severity: "high"
applies_to: ["backend", "distributed-systems"]
automation_potential: ["code-review"]
suggested_tools: ["Erlang/OTP"]
related_rules: ["erlang-fault-tolerance", "erlang-otp-patterns"]
---

### Core Principles:
- Embrace the Actor model for concurrency.
- Use message passing for inter-process communication.
- Design for isolation and fault tolerance.

### Production Checklist:
- [ ] Processes are isolated and communicate via messages.
- [ ] Message handling is robust.
- [ ] Concurrency patterns are used safely.
