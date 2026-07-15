"""
Slack integration for the AI Engineering Framework.

This package provides framework-independent abstractions for interacting
with Slack workspaces, channels, messages, files, and webhooks.
"""

from ai_integrations.slack.constants import (
    DEFAULT_API_BASE,
    DEFAULT_TIMEOUT,
    SUPPORTED_MESSAGE_TYPES,
)
from ai_integrations.slack.exceptions import (
    SlackAuthenticationError,
    SlackConfigurationError,
    SlackError,
    SlackProviderError,
    SlackRateLimitError,
)
from ai_integrations.slack.operations import (
    SlackChannel,
    SlackClient,
    SlackMessage,
)

__all__ = [
    "DEFAULT_API_BASE",
    "DEFAULT_TIMEOUT",
    "SUPPORTED_MESSAGE_TYPES",
    "SlackError",
    "SlackConfigurationError",
    "SlackAuthenticationError",
    "SlackRateLimitError",
    "SlackProviderError",
    "SlackChannel",
    "SlackMessage",
    "SlackClient",
]