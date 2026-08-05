from typing import Dict, List

REQUIRED_POLICY_TERMS = [
    "policy-manifest.yaml",
    "policy-set.yaml",
    "pipeline.yml",
    "cdp policy validate",
    "cdp pipeline run --policy-check",
    "cdp policy detect-drift --pipeline <id>",
    "Questions for Lena",
]

FORBIDDEN_POLICY_TERMS = [
    "apiVersion: cdp.policy/v1",
    "defaultViolationAction",
    "cdp policy validate --manifest",
    "cdp pipeline run --policy-check --pipeline",
]


def validate_outputs(outputs: Dict[str, str]) -> List[Dict[str, str]]:
    results: List[Dict[str, str]] = []
    policy = outputs.get("policy_enforcement_overview.md", "")
    sentinel = outputs.get("project_sentinel_strategy.md", "")

    for term in REQUIRED_POLICY_TERMS:
        results.append({
            "status": "PASS" if term in policy else "FAIL",
            "check": f"Required policy content: {term}",
        })

    for term in FORBIDDEN_POLICY_TERMS:
        results.append({
            "status": "PASS" if term not in policy else "FAIL",
            "check": f"Unsupported detail absent: {term}",
        })

    results.extend([
        {
            "status": "PASS" if "Proposed documentation structure" in sentinel else "FAIL",
            "check": "Scenario 2 hierarchy included",
        },
        {
            "status": "PASS" if "Workflow:" in sentinel else "FAIL",
            "check": "Scenario 2 workflow included",
        },
        {
            "status": "PASS" if sentinel.count("Anticipated challenge") >= 2 else "FAIL",
            "check": "Scenario 2 includes two challenges",
        },
    ])
    return results
