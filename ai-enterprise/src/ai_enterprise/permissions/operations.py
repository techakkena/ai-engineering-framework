"""Operations for the ai_enterprise.permissions module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_enterprise.permissions.constants import (
    DEFAULT_ENABLED,
    DEFAULT_PERMISSION_NAME,
    DEFAULT_RESOURCE,
    MAX_PERMISSION_NAME_LENGTH,
    MIN_PERMISSION_NAME_LENGTH,
    SUPPORTED_PERMISSION_NAMES,
)
from ai_enterprise.permissions.exceptions import (
    DuplicatePermissionError,
    PermissionNotFoundError,
    PermissionValidationError,
    UnsupportedPermissionError,
)


@dataclass(slots=True, frozen=True)
class EnterprisePermission:
    """Represents an enterprise permission."""

    name: str = DEFAULT_PERMISSION_NAME
    resource: str = DEFAULT_RESOURCE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the permission."""
        normalized_name = self.name.strip()
        normalized_resource = self.resource.strip()

        if not (
            MIN_PERMISSION_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_PERMISSION_NAME_LENGTH
        ):
            raise PermissionValidationError(
                "Permission name length is outside the allowed range."
            )

        if normalized_name not in SUPPORTED_PERMISSION_NAMES:
            raise UnsupportedPermissionError(
                f"Unsupported permission: {normalized_name!r}."
            )

        if not normalized_resource:
            raise PermissionValidationError(
                "Resource cannot be empty."
            )

        object.__setattr__(self, "name", normalized_name)
        object.__setattr__(
            self,
            "resource",
            normalized_resource,
        )


class PermissionRegistry:
    """Registry for enterprise permissions."""

    __slots__ = ("_permissions",)

    def __init__(self) -> None:
        self._permissions: dict[
            str,
            EnterprisePermission,
        ] = {}

    def register(
        self,
        permission: EnterprisePermission,
    ) -> None:
        if permission.name in self._permissions:
            raise DuplicatePermissionError(
                f"Permission {permission.name!r} is already registered."
            )

        self._permissions[permission.name] = permission

    def unregister(
        self,
        name: str,
    ) -> None:
        if name not in self._permissions:
            raise PermissionNotFoundError(
                f"Permission {name!r} is not registered."
            )

        del self._permissions[name]

    def get(
        self,
        name: str,
    ) -> EnterprisePermission:
        try:
            return self._permissions[name]
        except KeyError as exc:
            raise PermissionNotFoundError(
                f"Permission {name!r} is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._permissions

    def clear(self) -> None:
        self._permissions.clear()

    def list(
        self,
    ) -> tuple[
        EnterprisePermission,
        ...,
    ]:
        return tuple(self._permissions.values())

    def __len__(self) -> int:
        return len(self._permissions)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        return (
            isinstance(name, str)
            and name in self._permissions
        )


def build_permission(
    *,
    name: str,
    resource: str,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> EnterprisePermission:
    """Build a validated permission."""

    return EnterprisePermission(
        name=name,
        resource=resource,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "EnterprisePermission",
    "PermissionRegistry",
    "build_permission",
]