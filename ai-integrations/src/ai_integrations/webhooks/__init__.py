"""
Webhook integration for the AI Engineering Framework.

Framework-independent webhook abstractions supporting incoming and
outgoing webhooks, signature verification, retries, and event
dispatching.
"""

from ai_integrations.webhooks.constants import (
    DEFAULT_CONTENT_TYPE,
    DEFAULT_TIMEOUT,
    SUPPORTED_HTTP_METHODS,
)
from ai_integrations.webhooks.exceptions import (
    WebhookAuthenticationError,
    WebhookConfigurationError,
    WebhookError,
    WebhookProviderError,
)
from ai_integrations.webhooks.operations import (
    WebhookClient,
    WebhookEvent,
    WebhookRequest,
)

__all__ = [
    "DEFAULT_CONTENT_TYPE",
    "DEFAULT_TIMEOUT",
    "SUPPORTED_HTTP_METHODS",
    "WebhookError",
    "WebhookConfigurationError",
    "WebhookAuthenticationError",
    "WebhookProviderError",
    "WebhookEvent",
    "WebhookRequest",
    "WebhookClient",
]