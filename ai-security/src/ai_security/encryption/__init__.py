"""
ai_security.encryption

Framework-independent encryption utilities.

This module provides reusable constants, exceptions, and helper
operations for encryption across AI applications.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_security.encryption.constants import (
    DEFAULT_ENCRYPTION_ALGORITHM,
    DEFAULT_KEY_SIZE,
    DEFAULT_PROVIDER,
    SUPPORTED_ENCRYPTION_ALGORITHMS,
)
from ai_security.encryption.exceptions import (
    EncryptionConfigurationError,
    EncryptionError,
    EncryptionValidationError,
    InvalidEncryptionProviderError,
)
from ai_security.encryption.operations import (
    build_encryption_id,
    is_supported_encryption_provider,
    normalize_encryption_provider,
    validate_encryption_id,
    validate_encryption_provider,
)

__all__ = [
    # Constants
    "DEFAULT_ENCRYPTION_ALGORITHM",
    "DEFAULT_KEY_SIZE",
    "DEFAULT_PROVIDER",
    "SUPPORTED_ENCRYPTION_ALGORITHMS",
    # Exceptions
    "EncryptionError",
    "InvalidEncryptionProviderError",
    "EncryptionConfigurationError",
    "EncryptionValidationError",
    # Operations
    "build_encryption_id",
    "is_supported_encryption_provider",
    "normalize_encryption_provider",
    "validate_encryption_id",
    "validate_encryption_provider",
]