# Validation report

- **PASS** - Required policy content: policy-manifest.yaml
- **PASS** - Required policy content: policy-set.yaml
- **PASS** - Required policy content: pipeline.yml
- **PASS** - Required policy content: cdp policy validate
- **PASS** - Required policy content: cdp pipeline run --policy-check
- **PASS** - Required policy content: cdp policy detect-drift --pipeline <id>
- **PASS** - Required policy content: Questions for Lena
- **PASS** - Unsupported detail absent: apiVersion: cdp.policy/v1
- **PASS** - Unsupported detail absent: defaultViolationAction
- **PASS** - Unsupported detail absent: cdp policy validate --manifest
- **PASS** - Unsupported detail absent: cdp pipeline run --policy-check --pipeline
- **PASS** - Scenario 2 hierarchy included
- **PASS** - Scenario 2 workflow included
- **PASS** - Scenario 2 includes two challenges

## Review requirement

The generated files require human review before publication. Validation confirms structural and source-grounding requirements; it does not replace engineering or SME approval.
