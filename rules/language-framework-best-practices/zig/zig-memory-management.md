---
id: "zig-memory-management"
title: "Zig Memory Management"
description: "Guidelines for explicit and safe memory management in Zig."
tags: ["zig", "memory-management", "safety"]
severity: "critical"
applies_to: ["backend", "system-programming"]
automation_potential: ["zig-compiler", "code-review"]
suggested_tools: ["Zig Compiler"]
related_rules: ["zig-best-practices"]
---

### Core Principles:
- Understand Zig's allocator concept.
- Use appropriate allocators for different contexts.
- Ensure memory is freed correctly to prevent leaks.

### Production Checklist:
- [ ] Allocators are used consistently.
- [ ] Memory leaks are prevented through careful management.
- [ ] Memory safety is prioritized.
