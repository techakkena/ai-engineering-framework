"""
Operations for ai_models.base.
"""

from __future__ import annotations

import re
import uuid

from ai_models.base.constants import (
    SUPPORTED_MODEL_TYPES,
)
from ai_models.base.exceptions import (
    InvalidModelTypeError,
)


def normalize_model_type(
    model_type: str,
) -> str:
    """
    Normalize a model type.
    """
    return model_type.strip().lower()


def validate_model_type(
    model_type: str,
) -> str:
    """
    Validate a model type.
    """
    normalized = normalize_model_type(model_type)

    if normalized not in SUPPORTED_MODEL_TYPES:
        raise InvalidModelTypeError(model_type)

    return normalized


def is_supported_model_type(
    model_type: str,
) -> bool:
    """
    Determine whether a model type is supported.
    """
    return (
        normalize_model_type(model_type)
        in SUPPORTED_MODEL_TYPES
    )


def validate_model_id(
    model_id: str,
) -> str:
    """
    Validate a model identifier.
    """
    normalized = model_id.strip().lower()

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            f"Invalid model identifier: '{model_id}'."
        )

    return normalized


def build_model_id() -> str:
    """
    Build a unique model identifier.
    """
    return f"model-{uuid.uuid4()}"