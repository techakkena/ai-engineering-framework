"""Operations for the ai_plugins.validation module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_plugins.validation.constants import (
    DEFAULT_ENABLED,
    DEFAULT_VALIDATION_LEVEL,
    MAX_VALIDATION_NAME_LENGTH,
    MIN_VALIDATION_NAME_LENGTH,
    SUPPORTED_VALIDATION_LEVELS,
)
from ai_plugins.validation.exceptions import (
    DuplicateValidationError,
    UnsupportedValidationLevelError,
    ValidationDefinitionError,
    ValidationNotFoundError,
)


@dataclass(slots=True, frozen=True)
class ValidationDefinition:
    """Represents a plugin validation configuration."""

    name: str
    rule_count: int
    level: str = DEFAULT_VALIDATION_LEVEL
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the validation definition."""
        normalized = self.name.strip()

        if not (
            MIN_VALIDATION_NAME_LENGTH
            <= len(normalized)
            <= MAX_VALIDATION_NAME_LENGTH
        ):
            raise ValidationDefinitionError(
                "Validation name length is outside the allowed range."
            )

        if self.rule_count <= 0:
            raise ValidationDefinitionError(
                "Rule count must be greater than zero."
            )

        if self.level not in SUPPORTED_VALIDATION_LEVELS:
            raise UnsupportedValidationLevelError(
                f"Unsupported validation level: {self.level!r}."
            )

        object.__setattr__(self, "name", normalized)


class ValidationRegistry:
    """Registry for validation definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, ValidationDefinition] = {}

    def register(
        self,
        validation: ValidationDefinition,
    ) -> None:
        """Register a validation definition."""
        if validation.name in self._definitions:
            raise DuplicateValidationError(
                f"Validation {validation.name!r} is already registered."
            )

        self._definitions[validation.name] = validation

    def unregister(self, name: str) -> None:
        """Remove a validation definition."""
        if name not in self._definitions:
            raise ValidationNotFoundError(
                f"Validation {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> ValidationDefinition:
        """Return a validation definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise ValidationNotFoundError(
                f"Validation {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a validation exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all validations."""
        self._definitions.clear()

    def list(self) -> tuple[ValidationDefinition, ...]:
        """Return registered validations."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return registry size."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a validation exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_validation(
    *,
    name: str,
    rule_count: int,
    level: str = DEFAULT_VALIDATION_LEVEL,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> ValidationDefinition:
    """Build and validate a validation definition."""
    return ValidationDefinition(
        name=name,
        rule_count=rule_count,
        level=level,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "ValidationDefinition",
    "ValidationRegistry",
    "build_validation",
]