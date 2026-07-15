from pydantic import BaseModel, model_validator
from enum import Enum
from typing import Self


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

    @model_validator(mode="after")
    def validate_fields_for_service_type(self) -> Self:
        if self.type == ServiceType.LOCAL:
            missing_fields = [
                field_name
                for field_name, value in {
                    "command": self.command,
                    "working_dir": self.working_dir,
                }.items()
                if value is None
            ]

            if missing_fields:
                raise ValueError(f"Local service requires: {', '.join(missing_fields)}")

        if self.type == ServiceType.CONTAINER:
            missing_fields = [
                field_name
                for field_name, value in {
                    "container_name": self.container_name,
                    "image": self.image,
                }.items()
                if value is None
            ]

            if missing_fields:
                raise ValueError(
                    f"Container service requires: {', '.join(missing_fields)}"
                )

        return self


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
