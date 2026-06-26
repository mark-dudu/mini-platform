from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.routes.services import router as services_router
from app.runtime.manager import list_service_views, start_service, stop_service

app = FastAPI(title="Mini Platform")

app.include_router(services_router)

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"services": list_service_views()},
    )


@app.post("/services/{service_name}/start")
def start_service_from_dashboard(service_name: str):
    start_service(service_name)
    return RedirectResponse(url="/", status_code=303)


@app.post("/services/{service_name}/stop")
def stop_service_from_dashboard(service_name: str):
    stop_service(service_name)
    return RedirectResponse(url="/", status_code=303)