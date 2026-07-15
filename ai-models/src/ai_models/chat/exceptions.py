"""
Exceptions for ai_models.chat.
"""

from __future__ import annotations


class ChatError(Exception):
    """
    Base chat exception.
    """

    def __init__(
        self,
        message: str = "A chat error occurred.",
    ) -> None:
        super().__init__(message)


class InvalidChatProviderError(ChatError):
    """
    Raised when an unsupported provider is supplied.
    """

    def __init__(
        self,
        provider: str,
    ) -> None:
        self.provider = provider

        super().__init__(
            f"Invalid chat provider: '{provider}'."
        )


class ChatConfigurationError(ChatError):
    """
    Raised when chat configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            f"Invalid chat configuration: '{configuration}'."
        )


class ChatValidationError(ChatError):
    """
    Raised when chat validation fails.
    """

    def __init__(
        self,
        model: str,
        reason: str,
    ) -> None:
        self.model = model
        self.reason = reason

        super().__init__(
            f"Chat model '{model}' validation failed: {reason}."
        )