import json
from pathlib import Path

from .config import INPUT_DIR, REFERENCE_DIR, OUTPUT_DIR
from .input_reader import read_pdf
from .source_analyzer import analyze_source
from .document_planner import create_plan
from .processor import generate_from_reference
from .validator import validate_outputs
from .output_writer import write_outputs, write_validation_report, write_sme_questions


def run_workflow() -> None:
    pdf_files = sorted(INPUT_DIR.glob("*.pdf"))
    if not pdf_files:
        raise FileNotFoundError(f"No PDF found in {INPUT_DIR}")

    source = read_pdf(pdf_files[0])
    analysis = analyze_source(source)
    plan = create_plan(analysis)
    outputs = generate_from_reference(REFERENCE_DIR)
    validation = validate_outputs(outputs)

    write_outputs(OUTPUT_DIR, outputs)
    write_validation_report(OUTPUT_DIR, validation)
    write_sme_questions(
        OUTPUT_DIR,
        outputs.get("policy_enforcement_overview.md", ""),
    )

    (OUTPUT_DIR / "workflow_metadata.json").write_text(
        json.dumps({"analysis": analysis, "plan": plan}, indent=2),
        encoding="utf-8",
    )
