import re
from typing import Dict, List


def analyze_source(document: Dict[str, object]) -> Dict[str, object]:
    text = "\n".join(page["text"] for page in document["pages"])
    commands = sorted(set(re.findall(r"cdp\s+[a-zA-Z0-9_<>&.-]+(?:\s+[a-zA-Z0-9_<>&.-]+)*", text)))
    filenames = sorted(set(re.findall(r"[A-Za-z0-9_-]+\.(?:yaml|yml)", text)))
    interface_paths = []
    if "Settings" in text and "Cloud Integrations" in text:
        interface_paths.append("Settings > Cloud Integrations > Policy Engine IAM Role")

    confirmed = []
    for phrase in [
        "policy enforcement",
        "Open Policy Agent",
        "drift detection",
        "automatic remediation",
        "Project Sentinel",
    ]:
        if phrase.lower() in text.lower():
            confirmed.append(phrase)

    return {
        "source_file": document["filename"],
        "commands": commands,
        "filenames": filenames,
        "interface_paths": interface_paths,
        "confirmed_topics": confirmed,
        "missing_execution_details": [
            "complete YAML schemas",
            "complete UI navigation and field names",
            "provider-specific permissions",
            "validated command output",
            "failure and recovery behavior",
        ],
    }
