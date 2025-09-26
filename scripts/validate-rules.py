import os
import json
import glob
import sys

# --- Configuration ---
RULES_DIR = "rules"

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
            print(f"[OK] {file_path} is valid JSON.")
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


if __name__ == "__main__":
    total_errors = 0
    total_errors += validate_json_files()

    if total_errors > 0:
        print("\nValidation FAILED with errors.")
        sys.exit(1)
    else:
        print("\nValidation PASSED.")
        sys.exit(0)