"""Operations for the ai_enterprise.roles module."""

from __future__ import annotations

from dataclasses import dataclass, field

from ai_enterprise.roles.constants import (
    DEFAULT_ENABLED,
    DEFAULT_ROLE_NAME,
    MAX_ROLE_NAME_LENGTH,
    MIN_ROLE_NAME_LENGTH,
    SUPPORTED_ROLE_NAMES,
)
from ai_enterprise.roles.exceptions import (
    DuplicateRoleError,
    RoleNotFoundError,
    RoleValidationError,
    UnsupportedRoleError,
)


@dataclass(slots=True, frozen=True)
class EnterpriseRole:
    """Represents an enterprise role."""

    name: str = DEFAULT_ROLE_NAME
    permissions: tuple[str, ...] = field(default_factory=tuple)
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the role."""
        normalized = self.name.strip()

        if not (
            MIN_ROLE_NAME_LENGTH
            <= len(normalized)
            <= MAX_ROLE_NAME_LENGTH
        ):
            raise RoleValidationError(
                "Role name length is outside the allowed range."
            )

        if normalized not in SUPPORTED_ROLE_NAMES:
            raise UnsupportedRoleError(
                f"Unsupported role: {normalized!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized,
        )


class RoleRegistry:
    """Registry for enterprise roles."""

    __slots__ = ("_roles",)

    def __init__(self) -> None:
        self._roles: dict[str, EnterpriseRole] = {}

    def register(
        self,
        role: EnterpriseRole,
    ) -> None:
        if role.name in self._roles:
            raise DuplicateRoleError(
                f"Role {role.name!r} is already registered."
            )

        self._roles[role.name] = role

    def unregister(
        self,
        name: str,
    ) -> None:
        if name not in self._roles:
            raise RoleNotFoundError(
                f"Role {name!r} is not registered."
            )

        del self._roles[name]

    def get(
        self,
        name: str,
    ) -> EnterpriseRole:
        try:
            return self._roles[name]
        except KeyError as exc:
            raise RoleNotFoundError(
                f"Role {name!r} is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._roles

    def clear(self) -> None:
        self._roles.clear()

    def list(
        self,
    ) -> tuple[EnterpriseRole, ...]:
        return tuple(self._roles.values())

    def __len__(self) -> int:
        return len(self._roles)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        return (
            isinstance(name, str)
            and name in self._roles
        )


def build_role(
    *,
    name: str,
    permissions: tuple[str, ...] = (),
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> EnterpriseRole:
    """Build a validated enterprise role."""

    return EnterpriseRole(
        name=name,
        permissions=permissions,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "EnterpriseRole",
    "RoleRegistry",
    "build_role",
]