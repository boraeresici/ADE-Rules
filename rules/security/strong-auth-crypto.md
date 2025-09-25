---
id: "strong-auth-crypto"
title: "Use Strong Authentication and Cryptography"
description: "Implement strong authentication mechanisms and encrypt all sensitive data using strong, modern algorithms."
tags: ["security", "authentication", "cryptography", "mfa"]
severity: "critical"
applies_to: ["all"]
automation_potential: ["sast", "code-review"]
suggested_tools: ["OWASP ZAP", "SAST tools", "cryptography libraries"]
related_rules: ["secure-config-secrets", "automate-vulnerability-management"]
---

# Rule: Use Strong Authentication and Cryptography

**Description:** This rule mandates the implementation of strong authentication mechanisms, including multi-factor authentication (MFA) where appropriate. Furthermore, all sensitive data, whether in transit or at rest, must be encrypted using robust, modern, and industry-standard cryptographic algorithms.

**Rationale:** Weak authentication mechanisms can be easily bypassed by attackers, leading to unauthorized access and account compromise. Similarly, unencrypted sensitive data is vulnerable to theft and exposure. Employing strong cryptography and MFA are fundamental security controls essential for protecting user accounts, sensitive information, and maintaining the overall integrity and confidentiality of the system.

### Good Practice:
```python
# Example: Hashing passwords with a strong, modern algorithm (e.g., bcrypt)
import bcrypt

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Example: Ensuring HTTPS for all communication
# (This is typically configured at the web server/load balancer level)
# In Flask, ensure app.config['PREFERRED_URL_SCHEME'] = 'https'
# In Node.js/Express, use a middleware to redirect HTTP to HTTPS
```

### Bad Practice:
```python
# Example: Storing passwords in plain text or using weak hashing algorithms (e.g., MD5, SHA1)
def store_password_vulnerable(password):
    # NEVER store passwords in plain text!
    # NEVER use weak, outdated hashing algorithms!
    # db.save_password(password) # BAD
    pass

# Example: Transmitting sensitive data over unencrypted HTTP
# (This is typically prevented by server configuration, but code should not allow it)
# fetch('http://api.example.com/sensitive-data') # BAD
```

---

**Automation Potential:** SAST (Static Application Security Testing) tools can detect the use of weak cryptographic algorithms or insecure authentication patterns. Code reviews are essential for validating the correct implementation of authentication flows and cryptographic practices. Security scanners can check for proper SSL/TLS configurations.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
