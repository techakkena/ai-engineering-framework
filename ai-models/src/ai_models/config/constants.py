"""
Constants for ai_models.config.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Configuration Defaults
# ============================================================================

DEFAULT_MODEL_CONFIG_NAME: Final[str] = "default"

DEFAULT_TEMPERATURE: Final[float] = 0.7

DEFAULT_MAX_TOKENS: Final[int] = 4096

DEFAULT_TOP_P: Final[float] = 1.0

DEFAULT_FREQUENCY_PENALTY: Final[float] = 0.0

DEFAULT_PRESENCE_PENALTY: Final[float] = 0.0

DEFAULT_STREAM: Final[bool] = False

DEFAULT_TIMEOUT: Final[int] = 60

DEFAULT_RETRIES: Final[int] = 3

# ============================================================================
# Environments
# ============================================================================

DEVELOPMENT: Final[str] = "development"

TESTING: Final[str] = "testing"

STAGING: Final[str] = "staging"

PRODUCTION: Final[str] = "production"

SUPPORTED_ENVIRONMENTS: Final[
    frozenset[str]
] = frozenset(
    {
        DEVELOPMENT,
        TESTING,
        STAGING,
        PRODUCTION,
    }
)

# ============================================================================
# Response Formats
# ============================================================================

TEXT_RESPONSE: Final[str] = "text"

JSON_RESPONSE: Final[str] = "json"

STRUCTURED_RESPONSE: Final[str] = "structured"

SUPPORTED_RESPONSE_FORMATS: Final[
    frozenset[str]
] = frozenset(
    {
        TEXT_RESPONSE,
        JSON_RESPONSE,
        STRUCTURED_RESPONSE,
    }
)

# ============================================================================
# Tool Choice
# ============================================================================

AUTO_TOOL_CHOICE: Final[str] = "auto"

NONE_TOOL_CHOICE: Final[str] = "none"

REQUIRED_TOOL_CHOICE: Final[str] = "required"

SUPPORTED_TOOL_CHOICES: Final[
    frozenset[str]
] = frozenset(
    {
        AUTO_TOOL_CHOICE,
        NONE_TOOL_CHOICE,
        REQUIRED_TOOL_CHOICE,
    }
)

# ============================================================================
# Limits
# ============================================================================

MIN_TEMPERATURE: Final[float] = 0.0

MAX_TEMPERATURE: Final[float] = 2.0

MIN_MAX_TOKENS: Final[int] = 1

MAX_MAX_TOKENS: Final[int] = 1_000_000

# ============================================================================
# Retry Configuration
# ============================================================================

MIN_RETRIES: Final[int] = 0

MAX_RETRIES: Final[int] = 10