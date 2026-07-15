"""
Email integration for the AI Engineering Framework.

Framework-independent email abstractions supporting SMTP,
SendGrid, Amazon SES, Azure Communication Services, and
future providers.
"""

from ai_integrations.email.constants import (
    DEFAULT_PORT,
    DEFAULT_SMTP_HOST,
    DEFAULT_TIMEOUT,
    SUPPORTED_CONTENT_TYPES,
)
from ai_integrations.email.exceptions import (
    EmailAuthenticationError,
    EmailConfigurationError,
    EmailError,
    EmailProviderError,
)
from ai_integrations.email.operations import (
    EmailAttachment,
    EmailClient,
    EmailMessage,
)

__all__ = [
    "DEFAULT_PORT",
    "DEFAULT_SMTP_HOST",
    "DEFAULT_TIMEOUT",
    "SUPPORTED_CONTENT_TYPES",
    "EmailError",
    "EmailConfigurationError",
    "EmailAuthenticationError",
    "EmailProviderError",
    "EmailAttachment",
    "EmailMessage",
    "EmailClient",
]