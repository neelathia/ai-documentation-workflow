from typing import Dict


def create_plan(analysis: Dict[str, object]) -> Dict[str, str]:
    return {
        "scenario_1_document_type": "feature overview with planned child procedures",
        "scenario_2_document_type": "documentation strategy",
        "reason": (
            "The source supports feature concepts, lifecycle, artifacts, and commands, "
            "but does not provide enough verified implementation detail for complete procedures."
        ),
    }
