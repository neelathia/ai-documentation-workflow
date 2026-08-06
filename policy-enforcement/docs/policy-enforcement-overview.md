# Policy enforcement in Cloud Deployer Pro

## Assessment review information

> **Internal documentation note — remove before publication**
>
> Engineering email inputs form the basis of this draft. Before publication, the technical writer must:
>
> - access the Policy Enforcement feature in Cloud Deployer Pro;
> - validate the documented workflows, UI paths, commands, and expected results;
> - resolve the identified questions with engineering, security, platform, and governance subject-matter experts; and
> - finalize this overview and the related task and reference documentation.

### Working assumptions

> **Internal documentation note — confirm or revise; remove before publication**
>
> This draft uses the following assumptions because the source does not fully define policy ownership, team boundaries, or the operating model:
>
> - A centralized policy-authoring group creates, approves, versions, publishes, and maintains reusable policy manifests and policy sets.
> - Application or enablement teams consume approved policy assets and configure them for their deployment pipelines.
> - Deployment teams run policy checks and resolve deployment-time violations.
> - Operations or support teams monitor post-deployment drift and coordinate recovery.
> - The policy-engine identity remains separate from the deployment identity and uses read-only permissions for policy evaluation.
> - YAML schemas, supported values, UI fields, CLI outputs, permissions, and exact ownership boundaries require validation.
>
> Team names and responsibilities may vary. Confirm the actual ownership model before publication.
>
> For this guide, policy authoring and publication are grouped under pre-deployment because approved policy assets must exist before an application pipeline can consume them. In practice, these activities may occur as part of a separate enterprise governance lifecycle.

### Validation sources needed

> **Internal documentation note — author/reviewer communication; remove before publication**
>
> Before the related task and reference documentation can be completed, the technical writer needs access to:
>
> - the Cloud Deployer Pro Policy Enforcement UI;
> - current YAML schemas and example policy files;
> - the CLI command reference and sample outputs;
> - identity and provider-permission requirements;
> - policy ownership and approval guidance;
> - drift-event and integration configuration;
> - versioning and immutability behavior; and
> - engineering, security, platform, and operations subject-matter experts.

---

## About this guide

This guide provides an overview of the Policy Enforcement feature in Cloud Deployer Pro. It explains how policies are defined, associated with deployment pipelines, evaluated during deployment, and monitored after deployment.

Use this guide to understand:

- how policy requirements become reusable policy configuration;
- how approved policies are associated with deployment pipelines;
- how Cloud Deployer Pro evaluates and enforces policies;
- how deployed resources are monitored for drift; and
- where to find related task and configuration-reference documentation.

## Overview

Cloud Deployer Pro’s Policy Enforcement feature applies automated governance checks throughout the deployment lifecycle. It evaluates resources against approved policy requirements before and during deployment and monitors deployed resources for drift after deployment.

Policy Enforcement helps teams:

- apply governance requirements consistently across environments;
- identify noncompliant configurations before or during deployment;
- separate policy-evaluation permissions from deployment permissions; and
- detect changes from the approved post-deployment state.

Policy definitions use a simplified YAML syntax that compiles to Rego and runs through Open Policy Agent.

Depending on the configured violation response, the policy engine can:

- deny the deployment;
- issue a warning and log the violation; or
- attempt automatic remediation.

> **Note:** Automatic remediation is experimental for some resource types.

## How policy enforcement works

```text
Policy intent
     ↓
Reusable policy assets
     ↓
Pipeline policy evaluation
     ↓
Enforcement and post-deployment monitoring
```

1. Policy authors define the desired state in reusable policy manifests and policy sets.
2. Deployment teams reference approved policy assets from their pipelines.
3. Cloud Deployer Pro evaluates resources and applies the configured enforcement response.
4. After deployment, the platform monitors resources for drift from the approved state.

Policy requirements can include:

- requiring approved encryption for storage resources; and
- requiring standard tags such as `Owner`, `CostCenter`, and `Environment`.

## Policy enforcement workflow

Policy enforcement spans three stages of the deployment lifecycle:

```text
PRE-DEPLOYMENT
Author policies → Prepare the pipeline → Validate configuration
                                      ↓
DEPLOYMENT
Run policy checks → Evaluate resources → Enforce response
                                      ↓
POST-DEPLOYMENT
Detect drift → Investigate violation → Restore approved state
```

### Pre-deployment

The pre-deployment stage includes policy-authoring and deployment-readiness activities.

#### Author policy assets

As a policy author, complete the following high-level tasks:

1. **Define the desired deployment state.**

   Identify the security, compliance, cost, tagging, and environment-specific requirements that deployments must satisfy.

2. **Define reusable constraints and violation responses.**

   Record the required state, constraints, optional conditions, and enforcement responses in `policy-manifest.yaml`.

3. **Create modular policy files.**

   Separate reusable policies into domains such as security, compliance, or cost when modular ownership or reuse is required.

4. **Compose modular policies into a policy set.**

   Reference approved modular policy files from `policy-set.yaml`.

5. **Review, test, approve, and version the policy assets.**

6. **Publish the approved policy manifest or policy set.**

   Make the approved policy assets available to application, enablement, release, or deployment teams.

For schemas, supported fields, values, and examples, refer to the related policy-authoring and configuration-reference documentation.

#### Prepare the deployment pipeline

As a developer or deployment-team member, complete the following high-level tasks:

1. **Identify the approved policy asset.**

   Identify the approved policy manifest or policy set required for the deployment.

2. **Configure or select the policy-engine identity.**

   The policy-engine identity:

   - uses granular, read-only permissions;
   - remains separate from the deployment identity;
   - can support cross-account or cross-cloud role assumption; and
   - includes only the permissions needed to evaluate resource state.

   In Cloud Deployer Pro, the source identifies the following configuration location:

   **Settings > Cloud Integrations > Policy Engine IAM Role**

3. **Reference the approved policy asset from the pipeline.**

   Reference the approved policy manifest or policy set from the top-level `policies` block in `pipeline.yml`.

4. **Specify the applicable deployment stages.**

5. **Configure permitted stage-specific overrides.**

6. **Validate the policy configuration.**

   ```bash
   cdp policy validate
   ```

Refer to the related task guides for complete steps, YAML syntax, expected results, and troubleshooting information.

### Deployment

#### Run a deployment with policy checks

As a developer or deployment-team member:

1. Run the deployment with policy checks enabled.

   ```bash
   cdp pipeline run --policy-check
   ```

2. Review the policy-evaluation result.

During the pipeline run, Cloud Deployer Pro:

1. loads the approved policy manifest or policy set referenced by `pipeline.yml`;
2. applies the configured deployment stage and permitted overrides;
3. assumes the read-only policy-engine identity;
4. evaluates the current resource state against the desired state; and
5. applies the configured enforcement response.

The policy engine can:

- deny the deployment;
- issue a warning and log the violation; or
- attempt automatic remediation for supported resource types.

> **Note:** Automatic remediation is experimental for some resource types.

Review violation details and Rego evaluation traces when available. Resolve failed evaluations before continuing the deployment.

Refer to *Run a deployment with policy checks* and *Troubleshoot policy violations* for detailed instructions.

### Post-deployment

#### Detect and resolve policy drift

As an operations or support-team member:

1. **Review drift events.**

   Review drift events received through supported integrations, including webhooks, Amazon SNS, and Amazon SQS.

2. **Run manual drift detection when required.**

   ```bash
   cdp policy detect-drift --pipeline <id>
   ```

3. **Review the affected resource and violated constraint.**

4. **Compare the current resource state with the approved policy state.**

5. **Restore the approved state.**

   Restore the approved configuration or rerun the deployment pipeline.

6. **Preserve the policy version used for evaluation and investigation.**

Refer to *Detect and resolve policy drift* for detailed instructions.

## Related documentation

This overview explains the end-to-end policy-enforcement workflow. Refer to the related task and reference documentation for implementation details.

### Task guides

- *Author and publish policy assets*
- *Prepare a deployment pipeline for policy enforcement*
- *Run a deployment with policy checks*
- *Troubleshoot policy violations*
- *Detect and resolve policy drift*

### Configuration reference

- *policy-manifest.yaml reference*
- *policy-set.yaml reference*
- *pipeline.yml policies block reference*
- *Policy-engine identity configuration reference*
- *Policy Enforcement CLI reference*

---

## Questions for Lena

> **Internal documentation note — clarification required; remove before publication**
>
> The following questions identify the information needed to validate this overview and create the related task and reference documentation.

### Ownership and operating model

1. Which team creates, approves, publishes, versions, and maintains policy manifests and policy sets?
2. Can application teams create or extend policies, or can they only consume approved enterprise policies?
3. Which settings can application teams override?
4. Which enterprise controls are protected from override?
5. Which roles own policy authoring, pipeline configuration, deployment response, and drift remediation?
6. Where is the approved ownership and operating model documented?

### Policy artifacts and configuration

1. Where can the current schemas and examples for `policy-manifest.yaml` and `policy-set.yaml` be found?
2. What syntax does the top-level `policies` block use in `pipeline.yml`?
3. How do deployment teams discover and select approved policy assets?
4. How are approved policy assets versioned and published?
5. Where are the supported fields, values, conditions, and validation rules documented?

### Identity and permissions

1. What UI fields appear under **Settings > Cloud Integrations > Policy Engine IAM Role**?
2. Which provider-specific permissions are required for the read-only policy-engine identity?
3. How does cross-account or cross-cloud role assumption work?
4. Which roles are permitted to configure or select the policy-engine identity?
5. Where can the approved identity and permission model be found?

### Commands and enforcement behavior

1. What output does `cdp policy validate` return for successful and failed validation?
2. What output does `cdp pipeline run --policy-check` return for deny, warn, and auto-remediate responses?
3. Which failure messages appear when role assumption or policy evaluation fails?
4. Is `cdp policy enforc` incomplete or mistyped in the source material?
5. Which policy types support automatic remediation, and what limitations apply?
6. Where is the current CLI command reference maintained?

### Drift monitoring and versioning

1. Which webhook, Amazon SNS, and Amazon SQS configurations are supported for drift events?
2. How are immutable policy versions stored, identified, and retrieved?
3. How is the policy version associated with an evaluation or drift event?
4. Which team receives and resolves drift notifications?
5. Where are drift-monitoring and recovery procedures documented?
