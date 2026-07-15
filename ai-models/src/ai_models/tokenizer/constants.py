"""
Constants for ai_models.tokenizer.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Defaults
# ============================================================================

DEFAULT_TOKENIZER: Final[str] = "cl100k_base"

DEFAULT_TOKENIZER_PROVIDER: Final[str] = "openai"

DEFAULT_CONTEXT_WINDOW: Final[int] = 128000

# ============================================================================
# Providers
# ============================================================================

OPENAI: Final[str] = "openai"

ANTHROPIC: Final[str] = "anthropic"

GOOGLE: Final[str] = "google"

MISTRAL: Final[str] = "mistral"

GROQ: Final[str] = "groq"

OLLAMA: Final[str] = "ollama"

DEEPSEEK: Final[str] = "deepseek"

SUPPORTED_TOKENIZER_PROVIDERS: Final[
    frozenset[str]
] = frozenset(
    {
        OPENAI,
        ANTHROPIC,
        GOOGLE,
        MISTRAL,
        GROQ,
        OLLAMA,
        DEEPSEEK,
    }
)

# ============================================================================
# Common Tokenizers
# ============================================================================

CL100K_BASE: Final[str] = "cl100k_base"

O200K_BASE: Final[str] = "o200k_base"

P50K_BASE: Final[str] = "p50k_base"

R50K_BASE: Final[str] = "r50k_base"

GPT2: Final[str] = "gpt2"

SUPPORTED_TOKENIZERS: Final[
    frozenset[str]
] = frozenset(
    {
        CL100K_BASE,
        O200K_BASE,
        P50K_BASE,
        R50K_BASE,
        GPT2,
    }
)

# ============================================================================
# Context Windows
# ============================================================================

SMALL_CONTEXT_WINDOW: Final[int] = 8192

MEDIUM_CONTEXT_WINDOW: Final[int] = 32768

LARGE_CONTEXT_WINDOW: Final[int] = 128000

XLARGE_CONTEXT_WINDOW: Final[int] = 200000

# ============================================================================
# Configuration
# ============================================================================

DEFAULT_TIMEOUT: Final[int] = 30

DEFAULT_RETRIES: Final[int] = 3

DEFAULT_BATCH_SIZE: Final[int] = 100