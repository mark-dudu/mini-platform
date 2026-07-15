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

## Day 5 - Display Configured Services (2026-06-25)

### Goal

* Build a simple server-rendered dashboard.
* Display configured services from the YAML configuration file.
* Keep the UI minimal and focused on service visibility.

### Completed

* Updated the root endpoint to render a Jinja2 template.
* Added `index.html` as the initial dashboard page.
* Displayed service name, command, working directory, port, and status.
* Verified that the dashboard and `/api/services/` endpoint both work.

### Issues Encountered

* The initial `TemplateResponse` call used the older positional style and failed with the current Starlette version.
* The issue was fixed by using explicit keyword arguments: `request`, `name`, and `context`.
* The root page and API route currently duplicate service view construction logic.
* The dashboard is intentionally minimal and does not include styling or actions yet.

### Key Learnings

* Jinja2 is sufficient for the V1 dashboard.
* Server-side rendering keeps the frontend simple for this stage.
* `TemplateResponse` behavior can vary by framework version, so explicit keyword arguments improve readability and compatibility.
* Displaying configuration data in the UI makes the platform concept more concrete.
* Duplication is acceptable temporarily, but should be cleaned up when runtime state management is introduced.

### Next

* Add mock start and stop controls.
* Introduce a runtime manager to handle service status changes.
* Keep real command execution out of V1.

## Day 6 - Add Mock Service Controls (2026-06-26)

### Goal

* Add mock start and stop actions for configured services.
* Introduce runtime state management without executing real commands.
* Allow the dashboard to control service status.

### Completed

* Added an in-memory runtime manager for service status.
* Implemented mock start and stop logic.
* Added API endpoints for starting and stopping services.
* Updated the dashboard with Start and Stop buttons.
* Verified that service status can change between `running` and `stopped`.
* Kept real command execution out of V1.

### Issues Encountered

* The initial dashboard buttons returned JSON responses from API endpoints.
* This was improved by adding dashboard-specific form routes that redirect back to the homepage.

### Key Learnings

* Runtime state should be separated from static service configuration.
* Mock actions are useful for validating API and UI flow before implementing real process management.
* Keeping real command execution out of V1 makes the system safer and easier to complete.
* Redirecting after form submission provides a better dashboard experience than returning raw JSON.

### Next

* Review Mini Platform V1 against the original scope.
* Update README status.
* Prepare a short project summary for the Blog Projects section.

## Day 7 - V1 Verification and V2 Direction (2026-06-28)

### Goal

Verify that Mini Platform V1 still works correctly and define the direction for V2 container-aware service modeling.

### Completed

* Verified the current Git status.
* Started the Mini Platform application locally.
* Checked that services can be loaded from `services.yaml`.
* Verified that `/api/services` returns the configured services.
* Verified that the dashboard displays service information.
* Confirmed that mock start / stop controls work.
* Defined the V2 direction around container-aware service definitions.

### Issues Encountered

* None for now.

### Key Learnings

* V1 should remain stable before expanding the project scope.
* V2 should first improve service modeling before integrating real container runtime operations.
* Container support should be introduced incrementally through configuration design, not by jumping directly into process control or orchestration.

### Next

* Add a `type` field to service definitions.
* Support `local` and `container` service metadata.
* Display service type in the API and dashboard.

## Day 8 - Add Service Type Field (2026-06-29)

### Goal

Add a service type field to distinguish local services from future container-based services.

### Completed

* Added `type: local` to existing service definitions in `services.yaml`.
* Updated the service model to include a `type` field.
* Verified that `/api/services` returns the service type.
* Updated the dashboard to display the service type.
* Confirmed that existing mock start / stop controls still work.

### Issues Encountered

* None for now.

### Key Learnings

* Adding a `type` field is a small but important modeling step.
* Service modeling should evolve before runtime integration.
* Keeping existing local services working helps avoid breaking V1 while preparing for V2.

### Next

* Add container service metadata such as image, container name, and port mappings.
* Keep container support as metadata first before implementing real Podman or Docker operations.

## Day 9 - Container Runtime Basics (2026-06-30)

### Goal

Practice basic container runtime commands and understand the core concepts needed for future Mini Platform container integration.

### Completed

* Verified that Podman is available locally.
* Ran the hello-world container successfully.
* Checked running and stopped containers with `podman ps` and `podman ps -a`.
* Listed local images with `podman images`.
* Ran an nginx container with port mapping.
* Verified nginx through `curl http://localhost:8080`.
* Checked container logs with `podman logs`.
* Stopped and removed the nginx demo container.

### Issues Encountered

* None.

### Key Learnings

* An image is a reusable template for creating containers.
* A container is a running or stopped instance created from an image.
* `podman ps` shows running containers, while `podman ps -a` shows all containers, including stopped ones.
* Port mapping connects a host port to a container port, such as `8080:80`.
* Container logs can become a useful data source for future service diagnostics in Mini Platform.
* Container runtime integration should come after clear service modeling.

### Next

* Add container service metadata such as image, container name, and port mappings.
* Keep the first container-related implementation focused on metadata, not real runtime control.

## Day 10 - Cloud Server Container Runtime Test (2026-07-04)

### Goal

Install Podman on the cloud server and verify that the server can be used as a lightweight container experiment environment.

### Completed

* Installed Podman on the Ubuntu cloud server.
* Verified Podman with `podman --version` and `podman info`.
* Confirmed that Podman runs in rootless mode under the normal user.
* Ran `quay.io/podman/hello` successfully.
* Checked containers and images with `podman ps`, `podman ps -a`, and `podman images`.
* Started a long-running container with port mapping.
* Verified a BusyBox-based HTTP server through `curl http://localhost:8080`.
* Stopped and removed test containers.

### Issues Encountered

* Pulling images from Docker Hub timed out on the cloud server.
* `quay.io/podman/hello` worked successfully.
* `quay.io/libpod/banner` started, but `curl http://localhost:8080` returned `Recv failure: Connection reset by peer`.
* Switched to a simpler BusyBox HTTP server test to isolate the runtime from image-specific behavior.

### Key Learnings

* A container runtime can be installed correctly even if a specific image registry is unreachable.
* Docker Hub access may be unstable from some cloud server environments.
* Using an alternative registry such as Quay helps distinguish runtime issues from registry network issues.
* Rootless Podman is suitable for lightweight personal container experiments.
* Server-side container tests should first be verified locally on the server before exposing ports publicly.
* Cloud deployment should be introduced gradually after runtime basics are stable.

### Next

* Add container service metadata to Mini Platform.
* Keep the next implementation focused on metadata and display, not real remote deployment.

## Day 10 - Establish V1 Test Coverage

### Goal

Preserve service type information across runtime layers and establish a regression test baseline for Mini Platform V1.

### Completed

* Fixed service type propagation in `list_service_views()`.
* Fixed service type propagation in `start_service()` and `stop_service()`.
* Added configuration loader tests.
* Added runtime manager tests.
* Added API tests for list, start, stop, and 404 responses.
* Added a dashboard smoke test.
* Added `pytest` and `httpx2` to project dependencies.
* Verified that the complete test suite passes.

### Issues Encountered

* `pytest` was not initially installed in the virtual environment.
* The project initially contained no test files, so pytest collected zero tests.
* The installed Starlette version required `httpx2` for `TestClient`.

### Key Learnings

* Default model values can hide missing data propagation between layers.
* Regression tests should protect behavior across configuration, runtime, API, and presentation boundaries.
* External framework test dependencies must be explicitly recorded.
* Mocking runtime dependencies keeps API tests isolated and deterministic.
* Smoke tests are useful for verifying that the application can render without coupling tests to HTML details.

### Next

Define explicit `local` and `container` service types and add container-specific metadata.

## Day 11 - Define Service Types and Container Metadata

### Goal

Introduce explicit service types and extend the data model to represent container services.

### Completed

* Added the `ServiceType` enum with `local` and `container` values.
* Replaced unrestricted string service types with the enum.
* Added container-specific metadata fields to `ServiceConfig`.
* Added container-specific metadata fields to `ServiceView`.
* Updated internal model construction to use enum members.
* Added model tests for default types, container metadata, external string parsing, and invalid type values.
* Verified that the complete test suite passes.

### Issues Encountered

* Existing API tests failed because the response model began serializing new optional fields as `null`.
* Static type checking rejected raw string values when constructing models directly in Python.

### Key Learnings

* Response-model changes can break exact-response assertions even when endpoint behavior remains correct.
* Internal Python code should use enum members for type safety.
* External YAML or JSON input can still be validated from string values through Pydantic.
* Optional fields provide structural flexibility, but type-specific validation is still needed.
* Regression tests help expose compatibility changes immediately.

### Next

Add type-specific validation rules and preserve container metadata through the runtime layer.

## Day 12 - Add Type-specific Validation

### Goal

Enforce service-type-specific configuration rules and preserve container metadata through the runtime layer.

### Completed

* Added validation rules for local and container service configurations.
* Required local services to define `command` and `working_dir`.
* Required container services to define `container_name` and `image`.
* Added tests for missing type-specific fields.
* Added a shared helper for converting `ServiceConfig` into `ServiceView`.
* Preserved container metadata in list, start, and stop operations.
* Verified that the complete test suite passes.

### Issues Encountered

* Existing tests using incomplete container service data had to be updated.

### Key Learnings

* Optional fields still require business-level validation.
* Type-specific rules belong in the configuration model.
* Centralizing model conversion prevents repeated field-propagation bugs.
* Tests should use valid domain objects unless invalid input is the behavior being tested.

### Next

Add a container service to the YAML configuration and verify API and dashboard compatibility.
