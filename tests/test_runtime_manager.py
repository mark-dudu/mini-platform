from unittest.mock import patch

from app.models.service import ServiceConfig, ServiceType
from app.runtime.manager import list_service_views, start_service, stop_service

import pytest

from app.runtime import manager


@pytest.fixture(autouse=True)
def clear_service_status():
    manager._service_status.clear()
    yield
    manager._service_status.clear()


def build_container_service() -> ServiceConfig:
    return ServiceConfig(
        name="demo-container",
        type=ServiceType.CONTAINER,
        container_name="demo-container",
        image="docker.io/library/nginx:alpine",
        host_port=8080,
        container_port=80,
    )


def build_local_service() -> ServiceConfig:
    return ServiceConfig(
        name="demo-local",
        type=ServiceType.LOCAL,
        command="python app.py",
        working_dir=".",
        port=8000,
    )


@patch("app.runtime.manager.get_container_status")
@patch("app.runtime.manager.load_services")
def test_list_service_views_preserves_service_type(
    mock_load_services, mock_get_container_status
):
    mock_load_services.return_value = [build_container_service()]
    mock_get_container_status.return_value = "stopped"

    services = list_service_views()

    assert len(services) == 1
    assert services[0].name == "demo-container"
    assert services[0].type == ServiceType.CONTAINER
    assert services[0].status == "stopped"

    mock_get_container_status.assert_called_once_with("demo-container")


@patch("app.runtime.manager.get_container_status")
@patch("app.runtime.manager.start_container")
@patch("app.runtime.manager.load_services")
def test_start_service_preserves_service_type(
    mock_load_services, mock_start_container, mock_get_container_status
):
    mock_load_services.return_value = [build_container_service()]
    mock_get_container_status.return_value = "stopped"

    service = start_service("demo-container")

    assert service is not None
    assert service.type == ServiceType.CONTAINER
    assert service.status == "stopped"

    mock_get_container_status.assert_called_once_with("demo-container")
    mock_start_container.assert_called_once_with("demo-container")


@patch("app.runtime.manager.get_container_status")
@patch("app.runtime.manager.stop_container")
@patch("app.runtime.manager.load_services")
def test_stop_service_preserves_service_type(
    mock_load_services, mock_stop_container, mock_get_container_status
):
    mock_load_services.return_value = [build_container_service()]
    mock_get_container_status.return_value = "running"

    service = stop_service("demo-container")

    assert service is not None
    assert service.type == ServiceType.CONTAINER
    assert service.status == "running"

    mock_get_container_status.assert_called_once_with("demo-container")
    mock_stop_container.assert_called_once_with("demo-container")


@patch("app.runtime.manager.get_container_status")
@patch("app.runtime.manager.load_services")
def test_list_service_views_uses_container_runtime_status(
    mock_load_services,
    mock_get_container_status,
):
    mock_load_services.return_value = [build_container_service()]
    mock_get_container_status.return_value = "not_found"

    services = list_service_views()

    assert services[0].status == "not_found"
    mock_get_container_status.assert_called_once_with("demo-container")


@patch("app.runtime.manager.get_container_status")
@patch("app.runtime.manager.load_services")
def test_list_local_service_defaults_to_stopped(
    mock_load_services,
    mock_get_container_status,
):
    mock_load_services.return_value = [build_local_service()]

    services = list_service_views()

    assert services[0].status == "stopped"
    mock_get_container_status.assert_not_called()


@patch("app.runtime.manager.load_services")
def test_list_service_views_preserves_container_metadata(mock_load_services):
    mock_load_services.return_value = [build_container_service()]

    services = list_service_views()

    assert len(services) == 1

    service = services[0]

    assert service.type == ServiceType.CONTAINER
    assert service.container_name == "demo-container"
    assert service.image == "docker.io/library/nginx:alpine"
    assert service.host_port == 8080
    assert service.container_port == 80
    assert service.command is None
    assert service.working_dir is None


@patch("app.runtime.manager.load_services")
def test_start_local_service_updates_runtime_status(mock_load_services):
    mock_load_services.return_value = [build_local_service()]

    start_service("demo-local")
    services = list_service_views()

    assert services[0].status == "running"


@patch("app.runtime.manager.get_container_status")
@patch("app.runtime.manager.start_container")
@patch("app.runtime.manager.load_services")
def test_start_service_preserves_container_metadata(
    mock_load_services, mock_start_container, mock_get_container_status
):
    mock_load_services.return_value = [build_container_service()]
    mock_get_container_status.return_value = "stopped"

    service = start_service("demo-container")

    assert service is not None
    assert service.type == ServiceType.CONTAINER
    assert service.container_name == "demo-container"
    assert service.image == "docker.io/library/nginx:alpine"
    assert service.status == "stopped"
    mock_get_container_status.assert_called_once_with("demo-container")
    mock_start_container.assert_called_once_with("demo-container")


@patch("app.runtime.manager.load_services")
def test_stop_local_service_updates_runtime_status(mock_load_services):
    mock_load_services.return_value = [build_local_service()]

    start_service("demo-local")
    stop_service("demo-local")
    services = list_service_views()

    assert services[0].status == "stopped"


@patch("app.runtime.manager.get_container_status")
@patch("app.runtime.manager.stop_container")
@patch("app.runtime.manager.load_services")
def test_stop_service_preserves_container_metadata(
    mock_load_services, mock_stop_container, mock_get_container_status
):
    mock_load_services.return_value = [build_container_service()]
    mock_get_container_status.return_value = "running"

    service = stop_service("demo-container")

    assert service is not None
    assert service.type == ServiceType.CONTAINER
    assert service.container_name == "demo-container"
    assert service.image == "docker.io/library/nginx:alpine"
    assert service.status == "running"
    mock_get_container_status.assert_called_once_with("demo-container")
    mock_stop_container.assert_called_once_with("demo-container")


@patch("app.runtime.manager.load_services")
def test_start_service_returns_none_for_unknown_service(mock_load_services):
    mock_load_services.return_value = [build_container_service()]

    service = start_service("missing-service")

    assert service is None


@patch("app.runtime.manager.load_services")
def test_stop_service_returns_none_for_unknown_service(mock_load_services):
    mock_load_services.return_value = [build_container_service()]

    service = stop_service("missing-service")

    assert service is None


@patch("app.runtime.manager.get_container_status")
@patch("app.runtime.manager.start_container")
@patch("app.runtime.manager.load_services")
def test_start_container_service_returns_actual_runtime_status(
    mock_load_services,
    mock_start_container,
    mock_get_container_status,
):
    mock_load_services.return_value = [build_container_service()]
    mock_get_container_status.return_value = "stopped"

    service = start_service("demo-container")

    assert service is not None
    assert service.status == "stopped"
    mock_get_container_status.assert_called_once_with("demo-container")
    mock_start_container.assert_called_once_with("demo-container")


@patch("app.runtime.manager.get_container_status")
@patch("app.runtime.manager.stop_container")
@patch("app.runtime.manager.load_services")
def test_stop_container_service_returns_actual_runtime_status(
    mock_load_services,
    mock_stop_container,
    mock_get_container_status,
):
    mock_load_services.return_value = [build_container_service()]
    mock_get_container_status.return_value = "running"

    service = stop_service("demo-container")

    assert service is not None
    assert service.status == "running"
    mock_get_container_status.assert_called_once_with("demo-container")
    mock_stop_container.assert_called_once_with("demo-container")

@patch("app.runtime.manager.get_container_status")
@patch("app.runtime.manager.start_container")
@patch("app.runtime.manager.load_services")
def test_start_container_service_calls_runtime_and_refreshes_status(
    mock_load_services,
    mock_start_container,
    mock_get_container_status,
):
    mock_load_services.return_value = [build_container_service()]
    mock_get_container_status.return_value = "running"

    service = start_service("demo-container")

    assert service is not None
    assert service.status == "running"

    mock_start_container.assert_called_once_with("demo-container")
    mock_get_container_status.assert_called_once_with("demo-container")

@patch("app.runtime.manager.get_container_status")
@patch("app.runtime.manager.stop_container")
@patch("app.runtime.manager.load_services")
def test_stop_container_service_calls_runtime_and_refreshes_status(
    mock_load_services,
    mock_stop_container,
    mock_get_container_status,
):
    mock_load_services.return_value = [build_container_service()]
    mock_get_container_status.return_value = "stopped"

    service = stop_service("demo-container")

    assert service is not None
    assert service.status == "stopped"

    mock_stop_container.assert_called_once_with("demo-container")
    mock_get_container_status.assert_called_once_with("demo-container")

@patch("app.runtime.manager.start_container")
@patch("app.runtime.manager.load_services")
def test_start_local_service_does_not_call_container_runtime(
    mock_load_services,
    mock_start_container,
):
    mock_load_services.return_value = [build_local_service()]

    service = start_service("demo-local")

    assert service is not None
    assert service.status == "running"
    mock_start_container.assert_not_called()

@patch("app.runtime.manager.stop_container")
@patch("app.runtime.manager.load_services")
def test_stop_local_service_does_not_call_container_runtime(
    mock_load_services,
    mock_stop_container,
):
    mock_load_services.return_value = [build_local_service()]

    service = stop_service("demo-local")

    assert service is not None
    assert service.status == "stopped"
    mock_stop_container.assert_not_called()

