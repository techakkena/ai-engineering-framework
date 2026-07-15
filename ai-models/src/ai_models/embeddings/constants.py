"""
Constants for ai_models.embeddings.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Defaults
# ============================================================================

DEFAULT_EMBEDDING_MODEL: Final[str] = (
    "text-embedding-3-small"
)

DEFAULT_EMBEDDING_PROVIDER: Final[str] = "openai"

DEFAULT_EMBEDDING_DIMENSIONS: Final[int] = 1536

# ============================================================================
# Providers
# ============================================================================

OPENAI: Final[str] = "openai"

VOYAGE: Final[str] = "voyage"

COHERE: Final[str] = "cohere"

BGE: Final[str] = "bge"

E5: Final[str] = "e5"

INSTRUCTOR: Final[str] = "instructor"

OLLAMA: Final[str] = "ollama"

SUPPORTED_EMBEDDING_PROVIDERS: Final[
    frozenset[str]
] = frozenset(
    {
        OPENAI,
        VOYAGE,
        COHERE,
        BGE,
        E5,
        INSTRUCTOR,
        OLLAMA,
    }
)

# ============================================================================
# Configuration
# ============================================================================

DEFAULT_BATCH_SIZE: Final[int] = 100

DEFAULT_TIMEOUT: Final[int] = 60

DEFAULT_RETRIES: Final[int] = 3