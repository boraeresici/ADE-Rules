---
id: "secure-logging-monitoring"
title: "Implement Secure Logging and Monitoring"
description: "Log all security-relevant events, centralize logs, and monitor for suspicious activity to enable incident response."
tags: ["security", "logging", "monitoring", "observability"]
severity: "critical"
applies_to: ["all"]
automation_potential: ["tool-integration", "ci-cd-check"]
suggested_tools: ["SIEM systems", "ELK Stack", "Splunk"]
related_rules: ["automate-vulnerability-management", "observability-best-practices"]
---

# Rule: Implement Secure Logging and Monitoring

**Description:** This rule mandates the logging of all security-relevant events, such as successful and failed login attempts, access control failures, and significant server-side errors. These logs must be centralized and continuously monitored for suspicious activity to enable timely incident detection and response.

**Rationale:** Without proper logging and monitoring, detecting, investigating, and responding to a security incident is nearly impossible. Comprehensive and secure logs are essential for forensic analysis, threat detection, compliance auditing, and understanding the scope and impact of a breach. They form the backbone of an effective security operations center (SOC).

### Good Practice:
```python
# Example: Logging a failed login attempt with relevant context
import logging

logger = logging.getLogger(__name__)

def handle_failed_login(username, ip_address):
    logger.warning(
        "SECURITY_EVENT: Failed login attempt",
        extra={
            "event_type": "login_failure",
            "username": username,
            "ip_address": ip_address,
            "severity": "medium"
        }
    )
    # ... further actions like rate limiting ...
```
*Example: Structured logging of a security event, including event type, username, and IP address, for easy analysis.*

### Bad Practice:
```python
# Example: Logging sensitive user data or insufficient detail
import logging

logger = logging.getLogger(__name__)

def process_user_request(user_id, password, credit_card_number):
    # BAD: Logging sensitive data directly
    logger.info(f"User {user_id} requested with password {password} and CC {credit_card_number}")
    # BAD: Logging only generic messages without context
    logger.error("An error occurred during processing")
```
*Example: Logging sensitive user data in plain text or logging generic errors without sufficient context for security analysis.*

---

**Automation Potential:** SIEM (Security Information and Event Management) systems automate log aggregation, correlation, and analysis for threat detection. Alerting tools can trigger notifications for anomalous security events. CI/CD checks can ensure logging configurations are secure and comprehensive. Code reviews are essential for preventing sensitive data from being logged.

**Further Reading:** [Optional: Links to external resources, articles, or documentation related to this rule.]
