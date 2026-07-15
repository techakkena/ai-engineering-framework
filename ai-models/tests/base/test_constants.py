"""
Unit tests for ai_models.base.constants.
"""

from __future__ import annotations

from ai_models.base.constants import (
    AUDIO_MODEL,
    CHAT_MODEL,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL_NAME,
    DEFAULT_MODEL_PROVIDER,
    DEFAULT_MODEL_TYPE,
    DEFAULT_TEMPERATURE,
    DEFAULT_TIMEOUT,
    EMBEDDING_MODEL,
    MULTIMODAL_MODEL,
    SUPPORTED_MODEL_TYPES,
    VISION_MODEL,
)


def test_model_defaults() -> None:
    """Test default model constants."""
    assert DEFAULT_MODEL_NAME == "model"
    assert DEFAULT_MODEL_PROVIDER == "openai"
    assert DEFAULT_MODEL_TYPE == CHAT_MODEL


def test_supported_model_types() -> None:
    """Test supported model types."""
    expected = {
        CHAT_MODEL,
        EMBEDDING_MODEL,
        VISION_MODEL,
        AUDIO_MODEL,
        MULTIMODAL_MODEL,
    }

    assert SUPPORTED_MODEL_TYPES == expected


def test_supported_model_types_are_immutable() -> None:
    """Supported model types should be immutable."""
    assert isinstance(
        SUPPORTED_MODEL_TYPES,
        frozenset,
    )


def test_model_configuration_defaults() -> None:
    """Test model configuration defaults."""
    assert DEFAULT_MAX_TOKENS == 4096
    assert DEFAULT_TEMPERATURE == 0.7
    assert DEFAULT_TIMEOUT == 60