# Project Sentinel Documentation Strategy

> **Internal assessment note — remove before publication**
>
> This strategy and its supporting documentation are based on the illustrative Project Sentinel prototype created for the assessment. Product navigation, field names, permissions, workflows, and system behavior must be validated against the actual product before publication.

## Purpose

This strategy defines how Project Sentinel documentation will help developers, platform teams, operations users, and administrators monitor microservices, investigate performance problems, configure alerting, connect integrations, and automate common activities.

The documentation uses the prototype as the assumed product interface for this assessment.

## Documentation delivery model

Project Sentinel help is delivered through a hybrid model:

1. **Contextual help in the product** — A Help action opens guidance relevant to the current page.
2. **Field-level help** — Tooltips explain unfamiliar fields, thresholds, and evaluation settings.
3. **Standalone Help Center** — Users can search and browse the complete documentation.
4. **Portable outputs** — Core documents can also be exported to PDF for review and email distribution.

The same topic should be authored once and surfaced through multiple entry points.

## Primary organization: task-based

The primary Help Center structure is task-based because users typically seek help to accomplish a goal or resolve a problem.

### Get started

- Understand Project Sentinel
- Understand the interface
- Understand health states and severity
- Understand roles and permissions
- Set up your first monitored service

### Monitor and investigate

- View portfolio health
- Find a monitored service
- Investigate degraded service performance
- Review service dependencies
- Review active alerts and recent changes

### Configure monitoring

- Add a microservice to monitoring
- Connect a telemetry source
- Configure service ownership and environment
- Define initial thresholds
- Test monitoring connectivity
- Update service configuration

### Configure alerts

- Create an alert rule
- Define thresholds and evaluation windows
- Assign severity
- Configure notification routing
- Test an alert
- Tune noisy alerts

### Configure integrations

- Connect the internal logging system
- Connect Jira
- Connect Microsoft Teams
- Connect PagerDuty
- Configure a webhook
- Test and troubleshoot integrations

### Operate and troubleshoot

- Troubleshoot missing monitoring data
- Troubleshoot excessive alerts
- Investigate a degraded service
- Resolve an integration failure
- Diagnose permission problems

### Automate with the API

- Authenticate
- Retrieve services and health
- Manage alert rules
- Manage integrations
- Handle errors and rate limits

## Alternate navigation: role-based

The same topics are also available through role-based landing pages.

### Developer or application owner

Typical tasks include adding a service, reviewing service health, investigating performance, reviewing dependencies, and configuring service-level alerts.

### Platform or enablement engineer

Typical tasks include standardizing service onboarding, configuring shared integrations, defining reusable monitoring patterns, troubleshooting telemetry, and automating with the API.

### Operations or production-support user

Typical tasks include reviewing active issues, investigating degraded services, correlating alerts with recent changes, and coordinating response.

### Administrator

Typical tasks include managing access, shared integrations, API credentials, retention, and system-level settings.

> **Internal assumption — confirm before publication**
>
> These role groupings are inferred from the proposed workflows. Confirm actual roles, permissions, and ownership with the product team.

## Alternate navigation: product area

Users can also browse by the interface area they are currently using:

- Overview
- Services
- Service details
- Alerts
- Incidents
- Integrations
- Settings
- API documentation

## Contextual help pattern

Each product page includes a Help action. The contextual panel contains:

- a short description of the page;
- common tasks;
- related help topics;
- a link to the complete Help Center.

Field-level tooltips are used only for terms that need immediate clarification, such as telemetry source, latency threshold, error-rate threshold, evaluation window, and escalation delay.

## Topic types

| Topic type | Purpose |
|---|---|
| Overview | Introduce a product area and connect related topics |
| Concept | Explain what something is and why it matters |
| Task | Explain how to complete a user goal |
| Reference | Define fields, statuses, API elements, and supported values |
| Troubleshooting | Diagnose and resolve a problem |

## Fully developed workflow

The assessment workflow is **Add a microservice to monitoring**.

It demonstrates how a developer:

1. Opens **Services**.
2. Selects **Add service**.
3. Enters service identity and ownership information.
4. Selects the telemetry source.
5. Enters the service endpoint.
6. Defines initial latency and error-rate thresholds.
7. Tests the connection.
8. Adds the service.
9. Verifies that the service appears in the inventory.
10. Opens the service and confirms monitoring data.
11. Creates an initial alert rule and notification route.

See [Add a microservice to monitoring](../tasks/add-a-microservice-to-monitoring.md).

## Anticipated challenge 1: Monitoring data does not appear

This challenge prevents users from validating service health and makes every later dashboard or alert decision unreliable.

Documentation response:

- state prerequisites clearly;
- explain telemetry and endpoint requirements;
- provide connection-testing steps;
- identify required permissions;
- show how to verify environment and service identity;
- provide diagnostic and escalation information.

## Anticipated challenge 2: Alerts are noisy or ineffective

Poor thresholds can create alert fatigue or fail to detect meaningful degradation.

Documentation response:

- explain threshold selection;
- explain evaluation windows and severity;
- show how to test a rule;
- explain notification routing;
- document tuning, suppression, and review of alert history.

## Prototype and source status

The prototype distinguishes:

- assessment-confirmed components;
- assessment-confirmed capabilities represented through illustrative workflows;
- market-informed supporting views.

This provenance must remain visible during review and be removed or replaced after product validation.
