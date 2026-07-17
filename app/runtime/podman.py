import subprocess


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
