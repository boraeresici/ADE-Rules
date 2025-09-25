---
id: "rollback-plan"
title: "AI Rollback Plan"
description: "Define and test a one-command or toggle rollback mechanism to a previous safe state for AI systems, avoiding ad-hoc fixes during live incidents, building on general deployment and incident management principles."
tags: ["ai-operations", "deployment", "reliability", "ci-cd"]
severity: "critical"
applies_to: ["ai", "llm", "ml"]
automation_potential: ["ci-cd-integration", "deployment-automation"]
suggested_tools: ["CI/CD platforms", "version control systems"]
related_rules: ["incident-path", "automate-deployments-ci-cd"]
---

**Note:** This rule is a critical component of `incident-path.md` and relies on the automated deployment capabilities defined in `automate-deployments-ci-cd.md`.

### Core Principles for AI Rollback Plan:
- **One-Command/Toggle Rollback:** Implement a simple, automated mechanism (e.g., a single command or feature toggle) to revert AI systems to a previous, known-good state.
- **Avoid Ad-Hoc Fixes:** Strictly avoid manual, ad-hoc fixes during live incidents, relying instead on tested rollback procedures.
- **Versioned Safe States:** Ensure that previous safe states, including model versions, configurations, and code, are versioned and easily accessible.
- **Regular Testing:** Periodically test the rollback mechanism to ensure its reliability and effectiveness.

### Production Checklist:
- [ ] Rollback automation is fully tested and integrated into deployment pipelines.  
- [ ] All necessary artifacts (model versions, configurations) for a safe rollback are stored and versioned.  
- [ ] On-call staff are thoroughly trained in rollback procedures and protocols.  
- [ ] The rollback mechanism is regularly exercised and validated.  
