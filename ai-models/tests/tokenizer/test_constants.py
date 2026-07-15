"""
Unit tests for ai_models.tokenizer.constants.
"""

from __future__ import annotations

from ai_models.tokenizer.constants import (
    ANTHROPIC,
    CL100K_BASE,
    DEEPSEEK,
    DEFAULT_BATCH_SIZE,
    DEFAULT_CONTEXT_WINDOW,
    DEFAULT_RETRIES,
    DEFAULT_TIMEOUT,
    DEFAULT_TOKENIZER,
    DEFAULT_TOKENIZER_PROVIDER,
    GOOGLE,
    GPT2,
    GROQ,
    LARGE_CONTEXT_WINDOW,
    MEDIUM_CONTEXT_WINDOW,
    MISTRAL,
    O200K_BASE,
    OLLAMA,
    OPENAI,
    P50K_BASE,
    R50K_BASE,
    SMALL_CONTEXT_WINDOW,
    SUPPORTED_TOKENIZER_PROVIDERS,
    SUPPORTED_TOKENIZERS,
    XLARGE_CONTEXT_WINDOW,
)


def test_tokenizer_defaults() -> None:
    """Test tokenizer default configuration."""
    assert DEFAULT_TOKENIZER == "cl100k_base"
    assert DEFAULT_TOKENIZER_PROVIDER == OPENAI
    assert DEFAULT_CONTEXT_WINDOW == 128000


def test_supported_tokenizer_providers() -> None:
    """Test supported tokenizer providers."""
    expected = {
        OPENAI,
        ANTHROPIC,
        GOOGLE,
        MISTRAL,
        GROQ,
        OLLAMA,
        DEEPSEEK,
    }

    assert (
        SUPPORTED_TOKENIZER_PROVIDERS
        == expected
    )


def test_supported_tokenizer_providers_are_immutable() -> None:
    """Supported providers should be immutable."""
    assert isinstance(
        SUPPORTED_TOKENIZER_PROVIDERS,
        frozenset,
    )


def test_supported_tokenizers() -> None:
    """Test supported tokenizer names."""
    expected = {
        CL100K_BASE,
        O200K_BASE,
        P50K_BASE,
        R50K_BASE,
        GPT2,
    }

    assert SUPPORTED_TOKENIZERS == expected


def test_supported_tokenizers_are_immutable() -> None:
    """Supported tokenizer names should be immutable."""
    assert isinstance(
        SUPPORTED_TOKENIZERS,
        frozenset,
    )


def test_context_window_constants() -> None:
    """Test context window constants."""
    assert SMALL_CONTEXT_WINDOW == 8192
    assert MEDIUM_CONTEXT_WINDOW == 32768
    assert LARGE_CONTEXT_WINDOW == 128000
    assert XLARGE_CONTEXT_WINDOW == 200000


def test_tokenizer_configuration_defaults() -> None:
    """Test tokenizer configuration defaults."""
    assert DEFAULT_TIMEOUT == 30
    assert DEFAULT_RETRIES == 3
    assert DEFAULT_BATCH_SIZE == 100