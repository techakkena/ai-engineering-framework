"""
Exceptions for ai_runtime.config.
"""

from __future__ import annotations


class ConfigError(Exception):
    """
    Base configuration exception.
    """

    def __init__(
        self,
        message: str = "A configuration error occurred.",
    ) -> None:
        super().__init__(message)


class InvalidEnvironmentError(ConfigError):
    """
    Raised when an invalid environment is supplied.
    """

    def __init__(
        self,
        environment: str,
    ) -> None:
        self.environment = environment

        super().__init__(
            f"Invalid environment: '{environment}'."
        )


class ConfigConfigurationError(ConfigError):
    """
    Raised when configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            f"Invalid configuration: '{configuration}'."
        )


class ConfigValidationError(ConfigError):
    """
    Raised when configuration validation fails.
    """

    def __init__(
        self,
        configuration: str,
        reason: str,
    ) -> None:
        self.configuration = configuration
        self.reason = reason

        super().__init__(
            f"Configuration '{configuration}' validation failed: {reason}."
        )