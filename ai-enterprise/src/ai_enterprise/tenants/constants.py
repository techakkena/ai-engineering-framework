"""Constants for the ai_enterprise.tenants module."""

from __future__ import annotations

from typing import Final

DEFAULT_TENANT_NAME: Final[str] = "tenant"
DEFAULT_TENANT_PLAN: Final[str] = "standard"
DEFAULT_ENABLED: Final[bool] = True

STANDARD_PLAN: Final[str] = "standard"
PROFESSIONAL_PLAN: Final[str] = "professional"
ENTERPRISE_PLAN: Final[str] = "enterprise"
TRIAL_PLAN: Final[str] = "trial"

SUPPORTED_TENANT_PLANS: Final[frozenset[str]] = frozenset(
    {
        STANDARD_PLAN,
        PROFESSIONAL_PLAN,
        ENTERPRISE_PLAN,
        TRIAL_PLAN,
    }
)

MIN_TENANT_NAME_LENGTH: Final[int] = 1
MAX_TENANT_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
PLAN_KEY: Final[str] = "plan"
ORGANIZATION_KEY: Final[str] = "organization"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_ENABLED",
    "DEFAULT_TENANT_NAME",
    "DEFAULT_TENANT_PLAN",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "ENTERPRISE_PLAN",
    "MAX_TENANT_NAME_LENGTH",
    "MIN_TENANT_NAME_LENGTH",
    "NAME_KEY",
    "ORGANIZATION_KEY",
    "PLAN_KEY",
    "PROFESSIONAL_PLAN",
    "STANDARD_PLAN",
    "SUPPORTED_TENANT_PLANS",
    "TRIAL_PLAN",
]