---
id: "containerize-applications"
title: "Containerize Applications"
description: "All applications should be containerized using Docker, with images optimized for size and security."
tags: ["devops", "containers", "docker", "microservices"]
severity: "high"
applies_to: ["devops", "backend", "frontend"]
automation_potential: ["ci-cd-check", "static-analysis"]
suggested_tools: ["Docker", "Hadolint", "Trivy"]
related_rules: ["infrastructure-as-code", "automate-deployments-ci-cd"]
---

**Description:** All applications should be containerized using Docker. Container images should be optimized for size and security.

**Rationale:** Containerization provides a consistent and portable environment for applications, eliminating "it works on my machine" problems. Optimized images are faster to deploy and have a smaller attack surface.

**Good Practice:**
- Use multi-stage builds to create small production images.
- Run containers as a non-root user.
- Use minimal base images (e.g., `alpine`, `distroless`).
