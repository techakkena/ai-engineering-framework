from __future__ import annotations

"""Email tool."""

from .constants import DEFAULT_EMAIL_SUBJECT
from .exceptions import EmailToolError
from .operations import (
    EmailClient,
    EmailMessage,
)

__all__ = [
    "DEFAULT_EMAIL_SUBJECT",
    "EmailToolError",
    "EmailClient",
    "EmailMessage",
]
