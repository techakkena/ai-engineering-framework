"""
Exceptions for ai_models.tokenizer.
"""

from __future__ import annotations


class TokenizerError(Exception):
    """
    Base tokenizer exception.
    """

    def __init__(
        self,
        message: str = (
            "A tokenizer error occurred."
        ),
    ) -> None:
        super().__init__(message)


class InvalidTokenizerProviderError(
    TokenizerError,
):
    """
    Raised when an unsupported tokenizer
    provider is supplied.
    """

    def __init__(
        self,
        provider: str,
    ) -> None:
        self.provider = provider

        super().__init__(
            (
                "Invalid tokenizer provider: "
                f"'{provider}'."
            )
        )


class TokenizerConfigurationError(
    TokenizerError,
):
    """
    Raised when tokenizer configuration
    is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            (
                "Invalid tokenizer "
                "configuration: "
                f"'{configuration}'."
            )
        )


class TokenizerValidationError(
    TokenizerError,
):
    """
    Raised when tokenizer validation fails.
    """

    def __init__(
        self,
        tokenizer: str,
        reason: str,
    ) -> None:
        self.tokenizer = tokenizer
        self.reason = reason

        super().__init__(
            (
                f"Tokenizer '{tokenizer}' "
                f"validation failed: "
                f"{reason}."
            )
        )