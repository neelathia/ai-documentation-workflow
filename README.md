# AI-assisted documentation workflow

## Project purpose

This repository shows how a manually authored technical-writing assessment can be reverse-engineered into a reusable documentation workflow.

The project has two roots:

- `manual/` contains the original source and the human-authored reference deliverables.
- `automation/` contains the same source, the approved manual outputs as references, modular instructions and templates, working Python modules, generated outputs, and validation artifacts.

The purpose is not to claim that the first Siemens documents were generated automatically. The first output was created manually. The authoring decisions were then analyzed and encoded into reusable rules, templates, processing modules, and validation checks so future documentation work can follow the same controlled pattern.

## Phase 1: Manual authoring

### Input

`manual/input/technical_writing_test_SiemensXPE.pdf`

The PDF contains the assessment instructions, the supplied style guide, Scenario 1 engineering input, and Scenario 2 requirements.

### Processing

The source is reviewed manually. Human judgment is used to:

- identify source-supported facts;
- distinguish an overview from an executable procedure;
- organize Scenario 1 by pre-deployment, deployment, and post-deployment;
- avoid unsupported schemas, flags, and interface details;
- create SME questions for missing implementation information; and
- develop the Scenario 2 hierarchy, workflow, and documentation challenges.

The `manual/processing/README.md` records this phase. No automation is claimed.

### Output

- `manual/output/policy_enforcement_overview.md`
- `manual/output/policy_enforcement_overview.pdf`
- `manual/output/project_sentinel_strategy.md`
- `manual/output/project_sentinel_strategy.pdf`

These files are the human-approved reference outputs.

## Phase 2: Reverse-engineer the reusable method

### Input

- the original Siemens PDF;
- the approved manual outputs;
- the reasoning used to select the document types and structures.

### Processing

The manual method is converted into modular assets:

- `automation/instructions/ai_assisted_documentation_workflow.md` defines the reusable workflow;
- `automation/instructions/source_grounding_rules.md` limits unsupported additions;
- `automation/instructions/siemens_style_guide.md` extracts the style rules from the PDF;
- `automation/instructions/assessment_requirements.md` records the required deliverables;
- `automation/templates/feature_document_template.md` defines the feature-document structure;
- `automation/templates/documentation_strategy_template.md` defines the strategy-document structure.

### Output

A reusable documentation model that can guide future feature, migration, process, and operational documentation.

## Phase 3: Automated processing

### Input

- `automation/input/technical_writing_test_SiemensXPE.pdf`
- `automation/input/reference_output/`
- `automation/instructions/`
- `automation/templates/`

### Processing

The Python files in `automation/processing/` perform the workflow:

- `main.py` starts the process.
- `config.py` defines project paths.
- `input_reader.py` extracts page-level PDF text.
- `source_analyzer.py` identifies commands, filenames, interface paths, confirmed topics, and missing execution details.
- `document_planner.py` selects the appropriate document types.
- `processor.py` creates drafts using the approved reference-output contract.
- `validator.py` checks required content and unsupported additions.
- `output_writer.py` writes documentation and validation artifacts.
- `workflow.py` coordinates the complete sequence.

This portfolio version uses the approved manual documents as the generation contract. A production AI implementation can replace the reference-output renderer with an approved language-model call while preserving the same source, instructions, templates, document plan, and validation checks.

### Output

- `automation/output/policy_enforcement_overview.md`
- `automation/output/project_sentinel_strategy.md`
- `automation/output/validation_report.md`
- `automation/output/sme_review_questions.md`
- `automation/output/workflow_metadata.json`

## Phase 4: Validation and human review

### Input

- the generated outputs;
- source-grounding requirements;
- exact filenames and commands from the PDF;
- the human-approved reference outputs.

### Processing

The validator checks that:

- required lifecycle phases and artifacts are present;
- commands are preserved exactly;
- Questions for Lena are included;
- unsupported YAML schemas and command flags are absent;
- Scenario 2 includes a hierarchy, one workflow, and two challenges.

### Output

`automation/output/validation_report.md`

Validation supports quality control but does not replace technical review. Human and SME approval remain required before publication.

## Run the automation

From the repository root:

```bash
python automation/main.py
```

Then review the files in `automation/output/`.

## Relevance to migration documentation

The same pattern can support migration programs:

1. place repository inventories, migration plans, specifications, and engineering notes in an input area;
2. apply reusable migration instructions and templates;
3. generate playbooks, procedures, decision records, and validation checklists;
4. validate technical strings, required sections, source traceability, and unresolved gaps; and
5. route the result through human and engineering review.

## AI governance

AI supports extraction, classification, drafting, and validation. Human reviewers remain responsible for source authority, technical accuracy, final wording, and publication approval.
