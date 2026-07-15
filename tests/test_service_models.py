import pytest
from pydantic import ValidationError

from app.models.service import ServiceConfig, ServiceType, ServiceView


def test_service_config_defaults_to_local_type():
    service = ServiceConfig(
        name="blog",
        command="pnpm dev",
        working_dir="../my-blog",
        port=3000,
    )

    assert service.type == ServiceType.LOCAL


def test_service_config_parses_container_type_from_external_input():
    service = ServiceConfig.model_validate(
        {
            "name": "demo-nginx",
            "type": "container",
            "container_name": "mini-platform-nginx",
            "image": "docker.io/library/nginx:alpine",
            "host_port": 8080,
            "container_port": 80,
        }
    )

    assert service.type == ServiceType.CONTAINER
    assert service.container_name == "mini-platform-nginx"
    assert service.image == "docker.io/library/nginx:alpine"
    assert service.host_port == 8080
    assert service.container_port == 80


def test_service_config_rejects_unknown_type():
    with pytest.raises(ValidationError):
        ServiceConfig.model_validate(
            {
                "name": "invalid-service",
                "type": "docker",
            }
        )


def test_service_view_supports_container_metadata():
    service = ServiceView(
        name="demo-nginx",
        type=ServiceType.CONTAINER,
        container_name="mini-platform-nginx",
        image="docker.io/library/nginx:alpine",
        host_port=8080,
        container_port=80,
        status="stopped",
    )

    assert service.type == ServiceType.CONTAINER
    assert service.command is None
    assert service.working_dir is None
    assert service.container_name == "mini-platform-nginx"


def test_local_service_requires_command():
    with pytest.raises(
        ValidationError,
        match="Local service requires: command",
    ):
        ServiceConfig(
            name="blog",
            type=ServiceType.LOCAL,
            working_dir="../my-blog",
        )


def test_local_service_requires_working_dir():
    with pytest.raises(
        ValidationError,
        match="Local service requires: working_dir",
    ):
        ServiceConfig(
            name="blog",
            type=ServiceType.LOCAL,
            command="pnpm dev",
        )


def test_container_service_requires_container_name():
    with pytest.raises(
        ValidationError,
        match="Container service requires: container_name",
    ):
        ServiceConfig(
            name="demo-nginx",
            type=ServiceType.CONTAINER,
            image="docker.io/library/nginx:alpine",
        )


def test_container_service_requires_image():
    with pytest.raises(
        ValidationError,
        match="Container service requires: image",
    ):
        ServiceConfig(
            name="demo-nginx",
            type=ServiceType.CONTAINER,
            container_name="mini-platform-nginx",
        )


def test_container_service_reports_all_missing_required_fields():
    with pytest.raises(
        ValidationError,
        match="Container service requires: container_name, image",
    ):
        ServiceConfig(
            name="demo-nginx",
            type=ServiceType.CONTAINER,
        )
