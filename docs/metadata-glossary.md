# Metadata Glossary for ADE Rules

This document defines the meaning and allowed values for the optional metadata fields used in the YAML frontmatter of ADE Rule files. Adhering to these definitions ensures consistency and improves the machine-readability and utility of the rules for AI Development Environments (ADEs) and other automated tools.

## 1. `severity`

**Description:** Indicates the criticality or impact level of violating this rule. This helps prioritize rule enforcement and remediation efforts.

**Allowed Values:**
- `critical`: Violation of this rule leads to severe security vulnerabilities, major data loss, or critical system failures. Must be addressed immediately.
- `high`: Violation leads to significant security risks, performance degradation, or major maintainability issues. Should be addressed promptly.
- `medium`: Violation leads to minor security concerns, moderate performance impact, or maintainability challenges. Should be addressed in due course.
- `low`: Violation has minimal impact on security, performance, or maintainability. May be addressed as part of general code improvements.
- `suggestion`: A recommendation or best practice that improves code quality or efficiency but is not strictly enforced.

## 2. `applies_to`

**Description:** Specifies the technologies, domains, or layers of an application to which this rule is primarily applicable. This helps ADEs filter and apply rules contextually.

**Allowed Values (Examples - not exhaustive, can be extended as needed):**
- `all`: Applies to any part of the codebase.
- `backend`: Applies to server-side logic, APIs, and services.
- `frontend`: Applies to client-side user interfaces and logic.
- `devops`: Applies to infrastructure, deployment, and operational practices.
- `security`: Applies to security-related aspects across layers.
- `database`: Applies to database design, queries, and management.
- `microservices`: Applies specifically to microservice architectures.
- `ai`, `llm`, `ml`: Applies to Artificial Intelligence, Large Language Models, or Machine Learning systems.
- `language`: Specific programming languages (e.g., `python`, `javascript`, `rust`, `go`, `erlang`, `lua`, `zig`).
- `framework`: Specific frameworks (e.g., `django`, `react`, `fastapi`, `nextjs`, `supabase`, `zuplo`, `trpc`, `lancedb`, `firebase`).
- `system-programming`, `embedded-systems`, `game-development`, `scripting`, `network-services`, `distributed-systems`, `mobile`, `architecture`, `testing`, `qa`.

## 3. `automation_potential`

**Description:** Describes how the enforcement or checking of this rule can be automated. This guides ADEs and CI/CD pipelines in integrating automated checks.

**Allowed Values (Examples - not exhaustive, can be extended as needed):**
- `linter`: Can be checked by a linter (e.g., ESLint, Pylint, Clippy).
- `static-analysis`: Can be checked by static analysis tools (e.g., SonarQube, SAST tools).
- `type-checker`: Can be checked by a type checker (e.g., TypeScript compiler).
- `runtime-check`: Can be checked at runtime.
- `ci-cd-check`: Can be integrated as a check in CI/CD pipelines.
- `code-review`: Primarily requires manual code review.
- `tool-integration`: Requires integration with specific tools (e.g., APM, SIEM).
- `test-automation`: Can be verified through automated tests (unit, integration, E2E).
- `iac`: Can be enforced through Infrastructure as Code tools.
- `code-generation`: Can be enforced through code generation.
- `manual-review`: Primarily requires manual review.

## 4. `suggested_tools`

**Description:** Lists specific tools that can help enforce, check, or implement this rule.

**Format:** An array of strings, where each string is the name of a tool (e.g., `["ESLint", "SonarQube", "Prometheus"]`).

## 5. `related_rules`

**Description:** Lists the `id`s of other rules in the repository that are closely related or provide additional context.

**Format:** An array of strings, where each string is the `id` of a related rule (e.g., `["readability-clarity", "simplicity-kiss"]`).
