"""
Exceptions for ai_models.vision.
"""

from __future__ import annotations


class VisionError(Exception):
    """
    Base vision exception.
    """

    def __init__(
        self,
        message: str = "A vision error occurred.",
    ) -> None:
        super().__init__(message)


class InvalidVisionProviderError(
    VisionError,
):
    """
    Raised when an invalid vision provider is supplied.
    """

    def __init__(
        self,
        provider: str,
    ) -> None:
        self.provider = provider

        super().__init__(
            f"Invalid vision provider: '{provider}'."
        )


class VisionConfigurationError(
    VisionError,
):
    """
    Raised when vision configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            "Invalid vision configuration: "
            f"'{configuration}'."
        )


class VisionValidationError(
    VisionError,
):
    """
    Raised when vision validation fails.
    """

    def __init__(
        self,
        model: str,
        reason: str,
    ) -> None:
        self.model = model
        self.reason = reason

        super().__init__(
            f"Vision model '{model}' "
            f"validation failed: {reason}."
        )