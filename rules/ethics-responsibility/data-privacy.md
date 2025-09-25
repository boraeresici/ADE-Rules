---
id: "data-privacy"
title: "Data Privacy"
description: "Best practices for protecting user data privacy, including minimization, encryption, anonymization, and access control."
tags: ["ethics", "data-privacy", "gdpr", "security"]
severity: "critical"
applies_to: ["all"]
automation_potential: ["tool-integration", "code-review"]
suggested_tools: ["GDPR compliance tools", "CCPA compliance tools", "encryption libraries"]
related_rules: ["ethical-software-development", "algorithmic-bias", "secure-config-secrets"]
---

1.  **Minimization**: Collect and process only the necessary data.
2.  **Encryption**: Encrypt sensitive data both during communication and storage.
3.  **Anonymization**: Anonymize data whenever possible.
4.  **Access Control**: Strictly control and log access to data.
5.  **Data Retention Policy**: Create a clear data retention and deletion policy.

**Rationale:** Protecting user data privacy is a fundamental ethical and legal obligation. These practices minimize risk and ensure compliance with regulations (e.g., GDPR, CCPA).

**Automation Potential:** Data anonymization tools, encryption libraries, and access control systems.

### Example (Data Anonymization):
```python
import hashlib

def anonymize_data(user_data):
    anonymized = user_data.copy()
    anonymized['id'] = hashlib.sha256(user_data['id'].encode()).hexdigest()
    anonymized['name'] = 'REDACTED'
    anonymized['email'] = f"{hashlib.md5(user_data['email'].encode()).hexdigest()}@example.com"
    return anonymized

# Usage
user = {
    'id': '12345',
    'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30
}

anonymized_user = anonymize_data(user)
print(anonymized_user)
```
