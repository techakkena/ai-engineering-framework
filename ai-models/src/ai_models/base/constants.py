"""
Constants for ai_models.base.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Defaults
# ============================================================================

DEFAULT_MODEL_NAME: Final[str] = "model"

DEFAULT_MODEL_PROVIDER: Final[str] = "openai"

DEFAULT_MODEL_TYPE: Final[str] = "chat"

# ============================================================================
# Model Types
# ============================================================================

CHAT_MODEL: Final[str] = "chat"

EMBEDDING_MODEL: Final[str] = "embedding"

VISION_MODEL: Final[str] = "vision"

AUDIO_MODEL: Final[str] = "audio"

MULTIMODAL_MODEL: Final[str] = "multimodal"

SUPPORTED_MODEL_TYPES: Final[frozenset[str]] = frozenset(
    {
        CHAT_MODEL,
        EMBEDDING_MODEL,
        VISION_MODEL,
        AUDIO_MODEL,
        MULTIMODAL_MODEL,
    }
)

# ============================================================================
# Configuration
# ============================================================================

DEFAULT_MAX_TOKENS: Final[int] = 4096

DEFAULT_TEMPERATURE: Final[float] = 0.7

DEFAULT_TIMEOUT: Final[int] = 60