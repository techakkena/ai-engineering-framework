"""
Exceptions for the Azure OpenAI provider.
"""

from __future__ import annotations


class AzureError(Exception):
    """Base exception for Azure provider errors."""


class AzureConfigurationError(AzureError):
    """Raised when Azure configuration is invalid."""


class AzureAuthenticationError(AzureError):
    """Raised when authentication fails."""


class AzureRateLimitError(AzureError):
    """Raised when rate limits are exceeded."""


class AzureConnectionError(AzureError):
    """Raised when communication with Azure fails."""


class AzureTimeoutError(AzureError):
    """Raised when a request times out."""


class AzureModelError(AzureError):
    """Raised when an unsupported model is requested."""


class AzureRequestError(AzureError):
    """Raised when a request is invalid."""


class AzureResponseError(AzureError):
    """Raised when an invalid response is received."""


class AzureProviderError(AzureError):
    """Raised for provider-specific runtime failures."""