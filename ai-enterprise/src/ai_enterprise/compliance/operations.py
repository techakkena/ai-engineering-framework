"""Operations for the ai_enterprise.compliance module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_enterprise.compliance.constants import (
    DEFAULT_ENABLED,
    DEFAULT_STANDARD,
    MAX_COMPLIANCE_NAME_LENGTH,
    MIN_COMPLIANCE_NAME_LENGTH,
    SUPPORTED_COMPLIANCE_STANDARDS,
)
from ai_enterprise.compliance.exceptions import (
    ComplianceNotFoundError,
    ComplianceValidationError,
    DuplicateComplianceError,
    UnsupportedComplianceStandardError,
)


@dataclass(slots=True, frozen=True)
class ComplianceDefinition:
    """Represents a compliance configuration."""

    name: str
    standard: str = DEFAULT_STANDARD
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the compliance definition."""
        normalized = self.name.strip()

        if not (
            MIN_COMPLIANCE_NAME_LENGTH
            <= len(normalized)
            <= MAX_COMPLIANCE_NAME_LENGTH
        ):
            raise ComplianceValidationError(
                "Compliance name length is outside the allowed range."
            )

        if (
            self.standard
            not in SUPPORTED_COMPLIANCE_STANDARDS
        ):
            raise UnsupportedComplianceStandardError(
                f"Unsupported compliance standard: {self.standard!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized,
        )


class ComplianceRegistry:
    """Registry for compliance definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        self._definitions: dict[
            str,
            ComplianceDefinition,
        ] = {}

    def register(
        self,
        definition: ComplianceDefinition,
    ) -> None:
        if definition.name in self._definitions:
            raise DuplicateComplianceError(
                f"Compliance {definition.name!r} is already registered."
            )

        self._definitions[
            definition.name
        ] = definition

    def unregister(
        self,
        name: str,
    ) -> None:
        if name not in self._definitions:
            raise ComplianceNotFoundError(
                f"Compliance {name!r} is not registered."
            )

        del self._definitions[name]

    def get(
        self,
        name: str,
    ) -> ComplianceDefinition:
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise ComplianceNotFoundError(
                f"Compliance {name!r} is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        return name in self._definitions

    def clear(self) -> None:
        self._definitions.clear()

    def list(
        self,
    ) -> tuple[
        ComplianceDefinition,
        ...,
    ]:
        return tuple(
            self._definitions.values()
        )

    def __len__(self) -> int:
        return len(self._definitions)

    def __contains__(
        self,
        name: object,
    ) -> bool:
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_compliance(
    *,
    name: str,
    standard: str = DEFAULT_STANDARD,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> ComplianceDefinition:
    """Build a validated compliance definition."""

    return ComplianceDefinition(
        name=name,
        standard=standard,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "ComplianceDefinition",
    "ComplianceRegistry",
    "build_compliance",
]