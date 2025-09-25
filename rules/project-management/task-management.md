---
id: "task-management"
title: "Task Management"
description: "Best practices for defining, organizing, and tracking tasks with clear descriptions and acceptance criteria."
tags: ["project-management", "agile", "tasks"]
severity: "high"
applies_to: ["project-management", "all"]
automation_potential: ["tool-integration"]
suggested_tools: ["Jira", "Trello", "Asana"]
related_rules: ["version-control", "methodology"]
---

- Define clear descriptions and acceptance criteria for each task.
- Create a detailed task list based on the Product Requirement Document (PRD).
- Structure tasks hierarchically as main tasks and subtasks.
- Store the task list in Markdown format in the `/tasks/` directory.
- Attach relevant files and notes to the task list.

**Rationale:** Clear task definitions and acceptance criteria ensure everyone understands what needs to be done and when it's considered complete. Hierarchical structuring helps manage complexity, and centralized task lists improve visibility and tracking.

**Automation Potential:** Project management tools (e.g., Jira, Trello, Asana) automate task tracking and reporting.

### Example (Task List Format):
```markdown
## Related Files

- `src/components/UserProfile.tsx` - Main user profile component.
- `src/components/UserProfile.test.tsx` - Unit tests for UserProfile.

### Notes

- Unit tests should generally be located in the same directory as the code files being tested.

## Tasks

- [ ] 1.0 Create User Profile Editing Interface
  - [ ] 1.1 Create form component for profile information
  - [ ] 1.2 Add form validation logic
- [ ] 2.0 Profile Update API Integration
  - [ ] 2.1 Write function to send API request
```