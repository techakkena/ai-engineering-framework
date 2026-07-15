"""
Exceptions for ai_models.audio.
"""

from __future__ import annotations


class AudioError(Exception):
    """
    Base audio exception.
    """

    def __init__(
        self,
        message: str = "An audio error occurred.",
    ) -> None:
        super().__init__(message)


class InvalidAudioProviderError(AudioError):
    """
    Raised when an unsupported audio provider is supplied.
    """

    def __init__(
        self,
        provider: str,
    ) -> None:
        self.provider = provider

        super().__init__(
            f"Invalid audio provider: '{provider}'."
        )


class AudioConfigurationError(AudioError):
    """
    Raised when audio configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            "Invalid audio configuration: "
            f"'{configuration}'."
        )


class AudioValidationError(AudioError):
    """
    Raised when audio validation fails.
    """

    def __init__(
        self,
        model: str,
        reason: str,
    ) -> None:
        self.model = model
        self.reason = reason

        super().__init__(
            f"Audio model '{model}' "
            f"validation failed: {reason}."
        )