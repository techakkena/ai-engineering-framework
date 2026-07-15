"""
Operations for ai_runtime.context.
"""

from __future__ import annotations

import re
import uuid

from ai_runtime.context.constants import (
    SUPPORTED_CONTEXT_SCOPES,
)
from ai_runtime.context.exceptions import (
    InvalidContextScopeError,
)


def normalize_context_scope(
    scope: str,
) -> str:
    """
    Normalize a context scope.
    """
    return scope.strip().lower()


def validate_context_scope(
    scope: str,
) -> str:
    """
    Validate a context scope.
    """
    normalized = normalize_context_scope(scope)

    if normalized not in SUPPORTED_CONTEXT_SCOPES:
        raise InvalidContextScopeError(scope)

    return normalized


def is_supported_context_scope(
    scope: str,
) -> bool:
    """
    Determine whether a context scope is supported.
    """
    return (
        normalize_context_scope(scope)
        in SUPPORTED_CONTEXT_SCOPES
    )


def validate_context_id(
    context_id: str,
) -> str:
    """
    Validate a context identifier.
    """
    normalized = context_id.strip().lower()

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            f"Invalid context identifier: '{context_id}'."
        )

    return normalized


def build_context_id() -> str:
    """
    Build a unique context identifier.
    """
    return f"context-{uuid.uuid4()}"