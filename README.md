# Mini Platform

A lightweight platform for managing local development services through a unified interface.

# What

Mini Platform provides a simple dashboard to manage local development services without relying on multiple terminals and scripts.

# Why

As the number of local development projects grows,
managing them manually becomes inefficient.

Developers often switch between terminals, scripts, and commands to start or stop services.

This project aims to provide a unified interface to simplify those daily workflows.

# V1 Scope

- [ ] Define services using a local YAML configuration file
- [ ] Display configured services
- [ ] Show service status
- [ ] Mock start services
- [ ] Mock stop services

# Out of Scope

The following items are intentionally excluded from V1:

- Kubernetes integration
- Authentication and authorization
- Database support
- Distributed deployment
- Monitoring and alerting
- Plugin system
- Frontend frameworks such as React

# Tech Stack

## Backend

- FastAPI

## Frontend

- Jinja2 Templates (server-side rendering) to keep V1 simple and focused on backend capabilities.

## Container

- Podman

## Database

- None (configuration-based approach for simplicity)

## Deployment

- Local only

# Future Directions

Possible enhancements after V1:

- Execute real start/stop commands
- Support container-based services
- Add service logs
- Introduce a dedicated frontend application
- Provide plugin support