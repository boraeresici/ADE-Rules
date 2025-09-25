---
id: "never-trust-user-input"
title: "Never Trust User Input"
description: "Treat all input from users or external systems as untrusted and validate/sanitize to prevent injection attacks."
tags: ["security", "input-validation", "xss", "sqli"]
severity: "critical"
applies_to: ["all"]
automation_potential: ["linter", "sast", "dast", "code-review"]
suggested_tools: ["OWASP ESAPI", "DOMPurify", "SAST tools"]
related_rules: ["least-privilege", "automate-vulnerability-management"]
---

# Rule: Never Trust User Input

**Description:** This rule mandates that all input originating from users or external systems must be treated as untrusted. Comprehensive validation and sanitization are required at all entry points to prevent various injection attacks, such as SQL Injection (SQLi) and Cross-Site Scripting (XSS).

**Rationale:** Untrusted input is a primary and highly effective vector for a wide range of security attacks. Implementing strict validation and sanitization at the earliest possible point in the application's processing flow serves as the first and most critical line of defense against malicious data, protecting data integrity, system functionality, and user privacy.

### Good Practice:
```python
# Example: Using parameterized queries for SQL injection prevention
import sqlite3

def get_user_data(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Parameterized query prevents SQL injection
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

# Example: Sanitizing user input before rendering in HTML to prevent XSS
from html import escape

def render_comment(comment_text):
    # Escape HTML special characters
    safe_comment = escape(comment_text)
    return f"<div>{safe_comment}</div>"
```

### Bad Practice:
```python
# Example: Direct string concatenation in SQL query (SQL Injection vulnerability)
import sqlite3

def get_user_data_vulnerable(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Direct string concatenation - highly vulnerable to SQL injection
    cursor.execute(f"SELECT * FROM users WHERE id = '{user_id}'")
    user = cursor.fetchone()
    conn.close()
    return user

# Example: Rendering user input directly in HTML (XSS vulnerability)
def render_comment_vulnerable(comment_text):
    # No sanitization, allows malicious scripts to be injected
    return f"<div>{comment_text}</div>"
```

---

**Automation Potential:** Static Application Security Testing (SAST) tools can detect common input validation vulnerabilities. Dynamic Application Security Testing (DAST) tools can test for injection attacks. Linters can enforce some input handling patterns. Code reviews are crucial for ensuring comprehensive input validation strategies.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
