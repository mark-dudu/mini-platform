from pathlib import Path

import yaml

from app.models.service import ServiceConfig


CONFIG_PATH = Path("config/services.yaml")


def load_services(config_path: Path = CONFIG_PATH) -> list[ServiceConfig]:
    if not config_path.exists():
        raise FileNotFoundError(f"Service config file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as file:
        raw_config = yaml.safe_load(file)

    if not raw_config or "services" not in raw_config:
        return []

    services = raw_config["services"]

    if not isinstance(services, list):
        raise ValueError("services must be a list")

    return [ServiceConfig(**service) for service in services]