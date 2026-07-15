"""
Constants for ai_runtime.utils.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Encoding
# ============================================================================

DEFAULT_ENCODING: Final[str] = "utf-8"

SUPPORTED_ENCODINGS: Final[frozenset[str]] = frozenset(
    {
        "utf-8",
        "utf-16",
        "utf-32",
        "ascii",
        "latin-1",
    }
)

# ============================================================================
# Runtime
# ============================================================================

DEFAULT_TIMEOUT: Final[int] = 30

UUID_LENGTH: Final[int] = 36

REQUEST_ID_PREFIX: Final[str] = "req"

RUNTIME_ID_PREFIX: Final[str] = "runtime"

# ============================================================================
# Validation
# ============================================================================

IDENTIFIER_PATTERN: Final[str] = (
    r"^[A-Za-z_][A-Za-z0-9_-]*$"
)