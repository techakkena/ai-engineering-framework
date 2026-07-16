"""Role management for ai-enterprise."""

from __future__ import annotations

from ai_enterprise.roles.operations import (
    EnterpriseRole,
    RoleRegistry,
    build_role,
)

__all__ = [
    "EnterpriseRole",
    "RoleRegistry",
    "build_role",
]