"""Constants for the ai_enterprise.compliance module."""

from __future__ import annotations

from typing import Final

DEFAULT_COMPLIANCE_NAME: Final[str] = "compliance"
DEFAULT_STANDARD: Final[str] = "iso27001"
DEFAULT_ENABLED: Final[bool] = True

ISO27001_STANDARD: Final[str] = "iso27001"
SOC2_STANDARD: Final[str] = "soc2"
GDPR_STANDARD: Final[str] = "gdpr"
HIPAA_STANDARD: Final[str] = "hipaa"

SUPPORTED_COMPLIANCE_STANDARDS: Final[frozenset[str]] = frozenset(
    {
        ISO27001_STANDARD,
        SOC2_STANDARD,
        GDPR_STANDARD,
        HIPAA_STANDARD,
    }
)

MIN_COMPLIANCE_NAME_LENGTH: Final[int] = 3
MAX_COMPLIANCE_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
STANDARD_KEY: Final[str] = "standard"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_COMPLIANCE_NAME",
    "DEFAULT_STANDARD",
    "DEFAULT_ENABLED",
    "ISO27001_STANDARD",
    "SOC2_STANDARD",
    "GDPR_STANDARD",
    "HIPAA_STANDARD",
    "SUPPORTED_COMPLIANCE_STANDARDS",
    "MIN_COMPLIANCE_NAME_LENGTH",
    "MAX_COMPLIANCE_NAME_LENGTH",
    "NAME_KEY",
    "STANDARD_KEY",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
]