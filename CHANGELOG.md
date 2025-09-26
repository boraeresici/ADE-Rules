# CHANGELOG

## vFull — Complete Parity from generic-rules.md
- Copied every section from `generic-rules.md` into its matching file under `rules/`.
- Appended expansions for CI/CD, Bisect Automation, AI Workflow, PR Template, IDE Setup.

## v1.1.0 — AI Rule Refactoring & New Technology Rules
- Refactored all rules in `ai-safety-operations` for single responsibility and improved cross-referencing.
- Added new rule categories and rules for Rust, Zig, Go (expanded), Lua, Zuplo, Supabase, tRPC, LanceDB, Erlang, Cognee AI, Kubernetes, Serverless, Firebase, and E2E Testing.
- Added `awesome-rules-main/` and `old-docs/` to `.gitignore`.
- Added GitHub repository link to `rules/readme.md`.
- Updated project version to 1.1.0 in `CONTRIBUTING.md`.

## v1.2.0 — Documentation Enhancements & Validation Planning
- Implemented feedback: Created `docs/metadata-glossary.md` and updated `rule-template.md` to refer to it.
- Enhanced `rules/readme.md` with a dynamic, category-based rule index.
- Updated `CONTRIBUTING.md` with guidance for rule quality, metadata, and CI validation script planning.
- Created placeholder `scripts/validate-rules.py` for future CI integration.
- Updated project version to 1.2.0 in `CONTRIBUTING.md`.

## v1.3.0 — Implementing Prioritized Enhancements & Playbook Scaffolding
- Updated `CONTRIBUTING.md` with detailed guidance for contributors on:
  - Applying the granular `severity` scale.
  - Populating "Further Reading" sections with vetted resources.
  - Expanding "Automation Potential" sections with concrete snippets.
  - Introducing Domain Playbooks.
- Created `rules/playbooks/` directory with an example playbook and `rules.json` scaffolding.
- Updated project version to 1.3.0 in `CONTRIBUTING.md`.
