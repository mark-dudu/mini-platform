from fastapi import FastAPI

from app.routes.services import router as services_router

app = FastAPI(title="Mini Platform")

app.include_router(services_router)


@app.get("/")
def read_root():
    return {"message": "Mini Platform is running"}