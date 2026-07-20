from app.runtime.exceptions import (
    ContainerNotFoundError,
    RuntimeCommandError,
    RuntimeErrorBase,
    RuntimeUnavailableError,
)


def test_runtime_unavailable_error_inherits_from_runtime_base():
    assert issubclass(RuntimeUnavailableError, RuntimeErrorBase)


def test_container_not_found_error_inherits_from_runtime_base():
    assert issubclass(ContainerNotFoundError, RuntimeErrorBase)


def test_runtime_command_error_inherits_from_runtime_base():
    assert issubclass(RuntimeCommandError, RuntimeErrorBase)