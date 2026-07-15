"""
Exceptions for the Google AI provider.
"""

from __future__ import annotations


class GoogleError(Exception):
    """Base exception for Google provider errors."""


class GoogleConfigurationError(GoogleError):
    """Raised when provider configuration is invalid."""


class GoogleAuthenticationError(GoogleError):
    """Raised when authentication fails."""


class GoogleRateLimitError(GoogleError):
    """Raised when rate limits are exceeded."""


class GoogleConnectionError(GoogleError):
    """Raised when communication with Google AI fails."""


class GoogleTimeoutError(GoogleError):
    """Raised when a request times out."""


class GoogleModelError(GoogleError):
    """Raised when an unsupported model is requested."""


class GoogleRequestError(GoogleError):
    """Raised when a request is invalid."""


class GoogleResponseError(GoogleError):
    """Raised when an invalid response is returned."""


class GoogleProviderError(GoogleError):
    """Raised for provider-specific runtime failures."""