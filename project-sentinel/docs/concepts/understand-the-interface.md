# Understand the Project Sentinel interface

Project Sentinel uses primary navigation for product-wide activities and service-level tabs for investigation and configuration.

## Primary navigation

- **Overview** — Review monitoring health across services.
- **Services** — Search, filter, add, and open monitored services.
- **Alerts** — Configure alert conditions and notification routing.
- **Incidents** — Review grouped operational problems. This is a proposed supporting view.
- **Integrations** — Connect telemetry, ticketing, collaboration, and automation systems.
- **Settings** — Manage shared administrative settings. This is a proposed area.
- **API documentation** — Review programmatic interfaces and examples.

## Service-level navigation

When you open a service, use the tabs to review:

- **Overview** — Current health and key metrics.
- **Dependencies** — Upstream and downstream services.
- **Alerts** — Alerts affecting the service.
- **Configuration** — Service identity, environment, ownership, and telemetry settings.

## Health states

- **Healthy** — The service is operating within configured limits.
- **Warning** — One or more indicators require attention.
- **Critical** — The service has a serious active condition requiring investigation.

> Exact health-state logic must be confirmed with the product team.
