---
id: "lua-scripting-guidelines"
title: "Lua Scripting Guidelines"
description: "Best practices for integrating Lua as a scripting language in host applications."
tags: ["lua", "scripting", "integration"]
severity: "medium"
applies_to: ["embedded-systems", "game-development", "host-applications"]
automation_potential: ["code-review"]
suggested_tools: []
related_rules: ["lua-best-practices"]
---

### Core Principles:
- Define clear APIs between host and Lua scripts.
- Implement robust error handling for script execution.
- Secure the Lua environment to prevent malicious scripts.

### Production Checklist:
- [ ] Host-Lua API is well-documented.
- [ ] Script errors are caught and reported.
- [ ] Lua sandbox is properly configured.
