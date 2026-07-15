"""
Unit tests for ai_models.multimodal.constants.
"""

from __future__ import annotations

from ai_models.multimodal.constants import (
    ANTHROPIC,
    AUDIO_INPUT,
    AUDIO_OUTPUT,
    AZURE,
    DEFAULT_ENABLE_CACHE,
    DEFAULT_MAX_AUDIO_FILES,
    DEFAULT_MAX_DOCUMENTS,
    DEFAULT_MAX_IMAGES,
    DEFAULT_MAX_MODALITIES,
    DEFAULT_MAX_VIDEO_FILES,
    DEFAULT_MULTIMODAL_MODEL,
    DEFAULT_MULTIMODAL_PROVIDER,
    DEFAULT_PRIMARY_MODALITY,
    DEFAULT_RETRIES,
    DEFAULT_STREAMING,
    DEFAULT_TIMEOUT,
    DOCUMENT_INPUT,
    GOOGLE,
    IMAGE_INPUT,
    IMAGE_OUTPUT,
    JSON_OUTPUT,
    OLLAMA,
    OPENAI,
    STRUCTURED_OUTPUT,
    SUPPORTED_INPUT_MODALITIES,
    SUPPORTED_MULTIMODAL_PROVIDERS,
    SUPPORTED_OUTPUT_MODALITIES,
    TEXT_INPUT,
    TEXT_OUTPUT,
    VIDEO_INPUT,
)


def test_multimodal_defaults() -> None:
    """Test multimodal default configuration."""
    assert DEFAULT_MULTIMODAL_MODEL == "gpt-5"
    assert DEFAULT_MULTIMODAL_PROVIDER == OPENAI
    assert DEFAULT_PRIMARY_MODALITY == TEXT_INPUT
    assert DEFAULT_MAX_MODALITIES == 5


def test_supported_multimodal_providers() -> None:
    """Test supported providers."""
    expected = {
        OPENAI,
        GOOGLE,
        ANTHROPIC,
        OLLAMA,
        AZURE,
    }

    assert (
        SUPPORTED_MULTIMODAL_PROVIDERS
        == expected
    )


def test_supported_multimodal_providers_are_immutable() -> None:
    """Supported providers should be immutable."""
    assert isinstance(
        SUPPORTED_MULTIMODAL_PROVIDERS,
        frozenset,
    )


def test_supported_input_modalities() -> None:
    """Test supported input modalities."""
    expected = {
        TEXT_INPUT,
        IMAGE_INPUT,
        AUDIO_INPUT,
        VIDEO_INPUT,
        DOCUMENT_INPUT,
    }

    assert SUPPORTED_INPUT_MODALITIES == expected


def test_supported_input_modalities_are_immutable() -> None:
    """Input modalities should be immutable."""
    assert isinstance(
        SUPPORTED_INPUT_MODALITIES,
        frozenset,
    )


def test_supported_output_modalities() -> None:
    """Test supported output modalities."""
    expected = {
        TEXT_OUTPUT,
        IMAGE_OUTPUT,
        AUDIO_OUTPUT,
        JSON_OUTPUT,
        STRUCTURED_OUTPUT,
    }

    assert SUPPORTED_OUTPUT_MODALITIES == expected


def test_supported_output_modalities_are_immutable() -> None:
    """Output modalities should be immutable."""
    assert isinstance(
        SUPPORTED_OUTPUT_MODALITIES,
        frozenset,
    )


def test_multimodal_limits() -> None:
    """Test multimodal limits."""
    assert DEFAULT_MAX_IMAGES == 20
    assert DEFAULT_MAX_AUDIO_FILES == 10
    assert DEFAULT_MAX_DOCUMENTS == 25
    assert DEFAULT_MAX_VIDEO_FILES == 5


def test_multimodal_configuration_defaults() -> None:
    """Test configuration defaults."""
    assert DEFAULT_TIMEOUT == 60
    assert DEFAULT_RETRIES == 3
    assert DEFAULT_STREAMING is False
    assert DEFAULT_ENABLE_CACHE is True