"""
ai_api.utils

Framework-independent utility functions for the AI API package.

This module provides reusable constants, exceptions, and helper
operations shared across the AI API package.

The module is intentionally framework-independent and can be used
by any API framework including FastAPI, Starlette, Quart,
Litestar, Flask, Django, or future frameworks.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_api.utils.constants import (
    DEFAULT_ENCODING,
    DEFAULT_INDENT,
    DEFAULT_SEPARATOR,
    DEFAULT_TIMEOUT,
    SUPPORTED_ENCODINGS,
    UUID_LENGTH,
)
from ai_api.utils.exceptions import (
    InvalidEncodingError,
    InvalidIdentifierError,
    InvalidUtilityOperationError,
    UtilityConfigurationError,
    UtilityError,
)
from ai_api.utils.operations import (
    generate_request_id,
    is_supported_encoding,
    normalize_encoding,
    slugify,
    validate_encoding,
    validate_identifier,
)

__all__ = [
    # Constants
    "DEFAULT_ENCODING",
    "DEFAULT_INDENT",
    "DEFAULT_SEPARATOR",
    "DEFAULT_TIMEOUT",
    "SUPPORTED_ENCODINGS",
    "UUID_LENGTH",
    # Exceptions
    "UtilityError",
    "InvalidEncodingError",
    "InvalidIdentifierError",
    "InvalidUtilityOperationError",
    "UtilityConfigurationError",
    # Operations
    "generate_request_id",
    "is_supported_encoding",
    "normalize_encoding",
    "slugify",
    "validate_encoding",
    "validate_identifier",
]