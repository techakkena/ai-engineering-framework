"""
Enterprise secrets management for the AI Engineering Framework.

This package provides framework-independent abstractions for securely
generating, storing, retrieving, and managing secrets.
"""

from ai_security.secrets.constants import (
    DEFAULT_SECRET_LENGTH,
    DEFAULT_SECRET_ENCODING,
    DEFAULT_TOKEN_LENGTH,
)
from ai_security.secrets.exceptions import (
    SecretConfigurationError,
    SecretError,
    SecretGenerationError,
    SecretNotFoundError,
)
from ai_security.secrets.operations import (
    Secret,
    SecretManager,
)

__all__ = [
    "DEFAULT_SECRET_LENGTH",
    "DEFAULT_SECRET_ENCODING",
    "DEFAULT_TOKEN_LENGTH",
    "SecretError",
    "SecretConfigurationError",
    "SecretGenerationError",
    "SecretNotFoundError",
    "Secret",
    "SecretManager",
]