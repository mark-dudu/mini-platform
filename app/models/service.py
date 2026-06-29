from pydantic import BaseModel


class ServiceConfig(BaseModel):
    name: str
    type: str = "local"
    command: str
    working_dir: str
    port: int


class ServiceView(BaseModel):
    name: str
    type: str = "local"
    command: str
    working_dir: str
    port: int
    status: str = "stopped"
