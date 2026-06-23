from pydantic import BaseModel

class ServiceConfig(BaseModel):
    name: str
    command: str
    working_dir: str
    port: int