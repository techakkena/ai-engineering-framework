"""
Exceptions for the Slack integration.
"""

from __future__ import annotations


class SlackError(Exception):
    """Base exception for Slack operations."""


class SlackConfigurationError(SlackError):
    """Raised when Slack configuration is invalid."""


class SlackAuthenticationError(SlackError):
    """Raised when Slack authentication fails."""


class SlackRateLimitError(SlackError):
    """Raised when the Slack API rate limit is exceeded."""


class SlackConnectionError(SlackError):
    """Raised when communication with Slack fails."""


class SlackTimeoutError(SlackError):
    """Raised when a request times out."""


class SlackRequestError(SlackError):
    """Raised when a Slack request is invalid."""


class SlackResponseError(SlackError):
    """Raised when Slack returns an invalid response."""


class SlackProviderError(SlackError):
    """Raised for provider-specific runtime failures."""