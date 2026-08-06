# Add a microservice to monitoring

> **Internal assessment note — remove before publication**
>
> This task is based on the illustrative Project Sentinel prototype. Validate the actual navigation, fields, permissions, and system responses before publication.

## Goal

Register a microservice in Project Sentinel, connect its telemetry source, define initial thresholds, and verify that monitoring data is available.

## Before you begin

You need:

- permission to add monitored services;
- the service name;
- the deployment environment;
- the owning team;
- the repository or service identifier, when required;
- the telemetry source;
- the service endpoint;
- initial latency and error-rate thresholds.

## Procedure

1. In the primary navigation, select **Services**.
2. Select **Add service**.
3. In **Service identity**, enter the service name.
4. Select the deployment environment.
5. Enter the owner or team.
6. Enter the repository location, when required.
7. In **Monitoring connection**, select the telemetry source.
8. Enter the service endpoint.
9. Enter the initial latency threshold.
10. Enter the initial error-rate threshold.
11. Select **Test connection**.
12. Confirm that the connection test succeeds.
13. Select **Add service**.
14. Return to **Services**.
15. Search for the new service and confirm that it appears in the inventory.
16. Open the service and confirm that health and performance information is available.
17. Open **Alerts** and create an initial alert rule.
18. Configure a notification destination and test the notification.

## Expected result

The service appears in the service inventory and begins reporting monitoring information. An initial alert rule is configured for the service.

## Next steps

- Review the service details page.
- Configure additional alerts.
- Connect Jira, Microsoft Teams, PagerDuty, or another required integration.
- Tune thresholds after observing normal service behavior.

## Related help

- Understand the Project Sentinel interface
- Troubleshoot missing monitoring data
- Create an alert rule
- Configure notification routing
