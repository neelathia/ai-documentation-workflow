# Automated processing

This document describes the Python modules in [automation/processing/](.). It is the automation counterpart to [manual/processing/README.md](../../manual/processing/README.md), which records the human authoring phase.

The modules turn the Siemens source PDF, the approved reference outputs, the instruction files, and the templates into generated documentation plus validation artifacts. Each module has one responsibility, so any stage can be replaced without changing the rest of the workflow.

## Execution order

```text
main.py
  └── workflow.run_workflow()
        ├── input_reader.read_pdf()          source PDF -> page text
        ├── source_analyzer.analyze_source() page text -> commands, filenames, topics, gaps
        ├── document_planner.create_plan()   analysis -> document types and rationale
        ├── processor.generate_from_reference()  reference outputs -> drafts
        ├── validator.validate_outputs()     drafts -> PASS/FAIL checks
        └── output_writer.*                  drafts, checks -> automation/output/
```

Run it from the repository root:

```bash
python automation/main.py
```

## Modules

### `config.py`

Defines every path used by the workflow, all derived from the location of the module itself so the workflow runs from any working directory.

| Constant | Path |
| --- | --- |
| `BASE_DIR` | `automation/` |
| `INPUT_DIR` | `automation/input/` |
| `REFERENCE_DIR` | `automation/input/reference_output/` |
| `INSTRUCTIONS_DIR` | `automation/instructions/` |
| `TEMPLATES_DIR` | `automation/templates/` |
| `OUTPUT_DIR` | `automation/output/` |

`INPUT_DIR` must contain the source PDF, and `REFERENCE_DIR` must contain the approved Markdown reference outputs.

### `input_reader.py`

Reads source material.

- `read_pdf(path)` uses `pypdf` to extract text page by page and returns `{"filename": str, "pages": [{"page": int, "text": str}, ...]}`. Page numbers start at 1, and pages with no extractable text yield an empty string rather than `None`.
- `read_text_files(directory)` returns a `{filename: contents}` mapping for the `*.md` files in a directory, sorted by name. It is available for loading instruction and template files.

### `source_analyzer.py`

`analyze_source(document)` flattens the page text and extracts, using regular expressions and fixed phrase lists:

- `commands` — `cdp ...` command strings found in the source;
- `filenames` — referenced `.yaml` / `.yml` files;
- `interface_paths` — a UI path, recorded only when the supporting terms appear in the source;
- `confirmed_topics` — which of the expected subject-matter phrases are actually present;
- `missing_execution_details` — the known gaps (schemas, UI field names, permissions, command output, failure behaviour) that must go to an SME rather than be invented.

The module never adds detail that is absent from the source; anything unverified is reported as a gap.

### `document_planner.py`

`create_plan(analysis)` decides what should be written. It returns the Scenario 1 document type (a feature overview with planned child procedures), the Scenario 2 document type (a documentation strategy), and the reason for that choice: the source supports concepts, lifecycle, artifacts, and commands, but not complete procedures. The plan is stored in `workflow_metadata.json` so the decision is auditable.

### `processor.py`

`generate_from_reference(reference_dir)` produces the document drafts as `{filename: contents}` by reading the approved reference Markdown.

This is deliberate: the portfolio version demonstrates the repeatable packaging and validation workflow, not language-model authoring. A production implementation replaces this single function with an approved model call driven by the source, instructions, templates, and plan; the rest of the workflow is unchanged because the output contract stays the same.

### `validator.py`

`validate_outputs(outputs)` returns a list of `{"status": "PASS" | "FAIL", "check": str}` records covering three groups:

- `REQUIRED_POLICY_TERMS` — exact filenames, exact `cdp` commands, and the "Questions for Lena" section must appear in `policy_enforcement_overview.md`;
- `FORBIDDEN_POLICY_TERMS` — invented YAML schemas and command flags must not appear;
- Scenario 2 structure — `project_sentinel_strategy.md` must contain a proposed documentation structure, at least one workflow, and at least two anticipated challenges.

Validation is a structural and source-grounding gate only. It does not assess technical accuracy, and human and SME approval are still required.

### `output_writer.py`

Writes everything to `automation/output/`, creating the directory when needed.

- `write_outputs(output_dir, outputs)` writes each generated document.
- `write_validation_report(output_dir, results)` writes `validation_report.md` as a status list plus a standing note that human review is required.
- `write_sme_questions(output_dir, policy_document)` extracts the "Questions for Lena" section into `sme_review_questions.md`, or records that no SME question section was found.

### `workflow.py`

`run_workflow()` orchestrates the sequence above. It selects the first PDF in `INPUT_DIR` (sorted by name) and raises `FileNotFoundError` if there is none, then runs analysis, planning, generation, validation, and writing, and finally records the analysis and plan in `workflow_metadata.json`.

### `main.py`

The entry point. It calls `run_workflow()` and prints a completion message pointing at `automation/output`. It imports `processing.workflow`, so it is run from the repository root as `python automation/main.py`.

### `__init__.py`

Empty; marks `processing` as a package.

## Generated artifacts

| File | Written by |
| --- | --- |
| `policy_enforcement_overview.md` | `write_outputs` |
| `project_sentinel_strategy.md` | `write_outputs` |
| `validation_report.md` | `write_validation_report` |
| `sme_review_questions.md` | `write_sme_questions` |
| `workflow_metadata.json` | `run_workflow` |

## Dependencies

`pypdf`, as listed in [requirements.txt](../../requirements.txt).

## Extending the workflow

- New document type: extend `create_plan` and add the matching output contract.
- New source format: add a reader alongside `read_pdf` in `input_reader.py`.
- New quality rule: add a term to the validator lists or a new check in `validate_outputs`.
- Model-based drafting: replace `generate_from_reference` while keeping the `{filename: contents}` return shape.
