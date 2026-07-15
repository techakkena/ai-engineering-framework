"""
Constants for the ai_api.config module.

This module defines immutable constants used throughout the
configuration components of the AI API package.

The constants are framework-independent and provide sensible defaults
for API configuration, networking, environments, and runtime settings.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# API Defaults
# ============================================================================

DEFAULT_API_VERSION: Final[str] = "v1"

DEFAULT_API_PREFIX: Final[str] = "/api"

DEFAULT_API_NAME: Final[str] = "AI API"

DEFAULT_TIMEOUT: Final[int] = 30

# ============================================================================
# Network Configuration
# ============================================================================

DEFAULT_HOST: Final[str] = "127.0.0.1"

DEFAULT_PORT: Final[int] = 8000

DEFAULT_SCHEME: Final[str] = "http"

DEFAULT_HTTPS_SCHEME: Final[str] = "https"

# ============================================================================
# Runtime Environments
# ============================================================================

DEVELOPMENT_ENVIRONMENT: Final[str] = "development"

TESTING_ENVIRONMENT: Final[str] = "testing"

STAGING_ENVIRONMENT: Final[str] = "staging"

PRODUCTION_ENVIRONMENT: Final[str] = "production"

SUPPORTED_ENVIRONMENTS: Final[frozenset[str]] = frozenset(
    {
        DEVELOPMENT_ENVIRONMENT,
        TESTING_ENVIRONMENT,
        STAGING_ENVIRONMENT,
        PRODUCTION_ENVIRONMENT,
    }
)

# ============================================================================
# Logging
# ============================================================================

DEFAULT_LOG_LEVEL: Final[str] = "INFO"

SUPPORTED_LOG_LEVELS: Final[frozenset[str]] = frozenset(
    {
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    }
)

# ============================================================================
# Server Defaults
# ============================================================================

DEFAULT_WORKERS: Final[int] = 1

DEFAULT_KEEP_ALIVE: Final[int] = 5

DEFAULT_MAX_REQUEST_SIZE: Final[int] = 10 * 1024 * 1024

# ============================================================================
# Configuration Keys
# ============================================================================

HOST_KEY: Final[str] = "host"

PORT_KEY: Final[str] = "port"

ENVIRONMENT_KEY: Final[str] = "environment"

API_PREFIX_KEY: Final[str] = "api_prefix"

API_VERSION_KEY: Final[str] = "api_version"

TIMEOUT_KEY: Final[str] = "timeout"

LOG_LEVEL_KEY: Final[str] = "log_level"

# ============================================================================
# Configuration File Names
# ============================================================================

DEFAULT_CONFIG_FILE: Final[str] = "config.toml"

DEFAULT_ENV_FILE: Final[str] = ".env"

DEFAULT_SETTINGS_FILE: Final[str] = "settings.toml"