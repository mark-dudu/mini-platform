from app.core.config_loader import load_services
from app.models.service import ServiceView, ServiceConfig, ServiceType
from app.runtime.podman import get_container_status, start_container, stop_container

_service_status: dict[str, str] = {}


def _build_service_view(
    service: ServiceConfig,
    status: str,
) -> ServiceView:
    return ServiceView(
        name=service.name,
        type=service.type,
        command=service.command,
        working_dir=service.working_dir,
        port=service.port,
        container_name=service.container_name,
        image=service.image,
        host_port=service.host_port,
        container_port=service.container_port,
        status=status,
    )


def _get_service_status(service: ServiceConfig) -> str:
    if service.type == ServiceType.CONTAINER:
        if service.container_name is None:
            return "unavailable"

        return get_container_status(service.container_name)

    return _service_status.get(service.name, "stopped")


def list_service_views() -> list[ServiceView]:
    services = load_services()

    return [
        _build_service_view(
            service,
            _get_service_status(service),
        )
        for service in services
    ]


def start_service(service_name: str) -> ServiceView | None:
    services = load_services()
    service = next((item for item in services if item.name == service_name), None)

    if service is None:
        return None
    if service.type == ServiceType.CONTAINER:
        if service.container_name is None:
            return _build_service_view(
                service,
                "unavailable",
            )

        start_container(service.container_name)
        return _build_service_view(
            service,
            _get_service_status(service),
        )

    _service_status[service.name] = "running"

    return _build_service_view(service, "running")


def stop_service(service_name: str) -> ServiceView | None:
    services = load_services()
    service = next((item for item in services if item.name == service_name), None)

    if service is None:
        return None

    if service.type == ServiceType.CONTAINER:
        if service.container_name is None:
            return _build_service_view(
                service,
                "unavailable",
            )

        stop_container(service.container_name)
        return _build_service_view(
            service,
            _get_service_status(service),
        )

    _service_status[service.name] = "stopped"

    return _build_service_view(service, "stopped")
