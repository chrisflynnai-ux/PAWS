"""Tests for migration inventory helpers."""
import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from migrate import build_inventory


def test_build_inventory_reports_migrated_and_pending_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as output_dir:
        source_root = Path(source_dir)
        output_root = Path(output_dir)

        (source_root / "copy").mkdir()
        (source_root / "design").mkdir()
        (source_root / "copy" / "alpha.xml").write_text("<Skill />", encoding="utf-8")
        (source_root / "copy" / "beta.xml").write_text("<Skill />", encoding="utf-8")
        (source_root / "design" / "gamma.xml").write_text("<Skill />", encoding="utf-8")

        migrated_pkg = output_root / "copy" / "skill-copy-alpha-v1_0_0"
        migrated_pkg.mkdir(parents=True)
        (migrated_pkg / "manifest.json").write_text(
            json.dumps(
                {
                    "id": "skill.copy.alpha.v1_0_0",
                    "provenance": {"migrated_from": "alpha.xml"},
                }
            ),
            encoding="utf-8",
        )

        report = build_inventory(str(source_root), str(output_root))

        assert report["xml_total"] == 3
        assert report["migrated_total"] == 1
        assert report["pending_total"] == 2
        assert report["families"]["copy"]["migrated_count"] == 1
        assert report["families"]["copy"]["pending_count"] == 1
        assert report["families"]["design"]["pending_count"] == 1


if __name__ == "__main__":
    test_build_inventory_reports_migrated_and_pending_files()
    print("All tests passed!")
