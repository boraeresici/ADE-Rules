---
id: "rust-ownership-borrowing"
title: "Rust Ownership and Borrowing"
description: "Mastering Rust's ownership and borrowing system for memory safety without a garbage collector."
tags: ["rust", "memory-management", "safety"]
severity: "critical"
applies_to: ["backend", "system-programming"]
automation_potential: ["rustc-compiler", "clippy"]
suggested_tools: ["Rust Compiler", "Clippy"]
related_rules: ["rust-best-practices"]
---

### Core Principles:
- Understand ownership rules: each value has an owner.
- Understand borrowing rules: references borrow ownership.
- Avoid common borrowing pitfalls like dangling references.

### Production Checklist:
- [ ] Code compiles without ownership/borrowing errors.
- [ ] Lifetimes are correctly specified where needed.
- [ ] Unsafe Rust is minimized and thoroughly reviewed.
