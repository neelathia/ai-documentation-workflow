from pathlib import Path
from typing import Dict


def generate_from_reference(reference_dir: Path) -> Dict[str, str]:
    """Create source-grounded drafts from approved reference outputs.

    This portfolio implementation demonstrates the repeatable packaging and
    validation workflow. In a production AI implementation, the same output
    contracts can be populated by an approved language model using the source,
    instructions, templates, and document plan.
    """
    return {
        path.name: path.read_text(encoding="utf-8")
        for path in sorted(reference_dir.glob("*.md"))
    }
