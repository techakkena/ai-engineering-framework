"""
Constants for ai_models.vision.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Defaults
# ============================================================================

DEFAULT_VISION_MODEL: Final[str] = "gpt-5-vision"

DEFAULT_VISION_PROVIDER: Final[str] = "openai"

DEFAULT_IMAGE_DETAIL: Final[str] = "auto"

# ============================================================================
# Providers
# ============================================================================

OPENAI: Final[str] = "openai"

GOOGLE: Final[str] = "google"

ANTHROPIC: Final[str] = "anthropic"

OLLAMA: Final[str] = "ollama"

SUPPORTED_VISION_PROVIDERS: Final[
    frozenset[str]
] = frozenset(
    {
        OPENAI,
        GOOGLE,
        ANTHROPIC,
        OLLAMA,
    }
)

# ============================================================================
# Image Detail
# ============================================================================

LOW_DETAIL: Final[str] = "low"

HIGH_DETAIL: Final[str] = "high"

AUTO_DETAIL: Final[str] = "auto"

SUPPORTED_IMAGE_DETAILS: Final[
    frozenset[str]
] = frozenset(
    {
        LOW_DETAIL,
        HIGH_DETAIL,
        AUTO_DETAIL,
    }
)

# ============================================================================
# Configuration
# ============================================================================

DEFAULT_TIMEOUT: Final[int] = 60

DEFAULT_RETRIES: Final[int] = 3