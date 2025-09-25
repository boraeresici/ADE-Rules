---
id: "aws-lambda-function-optimization"
title: "AWS Lambda Function Optimization"
description: "Best practices for optimizing AWS Lambda functions for performance and cost efficiency."
tags: ["serverless", "aws", "lambda", "optimization"]
severity: "high"
applies_to: ["devops", "backend"]
automation_potential: ["monitoring", "code-review"]
suggested_tools: ["AWS Lambda Power Tuning", "CloudWatch"]
related_rules: ["serverless-framework-usage", "event-driven-architecture-principles"]
---

### Core Principles:
- Optimize memory and CPU allocation.
- Minimize cold starts.
- Use appropriate triggers and event sources.

### Production Checklist:
- [ ] Lambda functions are configured for optimal performance.
- [ ] Cold starts are minimized.
- [ ] Event sources are correctly configured.
