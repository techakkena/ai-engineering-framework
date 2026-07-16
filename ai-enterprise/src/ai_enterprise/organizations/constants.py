"""Constants for the ai_enterprise.organizations module."""

from __future__ import annotations

from typing import Final

DEFAULT_ORGANIZATION_NAME: Final[str] = "organization"
DEFAULT_ORGANIZATION_TYPE: Final[str] = "enterprise"
DEFAULT_ENABLED: Final[bool] = True

ENTERPRISE_TYPE: Final[str] = "enterprise"
BUSINESS_TYPE: Final[str] = "business"
STARTUP_TYPE: Final[str] = "startup"
GOVERNMENT_TYPE: Final[str] = "government"

SUPPORTED_ORGANIZATION_TYPES: Final[frozenset[str]] = frozenset(
    {
        ENTERPRISE_TYPE,
        BUSINESS_TYPE,
        STARTUP_TYPE,
        GOVERNMENT_TYPE,
    }
)

MIN_ORGANIZATION_NAME_LENGTH: Final[int] = 1
MAX_ORGANIZATION_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
DOMAIN_KEY: Final[str] = "domain"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "BUSINESS_TYPE",
    "DEFAULT_ENABLED",
    "DEFAULT_ORGANIZATION_NAME",
    "DEFAULT_ORGANIZATION_TYPE",
    "DESCRIPTION_KEY",
    "DOMAIN_KEY",
    "ENABLED_KEY",
    "ENTERPRISE_TYPE",
    "GOVERNMENT_TYPE",
    "MAX_ORGANIZATION_NAME_LENGTH",
    "MIN_ORGANIZATION_NAME_LENGTH",
    "NAME_KEY",
    "STARTUP_TYPE",
    "SUPPORTED_ORGANIZATION_TYPES",
    "TYPE_KEY",
]