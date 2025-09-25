# ADE Rules Project 🚀

Welcome to the **ADE Rules Project**! This repository serves as a comprehensive, structured, and machine-readable collection of best practices and rules for Application Development Environments (ADEs).

Our mission is to empower both human developers and AI-driven development assistants with clear, consistent, and actionable guidelines to foster high-quality, secure, performant, and collaborative software development.

## ✨ Why ADE Rules?

In today's fast-paced development landscape, maintaining code quality, ensuring security, and optimizing performance are paramount. This project addresses these challenges by:

- **Standardizing Development:** Providing a unified set of rules across various technologies and domains.
- **Empowering AI Assistants:** Offering a structured format that AI Development Environments can easily consume and apply.
- **Enhancing Collaboration:** Ensuring all team members adhere to consistent standards, reducing friction and improving code reviews.
- **Promoting Best Practices:** Guiding developers towards proven methods in coding, architecture, security, and operations.

## 📚 Project Structure & Philosophy

Our rules are organized into a modular, granular structure, making them easy to navigate, understand, and integrate into automated workflows. Each rule is designed to be atomic and independently applicable.

### Key Components:

- **Rule Categories:** Rules are grouped into logical directories (e.g., `rules/code-quality/`, `rules/ai-safety-operations/`).
- **Individual Rule Files (`.md`):** Each specific rule is defined in its own Markdown file, adhering to the Single Responsibility Principle. These files include:
    - **YAML Frontmatter:** Metadata like `id`, `title`, `description`, `tags`, `severity`, `applies_to`, `automation_potential`, `suggested_tools`, and `related_rules`.
    - **Detailed Content:** Explanations, rationales, good/bad practice examples, and production checklists.
- **Manifest Files (`rules.json`):** Each category contains a `rules.json` file that acts as a manifest, listing all rules within that category with their metadata. This facilitates programmatic access and rule discovery by ADEs and CLIs.

## 🚀 Getting Started

To explore the full set of rules and their detailed documentation, dive into the `rules/` directory:

[**Explore All Rules**](rules/readme.md)

## 🛠 Validate the Rule Catalog

We provide a Python helper script to make sure each `rules.json` manifest is valid JSON and remains synchronized with the YAML front matter defined inside the Markdown rule files. The validator also checks that metadata values use the allowed vocabulary and that the “Further Reading” placeholder text has been replaced with real resources.

```bash
pip install pyyaml
python scripts/validate_rules.py
```

The command exits with a non-zero status when it detects problems so it can be wired into CI workflows or executed locally before opening a pull request.

## 🤝 Contributing

We welcome contributions from the community! Whether it's adding new rules, improving existing ones, or enhancing the project's infrastructure, your input is valuable.

Please refer to our [**Contributing Guidelines**](CONTRIBUTING.md) for detailed instructions on how to get involved.

## 📜 Changelog

Stay informed about the latest updates, new features, and improvements by checking our [**Changelog**](CHANGELOG.md).

## 🔗 Repository

This project is proudly hosted on GitHub:

[https://github.com/boraeresici/ADE-Rules](https://github.com/boraeresici/ADE-Rules)

---

*Built with passion for better software development. ✨*
