"""Tests for XML -> AST parser."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from xml_to_ast import parse_xml_skill


def test_parse_extracts_metadata():
    """Parser should extract id, name, version from XML Skill element."""
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <Skill skill_id="skill.copy.test.v1_0_0" name="Test Skill" version="1.0.0"
           tier="production" status="active" model="sonnet">
      <Meta>
        <n>Test Skill</n>
        <Description>A test skill for validation.</Description>
        <Owner>supermind</Owner>
        <Tags><Tag>test</Tag><Tag>copy</Tag></Tags>
      </Meta>
    </Skill>'''
    ast = parse_xml_skill(xml)
    assert ast["id"] == "skill.copy.test.v1_0_0"
    assert ast["name"] == "Test Skill"
    assert ast["version"] == "1.0.0"
    assert ast["status"] == "active"
    assert ast["description"] == "A test skill for validation."
    assert ast["tags"] == ["test", "copy"]
    assert ast["owner"] == "supermind"


def test_parse_extracts_inputs_outputs():
    """Parser should extract InputSpec and OutputSpec elements."""
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <Skill skill_id="skill.copy.test.v1_0_0" name="Test" version="1.0.0"
           tier="production" status="active" model="sonnet">
      <Meta><n>Test</n><Description>Test skill.</Description><Owner>supermind</Owner>
        <Tags><Tag>test</Tag></Tags></Meta>
      <InputSpec>
        <Input name="sales_page_url" type="string" required="true">The URL to analyze</Input>
        <Input name="brand_brief" type="string" required="false">Optional brand context</Input>
      </InputSpec>
      <OutputSpec>
        <Output name="analysis_report" type="markdown">Full analysis</Output>
      </OutputSpec>
    </Skill>'''
    ast = parse_xml_skill(xml)
    assert len(ast["inputs"]) == 2
    assert ast["inputs"][0]["name"] == "sales_page_url"
    assert ast["inputs"][0]["required"] is True
    assert len(ast["outputs"]) == 1
    assert ast["outputs"][0]["name"] == "analysis_report"


def test_parse_handles_missing_sections_gracefully():
    """Parser should return empty defaults for missing XML sections."""
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <Skill skill_id="skill.copy.minimal.v1_0_0" name="Minimal" version="1.0.0"
           tier="draft" status="draft" model="sonnet">
      <Meta><n>Minimal</n><Description>Bare minimum skill.</Description>
        <Owner>supermind</Owner><Tags><Tag>test</Tag></Tags></Meta>
    </Skill>'''
    ast = parse_xml_skill(xml)
    assert ast["inputs"] == []
    assert ast["outputs"] == []
    assert ast["depends_on"] == []
    assert ast["failure_modes"] == []


if __name__ == "__main__":
    test_parse_extracts_metadata()
    test_parse_extracts_inputs_outputs()
    test_parse_handles_missing_sections_gracefully()
    print("All tests passed!")
