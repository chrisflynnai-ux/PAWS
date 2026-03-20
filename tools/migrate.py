"""XSkill Migration CLI.

Usage:
    python tools/migrate.py <xml_file> <output_dir>
    python tools/migrate.py --batch <xml_dir> <output_dir>

Runs the full pipeline: XML -> AST -> skill.md + manifest.json -> validate
"""
import argparse
import json
import os
import sys
from pathlib import Path

from xml_to_ast import parse_xml_file
from ast_to_skill_md import render_skill_md
from ast_to_manifest import render_manifest
from validate import validate_frontmatter, validate_manifest as validate_mf


def migrate_single(xml_path: str, output_dir: str) -> dict:
    """Migrate a single XML skill file to the XSkill package format.

    Args:
        xml_path: Path to source XML file.
        output_dir: Directory to write the skill package into.

    Returns:
        Result dictionary with status and any errors.
    """
    xml_name = os.path.basename(xml_path)
    print(f"  Parsing: {xml_name}")

    # Step 1: XML -> AST
    ast = parse_xml_file(xml_path)

    # Step 2: Derive package directory name from skill id
    skill_name = ast["id"].replace(".", "-") if ast["id"] else Path(xml_path).stem
    pkg_dir = os.path.join(output_dir, skill_name)
    os.makedirs(pkg_dir, exist_ok=True)

    # Step 3: AST -> skill.md
    skill_md = render_skill_md(ast)
    skill_md_path = os.path.join(pkg_dir, "skill.md")
    with open(skill_md_path, "w", encoding="utf-8") as f:
        f.write(skill_md)
    print(f"  Wrote: {skill_md_path}")

    # Step 4: AST -> manifest.json
    manifest_json = render_manifest(ast, source_xml=xml_name)
    manifest_path = os.path.join(pkg_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(manifest_json)
    print(f"  Wrote: {manifest_path}")

    # Step 5: Create empty experiences.jsonl
    exp_path = os.path.join(pkg_dir, "experiences.jsonl")
    if not os.path.exists(exp_path):
        with open(exp_path, "w", encoding="utf-8") as f:
            pass  # Empty file
        print(f"  Wrote: {exp_path}")

    # Step 6: Create stub directories
    for subdir in ["examples", "evals", "references", "scripts", "sub_skills", "templates"]:
        os.makedirs(os.path.join(pkg_dir, subdir), exist_ok=True)

    # Step 7: Validate
    import yaml
    with open(skill_md_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Extract frontmatter
    parts = content.split("---", 2)
    if len(parts) >= 3:
        fm = yaml.safe_load(parts[1])
    else:
        fm = {}

    manifest = json.loads(manifest_json)

    fm_errors = validate_frontmatter(fm)
    mf_errors = validate_mf(manifest)

    result = {
        "skill_id": ast["id"],
        "xml_source": xml_name,
        "package_dir": pkg_dir,
        "frontmatter_errors": fm_errors,
        "manifest_errors": mf_errors,
        "status": "PASS" if not fm_errors and not mf_errors else "FAIL",
    }

    if fm_errors:
        print(f"  WARNING Frontmatter errors: {fm_errors}")
    if mf_errors:
        print(f"  WARNING Manifest errors: {mf_errors}")
    if not fm_errors and not mf_errors:
        print(f"  VALID - Validation passed")

    return result


def migrate_batch(xml_dir: str, output_dir: str):
    """Migrate all XML files in a directory."""
    xml_files = sorted(Path(xml_dir).glob("*.xml"))
    print(f"Found {len(xml_files)} XML files in {xml_dir}\n")

    results = []
    for xml_file in xml_files:
        print(f"[{len(results)+1}/{len(xml_files)}] Migrating {xml_file.name}")
        try:
            result = migrate_single(str(xml_file), output_dir)
            results.append(result)
        except Exception as e:
            print(f"  ERROR: {e}")
            results.append({"xml_source": xml_file.name, "status": "ERROR", "error": str(e)})
        print()

    # Summary
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = sum(1 for r in results if r["status"] == "FAIL")
    errors = sum(1 for r in results if r["status"] == "ERROR")
    print(f"Migration complete: {passed} passed, {failed} failed, {errors} errors out of {len(results)} total")

    # Write results
    results_path = os.path.join(output_dir, "migration_report.json")
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Report: {results_path}")


def main():
    parser = argparse.ArgumentParser(description="XSkill Migration CLI")
    parser.add_argument("source", help="XML file or directory (with --batch)")
    parser.add_argument("output", help="Output directory for skill packages")
    parser.add_argument("--batch", action="store_true", help="Migrate all XMLs in directory")
    args = parser.parse_args()

    if args.batch:
        migrate_batch(args.source, args.output)
    else:
        result = migrate_single(args.source, args.output)
        print(f"\nResult: {result['status']}")


if __name__ == "__main__":
    main()
