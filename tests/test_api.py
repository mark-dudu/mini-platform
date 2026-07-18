from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app
from app.models.service import ServiceType, ServiceView

client = TestClient(app)


def build_service_view(status: str = "stopped") -> ServiceView:
    return ServiceView(
        name="demo-service",
        type=ServiceType.LOCAL,
        command="python app.py",
        working_dir=".",
        port=8000,
        status=status,
    )


def build_container_service_view(
    status: str = "stopped",
) -> ServiceView:
    return ServiceView(
        name="demo-nginx",
        type=ServiceType.CONTAINER,
        container_name="mini-platform-nginx",
        image="docker.io/library/nginx:alpine",
        host_port=8080,
        container_port=80,
        status=status,
    )


@patch("app.routes.services.list_service_views")
def test_list_services_returns_service_data(mock_list_service_views):
    mock_list_service_views.return_value = [build_service_view()]

    response = client.get("/api/services/")

    assert response.status_code == 200

    service = response.json()[0]

    assert service["name"] == "demo-service"
    assert service["type"] == "local"
    assert service["command"] == "python app.py"
    assert service["working_dir"] == "."
    assert service["port"] == 8000
    assert service["status"] == "stopped"


@patch("app.routes.services.start_service")
def test_start_service_returns_running_service(mock_start_service):
    mock_start_service.return_value = build_service_view(status="running")

    response = client.post("/api/services/demo-service/start")

    assert response.status_code == 200
    assert response.json()["status"] == "running"
    assert response.json()["type"] == "local"


@patch("app.routes.services.start_service")
def test_start_service_returns_404_for_unknown_service(mock_start_service):
    mock_start_service.return_value = None

    response = client.post("/api/services/missing-service/start")

    assert response.status_code == 404
    assert response.json() == {"detail": "Service not found"}


@patch("app.routes.services.stop_service")
def test_stop_service_returns_stopped_service(mock_stop_service):
    mock_stop_service.return_value = build_service_view(status="stopped")

    response = client.post("/api/services/demo-service/stop")

    assert response.status_code == 200
    assert response.json()["status"] == "stopped"


@patch("app.routes.services.stop_service")
def test_stop_service_returns_404_for_unknown_service(mock_stop_service):
    mock_stop_service.return_value = None

    response = client.post("/api/services/missing-service/stop")

    assert response.status_code == 404
    assert response.json() == {"detail": "Service not found"}


@patch("app.main.list_service_views")
def test_dashboard_returns_success(mock_list_service_views):
    mock_list_service_views.return_value = [build_service_view()]

    response = client.get("/")

    assert response.status_code == 200


@patch("app.main.list_service_views")
def test_dashboard_supports_mixed_service_types(mock_list_service_views):
    mock_list_service_views.return_value = [
        build_service_view(),
        build_container_service_view(),
    ]

    response = client.get("/")

    assert response.status_code == 200

    body = response.text

    assert "demo-service" in body
    assert "python app.py" in body
    assert "demo-nginx" in body
    assert "mini-platform-nginx" in body
    assert "docker.io/library/nginx:alpine" in body
    assert "8080:80" in body


@patch("app.main.list_service_views")
def test_dashboard_marks_container_service_as_read_only(
    mock_list_service_views,
):
    mock_list_service_views.return_value = [
        build_container_service_view(status="running"),
    ]

    response = client.get("/")

    assert response.status_code == 200
    assert "Read-only" in response.text
    assert "/services/demo-nginx/start" not in response.text
    assert "/services/demo-nginx/stop" not in response.text


@patch("app.main.list_service_views")
def test_dashboard_keeps_mock_controls_for_local_service(
    mock_list_service_views,
):
    mock_list_service_views.return_value = [
        build_service_view(),
    ]

    response = client.get("/")

    assert response.status_code == 200
    assert "/services/demo-service/start" in response.text
    assert "/services/demo-service/stop" in response.text
