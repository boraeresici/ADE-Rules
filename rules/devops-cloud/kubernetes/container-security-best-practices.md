---
id: "container-security-best-practices"
title: "Container Security Best Practices"
description: "Guidelines for securing container images and runtime environments."
tags: ["kubernetes", "container", "security"]
severity: "critical"
applies_to: ["devops", "backend"]
automation_potential: ["sast", "dast", "ci-cd-check"]
suggested_tools: ["Trivy", "Clair", "Falco"]
related_rules: ["kubernetes-cluster-management-scaling"]
---

### Core Principles:
- Use minimal base images.
- Scan images for vulnerabilities.
- Implement runtime security policies.

### Production Checklist:
- [ ] Images are built with minimal dependencies.
- [ ] Vulnerability scanning is integrated into CI/CD.
- [ ] Runtime security policies are enforced.
