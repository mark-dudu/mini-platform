from app.core.config_loader import load_services
from app.models.service import ServiceView


_service_status: dict[str, str] = {}


def list_service_views() -> list[ServiceView]:
    services = load_services()

    return [
        ServiceView(
            name=service.name,
            type=service.type,
            command=service.command,
            working_dir=service.working_dir,
            port=service.port,
            status=_service_status.get(service.name, "stopped"),
        )
        for service in services
    ]


def start_service(service_name: str) -> ServiceView | None:
    services = load_services()
    service = next((item for item in services if item.name == service_name), None)

    if service is None:
        return None

    _service_status[service.name] = "running"

    return ServiceView(
        name=service.name,
        type=service.type,
        command=service.command,
        working_dir=service.working_dir,
        port=service.port,
        status="running",
    )


def stop_service(service_name: str) -> ServiceView | None:
    services = load_services()
    service = next((item for item in services if item.name == service_name), None)

    if service is None:
        return None

    _service_status[service.name] = "stopped"

    return ServiceView(
        name=service.name,
        type=service.type,
        command=service.command,
        working_dir=service.working_dir,
        port=service.port,
        status="stopped",
    ) 