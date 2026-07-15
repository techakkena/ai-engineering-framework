"""
Exceptions for ai_models.embeddings.
"""

from __future__ import annotations


class EmbeddingError(Exception):
    """
    Base embedding exception.
    """

    def __init__(
        self,
        message: str = (
            "An embedding error occurred."
        ),
    ) -> None:
        super().__init__(message)


class InvalidEmbeddingProviderError(
    EmbeddingError,
):
    """
    Raised when an unsupported provider is supplied.
    """

    def __init__(
        self,
        provider: str,
    ) -> None:
        self.provider = provider

        super().__init__(
            f"Invalid embedding provider: "
            f"'{provider}'."
        )


class EmbeddingConfigurationError(
    EmbeddingError,
):
    """
    Raised when embedding configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            "Invalid embedding configuration: "
            f"'{configuration}'."
        )


class EmbeddingValidationError(
    EmbeddingError,
):
    """
    Raised when embedding validation fails.
    """

    def __init__(
        self,
        model: str,
        reason: str,
    ) -> None:
        self.model = model
        self.reason = reason

        super().__init__(
            f"Embedding model '{model}' "
            f"validation failed: {reason}."
        )