"""
Exceptions for ai_models.config.
"""

from __future__ import annotations


class ModelConfigError(Exception):
    """
    Base configuration exception.
    """

    def __init__(
        self,
        message: str = (
            "A model configuration error occurred."
        ),
    ) -> None:
        super().__init__(message)


class InvalidEnvironmentError(
    ModelConfigError,
):
    """
    Raised when an unsupported environment
    is supplied.
    """

    def __init__(
        self,
        environment: str,
    ) -> None:
        self.environment = environment

        super().__init__(
            (
                "Invalid environment: "
                f"'{environment}'."
            )
        )


class ModelConfigurationError(
    ModelConfigError,
):
    """
    Raised when a model configuration
    is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            (
                "Invalid model "
                "configuration: "
                f"'{configuration}'."
            )
        )


class ConfigurationValidationError(
    ModelConfigError,
):
    """
    Raised when configuration validation
    fails.
    """

    def __init__(
        self,
        configuration: str,
        reason: str,
    ) -> None:
        self.configuration = configuration
        self.reason = reason

        super().__init__(
            (
                f"Configuration "
                f"'{configuration}' "
                f"validation failed: "
                f"{reason}."
            )
        )


class InvalidConfigurationValueError(
    ModelConfigError,
):
    """
    Raised when a configuration value
    is outside the supported range.
    """

    def __init__(
        self,
        field: str,
        value: object,
    ) -> None:
        self.field = field
        self.value = value

        super().__init__(
            (
                "Invalid configuration "
                f"value for '{field}': "
                f"{value!r}."
            )
        )