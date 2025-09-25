# ADE Rules - Structured for AI/ADE Consumption

This repository contains Application Development Environment (ADE) Rules, designed to establish standards for quality, security, performance, and teamwork in software development processes. These rules aim to create a more sustainable and efficient working environment.

## Purpose and Structure

This repository is hosted on GitHub: [https://github.com/boraeresici/ADE-Rules](https://github.com/boraeresici/ADE-Rules)

The rules are organized into a modular, granular structure to facilitate consumption by both human developers and automated systems like AI Development Environments (ADEs) or Command-Line Interfaces (CLIs).

Each rule category resides in its own directory (e.g., `code-quality/`, `security/`). Within each category directory, you will find:

1.  **Individual Rule Files (`.md`):** Each specific rule is defined in its own Markdown file. This adheres to the Single Responsibility Principle, making each rule atomic, easy to understand, and independently applicable.
    *   Each rule file includes YAML frontmatter for metadata (ID, title, description, tags) and structured Markdown content detailing the rule, its rationale, good/bad practices, and examples.

2.  **Manifest File (`rules.json`):** A JSON file that acts as a manifest for all rules within that category. It lists each rule with its metadata and a pointer to its corresponding Markdown documentation file.

## 📚 Rule Categories and Index

Below is an index of all rule categories and the rules contained within them. Click on any rule to view its detailed documentation.

### AI Safety Operations
- [AI Auditability and Compliance](ai-safety-operations/auditability-compliance.md)
- [Cognee AI Memory Management](ai-safety-operations/cognee/cognee-ai-memory.md)
- [Cognee Best Practices](ai-safety-operations/cognee/cognee-best-practices.md)
- [Cognee Rule Generation](ai-safety-operations/cognee/cognee-generate-rules.md)
- [AI Cost per Task Monitoring](ai-safety-operations/cost-per-task.md)
- [AI Feedback Capture](ai-safety-operations/feedback-capture.md)
- [AI Guardrails](ai-safety-operations/guardrails.md)
- [Human-in-the-Loop for AI Decisions](ai-safety-operations/human-in-the-loop.md)
- [AI Incident Management](ai-safety-operations/incident-path.md)
- [AI Model Lifecycle Management](ai-safety-operations/model-lifecycle-management.md)
- [AI Monitoring and Observability](ai-safety-operations/monitoring-observability-ai.md)
- [AI Rollback Plan](ai-safety-operations/rollback-plan.md)
- [AI Shadow Evaluations](ai-safety-operations/shadow-evals.md)

### API Design
- [API Selection and Design Process](api-design/api-selection-process.md)
- [GraphQL API Design](api-design/graphql.md)
- [gRPC Design](api-design/grpc.md)
- [RESTful API Design](api-design/restful-api.md)
- [tRPC API Best Practices](api-design/trpc/trpc-api-best-practices.md)
- [Zuplo API Gateway Setup](api-design/zuplo/zuplo-api-gateway-setup.md)
- [Zuplo Deployment with GitOps](api-design/zuplo/zuplo-deployment-gitops.md)
- [Zuplo Performance Optimization](api-design/zuplo/zuplo-performance-optimization.md)
- [Zuplo Security Policies](api-design/zuplo/zuplo-security-policies.md)

### Backend
- [Backend Fundamentals](backend/backend-fundamentals.md)
- [Database Design](backend/database-design.md)
- [Firebase Best Practices](backend/firebase/firebase-best-practices.md)
- [LanceDB Best Practices](backend/lancedb/lancedb-best-practices.md)
- [Backend Performance Optimization](backend/performance-optimization.md)
- [RESTful API Design](backend/restful-api-design.md)
- [Backend Security](backend/security.md)
- [Backend Service Architecture](backend/service-architecture.md)
- [Supabase and Next.js Auth](backend/supabase/supabase-next-auth.md)

### Code Quality
- [Commenting and Documentation](code-quality/commenting-documentation.md)
- [Consistency](code-quality/consistency.md)
- [Readability and Clarity](code-quality/readability-clarity.md)
- [Refactoring](code-quality/refactoring.md)
- [Simplicity and Conciseness (KISS)](code-quality/simplicity-kiss.md)

### Code Review
- [Code Review Approach](code-review/review-approach.md)
- [Code Review Best Practices](code-review/code-review-best-practices.md)
- [Code Review Checklist](code-review/review-checklist.md)
- [Code Review Feedback Organization](code-review/feedback-organization.md)

### Debugging
- [Debugging Best Practices](debugging/debugging-best-practices.md)
- [Debugging Initial Steps](debugging/initial-steps.md)
- [Debugging Process](debugging/debugging-process.md)
- [Debugging Reporting](debugging/reporting.md)

### DevOps Cloud
- [Automate Deployments with CI/CD](devops-cloud/automate-deployments-ci-cd.md)
- [Containerize Applications](devops-cloud/containerize-applications.md)
- [Implement Comprehensive Monitoring and Logging](devops-cloud/comprehensive-monitoring-logging.md)
- [Infrastructure as Code (IaC)](devops-cloud/infrastructure-as-code.md)
- [Container Security Best Practices](devops-cloud/kubernetes/container-security-best-practices.md)
- [Helm Chart Development and Usage](devops-cloud/kubernetes/helm-chart-development-usage.md)
- [Istio Service Mesh Management](devops-cloud/kubernetes/istio-service-mesh-management.md)
- [Kubernetes Cluster Management and Scaling](devops-cloud/kubernetes/kubernetes-cluster-management-scaling.md)
- [Use Managed and Serverless Services](devops-cloud/managed-serverless-services.md)
- [AWS Lambda Function Optimization](devops-cloud/serverless/aws-lambda-function-optimization.md)
- [Azure Functions Best Practices](devops-cloud/serverless/azure-functions-best-practices.md)
- [Event-Driven Architecture Principles](devops-cloud/serverless/event-driven-architecture-principles.md)
- [Serverless Framework Usage Rules](devops-cloud/serverless/serverless-framework-usage.md)

### Docs UI
- [Clear and Concise UI Text](docs-ui/clear-concise-ui-text.md)
- [Comprehensive Documentation](docs-ui/comprehensive-documentation.md)
- [Consistency in Terminology and Style](docs-ui/consistency-terminology-style.md)
- [User-Centric and Guiding Language](docs-ui/user-centric-guiding-language.md)

### Error Testing
- [Comprehensive and Multi-Layered Testing](error-testing/comprehensive-multi-layered-testing.md)
- [End-to-End Testing Best Practices](error-testing/e2e-testing/e2e-testing-best-practices.md)
- [Principled Error Handling](error-testing/principled-error-handling.md)
- [Resilient Recovery Strategies](error-testing/resilient-recovery-strategies.md)
- [Semantic and Custom Error Types](error-testing/semantic-custom-error-types.md)

### Ethics Responsibility
- [Algorithmic Bias](ethics-responsibility/algorithmic-bias.md)
- [Data Privacy](ethics-responsibility/data-privacy.md)
- [Ethical Software Development](ethics-responsibility/ethical-software-development.md)
- [General Ethics and Responsibility Principles](ethics-responsibility/general-principles.md)
- [Sustainable Software Development](ethics-responsibility/sustainable-software-development.md)

### Frontend Frameworks
- [Angular Best Practices](frontend-frameworks/angular.md)
- [Astro Best Practices](frontend-frameworks/astro.md)
- [Gatsby Best Practices](frontend-frameworks/gatsby.md)
- [General Frontend Best Practices](frontend-frameworks/general-frontend-best-practices.md)
- [Next.js Best Practices](frontend-frameworks/nextjs.md)
- [Nuxt.js Best Practices](frontend-frameworks/nuxtjs.md)
- [Qwik Best Practices](frontend-frameworks/qwik.md)
- [React Best Practices](frontend-frameworks/react.md)
- [SolidJS Best Practices](frontend-frameworks/solidjs.md)
- [Svelte Best Practices](frontend-frameworks/svelte.md)
- [Vue.js Best Practices](frontend-frameworks/vuejs.md)
- [Web Components Best Practices](frontend-frameworks/web-components.md)

### IDE Setup
- [JetBrains IDE Setup](ide-setup/jetbrains-setup.md)
- [VS Code Extensions](ide-setup/vscode-extensions.md)
- [VS Code settings.json Configuration](ide-setup/vscode-settings.md)

### Language Framework Best Practices
- [Erlang Concurrent Programming](language-framework-best-practices/erlang/erlang-concurrent-programming.md)
- [Erlang Fault Tolerance](language-framework-best-practices/erlang/erlang-fault-tolerance.md)
- [Erlang OTP Patterns](language-framework-best-practices/erlang/erlang-otp-patterns.md)
- [FastAPI Best Practices](language-framework-best-practices/fastapi.md)
- [General Language and Framework Principles](language-framework-best-practices/general-principles.md)
- [Go Best Practices](language-framework-best-practices/go/go-best-practices.md)
- [Go Effective Programming](language-framework-best-practices/go/go-effective-programming.md)
- [Go Microservices Best Practices](language-framework-best-practices/go/go-microservices.md)
- [JavaScript/TypeScript Best Practices](language-framework-best-practices/javascript-typescript.md)
- [Lua Best Practices](language-framework-best-practices/lua/lua-best-practices.md)
- [Lua Performance Optimization](language-framework-best-practices/lua/lua-performance-optimization.md)
- [Lua Scripting Guidelines](language-framework-best-practices/lua/lua-scripting-guidelines.md)
- [Python and Django Best Practices](language-framework-best-practices/python-django.md)
- [React Specific Best Practices](language-framework-best-practices/react-specific.md)
- [Rust Async Programming](language-framework-best-practices/rust/rust-async-programming.md)
- [Rust Best Practices](language-framework-best-practices/rust/rust-best-practices.md)
- [Rust Ownership and Borrowing](language-framework-best-practices/rust/rust-ownership-borrowing.md)
- [Zig Best Practices](language-framework-best-practices/zig/zig-best-practices.md)
- [Zig Comptime Programming](language-framework-best-practices/zig/zig-comptime-programming.md)
- [Zig Memory Management](language-framework-best-practices/zig/zig-memory-management.md)

### Microservices
- [Data Consistency Strategies](microservices/data-consistency-strategies.md)
- [Defining Microservice Boundaries](microservices/defining-service-boundaries.md)
- [Distributed Tracing in Microservices](microservices/distributed-tracing.md)
- [Inter-Service Communication](microservices/inter-service-communication.md)
- [Microservices Best Practices](microservices/microservices-best-practices.md)
- [Microservice Scalability and Resilience](microservices/scalability-resilience.md)

### Observability
- [Alerting Strategy](observability/alerting-strategy.md)
- [Code Quality and Analysis](observability/code-quality-analysis.md)
- [Development Process Improvements](observability/development-process-improvements.md)
- [Distributed Tracing](observability/distributed-tracing.md)
- [Logging Best Practices](observability/logging-best-practices.md)
- [Metrics Implementation](observability/metrics-implementation.md)
- [Observability Best Practices](observability/observability-best-practices.md)
- [Performance Monitoring](observability/performance-monitoring.md)

### Performance
- [Algorithmic Optimization](performance/algorithmic-optimization.md)
- [Asynchronous Performance](performance/asynchronous-performance.md)
- [Caching Strategies](performance/caching-strategies.md)
- [Content Delivery Optimization](performance/content-delivery.md)
- [Database Optimization](performance/database-optimization.md)
- [Memory Optimization](performance/memory-optimization.md)
- [Performance Best Practices](performance/performance-best-practices.md)
- [Performance Principles](performance/performance-principles.md)
- [System Scalability](performance/system-scalability.md)

### Project Management
- [Agile Methodology](project-management/methodology.md)
- [Code Review Checklist](project-management/review-checklist.md)
- [Communication and Documentation](project-management/communication-and-documentation.md)
- [Project Structure and Code Quality](project-management/project-structure.md)
- [Quality Assurance](project-management/quality-assurance.md)
- [Task Management](project-management/task-management.md)
- [Version Control Best Practices](project-management/version-control.md)

### Reusability
- [Code Maintainability](reusability/maintainability.md)
- [Code Reusability](reusability/reusability.md)
- [Dependency Inversion Principle (DIP)](reusability/dip.md)
- [Interface Segregation Principle (ISP)](reusability/isp.md)
- [Liskov Substitution Principle (LSP)](reusability/lsp.md)
- [Open/Closed Principle (OCP)](reusability/ocp.md)
- [Single Responsibility Principle (SRP)](reusability/srp.md)

### Security
- [Automate Vulnerability Management](security/automate-vulnerability-management.md)
- [Enforce the Principle of Least Privilege](security/least-privilege.md)
- [Implement Secure Logging and Monitoring](security/secure-logging-monitoring.md)
- [Never Trust User Input](security/never-trust-user-input.md)
- [Secure Configuration and Secrets Management](security/secure-config-secrets.md)
- [Use Strong Authentication and Cryptography](security/strong-auth-crypto.md)

### UI UX
- [React Component Architecture](ui-ux/component-architecture-react.md)
- [UI Component Patterns](ui-ux/component-patterns.md)
- [UI/UX Design Principles](ui-ux/design-principles.md)
- [Frontend Performance Optimization](ui-ux/performance-optimization.md)
- [State Management in UI/UX](ui-ux/state-management.md)
- [UI/UX Best Practices](ui-ux/ui-ux-best-practices.md)
- [UI/UX Fundamentals](ui-ux/ui-ux-fundamentals.md)
- [User Experience Improvement](ui-ux/user-experience-improvement.md)

## Usage for ADEs/CLIs

This structured format is ideal for automated systems:

*   **Rule Discovery:** An ADE can easily discover all available rules by iterating through the category directories and reading their respective `rules.json` files. This allows for programmatic access to rule metadata (ID, name, description, tags).
*   **Detailed Rule Retrieval:** Once a rule is identified (e.g., by its ID or tags), the ADE can retrieve its full documentation by reading the `.md` file specified in the `documentation` field of the `rules.json` entry.
*   **Targeted Application:** The granular nature of the rules allows ADEs to apply very specific guidelines to particular code contexts, leading to more precise and effective suggestions.

## Goals

-   **Increase Code Quality:** Encourage writing readable, maintainable, and less error-prone code.
-   **Reduce Security Risks:** Detect and prevent security vulnerabilities at an early stage.
-   **Optimize Performance:** Ensure applications run faster and more efficiently.
-   **Improve Development Processes:** Standardize processes such as version control, testing, and documentation.
-   **Ensure Team Cohesion:** Increase team efficiency by enabling different developers to work with the same standards.

## Areas of Use

-   **Code Review:** Can be used as a checklist for code review processes.
-   **IDE Integration:** Can be integrated into the development environment to provide instant feedback to developers.
-   **CI/CD Pipelines:** These rules can be used as a basis for automated testing and auditing steps.
-   **Orientation for New Team Members:** Can serve as a resource for quickly learning project standards and expectations.

## Customization

These rules can be customized and extended according to the needs of the project and the team. They have a flexible structure and aim to provide a framework rather than a "one-size-fits-all" solution.

## Contribution & Contact

For questions, suggestions, or contributions, please contact [Your Contact Information or Link to Contribution Guide].
