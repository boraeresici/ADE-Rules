---
id: "erlang-fault-tolerance"
title: "Erlang Fault Tolerance"
description: "Strategies for building highly available and fault-tolerant systems with Erlang."
tags: ["erlang", "fault-tolerance", "reliability"]
severity: "critical"
applies_to: ["backend", "distributed-systems"]
automation_potential: ["code-review"]
suggested_tools: ["Erlang/OTP"]
related_rules: ["erlang-concurrent-programming", "erlang-otp-patterns"]
---

### Core Principles:
- Use supervisors to monitor and restart processes.
- Design processes to be isolated and fail fast.
- Implement robust error handling and recovery.

### Production Checklist:
- [ ] Supervisor trees are well-defined.
- [ ] Processes are designed for failure.
- [ ] System recovers gracefully from errors.
