---
id: "debugging-best-practices"
title: "Debugging Best Practices"
description: "General best practices for enhancing debugging efficiency and effectiveness, including systematic approach and collaboration."
tags: ["debugging", "best-practices", "collaboration"]
severity: "high"
applies_to: ["all"]
automation_potential: ["tool-integration", "manual-review"]
suggested_tools: ["IDE debuggers", "logging frameworks", "APM tools"]
related_rules: ["initial-steps", "debugging-process", "reporting"]
---

- Adopt a systematic approach.
- Validate assumptions, rely on facts.
- Create simple and isolated test scenarios.
- Effectively use debugging tools (breakpoints, step-by-step execution).
- Collaborate, ask for help when needed.

**Rationale:** These best practices enhance debugging efficiency and effectiveness. A systematic approach prevents aimless searching, while collaboration leverages collective knowledge.

**Automation Potential:** IDE debuggers provide powerful tools for breakpoints and step-by-step execution.

### Example (Debugging Report):
```markdown
### Issue Description
Users are receiving "500 Internal Server Error" when updating their profile pictures.

### Root Cause
During the file upload process, the system lacks write permissions for the temporary file directory.

### Evidence
1. The following error message is seen in server logs: "PermissionError: [Errno 13] Permission denied: '/tmp/uploads/'"
2. The error only occurs during profile picture update operations.
3. Upon checking directory permissions, it was found that '/tmp/uploads/' directory lacks write permissions.

### Fix
```python
import os

# To be run during application startup
upload_dir = '/tmp/uploads/'
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir, mode=0o755)
else:
    os.chmod(upload_dir, 0o755)
```

### Testing Approach
1. Perform manual tests by uploading profile pictures of different sizes.
2. Add file upload scenarios to automated tests.
3. Verify that permissions are retained after server restart.

### Prevention Recommendations
1. Add a script that checks if all necessary directories exist and have correct permissions during application startup.
2. Create an error handling layer for file operations and show more descriptive error messages to users.
3. Add comprehensive logging for file upload operations.
```
