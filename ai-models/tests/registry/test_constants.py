"""
Unit tests for ai_models.registry.constants.
"""

from __future__ import annotations

from ai_models.registry.constants import (
    AZURE,
    DEFAULT_CACHE_SIZE,
    DEFAULT_REFRESH_INTERVAL,
    DEFAULT_REGISTRY_NAME,
    DEFAULT_REGISTRY_PROVIDER,
    DEFAULT_REGISTRY_VERSION,
    DEFAULT_RETRIES,
    DEFAULT_TIMEOUT,
    HUGGINGFACE,
    LOCAL,
    OLLAMA,
    OPENAI,
    SUPPORTED_REGISTRY_PROVIDERS,
)


def test_registry_defaults() -> None:
    """Test registry default configuration."""
    assert DEFAULT_REGISTRY_NAME == "model-registry"
    assert DEFAULT_REGISTRY_PROVIDER == LOCAL
    assert DEFAULT_REGISTRY_VERSION == "1.0.0"


def test_supported_registry_providers() -> None:
    """Test supported registry providers."""
    expected = {
        LOCAL,
        OPENAI,
        OLLAMA,
        HUGGINGFACE,
        AZURE,
    }

    assert (
        SUPPORTED_REGISTRY_PROVIDERS
        == expected
    )


def test_supported_registry_providers_are_immutable() -> None:
    """Supported providers should be immutable."""
    assert isinstance(
        SUPPORTED_REGISTRY_PROVIDERS,
        frozenset,
    )


def test_registry_configuration_defaults() -> None:
    """Test registry configuration defaults."""
    assert DEFAULT_CACHE_SIZE == 1000
    assert DEFAULT_REFRESH_INTERVAL == 300
    assert DEFAULT_TIMEOUT == 30
    assert DEFAULT_RETRIES == 3