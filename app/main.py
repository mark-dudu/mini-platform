from fastapi import FastAPI
from app.core.config_loader import load_services

app = FastAPI(title="Mini Platform")

@app.get("/")
def read_root():
    services = load_services()
    return {
        "message": "Mini Platform is running",
        "services": services,
    }