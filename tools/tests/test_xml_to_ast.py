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


def test_parse_extracts_contract_blocks_and_phase_metadata():
    """Parser should preserve richer contract data from newer SkillML blocks."""
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <Skill skill_id="meta_zpwo" name="ZPWO" version="4.0.0"
           tier="meta" status="active" model="sonnet">
      <Meta>
        <Description>Routes work through the pipeline.</Description>
        <Owner>supermind</Owner>
        <Domain>meta</Domain>
        <Track>cross</Track>
        <Tags><Tag>orchestration</Tag></Tags>
      </Meta>
      <Contract>
        <InputsRequired>
          <Input type="parameter" format="text">
            <Name>command</Name>
            <Description>Slash command</Description>
          </Input>
        </InputsRequired>
        <InputsOptional>
          <Input type="ssot" format="yaml">
            <Name>PROJECT_BRIEF</Name>
            <Description>Project brief (required for T2+)</Description>
          </Input>
          <Input type="artifact" format="json">
            <Name>SESSION_STATE</Name>
            <Description>Workflow state</Description>
          </Input>
        </InputsOptional>
        <OutputsPrimary>
          <Output format="json">
            <Name>TaskRequest</Name>
            <Description>Dispatch object</Description>
          </Output>
        </OutputsPrimary>
      </Contract>
      <ReasoningFramework>
        <Step order="1">
          <Name>Identify Track</Name>
          <Action>Resolve the target track</Action>
          <Validation>Track exists</Validation>
        </Step>
      </ReasoningFramework>
    </Skill>'''
    ast = parse_xml_skill(xml)
    assert ast["category"] == "meta"
    assert ast["phase_type"] == "executional"
    assert ast["maturity_stage"] == "production"
    assert ast["inputs"][0]["name"] == "command"
    assert ast["conditional_inputs"][0]["name"] == "PROJECT_BRIEF"
    assert ast["optional_inputs"][0]["name"] == "SESSION_STATE"
    assert ast["outputs"][0]["name"] == "TaskRequest"
    assert "Identify Track" in ast["workflow_steps"][0]


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
    test_parse_extracts_contract_blocks_and_phase_metadata()
    test_parse_handles_missing_sections_gracefully()
    print("All tests passed!")
