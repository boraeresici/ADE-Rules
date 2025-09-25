---
id: "rust-async-programming"
title: "Rust Async Programming"
description: "Guidelines for effective asynchronous programming in Rust using `async`/`await`."
tags: ["rust", "async", "concurrency"]
severity: "high"
applies_to: ["backend", "network-services"]
automation_potential: ["clippy", "code-review"]
suggested_tools: ["Tokio", "async-std"]
related_rules: ["rust-best-practices"]
---

### Core Principles:
- Understand the `async`/`await` syntax and its implications.
- Choose an appropriate async runtime (e.g., Tokio, async-std).
- Handle futures and tasks efficiently.

### Production Checklist:
- [ ] Async code avoids common pitfalls like blocking operations.
- [ ] Proper error handling for futures.
- [ ] Concurrency patterns are used safely and efficiently.
