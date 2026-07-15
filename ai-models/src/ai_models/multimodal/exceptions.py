"""
Exceptions for ai_models.multimodal.
"""

from __future__ import annotations


class MultimodalError(Exception):
    """
    Base multimodal exception.
    """

    def __init__(
        self,
        message: str = (
            "A multimodal error occurred."
        ),
    ) -> None:
        super().__init__(message)


class InvalidMultimodalProviderError(
    MultimodalError,
):
    """
    Raised when an unsupported multimodal provider
    is supplied.
    """

    def __init__(
        self,
        provider: str,
    ) -> None:
        self.provider = provider

        super().__init__(
            (
                "Invalid multimodal provider: "
                f"'{provider}'."
            )
        )


class MultimodalConfigurationError(
    MultimodalError,
):
    """
    Raised when multimodal configuration
    is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            (
                "Invalid multimodal "
                "configuration: "
                f"'{configuration}'."
            )
        )


class MultimodalValidationError(
    MultimodalError,
):
    """
    Raised when multimodal validation fails.
    """

    def __init__(
        self,
        model: str,
        reason: str,
    ) -> None:
        self.model = model
        self.reason = reason

        super().__init__(
            (
                f"Multimodal model '{model}' "
                f"validation failed: "
                f"{reason}."
            )
        )