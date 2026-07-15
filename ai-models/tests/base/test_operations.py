"""
Unit tests for ai_models.base.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_models.base.exceptions import (
    InvalidModelTypeError,
)
from ai_models.base.operations import (
    build_model_id,
    is_supported_model_type,
    normalize_model_type,
    validate_model_id,
    validate_model_type,
)


@pytest.mark.parametrize(
    ("model_type", "expected"),
    [
        ("CHAT", "chat"),
        (" Vision ", "vision"),
        ("Embedding", "embedding"),
    ],
)
def test_normalize_model_type(
    model_type: str,
    expected: str,
) -> None:
    assert normalize_model_type(model_type) == expected


@pytest.mark.parametrize(
    "model_type",
    [
        "chat",
        "embedding",
        "vision",
        "audio",
        "multimodal",
    ],
)
def test_validate_model_type(
    model_type: str,
) -> None:
    assert validate_model_type(model_type) == model_type


@pytest.mark.parametrize(
    "model_type",
    [
        "",
        "text",
        "image",
    ],
)
def test_validate_model_type_invalid(
    model_type: str,
) -> None:
    with pytest.raises(
        InvalidModelTypeError,
    ):
        validate_model_type(model_type)


@pytest.mark.parametrize(
    ("model_type", "expected"),
    [
        ("chat", True),
        ("embedding", True),
        ("vision", True),
        ("text", False),
    ],
)
def test_is_supported_model_type(
    model_type: str,
    expected: bool,
) -> None:
    assert (
        is_supported_model_type(model_type)
        is expected
    )


@pytest.mark.parametrize(
    "model_id",
    [
        "model",
        "model_01",
        "model-01",
    ],
)
def test_validate_model_id(
    model_id: str,
) -> None:
    assert validate_model_id(model_id) == model_id.lower()


@pytest.mark.parametrize(
    "model_id",
    [
        "",
        "123model",
        "model name",
        "@model",
    ],
)
def test_validate_model_id_invalid(
    model_id: str,
) -> None:
    with pytest.raises(ValueError):
        validate_model_id(model_id)


def test_build_model_id() -> None:
    model_id = build_model_id()

    assert model_id.startswith("model-")

    pattern = re.compile(
        (
            r"^model-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert pattern.fullmatch(model_id) is not None