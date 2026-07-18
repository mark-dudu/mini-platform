# Mini Platform

Mini Platform is a lightweight development service manager for local processes and Podman-managed containers.

It provides a simple dashboard for defining and viewing development services from one place, instead of switching between terminals, scripts, and container commands.

Local services currently use mock start/stop controls, while container services expose read-only runtime status through Podman.

V1 established the core workflow with YAML-based service definitions, a dashboard, service status modeling, and mock start/stop actions.

V2 is extending that model with container-aware configuration and read-only Podman runtime integration.

This project is designed as a practical backend-focused portfolio project. It emphasizes clear API design, configuration-driven behavior, service state modeling, simple server-side rendering, and disciplined scope control.

---

## Vision

Mini Platform aims to simplify local development workflows by giving developers a single place to understand and control their local services.

It is not intended to be a general-purpose container dashboard or Kubernetes management tool. It is a developer workflow tool first.

Local processes, containers, scripts, and future runtime integrations are implementation mechanisms behind a unified service model.

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

## Project Status

Current phase:

**V2 in progress: read-only Podman runtime integration**

### V1 Completed

Mini Platform V1 has been completed as a mock local service manager.

Completed capabilities:

* Load service definitions from a local YAML configuration file
* Expose service data through `/api/services`
* Display configured services through a simple dashboard
* Show service status
* Provide mock start / stop controls

### V2 Progress

Completed:

* Added explicit local and container service types
* Added type-specific configuration validation
* Added container metadata support
* Added mixed local and container configuration
* Added a read-only Podman status adapter
* Integrated real container status into the API and dashboard
* Preserved mock controls for local services

Current limitations:

* Container services are read-only
* Real container start and stop actions are not implemented
* Docker is not supported

### Current Runtime Behavior

| Service type | Status source | Start/stop behavior |
| --- | --- | --- |
| `local` | In-memory mock state | Mock actions |
| `container` | Podman inspect | Read-only |

Container services currently expose real runtime status but do not execute real start or stop commands.

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

  - name: demo-nginx
    type: container
    container_name: "mini-platform-nginx"
    image: "docker.io/library/nginx:alpine"
    host_port: 8080
    container_port: 80
```

Local services require `command` and `working_dir`. Container services require `container_name` and `image`.

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
│   │   ├── manager.py
│   │   └── podman.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── services.py
│   └── templates/
│       └── index.html
├── config/
│   └── services.yaml
├── tests/
│   ├── test_api.py
│   ├── test_config_loader.py
│   ├── test_podman.py
│   ├── test_runtime_manager.py
│   └── test_service_models.py
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
* `app/runtime/manager.py`: type-aware service status coordination and mock state handling for local services
* `app/runtime/podman.py`: read-only adapter for querying Podman container status
* `app/routes/`: HTTP API routes
* `app/templates/`: server-side rendered dashboard templates
* `config/services.yaml`: local and container service definitions
* `tests/`: unit and integration tests for models, configuration, runtime behavior, API routes, and dashboard rendering

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
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the test suite:

```bash
python -m pytest
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open the application:

```text
http://127.0.0.1:8000
```

### Podman Requirement

Container status integration requires the Podman CLI to be installed and available on the host:

```bash
podman --version
```

Mini Platform currently queries Podman in read-only mode. Docker is not supported.

If Podman is unavailable, the container status is reported as `unavailable`. If a configured container does not exist, the status is reported as `not_found`.

---

## V1 Out of Scope

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

Possible enhancements include:

* Implement real Podman start and stop actions
* Add explicit runtime action error handling
* View service logs
* Restart services
* Detect and report port conflicts
* Support additional container runtimes when justified
* Introduce a dedicated frontend application
* Add plugin support
* Explore Kubernetes integration in a later phase

---

## Development Principles

This project follows a few guiding principles:

* Start simple and iterate quickly.
* Prefer clarity over completeness.
* Focus on solving real workflow problems.
* Avoid unnecessary complexity in early versions.
* Treat V1 as a learning and validation phase.
