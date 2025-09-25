---
id: "vscode-settings"
title: "VS Code settings.json Configuration"
description: "Recommended settings for VS Code's settings.json to ensure consistent code formatting and linting."
tags: ["ide-setup", "vscode", "configuration"]
severity: "medium"
applies_to: ["ide-setup", "vscode"]
automation_potential: ["tool-integration", "manual-setup"]
suggested_tools: ["VS Code"]
related_rules: ["vscode-extensions", "jetbrains-setup"]
---

```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "typescript.tsdk": "node_modules/typescript/lib",
  "files.insertFinalNewline": true
}
```

**Rationale:** These settings ensure consistent code formatting upon saving, automatically fix linting issues, and correctly configure TypeScript for the project, leading to a more unified codebase.

**Automation Potential:** VS Code automatically applies these settings based on the configuration.
