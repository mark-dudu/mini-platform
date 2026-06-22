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
