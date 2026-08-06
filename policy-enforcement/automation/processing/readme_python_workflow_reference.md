# Python workflow reference

## Purpose

This document explains the Python files in the `automation/` workflow. It is based on a direct review of the implementation and describes what the code currently does, how data moves between modules, and where the portfolio implementation differs from a production AI-assisted documentation system.

The workflow:

1. locates the Siemens assessment PDF;
2. extracts text from the PDF;
3. identifies selected commands, filenames, interface paths, and confirmed topics;
4. creates a document plan;
5. copies approved reference outputs into the generated-output folder;
6. validates required and unsupported content;
7. creates an SME-question file and workflow metadata.

> **Implementation note**
>
> The current `processor.py` does not generate new documentation with an AI model. It uses approved reference Markdown files as the generated drafts. This allows the repository to demonstrate workflow orchestration, validation, packaging, and traceability without requiring an external model or API key.

## Workflow architecture

```text
automation/main.py
        |
        v
processing/workflow.py
        |
        +--> processing/config.py
        |
        +--> processing/input_reader.py
        |        |
        |        +--> Reads the source PDF
        |
        +--> processing/source_analyzer.py
        |        |
        |        +--> Extracts selected source signals
        |
        +--> processing/document_planner.py
        |        |
        |        +--> Selects document types
        |
        +--> processing/processor.py
        |        |
        |        +--> Loads approved reference outputs
        |
        +--> processing/validator.py
        |        |
        |        +--> Applies content checks
        |
        +--> processing/output_writer.py
                 |
                 +--> Writes documents and reports
```

## Entry point

### `automation/main.py`

`main.py` is the command-line entry point.

```python
from processing.workflow import run_workflow


if __name__ == "__main__":
    run_workflow()
    print("Workflow complete. Review files in automation/output.")
```

### Behavior

When the file runs directly, it:

1. imports `run_workflow`;
2. executes the complete workflow;
3. prints a completion message.

### Run command

From the repository root:

```bash
python automation/main.py
```

### Expected result

The workflow writes files to:

```text
automation/output/
```

## Configuration

### `processing/config.py`

This module defines the workflow's folder paths.

### Defined paths

| Constant | Path represented | Purpose |
|---|---|---|
| `BASE_DIR` | `automation/` | Base folder for the automated workflow |
| `INPUT_DIR` | `automation/input/` | Original source files |
| `REFERENCE_DIR` | `automation/input/reference_output/` | Approved human-created reference documents |
| `INSTRUCTIONS_DIR` | `automation/instructions/` | Authoring and grounding instructions |
| `TEMPLATES_DIR` | `automation/templates/` | Reusable document templates |
| `OUTPUT_DIR` | `automation/output/` | Generated documents and reports |

### Design value

Centralizing the paths prevents each module from defining its own folder locations. This makes the workflow easier to maintain and relocate.

## Input processing

### `processing/input_reader.py`

This module reads source PDFs and Markdown files.

### `read_pdf(path)`

```python
def read_pdf(path: Path) -> Dict[str, object]:
```

#### Input

A `Path` pointing to a PDF file.

#### Processing

- opens the PDF with `pypdf.PdfReader`;
- iterates through the pages;
- extracts page text;
- assigns a one-based page number;
- substitutes an empty string when a page has no extractable text.

#### Output

```python
{
    "filename": "technical_writing_test_SiemensXPE.pdf",
    "pages": [
        {
            "page": 1,
            "text": "Extracted page text"
        }
    ]
}
```

#### Limitation

The function extracts text only. It does not interpret diagrams, screenshots, layout, or image-based text.

### `read_text_files(directory)`

```python
def read_text_files(directory: Path) -> Dict[str, str]:
```

#### Input

A folder containing Markdown files.

#### Processing

- finds files ending in `.md`;
- sorts the files by path;
- reads each file as UTF-8 text.

#### Output

A dictionary where each key is a filename and each value is its content.

```python
{
    "policy_enforcement_overview.md": "# Policy enforcement..."
}
```

#### Current usage

This helper exists in the module but is not called by the current workflow.

## Source analysis

### `processing/source_analyzer.py`

This module performs lightweight, rule-based analysis of the extracted PDF text.

### `analyze_source(document)`

```python
def analyze_source(document: Dict[str, object]) -> Dict[str, object]:
```

#### Input

The structured PDF result returned by `read_pdf()`.

#### Processing

The function:

1. joins all page text into one string;
2. uses regular expressions to locate CLI commands beginning with `cdp`;
3. finds filenames ending in `.yaml` or `.yml`;
4. checks for the source path **Settings > Cloud Integrations > Policy Engine IAM Role**;
5. checks whether selected topics appear in the source;
6. records a predefined list of missing execution details.

#### Output

```python
{
    "source_file": "technical_writing_test_SiemensXPE.pdf",
    "commands": [],
    "filenames": [],
    "interface_paths": [],
    "confirmed_topics": [],
    "missing_execution_details": []
}
```

### Confirmed-topic checks

The module currently checks for:

- policy enforcement;
- Open Policy Agent;
- drift detection;
- automatic remediation;
- Project Sentinel.

### Missing-detail model

The function records the following as unresolved:

- complete YAML schemas;
- complete UI navigation and field names;
- provider-specific permissions;
- validated command output;
- failure and recovery behavior.

### Limitations

The analysis is intentionally narrow. It does not currently:

- trace each extracted fact to a page number;
- classify facts as confirmed, inferred, conflicting, or missing;
- parse full YAML examples;
- identify all headings or scenario requirements;
- evaluate relationships between artifacts;
- use an AI model for semantic extraction.

## Document planning

### `processing/document_planner.py`

This module defines the document types supported by the available source.

### `create_plan(analysis)`

```python
def create_plan(analysis: Dict[str, object]) -> Dict[str, str]:
```

#### Input

The analysis created by `analyze_source()`.

#### Output

```python
{
    "scenario_1_document_type": "feature overview with planned child procedures",
    "scenario_2_document_type": "documentation strategy",
    "reason": "..."
}
```

### Planning decision

The function identifies:

- Scenario 1 as a feature overview with future child procedures;
- Scenario 2 as a documentation strategy.

It explains that the source contains feature concepts, lifecycle information, artifacts, and commands, but not enough verified implementation detail for complete step-by-step procedures.

### Current limitation

The decision is hard-coded. The `analysis` argument is accepted but not evaluated when selecting the document type.

## Draft generation

### `processing/processor.py`

This module supplies the documents that the workflow treats as generated output.

### `generate_from_reference(reference_dir)`

```python
def generate_from_reference(reference_dir: Path) -> Dict[str, str]:
```

#### Input

The `reference_output/` folder containing approved Markdown documents.

#### Processing

- finds all Markdown files;
- sorts them;
- reads them as UTF-8 text;
- returns them without altering their content.

#### Output

```python
{
    "policy_enforcement_overview.md": "...",
    "project_sentinel_strategy.md": "..."
}
```

### Why this implementation is used

The repository demonstrates a reference-first development model:

1. create a high-quality output manually;
2. define the expected output contract;
3. build the orchestration and validation workflow;
4. later replace reference loading with controlled AI generation.

### Production extension

A production processor could:

- load the extracted source;
- load the style guide and grounding rules;
- select a template from the document plan;
- call an approved language model;
- return a generated draft;
- preserve source citations or traceability metadata.

## Validation

### `processing/validator.py`

This module checks whether the output contains required content and avoids selected unsupported details.

### Required policy terms

The validator expects the policy overview to include:

- `policy-manifest.yaml`;
- `policy-set.yaml`;
- `pipeline.yml`;
- `cdp policy validate`;
- `cdp pipeline run --policy-check`;
- `cdp policy detect-drift --pipeline <id>`;
- `Questions for Lena`.

### Forbidden policy terms

The validator checks that the following unsupported details are absent:

- `apiVersion: cdp.policy/v1`;
- `defaultViolationAction`;
- `cdp policy validate --manifest`;
- `cdp pipeline run --policy-check --pipeline`.

### Scenario 2 checks

The validator checks whether the Project Sentinel document includes:

- a proposed documentation structure;
- a workflow;
- at least two anticipated challenges.

### `validate_outputs(outputs)`

```python
def validate_outputs(outputs: Dict[str, str]) -> List[Dict[str, str]]:
```

#### Input

A dictionary of generated filenames and content.

#### Output

A list of validation results.

```python
[
    {
        "status": "PASS",
        "check": "Required policy content: policy-manifest.yaml"
    }
]
```

### Limitations

The validator uses literal string matching. It does not currently verify:

- whether a statement is technically correct;
- whether each claim is supported by a specific source location;
- style-guide compliance;
- Markdown heading hierarchy;
- active voice;
- command syntax beyond the listed strings;
- semantic equivalence when wording changes.

## Output generation

### `processing/output_writer.py`

This module writes generated documents and supporting reports.

### `write_outputs(output_dir, outputs)`

Writes every filename and content pair to the output folder.

### `write_validation_report(output_dir, results)`

Creates `validation_report.md`.

The report includes:

- one line for each PASS or FAIL result;
- a human-review requirement explaining that automated checks do not replace engineering or SME approval.

### `write_sme_questions(output_dir, policy_document)`

Creates `sme_review_questions.md`.

The function:

1. searches for the heading `## Questions for Lena`;
2. extracts all content after that heading;
3. writes the extracted content under `# SME review questions`;
4. writes a warning when the heading is missing.

### Limitation

The extraction assumes that `Questions for Lena` is the final section. If another section appears after it, that content would also be copied.

## Workflow orchestration

### `processing/workflow.py`

This module coordinates the complete process.

### `run_workflow()`

Execution sequence:

```text
1. Locate the first PDF in automation/input/
2. Read the PDF
3. Analyze the source
4. Create the document plan
5. Load approved reference outputs
6. Validate the outputs
7. Write generated documents
8. Write the validation report
9. Extract and write SME questions
10. Write workflow metadata
```

### Missing-input behavior

When `automation/input/` contains no PDF, the function raises:

```python
FileNotFoundError
```

### Workflow metadata

The module creates `workflow_metadata.json` containing:

```json
{
  "analysis": {},
  "plan": {}
}
```

This file makes the analysis and planning results inspectable after the workflow finishes.

### Current file-selection behavior

The workflow processes the first PDF returned by a sorted directory search. It does not currently support selecting a PDF through a command-line argument.

## Package marker

### `processing/__init__.py`

This file marks `processing/` as a Python package. It contains no implementation code.

## Inputs and outputs

### Inputs

```text
automation/input/
├── technical_writing_test_SiemensXPE.pdf
└── reference_output/
    ├── policy_enforcement_overview.md
    └── project_sentinel_strategy.md
```

### Outputs

```text
automation/output/
├── policy_enforcement_overview.md
├── project_sentinel_strategy.md
├── sme_review_questions.md
├── validation_report.md
└── workflow_metadata.json
```

## Error handling

The workflow currently handles one explicit error:

- no source PDF found.

Additional production error handling could cover:

- unreadable or encrypted PDFs;
- pages with no extracted text;
- missing reference files;
- output-write failures;
- malformed configuration;
- failed model calls;
- failed validation thresholds.

## How to extend the workflow

### Replace reference copying with AI generation

Update `processor.py` so that it receives:

- source analysis;
- document plan;
- authoring instructions;
- selected template;
- approved model configuration.

The processor would then generate a draft instead of copying the reference file.

### Add source traceability

Modify `source_analyzer.py` to store:

- statement;
- source page;
- source excerpt;
- confidence status;
- intended output section.

### Make planning evidence-based

Modify `document_planner.py` so that it evaluates the source-analysis result before selecting a document type.

### Improve validation

Add checks for:

- required headings;
- sentence-case headings;
- command preservation;
- unsupported claims;
- source citations;
- style rules;
- unresolved questions;
- output completeness.

### Add tests

Recommended tests include:

- PDF extraction returns page-level records;
- source analysis identifies expected commands and filenames;
- the planner selects the expected document types;
- missing required terms produce FAIL results;
- forbidden terms produce FAIL results;
- SME questions are extracted correctly;
- missing PDFs raise `FileNotFoundError`.

## Summary

The current implementation is a transparent portfolio workflow rather than a full AI authoring engine. It demonstrates:

- modular Python organization;
- folder-based processing;
- separation of configuration, analysis, planning, generation, validation, and writing;
- reference-output-driven development;
- traceable workflow metadata;
- explicit human-review controls.

Its clearest next step is to replace `generate_from_reference()` with a controlled generation component while preserving the same output and validation contracts.
