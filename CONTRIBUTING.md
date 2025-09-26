# Contributing to ADE Rules

We welcome contributions to the ADE Rules project! By contributing, you help us maintain a high standard of quality, consistency, and best practices across our application development environments.

## Version: 1.3.0

## How to Contribute

We follow a standard GitHub flow for contributions:

1.  **Fork the Repository:** Start by forking this repository to your GitHub account.
2.  **Clone Your Fork:** Clone your forked repository to your local machine.
3.  **Create a New Branch:** Create a new branch for your changes. Use a descriptive name (e.g., `feat/add-new-python-rule`, `fix/typo-in-readability-rule`, `docs/update-security-guidelines`).

### Making Your Changes

Our rules are organized into a modular, directory-based structure. Each rule is a separate Markdown file (`.md`) within its category directory, accompanied by a `rules.json` manifest.

#### Adding a New Rule

1.  **Identify/Create Category:** Navigate to the appropriate category directory under `rules/` (e.g., `rules/code-quality/`). If a suitable category doesn't exist, create a new directory for it (e.g., `rules/new-category-name/`).
2.  **Create Rule File:** Create a new Markdown file for your rule within the chosen category directory (e.g., `rules/code-quality/my-new-rule.md`).
3.  **Add Rule Content:**
    *   Include **YAML Frontmatter** at the top of the file with `id`, `title`, `description`, and `tags`.
    *   Structure the rule content using Markdown headings, descriptions, rationales, good/bad practices, and code examples as established in existing rules.
4.  **Update `rules.json`:** Open the `rules.json` file in the same category directory and add an entry for your new rule. Ensure `id`, `name` (same as title), `description`, `documentation` (your new `.md` filename), and `tags` are correctly specified.

#### Updating an Existing Rule

1.  **Locate Rule File:** Find the specific `.md` file for the rule you wish to update (e.g., `rules/code-quality/readability-clarity.md`).
2.  **Make Modifications:** Edit the content of the Markdown file directly.
3.  **Update `rules.json` (if metadata changes):** If you change the `title`, `description`, or `tags` in the YAML frontmatter of the `.md` file, remember to update the corresponding entry in the `rules.json` file for that category.

#### Adding a New Category

1.  **Create Directory:** Create a new directory under `rules/` for your new category (e.g., `rules/my-new-category/`).
2.  **Add First Rule:** Follow the "Adding a New Rule" steps to create the first rule within this new category.
3.  **Create `rules.json`:** Create a `rules.json` file in your new category directory, including the entry for your first rule.

### Enhancing Rule Quality (Ongoing Tasks)

To continuously improve the quality and utility of our rules, contributors are encouraged to address the following:

*   **Apply Granular Severity Scale:** Review existing rules and update their `severity` metadata to align with the more granular scale defined in the [Metadata Glossary](docs/metadata-glossary.md#1-severity). This helps ADEs prioritize effectively.
*   **Populate "Further Reading" Sections:** For each rule, research and add at least two authoritative, clickable resources to the "Further Reading" section. This enriches the rule's context and provides credible learning paths.
*   **Expand Automation Sections:** Where applicable, expand the "Automation Potential" sections with concrete configuration snippets (e.g., sample ESLint rules, SonarQube quality gate settings) and tooling invocation commands. This accelerates ADE enforcement.
*   **Introduce Domain Playbooks:** For critical categories (e.g., security, DevOps, observability), create companion automation playbooks outlining detection, remediation, and verification checklists that ADEs can execute end-to-end. See `rules/playbooks/` for examples and guidance.

### Commit Your Changes

Write clear and concise commit messages. We recommend following the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification (e.g., `feat: add new rule for X`, `fix: correct typo in Y rule`).

### Push to Your Fork

Push your changes to your forked repository.

### Create a Pull Request

Open a pull request from your branch to the `main` branch of the original repository.
*   Provide a clear description of your changes.
*   Reference any related issues.
*   Ensure your changes adhere to the established structure and quality standards.

## Rule Versioning and Summaries

Each individual rule (`.md` file) can be considered a versionable unit, with its metadata managed in the YAML frontmatter and the `rules.json` manifest.

*   **`CHANGELOG.md`:** This file tracks significant changes and versions of the entire rule set. Please update it with a summary of your contributions if they introduce major changes or new rules.

## Automated Validation (Planned)

We plan to implement a CI validation script (`scripts/validate-rules.py`) to automatically check:

*   JSON syntax of all `rules.json` files.
*   YAML frontmatter syntax and required fields in `.md` files.
*   Consistency between `.md` frontmatter and `rules.json` entries.
*   Validation of optional fields against the [Metadata Glossary](docs/metadata-glossary.md).

Contributors are encouraged to run this script locally before committing changes once it is available.

## Code of Conduct

Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) in all your interactions and contributions.

Thank you for contributing to ADE Rules!
