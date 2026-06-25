from fastapi import APIRouter

from app.core.config_loader import load_services
from app.models.service import ServiceView

router = APIRouter(prefix="/api/services", tags=["services"])


@router.get("/", response_model=list[ServiceView])
def list_services():
    services = load_services()

    return [
        ServiceView(
            name=service.name,
            command=service.command,
            working_dir=service.working_dir,
            port=service.port,
            status="stopped",
        )
        for service in services
    ]
