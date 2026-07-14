from pydantic import BaseModel
from enum import Enum


class ServiceType(str, Enum):
    LOCAL = "local"
    CONTAINER = "container"


class ServiceConfig(BaseModel):
    name: str
    type: ServiceType = ServiceType.LOCAL

    command: str | None = None
    working_dir: str | None = None
    port: int | None = None

    container_name: str | None = None
    image: str | None = None
    host_port: int | None = None
    container_port: int | None = None


class ServiceView(BaseModel):
    name: str
    type: ServiceType = ServiceType.LOCAL

    command: str | None = None
    working_dir: str | None = None
    port: int | None = None

    container_name: str | None = None
    image: str | None = None
    host_port: int | None = None
    container_port: int | None = None

    status: str = "stopped"
