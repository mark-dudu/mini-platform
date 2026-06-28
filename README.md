# Mini Platform

Mini Platform is a lightweight local development service manager for developers.

It provides a simple dashboard for defining, viewing, and controlling local development services from one place, instead of switching between terminals, scripts, and manual commands.

The V1 goal is intentionally small: define services through a local YAML file, display configured services, show service status, and provide mock start/stop actions.

This project is designed as a practical backend-focused portfolio project. It emphasizes clear API design, configuration-driven behavior, service state modeling, simple server-side rendering, and disciplined scope control.

---

## Vision

Mini Platform aims to simplify local development workflows by giving developers a single place to understand and control their local services.

It is not intended to be a container dashboard or a Kubernetes management tool. It is a developer workflow tool first. Containers, scripts, and process managers are implementation details that may be supported later.

The long-term direction is to provide a small, practical control layer for local development environments while keeping the core experience simple and predictable.

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

---

## Example Configuration

Services are defined in `config/services.yaml`.

```yaml
services:
  - name: blog
    command: "pnpm dev"
    working_dir: "../my-blog"
    port: 3000

  - name: mini-platform
    command: "uvicorn app.main:app --reload"
    working_dir: "."
    port: 8000
```

---

## Project Structure

```text
mini-platform/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── service.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config_loader.py
│   ├── runtime/
│   │   ├── __init__.py
│   │   └── manager.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── services.py
│   └── templates/
│       └── index.html
├── config/
│   └── services.yaml
├── learning-log.md
├── README.md
├── requirements.txt
├── .gitignore
└── .gitattributes
```

### Directory Responsibilities

* `app/main.py`: FastAPI application entry point
* `app/models/`: data models for service configuration and status
* `app/core/`: core utilities such as configuration loading
* `app/runtime/`: runtime state management for mock service actions
* `app/routes/`: HTTP API routes
* `app/templates/`: server-side rendered dashboard templates
* `config/services.yaml`: local service definitions

---

## Tech Stack

### Backend

* Python
* FastAPI
* Pydantic

### Frontend

* Jinja2 templates

### Configuration

* YAML
* PyYAML

### Database

* None

### Deployment

* Local only

---

## Local Development

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open the application:

```text
http://127.0.0.1:8000
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

**V1 core functionality completed**

Progress:

* [x] Repository initialized
* [x] Initial README created
* [x] Set up Python virtual environment
* [x] Initialize FastAPI project structure
* [x] Define YAML schema
* [x] Load services from YAML configuration
* [x] Implement services API
* [x] Implement service dashboard
* [x] Mock service actions
* [x] Review and polish V1

---

## License

This project is currently intended for personal learning and experimentation.

## V2 Direction

Mini Platform V2 will introduce container-aware service definitions.

The goal is to prepare the project for managing local container-based development services. At this stage, V2 focuses on service modeling and container runtime understanding, not full container orchestration.

Planned V2 capabilities:

* Distinguish local services and container services
* Add container image and port mapping definitions
* Display service type on the dashboard
* Prepare for future Podman / Docker integration
