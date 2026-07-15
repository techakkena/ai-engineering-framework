"""
ai_security.hashing
===================

Enterprise hashing utilities for the AI Engineering Framework.

This module provides framework-independent hashing functionality for
secure password storage, integrity verification, and deterministic
digest generation.

Modules
-------
constants
    Shared hashing constants.

exceptions
    Hashing-specific exception hierarchy.

operations
    High-level hashing operations.
"""

from ai_security.hashing.constants import (
    DEFAULT_ENCODING,
    DEFAULT_HASH_ALGORITHM,
    DEFAULT_ITERATIONS,
    DEFAULT_KEY_LENGTH,
    DEFAULT_SALT_LENGTH,
    SUPPORTED_HASH_ALGORITHMS,
)
from ai_security.hashing.exceptions import (
    HashingAlgorithmError,
    HashingConfigurationError,
    HashingError,
    HashVerificationError,
)
from ai_security.hashing.operations import (
    HashResult,
    HashingService,
)

__all__ = [
    "DEFAULT_ENCODING",
    "DEFAULT_HASH_ALGORITHM",
    "DEFAULT_ITERATIONS",
    "DEFAULT_KEY_LENGTH",
    "DEFAULT_SALT_LENGTH",
    "SUPPORTED_HASH_ALGORITHMS",
    "HashingError",
    "HashingAlgorithmError",
    "HashingConfigurationError",
    "HashVerificationError",
    "HashResult",
    "HashingService",
]