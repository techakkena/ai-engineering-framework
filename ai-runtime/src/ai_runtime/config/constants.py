"""
Constants for ai_runtime.config.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Configuration Defaults
# ============================================================================

DEFAULT_CONFIG_NAME: Final[str] = "runtime-config"

DEFAULT_CONFIG_VERSION: Final[str] = "1.0.0"

DEFAULT_ENVIRONMENT: Final[str] = "development"

# ============================================================================
# Environments
# ============================================================================

DEVELOPMENT: Final[str] = "development"

TESTING: Final[str] = "testing"

STAGING: Final[str] = "staging"

PRODUCTION: Final[str] = "production"

SUPPORTED_ENVIRONMENTS: Final[frozenset[str]] = frozenset(
    {
        DEVELOPMENT,
        TESTING,
        STAGING,
        PRODUCTION,
    }
)

# ============================================================================
# Runtime Configuration
# ============================================================================

DEFAULT_HOST: Final[str] = "127.0.0.1"

DEFAULT_PORT: Final[int] = 8000

DEFAULT_LOG_LEVEL: Final[str] = "INFO"

DEFAULT_WORKERS: Final[int] = 4

DEFAULT_DEBUG: Final[bool] = False