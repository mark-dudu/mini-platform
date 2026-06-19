# Mini Platform

Mini Platform is a lightweight local development service manager for developers.

It provides a simple dashboard for defining, viewing, and controlling local development services from one place, instead of switching between terminals, scripts, and manual commands.

The V1 goal is intentionally small: define services through a local YAML file, display configured services, show service status, and provide mock start/stop actions.

This project is designed as a practical backend-focused portfolio project. It emphasizes clear API design, configuration-driven behavior, service state modeling, simple server-side rendering, and disciplined scope control.

## Vision

Mini Platform aims to simplify local development workflows by giving developers a single place to understand and control their local services.

It is not intended to be a container dashboard or a Kubernetes management tool. It is a developer workflow tool first. Containers, scripts, and process managers are implementation details that may be supported later.

The long-term direction is to provide a small, practical control layer for local development environments while keeping the core experience simple and predictable.

---

## Why

As the number of local development projects grows, managing services manually becomes inefficient.
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

Build a local service management dashboard that validates the core workflow without executing real system commands.

V1 focuses on four things:

* Reading service definitions from a local YAML configuration file
* Rendering configured services in a simple dashboard
* Modeling service status clearly
* Providing mock start/stop actions to validate the API and UI flow

Real command execution is intentionally excluded from V1 to keep the first milestone small, safe, and easy to complete.

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

### Database

* None

### Deployment

* Local only

---

## Future Directions

Possible enhancements after V1 include:
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
