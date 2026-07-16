"""Operations for the ai_optimization.tuning module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_optimization.tuning.constants import (
    DEFAULT_ENABLED,
    DEFAULT_TUNING_STRATEGY,
    MAX_TUNING_NAME_LENGTH,
    MIN_TUNING_NAME_LENGTH,
    SUPPORTED_TUNING_STRATEGIES,
)
from ai_optimization.tuning.exceptions import (
    DuplicateTuningError,
    TuningNotFoundError,
    TuningValidationError,
    UnsupportedTuningStrategyError,
)


@dataclass(slots=True, frozen=True)
class TuningDefinition:
    """Represents a tuning configuration."""

    name: str
    iterations: int
    strategy: str = DEFAULT_TUNING_STRATEGY
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the tuning definition."""
        normalized = self.name.strip()

        if not (
            MIN_TUNING_NAME_LENGTH
            <= len(normalized)
            <= MAX_TUNING_NAME_LENGTH
        ):
            raise TuningValidationError(
                "Tuning name length is outside the allowed range."
            )

        if self.iterations <= 0:
            raise TuningValidationError(
                "Iterations must be greater than zero."
            )

        if self.strategy not in SUPPORTED_TUNING_STRATEGIES:
            raise UnsupportedTuningStrategyError(
                f"Unsupported tuning strategy: {self.strategy!r}."
            )

        object.__setattr__(self, "name", normalized)


class TuningRegistry:
    """Registry for tuning definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, TuningDefinition] = {}

    def register(self, tuning: TuningDefinition) -> None:
        """Register a tuning definition."""
        if tuning.name in self._definitions:
            raise DuplicateTuningError(
                f"Tuning {tuning.name!r} is already registered."
            )

        self._definitions[tuning.name] = tuning

    def unregister(self, name: str) -> None:
        """Remove a tuning definition."""
        if name not in self._definitions:
            raise TuningNotFoundError(
                f"Tuning {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> TuningDefinition:
        """Return a registered tuning definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise TuningNotFoundError(
                f"Tuning {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a tuning definition exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all registered tuning definitions."""
        self._definitions.clear()

    def list(self) -> tuple[TuningDefinition, ...]:
        """Return all registered tuning definitions."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return registry size."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a tuning definition exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_tuning(
    *,
    name: str,
    iterations: int,
    strategy: str = DEFAULT_TUNING_STRATEGY,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> TuningDefinition:
    """Build and validate a tuning definition."""
    return TuningDefinition(
        name=name,
        iterations=iterations,
        strategy=strategy,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "TuningDefinition",
    "TuningRegistry",
    "build_tuning",
]