#!/usr/bin/env python3
"""Validate ADE rule manifests and Markdown front matter."""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
RULES_ROOT = REPO_ROOT / "rules"
PLACEHOLDER_FURTHER_READING = "[Optional: Links to external resources, articles, or documentation related to this rule.]"
ALLOWED_SEVERITIES = {"critical", "high", "medium", "low", "suggestion"}


@dataclass
class RuleEntry:
    rule_id: str
    manifest_path: Path
    manifest_index: int
    manifest_data: Dict[str, object]


def load_manifest(path: Path) -> Tuple[List[Dict[str, object]], List[str]]:
    errors: List[str] = []
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:  # pragma: no cover - filesystem errors
        errors.append(f"{path}: unable to read file ({exc})")
        return [], errors

    try:
        data = json.loads(content)
    except json.JSONDecodeError as exc:
        errors.append(f"{path}: invalid JSON - {exc}")
        return [], errors

    if not isinstance(data, list):
        errors.append(f"{path}: manifest root must be a list of rule objects")
        return [], errors

    manifest_entries: List[Dict[str, object]] = []
    for index, item in enumerate(data):
        if not isinstance(item, dict):
            errors.append(f"{path}: entry #{index + 1} must be an object")
            continue
        manifest_entries.append(item)

    return manifest_entries, errors


def extract_front_matter(markdown_path: Path) -> Tuple[Optional[Dict[str, object]], Optional[str], List[str]]:
    errors: List[str] = []
    try:
        text = markdown_path.read_text(encoding="utf-8")
    except OSError as exc:  # pragma: no cover - filesystem errors
        errors.append(f"{markdown_path}: unable to read file ({exc})")
        return None, None, errors

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        errors.append(f"{markdown_path}: missing YAML front matter delimiter '---'")
        return None, None, errors

    end_index: Optional[int] = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_index = idx
            break

    if end_index is None:
        errors.append(f"{markdown_path}: unable to locate closing '---' for YAML front matter")
        return None, None, errors

    front_matter_text = "\n".join(lines[1:end_index])
    body = "\n".join(lines[end_index + 1 :])

    try:
        metadata = yaml.safe_load(front_matter_text) or {}
    except yaml.YAMLError as exc:
        errors.append(f"{markdown_path}: invalid YAML front matter - {exc}")
        return None, None, errors

    if not isinstance(metadata, dict):
        errors.append(f"{markdown_path}: YAML front matter must be a mapping")
        return None, None, errors

    return metadata, body, errors


def ensure_relative_to_repo(path: Path) -> Tuple[Optional[Path], Optional[str]]:
    try:
        relative = path.relative_to(REPO_ROOT)
    except ValueError:
        return None, f"{path}: documentation path escapes repository root"
    return relative, None


def normalize_string_list(value: object, *, field_name: str, context: str, errors: List[str]) -> Optional[List[str]]:
    if value is None:
        errors.append(f"{context}: missing '{field_name}' list")
        return None
    if not isinstance(value, list):
        errors.append(f"{context}: '{field_name}' must be a list of strings")
        return None
    normalized: List[str] = []
    for idx, item in enumerate(value):
        if not isinstance(item, str):
            errors.append(f"{context}: '{field_name}' entry #{idx + 1} must be a string")
            continue
        normalized.append(item.strip())
    return normalized


def compare_lists(
    *,
    rule_id: str,
    field_name: str,
    manifest_values: Optional[List[str]],
    front_values: Optional[List[str]],
    manifest_context: str,
    front_context: str,
    errors: List[str],
) -> None:
    if manifest_values is None and front_values is None:
        return
    if manifest_values is None or front_values is None:
        errors.append(
            f"{rule_id}: field '{field_name}' must be present in both manifest ({manifest_context}) and front matter ({front_context})"
        )
        return
    if sorted(manifest_values) != sorted(front_values):
        errors.append(
            f"{rule_id}: mismatch in '{field_name}' between manifest ({manifest_context}) and front matter ({front_context})"
        )


def validate_rule(rule: RuleEntry, all_rule_ids: Iterable[str]) -> List[str]:
    errors: List[str] = []
    manifest_context = f"{rule.manifest_path}#{rule.manifest_index + 1}"

    documentation_value = rule.manifest_data.get("documentation")
    if not isinstance(documentation_value, str):
        errors.append(f"{manifest_context}: 'documentation' must be a string")
        return errors

    documentation_path = (rule.manifest_path.parent / documentation_value).resolve()
    relative_doc, rel_error = ensure_relative_to_repo(documentation_path)
    if rel_error:
        errors.append(rel_error)
        return errors

    if not documentation_path.exists():
        errors.append(f"{manifest_context}: documentation file '{documentation_value}' not found")
        return errors
    if not documentation_path.is_file():
        errors.append(f"{manifest_context}: documentation path '{documentation_value}' is not a file")
        return errors

    front_matter, body, fm_errors = extract_front_matter(documentation_path)
    errors.extend(fm_errors)
    if front_matter is None or body is None:
        return errors

    front_context = f"{relative_doc}"

    # Required scalar fields
    for field_name, manifest_key, front_key in (
        ("id", "id", "id"),
        ("name/title", "name", "title"),
        ("description", "description", "description"),
    ):
        manifest_value = rule.manifest_data.get(manifest_key)
        front_value = front_matter.get(front_key)
        if not isinstance(manifest_value, str):
            errors.append(f"{manifest_context}: '{manifest_key}' must be a string")
            continue
        if not isinstance(front_value, str):
            errors.append(f"{front_context}: '{front_key}' must be a string")
            continue
        if manifest_value.strip() != front_value.strip():
            errors.append(
                f"{rule.rule_id}: mismatch in '{field_name}' between manifest ({manifest_context}) and front matter ({front_context})"
            )

    # Severity validation
    manifest_severity = rule.manifest_data.get("severity")
    front_severity = front_matter.get("severity")
    if manifest_severity is None or front_severity is None:
        errors.append(
            f"{rule.rule_id}: field 'severity' must be present in both manifest ({manifest_context}) and front matter ({front_context})"
        )
    else:
        if not isinstance(manifest_severity, str):
            errors.append(f"{manifest_context}: 'severity' must be a string")
        if not isinstance(front_severity, str):
            errors.append(f"{front_context}: 'severity' must be a string")
        if isinstance(manifest_severity, str) and isinstance(front_severity, str):
            if manifest_severity != front_severity:
                errors.append(
                    f"{rule.rule_id}: mismatch in 'severity' between manifest ({manifest_context}) and front matter ({front_context})"
                )
            if manifest_severity not in ALLOWED_SEVERITIES:
                errors.append(f"{manifest_context}: 'severity' must be one of {sorted(ALLOWED_SEVERITIES)}")

    # List comparisons
    list_fields = [
        ("tags", "tags"),
        ("applies_to", "applies_to"),
        ("automation_potential", "automation_potential"),
        ("suggested_tools", "suggested_tools"),
        ("related_rules", "related_rules"),
    ]

    for field_name, key in list_fields:
        manifest_values = normalize_string_list(
            rule.manifest_data.get(key),
            field_name=key,
            context=manifest_context,
            errors=errors,
        )
        front_values = normalize_string_list(
            front_matter.get(key),
            field_name=key,
            context=front_context,
            errors=errors,
        )
        compare_lists(
            rule_id=rule.rule_id,
            field_name=field_name,
            manifest_values=manifest_values,
            front_values=front_values,
            manifest_context=manifest_context,
            front_context=front_context,
            errors=errors,
        )

    # Placeholder detection
    if PLACEHOLDER_FURTHER_READING in body:
        errors.append(
            f"{front_context}: replace the 'Further Reading' placeholder with real references"
        )

    # related_rules reference validation
    related_rules = front_matter.get("related_rules")
    if isinstance(related_rules, list):
        for related in related_rules:
            if isinstance(related, str) and related not in all_rule_ids:
                errors.append(
                    f"{front_context}: related rule '{related}' does not exist in repository manifests"
                )

    return errors


def main() -> int:
    if not RULES_ROOT.exists():
        print(f"rules directory not found at {RULES_ROOT}", file=sys.stderr)
        return 1

    all_errors: List[str] = []
    rule_index: Dict[str, RuleEntry] = {}

    manifest_paths = sorted(RULES_ROOT.rglob("rules.json"))
    if not manifest_paths:
        print("No manifest files found under 'rules/'.", file=sys.stderr)
        return 1

    for manifest_path in manifest_paths:
        manifest_entries, manifest_errors = load_manifest(manifest_path)
        all_errors.extend(manifest_errors)
        for idx, entry in enumerate(manifest_entries):
            rule_id = entry.get("id")
            if not isinstance(rule_id, str):
                all_errors.append(f"{manifest_path}#{idx + 1}: 'id' must be a string")
                continue
            if rule_id in rule_index:
                existing = rule_index[rule_id]
                all_errors.append(
                    f"Duplicate rule id '{rule_id}' in {manifest_path}#{idx + 1} and {existing.manifest_path}#{existing.manifest_index + 1}"
                )
                continue
            rule_index[rule_id] = RuleEntry(
                rule_id=rule_id,
                manifest_path=manifest_path,
                manifest_index=idx,
                manifest_data=entry,
            )

    all_rule_ids = set(rule_index.keys())

    for rule in rule_index.values():
        all_errors.extend(validate_rule(rule, all_rule_ids))

    if all_errors:
        print("Rule validation failed:\n", file=sys.stderr)
        for message in sorted(all_errors):
            print(f"- {message}", file=sys.stderr)
        return 1

    print("All rule manifests and Markdown files passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())