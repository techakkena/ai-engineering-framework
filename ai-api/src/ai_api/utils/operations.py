"""
Utility operations for the ai_api.utils module.

This module provides framework-independent helper functions for
working with encodings, identifiers, request IDs, and string
normalization.

All functions are deterministic, side-effect free (except UUID
generation), and easily testable.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

import re
import uuid

from ai_api.utils.constants import (
    IDENTIFIER_PATTERN,
    REQUEST_ID_PREFIX,
    SLUG_PATTERN,
    SUPPORTED_ENCODINGS,
    UUID_LENGTH,
)
from ai_api.utils.exceptions import (
    InvalidEncodingError,
    InvalidIdentifierError,
)


def normalize_encoding(encoding: str) -> str:
    """
    Normalize an encoding name.

    Args:
        encoding: Encoding name.

    Returns:
        Normalized encoding.
    """
    return encoding.strip().lower()


def validate_encoding(encoding: str) -> str:
    """
    Validate an encoding.

    Args:
        encoding: Encoding name.

    Returns:
        Validated encoding.

    Raises:
        InvalidEncodingError:
            If the encoding is unsupported.
    """
    normalized = normalize_encoding(encoding)

    if normalized not in SUPPORTED_ENCODINGS:
        raise InvalidEncodingError(encoding)

    return normalized


def is_supported_encoding(encoding: str) -> bool:
    """
    Determine whether an encoding is supported.

    Args:
        encoding: Encoding name.

    Returns:
        True if supported.
    """
    return (
        normalize_encoding(encoding)
        in SUPPORTED_ENCODINGS
    )


def validate_identifier(identifier: str) -> str:
    """
    Validate an identifier.

    Args:
        identifier: Identifier.

    Returns:
        Validated identifier.

    Raises:
        InvalidIdentifierError:
            If the identifier is invalid.
    """
    normalized = identifier.strip()

    if not re.fullmatch(
        IDENTIFIER_PATTERN,
        normalized,
    ):
        raise InvalidIdentifierError(identifier)

    return normalized


def slugify(value: str) -> str:
    """
    Convert text into a URL-friendly slug.

    Args:
        value: Input text.

    Returns:
        Slugified string.
    """
    slug = value.strip().lower()

    slug = re.sub(
        r"[^a-z0-9]+",
        "-",
        slug,
    )

    slug = slug.strip("-")

    if not re.fullmatch(
        SLUG_PATTERN,
        slug,
    ):
        return ""

    return slug


def generate_request_id() -> str:
    """
    Generate a unique request identifier.

    Returns:
        Request identifier.
    """
    return (
        f"{REQUEST_ID_PREFIX}-"
        f"{uuid.uuid4()}"
    )


def generate_uuid() -> str:
    """
    Generate a UUID.

    Returns:
        UUID string.
    """
    return str(uuid.uuid4())


def is_valid_uuid(value: str) -> bool:
    """
    Determine whether a string is a valid UUID.

    Args:
        value: UUID string.

    Returns:
        True if valid.
    """
    try:
        parsed = uuid.UUID(value)
    except ValueError:
        return False

    return len(str(parsed)) == UUID_LENGTH