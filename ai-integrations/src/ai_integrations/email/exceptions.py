"""
Exceptions for email integrations.
"""

from __future__ import annotations


class EmailError(Exception):
    """Base exception for email operations."""


class EmailConfigurationError(EmailError):
    """Raised when email configuration is invalid."""


class EmailAuthenticationError(EmailError):
    """Raised when authentication fails."""


class EmailConnectionError(EmailError):
    """Raised when connection fails."""


class EmailTimeoutError(EmailError):
    """Raised when an operation times out."""


class EmailRequestError(EmailError):
    """Raised when an email request is invalid."""


class EmailResponseError(EmailError):
    """Raised when an email provider returns an error."""


class EmailProviderError(EmailError):
    """Raised for provider-specific runtime failures."""