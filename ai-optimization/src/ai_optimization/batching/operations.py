"""Operations for the ai_optimization.batching module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_optimization.batching.constants import (
    DEFAULT_BATCH_STRATEGY,
    DEFAULT_ENABLED,
    MAX_BATCH_NAME_LENGTH,
    MIN_BATCH_NAME_LENGTH,
    SUPPORTED_BATCH_STRATEGIES,
)
from ai_optimization.batching.exceptions import (
    BatchNotFoundError,
    BatchValidationError,
    DuplicateBatchError,
    UnsupportedBatchStrategyError,
)


@dataclass(slots=True, frozen=True)
class BatchDefinition:
    """Represents a batching configuration."""

    name: str
    size: int
    strategy: str = DEFAULT_BATCH_STRATEGY
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the batch definition."""
        normalized = self.name.strip()

        if not (
            MIN_BATCH_NAME_LENGTH
            <= len(normalized)
            <= MAX_BATCH_NAME_LENGTH
        ):
            raise BatchValidationError(
                "Batch name length is outside the allowed range."
            )

        if self.size <= 0:
            raise BatchValidationError(
                "Batch size must be greater than zero."
            )

        if self.strategy not in SUPPORTED_BATCH_STRATEGIES:
            raise UnsupportedBatchStrategyError(
                f"Unsupported batch strategy: {self.strategy!r}."
            )

        object.__setattr__(self, "name", normalized)


class BatchRegistry:
    """Registry for batch definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, BatchDefinition] = {}

    def register(self, batch: BatchDefinition) -> None:
        """Register a batch definition."""
        if batch.name in self._definitions:
            raise DuplicateBatchError(
                f"Batch {batch.name!r} is already registered."
            )

        self._definitions[batch.name] = batch

    def unregister(self, name: str) -> None:
        """Remove a batch definition."""
        if name not in self._definitions:
            raise BatchNotFoundError(
                f"Batch {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> BatchDefinition:
        """Return a registered batch definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise BatchNotFoundError(
                f"Batch {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a batch exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all registered batches."""
        self._definitions.clear()

    def list(self) -> tuple[BatchDefinition, ...]:
        """Return all registered batches."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return the number of registered batches."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a batch exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_batch(
    *,
    name: str,
    size: int,
    strategy: str = DEFAULT_BATCH_STRATEGY,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> BatchDefinition:
    """Build and validate a batch definition."""
    return BatchDefinition(
        name=name,
        size=size,
        strategy=strategy,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "BatchDefinition",
    "BatchRegistry",
    "build_batch",
]