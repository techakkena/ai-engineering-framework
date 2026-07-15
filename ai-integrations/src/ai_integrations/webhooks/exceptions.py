"""
Exceptions for webhook integrations.
"""

from __future__ import annotations


class WebhookError(Exception):
    """Base exception for webhook operations."""


class WebhookConfigurationError(WebhookError):
    """Raised when webhook configuration is invalid."""


class WebhookAuthenticationError(WebhookError):
    """Raised when webhook authentication fails."""


class WebhookConnectionError(WebhookError):
    """Raised when communication fails."""


class WebhookTimeoutError(WebhookError):
    """Raised when a request times out."""


class WebhookRequestError(WebhookError):
    """Raised when a webhook request is invalid."""


class WebhookResponseError(WebhookError):
    """Raised when a webhook response is invalid."""


class WebhookProviderError(WebhookError):
    """Raised for provider-specific runtime failures."""