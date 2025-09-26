import os
import json
import glob
import sys
import re
import yaml

# --- Configuration ---
RULES_DIR = "rules"

REQUIRED_FRONTMATTER_FIELDS = ['id', 'title', 'description', 'tags']

def extract_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def validate_json_files():
    print("\n--- Validating rules.json files ---")
    errors = 0
    json_files = glob.glob(os.path.join(RULES_DIR, "**", "rules.json"), recursive=True)

    if not json_files:
        print("No rules.json files found.")
        return 0

    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                json.load(f)
            # print(f"[OK] {file_path} is valid JSON.")
        except json.JSONDecodeError as e:
            print(f"[ERROR] {file_path} has a JSON syntax error: {e}")
            errors += 1
        except Exception as e:
            print(f"[ERROR] {file_path} encountered an unexpected error: {e}")
            errors += 1

    if errors == 0:
        print("All rules.json files are valid JSON.")
    else:
        print(f"Found {errors} JSON syntax error(s).")
    return errors

def validate_md_files():
    print("\n--- Validating .md rule files (YAML Frontmatter & Required Fields) ---")
    errors = 0
    md_files = glob.glob(os.path.join(RULES_DIR, "**", "*.md"), recursive=True)

    if not md_files:
        print("No .md rule files found.")
        return 0

    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter_str = extract_frontmatter(content)

        if not frontmatter_str:
            print(f"[ERROR] {file_path} is missing YAML frontmatter.")
            errors += 1
            continue

        try:
            frontmatter = yaml.safe_load(frontmatter_str)
            # print(f"[OK] {file_path} has valid YAML frontmatter.")

            # Validate required fields
            for field in REQUIRED_FRONTMATTER_FIELDS:
                if field not in frontmatter:
                    print(f"[ERROR] {file_path} is missing required frontmatter field: '{field}'")
                    errors += 1
                elif not frontmatter[field]: # Check for empty values
                    print(f"[ERROR] {file_path} has an empty value for required frontmatter field: '{field}'")
                    errors += 1

        except yaml.YAMLError as e:
            print(f"[ERROR] {file_path} has a YAML syntax error in its frontmatter: {e}")
            errors += 1
        except Exception as e:
            print(f"[ERROR] {file_path} encountered an unexpected error during frontmatter parsing: {e}")
            errors += 1

    if errors == 0:
        print("All .md rule files have valid YAML frontmatter and required fields.")
    else:
        print(f"Found {errors} YAML frontmatter/required field error(s).")
    return errors


if __name__ == "__main__":
    total_errors = 0
    total_errors += validate_json_files()
    total_errors += validate_md_files()

    if total_errors > 0:
        print("\nValidation FAILED with errors.")
        sys.exit(1)
    else:
        print("\nValidation PASSED.")
        sys.exit(0)
