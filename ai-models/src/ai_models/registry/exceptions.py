"""
Exceptions for ai_models.registry.
"""

from __future__ import annotations


class RegistryError(Exception):
    """
    Base registry exception.
    """

    def __init__(
        self,
        message: str = (
            "A registry error occurred."
        ),
    ) -> None:
        super().__init__(message)


class InvalidRegistryProviderError(
    RegistryError,
):
    """
    Raised when an unsupported registry
    provider is supplied.
    """

    def __init__(
        self,
        provider: str,
    ) -> None:
        self.provider = provider

        super().__init__(
            (
                "Invalid registry provider: "
                f"'{provider}'."
            )
        )


class RegistryConfigurationError(
    RegistryError,
):
    """
    Raised when registry configuration
    is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            (
                "Invalid registry "
                "configuration: "
                f"'{configuration}'."
            )
        )


class RegistryValidationError(
    RegistryError,
):
    """
    Raised when registry validation fails.
    """

    def __init__(
        self,
        registry: str,
        reason: str,
    ) -> None:
        self.registry = registry
        self.reason = reason

        super().__init__(
            (
                f"Registry '{registry}' "
                f"validation failed: "
                f"{reason}."
            )
        )