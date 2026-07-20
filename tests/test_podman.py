import subprocess
import pytest
from unittest.mock import Mock, patch

from app.runtime.podman import get_container_status, start_container, stop_container


@patch("app.runtime.podman.subprocess.run")
def test_get_container_status_returns_running(mock_run):
    mock_run.return_value = Mock(
        returncode=0,
        stdout="running\n",
        stderr="",
    )

    status = get_container_status("demo-container")

    assert status == "running"

    mock_run.assert_called_once_with(
        [
            "podman",
            "inspect",
            "--format",
            "{{.State.Status}}",
            "demo-container",
        ],
        capture_output=True,
        text=True,
        check=False,
        timeout=5,
    )


@pytest.mark.parametrize(
    "podman_status",
    [
        "created",
        "configured",
        "exited",
        "paused",
        "stopped",
        "unknown",
    ],
)
@patch("app.runtime.podman.subprocess.run")
def test_get_container_status_maps_non_running_states_to_stopped(
    mock_run,
    podman_status,
):
    mock_run.return_value = Mock(
        returncode=0,
        stdout=f"{podman_status}\n",
        stderr="",
    )

    status = get_container_status("demo-container")

    assert status == "stopped"


@patch("app.runtime.podman.subprocess.run")
def test_get_container_status_returns_not_found(mock_run):
    mock_run.return_value = Mock(
        returncode=125,
        stdout="",
        stderr='Error: no such container "demo-container"',
    )

    status = get_container_status("demo-container")

    assert status == "not_found"


@patch("app.runtime.podman.subprocess.run")
def test_get_container_status_returns_not_found_for_no_such_object(
    mock_run,
):
    mock_run.return_value = Mock(
        returncode=125,
        stdout="",
        stderr='Error: no such object: "demo-container"',
    )

    status = get_container_status("demo-container")

    assert status == "not_found"


@patch("app.runtime.podman.subprocess.run")
def test_get_container_status_returns_unavailable_when_podman_is_missing(
    mock_run,
):
    mock_run.side_effect = FileNotFoundError

    status = get_container_status("demo-container")

    assert status == "unavailable"


@patch("app.runtime.podman.subprocess.run")
def test_get_container_status_returns_unavailable_on_timeout(mock_run):
    mock_run.side_effect = subprocess.TimeoutExpired(
        cmd=["podman", "inspect"],
        timeout=5,
    )

    status = get_container_status("demo-container")

    assert status == "unavailable"


@patch("app.runtime.podman.subprocess.run")
def test_get_container_status_returns_unavailable_on_command_error(
    mock_run,
):
    mock_run.return_value = Mock(
        returncode=1,
        stdout="",
        stderr="unexpected runtime error",
    )

    status = get_container_status("demo-container")

    assert status == "unavailable"


@patch("app.runtime.podman.subprocess.run")
def test_get_container_status_returns_unavailable_for_unknown_status(
    mock_run,
):
    mock_run.return_value = Mock(
        returncode=0,
        stdout="mystery-state\n",
        stderr="",
    )

    status = get_container_status("demo-container")

    assert status == "unavailable"

def test_start_container_interface_is_available():
    with pytest.raises(NotImplementedError):
        start_container("demo-container")


def test_stop_container_interface_is_available():
    with pytest.raises(NotImplementedError):
        stop_container("demo-container")