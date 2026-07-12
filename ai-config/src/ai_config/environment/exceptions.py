class EnvironmentError(Exception):
    """Base environment exception."""


class EnvironmentFileNotFoundError(EnvironmentError):
    """Raised when the .env file cannot be found."""


class EnvironmentVariableNotFoundError(EnvironmentError):
    """Raised when a required environment variable is missing."""


class EnvironmentValueError(EnvironmentError):
    """Raised when an environment variable cannot be converted to the requested type."""
