from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app
from app.models.service import ServiceView

client = TestClient(app)


def build_service_view(status: str = "stopped") -> ServiceView:
    return ServiceView(
        name="demo-service",
        type="local",
        command="python app.py",
        working_dir=".",
        port=8000,
        status=status,
    )


@patch("app.routes.services.list_service_views")
def test_list_services_returns_service_data(mock_list_service_views):
    mock_list_service_views.return_value = [build_service_view()]

    response = client.get("/api/services/")

    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "demo-service",
            "type": "local",
            "command": "python app.py",
            "working_dir": ".",
            "port": 8000,
            "status": "stopped",
        }
    ]


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
