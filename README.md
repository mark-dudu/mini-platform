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

The following capabilities have been completed in V1:

* [x] Define services using a local YAML configuration file
* [x] Display configured services
* [x] Show service status
* [x] Mock start services
* [x] Mock stop services

---

## Example Configuration

Services are defined in `config/services.yaml`.

```yaml
services:
  - name: blog
    type: local
    command: "pnpm dev"
    working_dir: "../my-blog"
    port: 3000

  - name: mini-platform
    type: local
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

* Local development
* Cloud server used as a Linux / container experiment environment

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

* Add container service metadata
* Support Podman-managed containers
* Execute real start and stop commands
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

## Project Status

Current phase:

**V2 preparation: container-aware service modeling**

### V1 Completed

Mini Platform V1 has been completed as a mock local service manager.

Completed capabilities:

* Load service definitions from a local YAML configuration file
* Expose service data through `/api/services`
* Display configured services through a simple dashboard
* Show service status
* Provide mock start / stop controls

### V2 Preparation

V2 preparation has started.

Completed preparation work:

* Added a `type` field to service definitions
* Marked existing services as `local`
* Displayed service type in the API and dashboard
* Practiced basic Podman commands locally
* Installed and verified Podman on a cloud server
* Verified a simple containerized HTTP service on the cloud server

Next step:

* Add container service metadata, including image, container name, and port mappings
* Keep container support as metadata first before implementing real runtime control