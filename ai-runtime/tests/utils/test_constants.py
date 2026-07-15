"""
Operations for ai_runtime.utils.
"""

from __future__ import annotations

import re
import uuid

from ai_runtime.utils.constants import (
    IDENTIFIER_PATTERN,
    REQUEST_ID_PREFIX,
    RUNTIME_ID_PREFIX,
    SUPPORTED_ENCODINGS,
)
from ai_runtime.utils.exceptions import (
    InvalidEncodingError,
)


def normalize_encoding(
    encoding: str,
) -> str:
    """
    Normalize an encoding.
    """
    return encoding.strip().lower()


def validate_encoding(
    encoding: str,
) -> str:
    """
    Validate an encoding.
    """
    normalized = normalize_encoding(encoding)

    if normalized not in SUPPORTED_ENCODINGS:
        raise InvalidEncodingError(encoding)

    return normalized


def is_supported_encoding(
    encoding: str,
) -> bool:
    """
    Determine whether an encoding is supported.
    """
    return (
        normalize_encoding(encoding)
        in SUPPORTED_ENCODINGS
    )


def validate_identifier(
    identifier: str,
) -> str:
    """
    Validate an identifier.
    """
    normalized = identifier.strip()

    if not re.fullmatch(
        IDENTIFIER_PATTERN,
        normalized,
    ):
        raise ValueError(
            f"Invalid identifier: '{identifier}'."
        )

    return normalized


def generate_request_id() -> str:
    """
    Generate a request identifier.
    """
    return (
        f"{REQUEST_ID_PREFIX}-"
        f"{uuid.uuid4()}"
    )


def generate_runtime_id() -> str:
    """
    Generate a runtime identifier.
    """
    return (
        f"{RUNTIME_ID_PREFIX}-"
        f"{uuid.uuid4()}"
    )