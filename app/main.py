from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from app.core.config_loader import load_services
from app.models.service import ServiceView
from app.routes.services import router as services_router

app = FastAPI(title="Mini Platform")

app.include_router(services_router)

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def read_root(request: Request):
    services = [
        ServiceView(
            name=service.name,
            command=service.command,
            working_dir=service.working_dir,
            port=service.port,
            status="stopped",
        )
        for service in load_services()
    ]
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"services": services},
    )
