# Mini Platform

A lightweight platform for managing local development services through a unified interface.

## Vision

Mini Platform aims to simplify the daily workflows of developers by providing a single place to manage local development services.

Instead of switching between terminals, scripts, and commands, developers can view and control their services from one dashboard.

Mini Platform is not a container dashboard. It is a developer workflow tool, where containers are only one possible implementation detail.

---

## Why

As the number of local development projects grows, managing services manually becomes inefficient.

Developers often need to:

* Open multiple terminal windows
* Remember different startup commands
* Run custom scripts
* Check whether services are running
* Stop and restart services during development

These repetitive tasks interrupt focus and increase cognitive load.

Mini Platform aims to reduce that friction by providing a simple and unified experience.

---

## V1 Goals

Build a local service management dashboard for personal use.

The first version focuses on validating the workflow and user experience before integrating with real service execution.

---

## V1 Scope

The following capabilities are planned for V1:

* [ ] Define services using a local YAML configuration file
* [ ] Display configured services
* [ ] Show service status
* [ ] Mock start services
* [ ] Mock stop services

### Example Configuration

```yaml
services:
  redis:
    command: "podman start redis"

  blog:
    command: "pnpm dev"

  api:
    command: "./start.sh"
```

---

## Out of Scope

The following items are intentionally excluded from V1:

* Kubernetes integration
* Authentication and authorization
* Database support
* Distributed deployment
* Monitoring and alerting
* Plugin system
* Dedicated frontend frameworks
* Real command execution

Keeping V1 intentionally small helps validate the core workflow quickly.

---

## Tech Stack

### Backend

* FastAPI

### Frontend

* Jinja2 Templates (server-side rendering)

### Configuration

* YAML

### Container Runtime

* Podman (future integration)

### Database

* None

### Deployment

* Local only

---

## Future Directions

Possible enhancements after V1 include:

* Execute real start and stop commands
* Support Podman-managed containers
* View service logs
* Restart services
* Introduce a dedicated frontend application
* Add plugin support
* Support Kubernetes environments

---

## Development Principles

This project follows a few guiding principles:

* Start simple and iterate quickly.
* Prefer clarity over completeness.
* Focus on solving real workflow problems.
* Avoid unnecessary complexity in early versions.
* Treat V1 as a learning and validation phase.

---

## Status

Current phase:

**Planning and foundation setup**

Progress:

* [x] Repository initialized
* [x] Initial README created
* [ ] Define YAML schema
* [ ] Implement service dashboard
* [ ] Mock service actions
* [ ] Complete V1

---

## License

This project is currently intended for personal learning and experimentation.
