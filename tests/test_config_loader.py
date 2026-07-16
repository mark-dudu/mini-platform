from pathlib import Path

import pytest

from app.core.config_loader import load_services
from app.models.service import ServiceType


def write_config(tmp_path: Path, content: str) -> Path:
    config_path = tmp_path / "services.yaml"
    config_path.write_text(content, encoding="utf-8")
    return config_path


def test_load_services_returns_configured_services(tmp_path):
    config_path = write_config(
        tmp_path,
        """
services:
  - name: blog
    type: local
    command: pnpm dev
    working_dir: ../my-blog
    port: 3000
""",
    )

    services = load_services(config_path)

    assert len(services) == 1
    assert services[0].name == "blog"
    assert services[0].type == "local"
    assert services[0].command == "pnpm dev"
    assert services[0].working_dir == "../my-blog"
    assert services[0].port == 3000


def test_load_services_raises_when_file_does_not_exist(tmp_path):
    missing_path = tmp_path / "missing.yaml"

    with pytest.raises(FileNotFoundError, match="Service config file not found"):
        load_services(missing_path)


def test_load_services_returns_empty_list_for_empty_file(tmp_path):
    config_path = write_config(tmp_path, "")

    services = load_services(config_path)

    assert services == []


def test_load_services_returns_empty_list_when_services_key_is_missing(tmp_path):
    config_path = write_config(
        tmp_path,
        """
name: mini-platform
""",
    )

    services = load_services(config_path)

    assert services == []


def test_load_services_raises_when_services_is_not_a_list(tmp_path):
    config_path = write_config(
        tmp_path,
        """
services:
  name: blog
""",
    )

    with pytest.raises(ValueError, match="services must be a list"):
        load_services(config_path)


def test_load_services_support_mixed_service_types(tmp_path):
    config_path = write_config(
        tmp_path,
        """
services:
  - name: blog
    type: local
    command: pnpm dev
    working_dir: ../my-blog
    port: 3000

  - name: demo-nginx
    type: container
    container_name: mini-platform-nginx
    image: docker.io/library/nginx:alpine
    host_port: 8080
    container_port: 80
""",
    )

    services = load_services(config_path)

    assert len(services) == 2

    local_service = services[0]
    assert local_service.name == "blog"
    assert local_service.type == ServiceType.LOCAL
    assert local_service.command == "pnpm dev"
    assert local_service.working_dir == "../my-blog"
    assert local_service.port == 3000

    container_service = services[1]
    assert container_service.name == "demo-nginx"
    assert container_service.type == ServiceType.CONTAINER
    assert container_service.container_name == "mini-platform-nginx"
    assert container_service.image == "docker.io/library/nginx:alpine"
    assert container_service.host_port == 8080
    assert container_service.container_port == 80
