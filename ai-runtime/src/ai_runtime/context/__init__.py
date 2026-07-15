"""
ai_runtime.context

Framework-independent runtime context utilities.

This module provides reusable constants, exceptions, and helper
operations for managing runtime execution context.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_runtime.context.constants import (
    DEFAULT_CONTEXT_ID,
    DEFAULT_CONTEXT_SCOPE,
    DEFAULT_CONTEXT_STATE,
    SUPPORTED_CONTEXT_SCOPES,
)
from ai_runtime.context.exceptions import (
    ContextConfigurationError,
    ContextError,
    ContextValidationError,
    InvalidContextScopeError,
)
from ai_runtime.context.operations import (
    build_context_id,
    is_supported_context_scope,
    normalize_context_scope,
    validate_context_id,
    validate_context_scope,
)

__all__ = [
    # Constants
    "DEFAULT_CONTEXT_ID",
    "DEFAULT_CONTEXT_SCOPE",
    "DEFAULT_CONTEXT_STATE",
    "SUPPORTED_CONTEXT_SCOPES",
    # Exceptions
    "ContextError",
    "InvalidContextScopeError",
    "ContextConfigurationError",
    "ContextValidationError",
    # Operations
    "build_context_id",
    "is_supported_context_scope",
    "normalize_context_scope",
    "validate_context_id",
    "validate_context_scope",
]