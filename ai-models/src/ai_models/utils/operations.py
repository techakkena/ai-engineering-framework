"""
Operations for ai_models.utils.
"""

from __future__ import annotations

import re
import uuid

from ai_models.utils.constants import (
    MAX_MODEL_NAME_LENGTH,
    MIN_MODEL_NAME_LENGTH,
    SUPPORTED_ENCODINGS,
)
from ai_models.utils.exceptions import (
    InvalidEncodingError,
)


def normalize_encoding(
    encoding: str,
) -> str:
    """
    Normalize an encoding name.
    """
    return encoding.strip().lower()


def validate_encoding(
    encoding: str,
) -> str:
    """
    Validate an encoding.
    """
    normalized = normalize_encoding(
        encoding,
    )

    if normalized not in SUPPORTED_ENCODINGS:
        raise InvalidEncodingError(
            encoding,
        )

    return normalized


def is_supported_encoding(
    encoding: str,
) -> bool:
    """
    Determine whether an encoding is supported.
    """
    return (
        normalize_encoding(
            encoding,
        )
        in SUPPORTED_ENCODINGS
    )


def validate_model_name(
    model_name: str,
) -> str:
    """
    Validate a model name.
    """
    normalized = model_name.strip()

    if not (
        MIN_MODEL_NAME_LENGTH
        <= len(normalized)
        <= MAX_MODEL_NAME_LENGTH
    ):
        raise ValueError(
            "Invalid model name length."
        )

    if not re.fullmatch(
        r"[A-Za-z0-9._-]+",
        normalized,
    ):
        raise ValueError(
            (
                "Invalid model name: "
                f"'{model_name}'."
            )
        )

    return normalized


def build_model_uuid() -> str:
    """
    Build a unique model UUID.
    """
    return (
        f"model-{uuid.uuid4()}"
    )