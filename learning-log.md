# Learning Log

## Day 1 - Project Initialization (2026-06-13)

### Goal

* Initialize the Mini Platform project.
* Define the project vision and V1 scope.
* Establish the documentation and workflow standards for future development.

### Completed

* Created the Mini Platform repository structure.
* Initialized the Git repository.
* Created the initial project documents:

  * `README.md`
  * `learning-log.md`
  * `.gitignore`
* Established a consistent Learning Log convention shared across projects.
* Documented the project's vision, scope, technology choices, and future directions in `README.md`.

### Issues Encountered

* It was tempting to continue refining the README indefinitely.
* Determining what not to build was more difficult than choosing what to build.

### Key Learnings

* A clear scope is more valuable than an ambitious feature list.
* Defining Out of Scope items early helps prevent unnecessary complexity.
* README documents should guide implementation rather than describe every possible future idea.
* Project initialization is not administrative work; it is a critical design activity that shapes future decisions.
* Consistent documentation practices reduce cognitive overhead when managing multiple projects.

### Next

* Initialize the FastAPI project structure.
* Create the first application entry point.
* Verify that the development environment runs successfully.
* Begin implementing the configuration-driven service model defined in V1 Scope.

## Day 2 - FastAPI Foundation Setup (2026-06-22)

### Goal

* Set up the FastAPI foundation for Mini Platform.
* Establish a clean Python development environment.
* Prepare the project structure for configuration-driven service management.

### Completed

* Reviewed the overall project architecture before writing feature code.
* Updated `README.md` to include local development setup, project structure, and V1 scope.
* Created a Python virtual environment using `.venv`.
* Added `requirements.txt` for project dependencies.
* Initialized the FastAPI project structure.
* Added core directories for:

  * `models`
  * `core`
  * `runtime`
  * `routes`
  * `templates`
* Prepared the project for future YAML configuration loading and mock service state management.
* Fixed an incomplete initialization commit by amending the previous commit and updating the remote branch safely.

### Issues Encountered

* Some project skeleton files were staged but not included in the first initialization commit.
* The issue was resolved by using `git commit --amend --no-edit` and pushing with `--force-with-lease`.
* The initial architecture needed review before implementation to avoid creating an unclear `services.py` file with too many responsibilities.

### Key Learnings

* Python projects should use a virtual environment from the beginning to isolate dependencies.
* README should be updated when project infrastructure decisions change.
* A small project still benefits from clear separation of responsibilities.
* `main.py`, `routes`, `models`, `core`, and `runtime` should have distinct roles.
* `git commit --amend` is useful when the latest commit missed files that belong to the same logical change.
* `--force-with-lease` is safer than plain `--force` when updating a remote branch after amending a pushed commit.

### Next

* Refine `config/services.yaml`.
* Define the initial YAML schema for local service definitions.
* Implement configuration loading logic in `app/core/config_loader.py`.
* Verify that service definitions can be loaded successfully by the backend.

## Day 3 - Load Services from YAML Config (2026-06-23)

### Goal

* Load local service definitions from a YAML configuration file.
* Convert raw YAML data into structured Python objects.
* Verify that the backend can access configured services.

### Completed

* Added `ServiceConfig` model using Pydantic.
* Implemented `load_services()` in `app/core/config_loader.py`.
* Loaded service definitions from `config/services.yaml`.
* Verified the result through the FastAPI root endpoint.
* Confirmed that configured services are returned as structured JSON.

### Issues Encountered

* The service list is currently exposed through the root endpoint for temporary verification.
* A dedicated `/api/services` endpoint has not been implemented yet.

### Key Learnings

* YAML configuration keeps service definitions separate from application logic.
* Pydantic models help validate and structure configuration data.
* Implementing configuration loading before API design keeps the development flow clear.
* Temporary verification endpoints are useful during early development, but should be cleaned up later.

### Next

* Add a dedicated `GET /api/services` endpoint.
* Introduce service status in the API response.
* Keep the root endpoint simple and move service listing logic into the routes layer.

## Day 4 - Add Services API (2026-06-25)

### Goal

* Add a dedicated API endpoint for listing configured services.
* Move service listing logic out of the root endpoint.
* Introduce a simple service view model with default status.

### Completed

* Added `ServiceView` model for API responses.
* Created `GET /api/services/` endpoint.
* Loaded service definitions from `config/services.yaml`.
* Added default `status: stopped` for each configured service.
* Registered the services router in `app/main.py`.
* Restored the root endpoint as a simple health check.

### Issues Encountered

* FastAPI uses a trailing slash for the current `/api/services/` route.
* The service status is still static and does not reflect runtime state yet.

### Key Learnings

* Separating configuration data from API response models makes the code easier to evolve.
* A dedicated routes layer keeps `main.py` focused on application setup.
* Static service status is acceptable for V1 because real command execution is intentionally out of scope.
* The API response format now provides a foundation for the future dashboard and mock service actions.

### Next

* Build a simple dashboard page to display configured services.
* Show service name, command, port, and status in the UI.
* Keep the UI minimal and server-rendered with Jinja2.