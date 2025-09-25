---
id: "erlang-otp-patterns"
title: "Erlang OTP Patterns"
description: "Best practices for utilizing Erlang/OTP behaviors and design principles."
tags: ["erlang", "otp", "design-patterns"]
severity: "high"
applies_to: ["backend", "distributed-systems"]
automation_potential: ["code-review"]
suggested_tools: ["Erlang/OTP"]
related_rules: ["erlang-concurrent-programming", "erlang-fault-tolerance"]
---

### Core Principles:
- Understand and apply OTP behaviors (e.g., `gen_server`, `gen_event`, `supervisor`).
- Design applications as OTP applications.
- Leverage OTP for common concurrency and fault-tolerance patterns.

### Production Checklist:
- [ ] OTP behaviors are used appropriately.
- [ ] Applications are structured as OTP applications.
- [ ] Common OTP patterns are applied correctly.
