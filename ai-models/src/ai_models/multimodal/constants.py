"""
Constants for ai_models.multimodal.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Defaults
# ============================================================================

DEFAULT_MULTIMODAL_MODEL: Final[str] = "gpt-5"

DEFAULT_MULTIMODAL_PROVIDER: Final[str] = "openai"

DEFAULT_PRIMARY_MODALITY: Final[str] = "text"

DEFAULT_MAX_MODALITIES: Final[int] = 5

# ============================================================================
# Providers
# ============================================================================

OPENAI: Final[str] = "openai"

GOOGLE: Final[str] = "google"

ANTHROPIC: Final[str] = "anthropic"

OLLAMA: Final[str] = "ollama"

AZURE: Final[str] = "azure"

SUPPORTED_MULTIMODAL_PROVIDERS: Final[
    frozenset[str]
] = frozenset(
    {
        OPENAI,
        GOOGLE,
        ANTHROPIC,
        OLLAMA,
        AZURE,
    }
)

# ============================================================================
# Input Modalities
# ============================================================================

TEXT_INPUT: Final[str] = "text"

IMAGE_INPUT: Final[str] = "image"

AUDIO_INPUT: Final[str] = "audio"

VIDEO_INPUT: Final[str] = "video"

DOCUMENT_INPUT: Final[str] = "document"

SUPPORTED_INPUT_MODALITIES: Final[
    frozenset[str]
] = frozenset(
    {
        TEXT_INPUT,
        IMAGE_INPUT,
        AUDIO_INPUT,
        VIDEO_INPUT,
        DOCUMENT_INPUT,
    }
)

# ============================================================================
# Output Modalities
# ============================================================================

TEXT_OUTPUT: Final[str] = "text"

IMAGE_OUTPUT: Final[str] = "image"

AUDIO_OUTPUT: Final[str] = "audio"

JSON_OUTPUT: Final[str] = "json"

STRUCTURED_OUTPUT: Final[str] = "structured"

SUPPORTED_OUTPUT_MODALITIES: Final[
    frozenset[str]
] = frozenset(
    {
        TEXT_OUTPUT,
        IMAGE_OUTPUT,
        AUDIO_OUTPUT,
        JSON_OUTPUT,
        STRUCTURED_OUTPUT,
    }
)

# ============================================================================
# Limits
# ============================================================================

DEFAULT_MAX_IMAGES: Final[int] = 20

DEFAULT_MAX_AUDIO_FILES: Final[int] = 10

DEFAULT_MAX_DOCUMENTS: Final[int] = 25

DEFAULT_MAX_VIDEO_FILES: Final[int] = 5

# ============================================================================
# Configuration
# ============================================================================

DEFAULT_TIMEOUT: Final[int] = 60

DEFAULT_RETRIES: Final[int] = 3

DEFAULT_STREAMING: Final[bool] = False

DEFAULT_ENABLE_CACHE: Final[bool] = True