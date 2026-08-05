from pathlib import Path
from typing import Dict, List


def write_outputs(output_dir: Path, outputs: Dict[str, str]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, content in outputs.items():
        (output_dir / filename).write_text(content, encoding="utf-8")


def write_validation_report(output_dir: Path, results: List[Dict[str, str]]) -> None:
    lines = ["# Validation report", ""]
    for result in results:
        lines.append(f"- **{result['status']}** - {result['check']}")
    lines.extend([
        "",
        "## Review requirement",
        "",
        "The generated files require human review before publication. Validation confirms structural and source-grounding requirements; it does not replace engineering or SME approval.",
    ])
    (output_dir / "validation_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_sme_questions(output_dir: Path, policy_document: str) -> None:
    heading = "## Questions for Lena"
    questions = "# SME review questions\n\n"
    if heading in policy_document:
        questions += policy_document.split(heading, 1)[1].strip() + "\n"
    else:
        questions += "The generated document does not contain an SME question section.\n"
    (output_dir / "sme_review_questions.md").write_text(questions, encoding="utf-8")
