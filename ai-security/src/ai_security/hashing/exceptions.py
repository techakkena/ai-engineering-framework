"""
Exceptions for the hashing module.
"""

from __future__ import annotations


class HashingError(Exception):
    """Base exception for hashing operations."""


class HashingConfigurationError(HashingError):
    """Raised when hashing configuration is invalid."""


class HashingAlgorithmError(HashingError):
    """Raised when an unsupported hashing algorithm is requested."""


class HashVerificationError(HashingError):
    """Raised when hash verification fails."""