"""
Constants for ai_models.chat.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Defaults
# ============================================================================

DEFAULT_CHAT_MODEL: Final[str] = "gpt-5"

DEFAULT_TEMPERATURE: Final[float] = 0.7

DEFAULT_MAX_OUTPUT_TOKENS: Final[int] = 4096

# ============================================================================
# Providers
# ============================================================================

OPENAI: Final[str] = "openai"

ANTHROPIC: Final[str] = "anthropic"

GOOGLE: Final[str] = "google"

GROQ: Final[str] = "groq"

MISTRAL: Final[str] = "mistral"

OLLAMA: Final[str] = "ollama"

DEEPSEEK: Final[str] = "deepseek"

SUPPORTED_CHAT_PROVIDERS: Final[frozenset[str]] = frozenset(
    {
        OPENAI,
        ANTHROPIC,
        GOOGLE,
        GROQ,
        MISTRAL,
        OLLAMA,
        DEEPSEEK,
    }
)

# ============================================================================
# Limits
# ============================================================================

DEFAULT_TIMEOUT: Final[int] = 60

DEFAULT_RETRIES: Final[int] = 3