"""Operations for the ai_analytics.aggregation module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_analytics.aggregation.constants import (
    DEFAULT_AGGREGATION_TYPE,
    DEFAULT_ENABLED,
    MAX_AGGREGATION_NAME_LENGTH,
    MIN_AGGREGATION_NAME_LENGTH,
    SUPPORTED_AGGREGATION_TYPES,
)
from ai_analytics.aggregation.exceptions import (
    AggregationNotFoundError,
    AggregationValidationError,
    DuplicateAggregationError,
    UnsupportedAggregationTypeError,
)


@dataclass(slots=True, frozen=True)
class AggregationDefinition:
    """Represents an aggregation definition."""

    name: str
    field: str
    aggregation_type: str = DEFAULT_AGGREGATION_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the aggregation definition."""
        normalized = self.name.strip()

        if not (
            MIN_AGGREGATION_NAME_LENGTH
            <= len(normalized)
            <= MAX_AGGREGATION_NAME_LENGTH
        ):
            raise AggregationValidationError(
                "Aggregation name length is outside the allowed range."
            )

        if not self.field.strip():
            raise AggregationValidationError(
                "Aggregation field cannot be empty."
            )

        if (
            self.aggregation_type
            not in SUPPORTED_AGGREGATION_TYPES
        ):
            raise UnsupportedAggregationTypeError(
                f"Unsupported aggregation type: "
                f"{self.aggregation_type!r}."
            )

        object.__setattr__(self, "name", normalized)
        object.__setattr__(
            self,
            "field",
            self.field.strip(),
        )


class AggregationRegistry:
    """Registry for aggregation definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[
            str,
            AggregationDefinition,
        ] = {}

    def register(
        self,
        aggregation: AggregationDefinition,
    ) -> None:
        """Register an aggregation."""
        if aggregation.name in self._definitions:
            raise DuplicateAggregationError(
                f"Aggregation "
                f"{aggregation.name!r} is already registered."
            )

        self._definitions[aggregation.name] = aggregation

    def unregister(self, name: str) -> None:
        """Remove an aggregation."""
        if name not in self._definitions:
            raise AggregationNotFoundError(
                f"Aggregation {name!r} is not registered."
            )

        del self._definitions[name]

    def get(
        self,
        name: str,
    ) -> AggregationDefinition:
        """Return an aggregation."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise AggregationNotFoundError(
                f"Aggregation {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether an aggregation exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all aggregations."""
        self._definitions.clear()

    def list(self) -> tuple[
        AggregationDefinition,
        ...,
    ]:
        """Return registered aggregations."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return registry size."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether an aggregation exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_aggregation(
    *,
    name: str,
    field: str,
    aggregation_type: str = DEFAULT_AGGREGATION_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> AggregationDefinition:
    """Build a validated aggregation."""

    return AggregationDefinition(
        name=name,
        field=field,
        aggregation_type=aggregation_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "AggregationDefinition",
    "AggregationRegistry",
    "build_aggregation",
]