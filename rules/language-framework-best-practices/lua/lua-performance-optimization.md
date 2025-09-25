---
id: "lua-performance-optimization"
title: "Lua Performance Optimization"
description: "Techniques for optimizing Lua code for speed and efficiency."
tags: ["lua", "performance", "optimization"]
severity: "high"
applies_to: ["embedded-systems", "game-development", "scripting"]
automation_potential: ["profiler", "code-review"]
suggested_tools: ["Lua Profiler"]
related_rules: ["lua-best-practices"]
---

### Core Principles:
- Profile your code to identify bottlenecks.
- Minimize global variable access.
- Optimize table lookups and string manipulations.

### Production Checklist:
- [ ] Performance-critical sections are profiled.
- [ ] Global variable usage is minimized.
- [ ] Efficient data structures are used.
