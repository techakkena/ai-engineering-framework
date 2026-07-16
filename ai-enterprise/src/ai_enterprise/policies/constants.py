"""Constants for the ai_enterprise.policies module."""

from __future__ import annotations

from typing import Final

DEFAULT_POLICY_NAME: Final[str] = "default"
DEFAULT_POLICY_TYPE: Final[str] = "access"
DEFAULT_ENABLED: Final[bool] = True

ACCESS_POLICY: Final[str] = "access"
SECURITY_POLICY: Final[str] = "security"
RETENTION_POLICY: Final[str] = "retention"
COMPLIANCE_POLICY: Final[str] = "compliance"

SUPPORTED_POLICY_TYPES: Final[frozenset[str]] = frozenset(
    {
        ACCESS_POLICY,
        SECURITY_POLICY,
        RETENTION_POLICY,
        COMPLIANCE_POLICY,
    }
)

MIN_POLICY_NAME_LENGTH: Final[int] = 3
MAX_POLICY_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
RULES_KEY: Final[str] = "rules"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "ACCESS_POLICY",
    "COMPLIANCE_POLICY",
    "DEFAULT_ENABLED",
    "DEFAULT_POLICY_NAME",
    "DEFAULT_POLICY_TYPE",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "MAX_POLICY_NAME_LENGTH",
    "MIN_POLICY_NAME_LENGTH",
    "NAME_KEY",
    "RETENTION_POLICY",
    "RULES_KEY",
    "SECURITY_POLICY",
    "SUPPORTED_POLICY_TYPES",
    "TYPE_KEY",
]