"""
Constants for ai_models.registry.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Defaults
# ============================================================================

DEFAULT_REGISTRY_NAME: Final[str] = "model-registry"

DEFAULT_REGISTRY_PROVIDER: Final[str] = "local"

DEFAULT_REGISTRY_VERSION: Final[str] = "1.0.0"

# ============================================================================
# Registry Providers
# ============================================================================

LOCAL: Final[str] = "local"

OPENAI: Final[str] = "openai"

OLLAMA: Final[str] = "ollama"

HUGGINGFACE: Final[str] = "huggingface"

AZURE: Final[str] = "azure"

SUPPORTED_REGISTRY_PROVIDERS: Final[
    frozenset[str]
] = frozenset(
    {
        LOCAL,
        OPENAI,
        OLLAMA,
        HUGGINGFACE,
        AZURE,
    }
)

# ============================================================================
# Configuration
# ============================================================================

DEFAULT_CACHE_SIZE: Final[int] = 1000

DEFAULT_REFRESH_INTERVAL: Final[int] = 300

DEFAULT_TIMEOUT: Final[int] = 30

DEFAULT_RETRIES: Final[int] = 3