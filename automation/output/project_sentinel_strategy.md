# Project Sentinel documentation strategy

## Proposed documentation structure

### Get started

- Project Sentinel overview
- Access and prerequisites
- Quick start: Monitor a first microservice
- Core concepts

### Dashboard

- Review service health
- Investigate performance issues
- Review security vulnerabilities

### Service configuration

- Add a service
- Configure monitoring thresholds
- Edit or remove a monitored service

### Alerting rules

- Create an alerting rule
- Configure email, Teams, or PagerDuty notifications
- Manage alert severity and routing

### Integrations

- Connect Jira for incident tracking
- Connect the internal logging system
- Troubleshoot integration issues

### API reference

- Authentication
- Service, alert, and integration endpoints
- Request and response examples
- Error responses

### Troubleshooting

- Monitoring data does not appear
- Alerts do not trigger
- Notifications do not arrive
- Integration connections fail

## Organizational rationale

The structure follows the sequence a developer is likely to use Project Sentinel: understand the tool, add a service, review health and vulnerability information, configure alerts, connect existing tools, and automate through the API.

Task-oriented sections keep procedures close to the product component where the work occurs. The troubleshooting section organizes recovery information by observable symptom so a developer can find guidance without first identifying the internal cause.

## Workflow: Set up monitoring for a new microservice

### Goal

Add a microservice to Project Sentinel, configure monitoring thresholds, and create an initial alert.

### Prerequisites

Confirm that you have:

- access to Project Sentinel;
- permission to create or edit service configurations;
- the service name and environment;
- the metrics and security checks required by the service team; and
- a notification destination.

### Procedure

1. Open **Service Configuration**.
2. Add the microservice.
3. Enter the service and environment details.
4. Select the performance metrics and security checks to monitor.
5. Configure initial thresholds.
6. Save the service configuration.
7. Open **Dashboard** and confirm that the service appears.
8. Open **Alerting Rules**.
9. Create an alerting rule for a high-impact event, such as sustained high CPU usage or a critical vulnerability.
10. Select email, Teams, or PagerDuty as the notification destination.
11. Confirm that monitoring data and notifications work as expected.

### Documentation design

Present this workflow as one task page so a developer can complete the initial setup without moving among several component sections.

The topic should include:

- a clear goal;
- prerequisites;
- numbered steps with exact interface labels;
- a final verification step; and
- links to threshold guidance, advanced alerting, integrations, and troubleshooting.

## Anticipated challenge 1: Noisy or ineffective alert thresholds

A threshold that is too sensitive can generate excessive notifications. A threshold that is too broad can hide an important performance issue or vulnerability.

Address this challenge with:

- threshold-selection guidance by metric or event type;
- recommended starting points labeled as examples;
- a procedure for reviewing and adjusting thresholds; and
- links from the service-configuration and alerting tasks.

This challenge matters because poor thresholds reduce confidence in Sentinel alerts.

## Anticipated challenge 2: Integration connection failures

Jira and internal logging integrations depend on credentials, permissions, and connection settings. Generic failure messages can make the cause difficult to identify.

Address this challenge with:

- integration prerequisites;
- authentication and permissions guidance;
- an error-message table that maps failures to likely causes and corrective actions; and
- links to troubleshooting from each integration task.

This challenge matters because the failure can occur outside Sentinel, making the cause difficult to locate without explicit guidance.
