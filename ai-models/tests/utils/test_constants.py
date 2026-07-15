"""
Unit tests for ai_models.utils.constants.
"""

from __future__ import annotations

from ai_models.utils.constants import (
    ASCII,
    DEFAULT_ENCODING,
    DEFAULT_RETRIES,
    DEFAULT_TIMEOUT,
    DEFAULT_UUID_PREFIX,
    DEFAULT_VERSION,
    LATIN1,
    MAX_MODEL_NAME_LENGTH,
    MIN_MODEL_NAME_LENGTH,
    SUPPORTED_ENCODINGS,
    UTF8,
    UTF16,
)


def test_utility_defaults() -> None:
    """Test utility default configuration."""
    assert DEFAULT_VERSION == "1.0.0"
    assert DEFAULT_ENCODING == UTF8
    assert DEFAULT_UUID_PREFIX == "model"


def test_supported_encodings() -> None:
    """Test supported encodings."""
    expected = {
        UTF8,
        UTF16,
        ASCII,
        LATIN1,
    }

    assert SUPPORTED_ENCODINGS == expected


def test_supported_encodings_are_immutable() -> None:
    """Supported encodings should be immutable."""
    assert isinstance(
        SUPPORTED_ENCODINGS,
        frozenset,
    )


def test_model_name_limits() -> None:
    """Test model name limits."""
    assert MIN_MODEL_NAME_LENGTH == 1
    assert MAX_MODEL_NAME_LENGTH == 128


def test_utility_configuration_defaults() -> None:
    """Test utility configuration defaults."""
    assert DEFAULT_TIMEOUT == 30
    assert DEFAULT_RETRIES == 3