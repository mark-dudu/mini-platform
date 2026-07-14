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
        command="podman start demo-container",
        working_dir=".",
        port=8080,
    )


@patch("app.runtime.manager.load_services")
def test_list_service_views_preserves_service_type(mock_load_services):
    mock_load_services.return_value = [build_container_service()]

    services = list_service_views()

    assert len(services) == 1
    assert services[0].name == "demo-container"
    assert services[0].type == "container"
    assert services[0].status == "stopped"


@patch("app.runtime.manager.load_services")
def test_start_service_preserves_service_type(mock_load_services):
    mock_load_services.return_value = [build_container_service()]

    service = start_service("demo-container")

    assert service is not None
    assert service.type == "container"
    assert service.status == "running"


@patch("app.runtime.manager.load_services")
def test_stop_service_preserves_service_type(mock_load_services):
    mock_load_services.return_value = [build_container_service()]

    service = stop_service("demo-container")

    assert service is not None
    assert service.type == "container"
    assert service.status == "stopped"


@patch("app.runtime.manager.load_services")
def test_list_service_views_defaults_to_stopped(mock_load_services):
    mock_load_services.return_value = [build_container_service()]

    services = list_service_views()

    assert services[0].status == "stopped"


@patch("app.runtime.manager.load_services")
def test_start_service_updates_runtime_status(mock_load_services):
    mock_load_services.return_value = [build_container_service()]

    start_service("demo-container")
    services = list_service_views()

    assert services[0].status == "running"


@patch("app.runtime.manager.load_services")
def test_stop_service_updates_runtime_status(mock_load_services):
    mock_load_services.return_value = [build_container_service()]

    start_service("demo-container")
    stop_service("demo-container")
    services = list_service_views()

    assert services[0].status == "stopped"


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
