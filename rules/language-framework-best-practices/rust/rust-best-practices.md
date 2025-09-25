---
id: "rust-best-practices"
title: "Rust Best Practices"
description: "Guidelines for writing idiomatic, safe, and efficient Rust code."
tags: ["rust", "best-practices", "language"]
severity: "high"
applies_to: ["backend", "system-programming"]
automation_potential: ["clippy", "rustfmt", "code-review"]
suggested_tools: ["Clippy", "Rustfmt"]
related_rules: ["rust-ownership-borrowing", "rust-async-programming"]
---

### Core Principles:
- Follow Rust's ownership and borrowing rules.
- Utilize Rust's powerful type system for compile-time guarantees.
- Write clear, concise, and idiomatic Rust code.

### Production Checklist:
- [ ] Code adheres to Rustfmt guidelines.
- [ ] Clippy lints are addressed.
- [ ] Error handling uses `Result` and `Option` effectively.
