"""
Constants for ai_models.utils.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Defaults
# ============================================================================

DEFAULT_VERSION: Final[str] = "1.0.0"

DEFAULT_ENCODING: Final[str] = "utf-8"

DEFAULT_UUID_PREFIX: Final[str] = "model"

# ============================================================================
# Encodings
# ============================================================================

UTF8: Final[str] = "utf-8"

UTF16: Final[str] = "utf-16"

ASCII: Final[str] = "ascii"

LATIN1: Final[str] = "latin-1"

SUPPORTED_ENCODINGS: Final[
    frozenset[str]
] = frozenset(
    {
        UTF8,
        UTF16,
        ASCII,
        LATIN1,
    }
)

# ============================================================================
# Limits
# ============================================================================

MIN_MODEL_NAME_LENGTH: Final[int] = 1

MAX_MODEL_NAME_LENGTH: Final[int] = 128

DEFAULT_TIMEOUT: Final[int] = 30

DEFAULT_RETRIES: Final[int] = 3