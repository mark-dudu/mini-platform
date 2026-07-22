import subprocess

from app.runtime.exceptions import ContainerNotFoundError, RuntimeCommandError, RuntimeUnavailableError


def get_container_status(container_name: str) -> str:
    try:
        result = subprocess.run(
            [
                "podman",
                "inspect",
                "--format",
                "{{.State.Status}}",
                container_name,
            ],
            capture_output=True,
            text=True,
            check=False,
            timeout=5,
        )
    except FileNotFoundError:
        return "unavailable"
    except subprocess.TimeoutExpired:
        return "unavailable"

    if result.returncode != 0:
        error_output = result.stderr.lower()

        not_found_markers = (
            "no such container",
            "no such object",
        )

        if any(marker in error_output for marker in not_found_markers):
            return "not_found"

        return "unavailable"

    status = result.stdout.strip().lower()

    if status == "running":
        return "running"

    if status in {
        "created",
        "configured",
        "exited",
        "paused",
        "stopped",
        "unknown",
    }:
        return "stopped"

    return "unavailable"

def start_container(container_name: str) -> None:
    """Start an existing Podman container."""
    try:
        result = subprocess.run(
            ["podman", "start", container_name],
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )
    except FileNotFoundError as exc:
        raise RuntimeUnavailableError(
            "Podman runtime is not available."
        ) from exc
    except subprocess.TimeoutExpired as exc:
        raise RuntimeUnavailableError(
            f"Timed out while starting container '{container_name}'."
        ) from exc

    if result.returncode == 0:
        return

    error_output = result.stderr.lower()

    not_found_markers = (
        "no such container",
        "no such object",
    )

    if any(marker in error_output for marker in not_found_markers):
        raise ContainerNotFoundError(
            f"Container '{container_name}' was not found."
        )

    raise RuntimeCommandError(
        f"Failed to start container '{container_name}'."
    )


def stop_container(container_name: str) -> None:
    """Stop a running Podman container."""
    try:
        result = subprocess.run(
            [
                "podman",
                "stop",
                container_name,
            ],
            capture_output=True,
            text=True,
            check=False,
            timeout=15,
        )
    except FileNotFoundError as exc:
        raise RuntimeUnavailableError(
            "Podman runtime is not available."
        ) from exc
    except subprocess.TimeoutExpired as exc:
        raise RuntimeUnavailableError(
            f"Timed out while stopping container '{container_name}'."
        ) from exc

    if result.returncode == 0:
        return

    error_output = result.stderr.lower()

    not_found_markers = (
        "no such container",
        "no such object",
    )

    if any(marker in error_output for marker in not_found_markers):
        raise ContainerNotFoundError(
            f"Container '{container_name}' was not found."
        )

    raise RuntimeCommandError(
        f"Failed to stop container '{container_name}'."
    )