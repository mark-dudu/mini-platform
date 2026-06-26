from fastapi import APIRouter, HTTPException

from app.models.service import ServiceView
from app.runtime.manager import list_service_views, start_service, stop_service

router = APIRouter(prefix="/api/services", tags=["services"])


@router.get("/", response_model=list[ServiceView])
def list_services():
    return list_service_views()


@router.post("/{service_name}/start", response_model=ServiceView)
def start_configured_service(service_name: str):
    service = start_service(service_name)

    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")

    return service


@router.post("/{service_name}/stop", response_model=ServiceView)
def stop_configured_service(service_name: str):
    service = stop_service(service_name)

    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")

    return service