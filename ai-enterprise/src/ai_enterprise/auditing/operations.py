"""Operations for the ai_enterprise.auditing module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_enterprise.auditing.constants import (
    DEFAULT_AUDIT_LEVEL,
    DEFAULT_ENABLED,
    MAX_AUDIT_NAME_LENGTH,
    MIN_AUDIT_NAME_LENGTH,
    SUPPORTED_AUDIT_LEVELS,
)
from ai_enterprise.auditing.exceptions import (
    AuditNotFoundError,
    AuditValidationError,
    DuplicateAuditError,
    UnsupportedAuditLevelError,
)


@dataclass(slots=True, frozen=True)
class AuditDefinition:
    """Represents an audit configuration."""

    name: str
    level: str = DEFAULT_AUDIT_LEVEL
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the audit definition."""
        normalized_name = self.name.strip()

        if not (
            MIN_AUDIT_NAME_LENGTH
            <= len(normalized_name)
            <= MAX_AUDIT_NAME_LENGTH
        ):
            raise AuditValidationError(
                "Audit name length is outside the allowed range."
            )

        if self.level not in SUPPORTED_AUDIT_LEVELS:
            raise UnsupportedAuditLevelError(
                f"Unsupported audit level: {self.level!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized_name,
        )


class AuditRegistry:
    """Registry for audit definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[
            str,
            AuditDefinition,
        ] = {}

    def register(
        self,
        definition: AuditDefinition,
    ) -> None:
        """Register an audit definition."""
        if definition.name in self._definitions:
            raise DuplicateAuditError(
                f"Audit {definition.name!r} is already registered."
            )

        self._definitions[
            definition.name
        ] = definition

    def unregister(
        self,
        name: str,
    ) -> None:
        """Remove an audit definition."""
        if name not in self._definitions:
            raise AuditNotFoundError(
                f"Audit {name!r} is not registered."
            )

        del self._definitions[name]

    def get(
        self,
        name: str,
    ) -> AuditDefinition:
        """Return an audit definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise AuditNotFoundError(
                f"Audit {name!r} is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        """Return whether an audit exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all audit definitions."""
        self._definitions.clear()

    def list(
        self,
    ) -> tuple[
        AuditDefinition,
        ...,
    ]:
        """Return all registered audit definitions."""
        return tuple(
            self._definitions.values()
        )

    def __len__(self) -> int:
        """Return registry size."""
        return len(self._definitions)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        """Return membership."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_audit(
    *,
    name: str,
    level: str = DEFAULT_AUDIT_LEVEL,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> AuditDefinition:
    """Build a validated audit definition."""

    return AuditDefinition(
        name=name,
        level=level,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "AuditDefinition",
    "AuditRegistry",
    "build_audit",
]