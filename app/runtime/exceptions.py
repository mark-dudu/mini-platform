class RuntimeErrorBase(Exception):
    """Base exception for container runtime failures."""


class RuntimeUnavailableError(RuntimeErrorBase):
    """Raised when the container runtime cannot be accessed."""


class ContainerNotFoundError(RuntimeErrorBase):
    """Raised when the requested container does not exist."""


class RuntimeCommandError(RuntimeErrorBase):
    """Raised when a container runtime command fails."""