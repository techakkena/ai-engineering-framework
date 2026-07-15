"""
Framework-independent permission management.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ai_security.permissions.constants import (
    DEFAULT_ROLE,
    WILDCARD_PERMISSION,
)
from ai_security.permissions.exceptions import (
    PermissionDeniedError,
    RoleNotFoundError,
)


@dataclass(slots=True, frozen=True)
class Permission:
    """Represents a permission."""

    name: str


@dataclass(slots=True)
class Role:
    """Represents a role."""

    name: str = DEFAULT_ROLE
    permissions: set[str] = field(default_factory=set)


class PermissionManager:
    """
    Simple framework-independent RBAC manager.

    This implementation serves as the default reference
    implementation. More advanced adapters may integrate with
    enterprise IAM providers.
    """

    def __init__(self) -> None:
        self._roles: dict[str, Role] = {}

    def add_role(self, role: Role) -> None:
        """Register a role."""
        self._roles[role.name] = role

    def get_role(self, name: str) -> Role:
        """Retrieve a registered role."""
        if name not in self._roles:
            raise RoleNotFoundError(
                f"Role '{name}' was not found."
            )

        return self._roles[name]

    def has_permission(
        self,
        role_name: str,
        permission: str,
    ) -> bool:
        """Determine whether a role has a permission."""
        role = self.get_role(role_name)

        if (
            WILDCARD_PERMISSION in role.permissions
            or permission in role.permissions
        ):
            return True

        raise PermissionDeniedError(
            f"Permission '{permission}' denied for role "
            f"'{role_name}'."
        )

    def grant_permission(
        self,
        role_name: str,
        permission: str,
    ) -> None:
        """Grant a permission to a role."""
        role = self.get_role(role_name)
        role.permissions.add(permission)

    def revoke_permission(
        self,
        role_name: str,
        permission: str,
    ) -> None:
        """Revoke a permission from a role."""
        role = self.get_role(role_name)
        role.permissions.discard(permission)

    @property
    def role_count(self) -> int:
        """Return the number of registered roles."""
        return len(self._roles)