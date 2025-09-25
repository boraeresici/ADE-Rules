---
id: "event-driven-architecture-principles"
title: "Event-Driven Architecture Principles"
description: "Guidelines for designing and implementing robust and scalable event-driven architectures."
tags: ["serverless", "architecture", "event-driven"]
severity: "high"
applies_to: ["backend", "architecture"]
automation_potential: ["code-review"]
suggested_tools: ["Kafka", "RabbitMQ", "AWS EventBridge"]
related_rules: ["serverless-framework-usage"]
---

### Core Principles:
- Design loosely coupled services.
- Use asynchronous communication.
- Ensure event immutability and ordering.

### Production Checklist:
- [ ] Services are loosely coupled.
- [ ] Asynchronous communication is used.
- [ ] Event contracts are well-defined.
