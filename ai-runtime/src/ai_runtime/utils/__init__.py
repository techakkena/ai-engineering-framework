"""
ai_runtime.utils

Framework-independent runtime utility functions.

This module provides reusable constants, exceptions, and helper
operations used throughout the runtime package.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_runtime.utils.constants import (
    DEFAULT_ENCODING,
    DEFAULT_TIMEOUT,
    REQUEST_ID_PREFIX,
    SUPPORTED_ENCODINGS,
    UUID_LENGTH,
)
from ai_runtime.utils.exceptions import (
    InvalidEncodingError,
    InvalidUtilityOperationError,
    RuntimeUtilityError,
    UtilityConfigurationError,
)
from ai_runtime.utils.operations import (
    generate_request_id,
    generate_runtime_id,
    is_supported_encoding,
    normalize_encoding,
    validate_encoding,
    validate_identifier,
)

__all__ = [
    # Constants
    "DEFAULT_ENCODING",
    "DEFAULT_TIMEOUT",
    "REQUEST_ID_PREFIX",
    "SUPPORTED_ENCODINGS",
    "UUID_LENGTH",
    # Exceptions
    "RuntimeUtilityError",
    "InvalidEncodingError",
    "InvalidUtilityOperationError",
    "UtilityConfigurationError",
    # Operations
    "generate_request_id",
    "generate_runtime_id",
    "is_supported_encoding",
    "normalize_encoding",
    "validate_encoding",
    "validate_identifier",
]