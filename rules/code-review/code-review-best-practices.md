---
id: "code-review-best-practices"
title: "Code Review Best Practices"
description: "Guidelines for constructive and respectful feedback, focusing on specific examples and fostering a positive team environment."
tags: ["code-review", "best-practices", "communication"]
severity: "high"
applies_to: ["project-management", "all"]
automation_potential: ["tool-integration", "manual-review"]
suggested_tools: ["GitHub PRs", "GitLab MRs"]
related_rules: ["review-approach", "review-checklist", "feedback-organization"]
---

- Always be constructive and respectful.
- Provide specific examples on how to fix issues.
- Highlight positive aspects as well.
- Consider the big picture.
- Refer to code style guides.
- Suggest face-to-face discussion when necessary.

**Rationale:** Constructive and respectful feedback fosters a positive team environment and encourages learning. Specific examples make feedback actionable. Highlighting positive aspects motivates the author.

**Automation Potential:** Code review platforms (e.g., GitHub, GitLab) facilitate discussion and tracking of feedback.

### Example (Code Review Feedback):
```markdown
### Critical Issues
1. User input in `processUserData` function is not validated. Please add input validation to prevent XSS and injection attacks.
   Example: `sanitizeInput(userData.name)` like a function can be used.

### Warnings
1. `fetchData` function lacks error handling. Add a try-catch block to handle error states.
2. `UserComponent` is over 200 lines, consider splitting it into smaller components.

### Suggestions
1. Adding JSDoc comments to `calculateTotal` function could make its usage clearer.
2. You might consider using the `useMemo` hook for performance.

### Positive Points
- Clean and consistent code style, easy to read.
- Descriptive function and variable names.
- Well-thought-out test coverage.
```
