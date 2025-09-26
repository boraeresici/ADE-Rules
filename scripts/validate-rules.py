import os
import json
import glob
import sys
import re
import yaml

# --- Configuration ---
RULES_DIR = "rules"
DOCS_DIR = "docs"
METADATA_GLOSSARY_PATH = os.path.join(DOCS_DIR, "metadata-glossary.md")

REQUIRED_FRONTMATTER_FIELDS = ['id', 'title', 'description', 'tags']

def extract_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def load_metadata_glossary():
    glossary_content = ""
    try:
        with open(METADATA_GLOSSARY_PATH, 'r', encoding='utf-8') as f:
            glossary_content = f.read()
    except FileNotFoundError:
        print(f"[ERROR] Metadata glossary not found at {METADATA_GLOSSARY_PATH}")
        return None

    # Simple regex to extract allowed values for severity, applies_to, automation_potential
    glossary = {}
    severity_match = re.search(r'## 1\. `severity`.*?Allowed Values:\n(.*?)\n##', glossary_content, re.DOTALL)
    if severity_match:
        glossary['severity'] = [line.strip().replace('-', '').strip() for line in severity_match.group(1).split('\n') if line.strip()]

    applies_to_match = re.search(r'## 2\. `applies_to`.*?Allowed Values \(Examples.*?\):\n(.*?)\n##', glossary_content, re.DOTALL)
    if applies_to_match:
        glossary['applies_to'] = [line.strip().replace('-', '').strip() for line in applies_to_match.group(1).split('\n') if line.strip()]

    automation_potential_match = re.search(r'## 3\. `automation_potential`.*?Allowed Values \(Examples.*?\):\n(.*?)\n##', glossary_content, re.DOTALL)
    if automation_potential_match:
        glossary['automation_potential'] = [line.strip().replace('-', '').strip() for line in automation_potential_match.group(1).split('\n') if line.strip()]

    return glossary

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

def validate_md_files(glossary):
    print("\n--- Validating .md rule files (YAML Frontmatter & Required Fields) ---")
    errors = 0
    md_files = glob.glob(os.path.join(RULES_DIR, "**", "*.md"), recursive=True)

    if not md_files:
        print("No .md rule files found.")
        return 0

    all_rule_ids = set() # To check related_rules integrity later
    rule_frontmatters = {} # To store frontmatter for consistency check

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
            
            # Validate required fields
            for field in REQUIRED_FRONTMATTER_FIELDS:
                if field not in frontmatter:
                    print(f"[ERROR] {file_path} is missing required frontmatter field: '{field}'")
                    errors += 1
                elif not frontmatter[field]: # Check for empty values
                    print(f"[ERROR] {file_path} has an empty value for required frontmatter field: '{field}'")
                    errors += 1
            
            # Validate optional fields against glossary
            if glossary:
                if 'severity' in frontmatter and frontmatter['severity'] not in glossary['severity']:
                    print(f"[ERROR] {file_path} has invalid 'severity': {frontmatter['severity']}. Allowed: {glossary['severity']}")
                    errors += 1
                
                if 'applies_to' in frontmatter:
                    if not isinstance(frontmatter['applies_to'], list):
                        print(f"[ERROR] {file_path} 'applies_to' must be a list.")
                        errors += 1
                    else:
                        for item in frontmatter['applies_to']:
                            # This check is more complex as applies_to can be very broad
                            # For now, just check if it's a string
                            if not isinstance(item, str):
                                print(f"[ERROR] {file_path} 'applies_to' item '{item}' must be a string.")
                                errors += 1
                
                if 'automation_potential' in frontmatter:
                    if not isinstance(frontmatter['automation_potential'], list):
                        print(f"[ERROR] {file_path} 'automation_potential' must be a list.")
                        errors += 1
                    else:
                        for item in frontmatter['automation_potential']:
                            if item not in glossary['automation_potential']:
                                print(f"[WARNING] {file_path} 'automation_potential' item '{item}' is not in glossary. Allowed: {glossary['automation_potential']}")

            if 'id' in frontmatter and frontmatter['id']:
                all_rule_ids.add(frontmatter['id'])
                rule_frontmatters[frontmatter['id']] = frontmatter

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
    
    return errors, all_rule_ids, rule_frontmatters

def validate_consistency(all_rule_ids, rule_frontmatters):
    print("\n--- Validating Consistency (rules.json vs .md frontmatter) ---")
    errors = 0
    json_files = glob.glob(os.path.join(RULES_DIR, "**", "rules.json"), recursive=True)

    for json_file_path in json_files:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            rules_in_json = json.load(f)
        
        for rule_entry in rules_in_json:
            rule_id = rule_entry.get('id')
            if not rule_id:
                print(f"[ERROR] {json_file_path} contains a rule entry without an 'id'.")
                errors += 1
                continue
            
            if rule_id not in rule_frontmatters:
                print(f"[ERROR] {json_file_path} rule '{rule_id}' has no corresponding .md file or its .md file is missing frontmatter.")
                errors += 1
                continue
            
            md_frontmatter = rule_frontmatters[rule_id]
            
            # Check documentation path
            expected_doc_path_suffix = rule_entry.get('documentation')
            if not expected_doc_path_suffix:
                print(f"[ERROR] {json_file_path} rule '{rule_id}' is missing 'documentation' field.")
                errors += 1
            else:
                # Construct full path to .md file relative to project root
                json_dir = os.path.dirname(json_file_path)
                full_md_path = os.path.abspath(os.path.join(json_dir, expected_doc_path_suffix))
                
                # Check if the file exists
                if not os.path.exists(full_md_path):
                    print(f"[ERROR] {json_file_path} rule '{rule_id}' documentation path '{expected_doc_path_suffix}' does not point to an existing file.")
                    errors += 1

            # Check consistency of id, name, description
            if rule_entry.get('name') != md_frontmatter.get('title'):
                print(f"[ERROR] {json_file_path} rule '{rule_id}': 'name' in JSON does not match 'title' in .md frontmatter.")
                errors += 1
            if rule_entry.get('description') != md_frontmatter.get('description'):
                print(f"[ERROR] {json_file_path} rule '{rule_id}': 'description' in JSON does not match 'description' in .md frontmatter.")
                errors += 1
            
            # Validate related_rules
            if 'related_rules' in rule_entry and isinstance(rule_entry['related_rules'], list):
                for related_id in rule_entry['related_rules']:
                    if related_id not in all_rule_ids:
                        print(f"[WARNING] {json_file_path} rule '{rule_id}' has a 'related_rules' entry '{related_id}' that does not correspond to an existing rule ID.")

    if errors == 0:
        print("All rules.json entries are consistent with .md frontmatter.")
    else:
        print(f"Found {errors} consistency error(s).")
    return errors


if __name__ == "__main__":
    total_errors = 0
    
    glossary = load_metadata_glossary()
    if not glossary:
        sys.exit(1) # Exit if glossary cannot be loaded

    total_errors += validate_json_files()
    md_errors, all_rule_ids, rule_frontmatters = validate_md_files(glossary)
    total_errors += md_errors
    total_errors += validate_consistency(all_rule_ids, rule_frontmatters)

    if total_errors > 0:
        print("\nValidation FAILED with errors.")
        sys.exit(1)
    else:
        print("\nValidation PASSED.")
        sys.exit(0)