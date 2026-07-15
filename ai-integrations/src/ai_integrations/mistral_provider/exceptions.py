"""
Exceptions for the Mistral AI provider.
"""

from __future__ import annotations


class MistralError(Exception):
    """Base exception for Mistral provider errors."""


class MistralConfigurationError(MistralError):
    """Raised when provider configuration is invalid."""


class MistralAuthenticationError(MistralError):
    """Raised when authentication fails."""


class MistralRateLimitError(MistralError):
    """Raised when API rate limits are exceeded."""


class MistralConnectionError(MistralError):
    """Raised when communication with the API fails."""


class MistralTimeoutError(MistralError):
    """Raised when a request times out."""


class MistralModelError(MistralError):
    """Raised when an unsupported model is requested."""


class MistralRequestError(MistralError):
    """Raised when a request is invalid."""


class MistralResponseError(MistralError):
    """Raised when an invalid response is received."""


class MistralProviderError(MistralError):
    """Raised for provider-specific runtime failures."""