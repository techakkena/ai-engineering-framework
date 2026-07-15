"""
Exceptions for the AWS provider.
"""

from __future__ import annotations


class AWSError(Exception):
    """Base exception for AWS provider errors."""


class AWSConfigurationError(AWSError):
    """Raised when AWS provider configuration is invalid."""


class AWSAuthenticationError(AWSError):
    """Raised when AWS authentication fails."""


class AWSRateLimitError(AWSError):
    """Raised when AWS rate limits are exceeded."""


class AWSConnectionError(AWSError):
    """Raised when communication with AWS fails."""


class AWSTimeoutError(AWSError):
    """Raised when a request times out."""


class AWSModelError(AWSError):
    """Raised when an unsupported model is requested."""


class AWSRequestError(AWSError):
    """Raised when a request is invalid."""


class AWSResponseError(AWSError):
    """Raised when an invalid response is received."""


class AWSProviderError(AWSError):
    """Raised for provider-specific runtime failures."""