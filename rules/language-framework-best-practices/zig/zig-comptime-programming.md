---
id: "zig-comptime-programming"
title: "Zig Comptime Programming"
description: "Leveraging Zig's compile-time features for metaprogramming and code generation."
tags: ["zig", "comptime", "metaprogramming"]
severity: "high"
applies_to: ["backend", "system-programming"]
automation_potential: ["zig-compiler"]
suggested_tools: ["Zig Compiler"]
related_rules: ["zig-best-practices"]
---

### Core Principles:
- Understand the power and limitations of `comptime`.
- Use `comptime` for code generation, type introspection, and optimization.
- Ensure `comptime` logic is clear and maintainable.

### Production Checklist:
- [ ] `comptime` is used to reduce runtime overhead.
- [ ] Generated code is correct and efficient.
- [ ] `comptime` errors are handled gracefully.
