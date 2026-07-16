"""Operations for the ai_testing.data module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_testing.data.constants import (
    DEFAULT_ENABLED,
    MAX_DATASET_NAME_LENGTH,
    MIN_DATASET_NAME_LENGTH,
)
from ai_testing.data.exceptions import (
    DataNotFoundError,
    DataValidationError,
    DuplicateDataError,
)


@dataclass(slots=True, frozen=True)
class DataSet:
    """Represents a reusable testing dataset."""

    name: str
    data: tuple[Any, ...]
    description: str = ""
    enabled: bool = DEFAULT_ENABLED
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the dataset."""
        normalized = self.name.strip()

        if not (
            MIN_DATASET_NAME_LENGTH
            <= len(normalized)
            <= MAX_DATASET_NAME_LENGTH
        ):
            raise DataValidationError(
                "Dataset name length is outside the allowed range."
            )

        object.__setattr__(self, "name", normalized)


class DataRegistry:
    """Registry for datasets."""

    __slots__ = ("_datasets",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._datasets: dict[str, DataSet] = {}

    def register(self, dataset: DataSet) -> None:
        """Register a dataset."""
        if dataset.name in self._datasets:
            raise DuplicateDataError(
                f"Dataset {dataset.name!r} is already registered."
            )

        self._datasets[dataset.name] = dataset

    def unregister(self, name: str) -> None:
        """Remove a dataset."""
        if name not in self._datasets:
            raise DataNotFoundError(
                f"Dataset {name!r} is not registered."
            )

        del self._datasets[name]

    def get(self, name: str) -> DataSet:
        """Return a registered dataset."""
        try:
            return self._datasets[name]
        except KeyError as exc:
            raise DataNotFoundError(
                f"Dataset {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a dataset exists."""
        return name in self._datasets

    def clear(self) -> None:
        """Remove all datasets."""
        self._datasets.clear()

    def list(self) -> tuple[DataSet, ...]:
        """Return all registered datasets."""
        return tuple(self._datasets.values())

    def __len__(self) -> int:
        """Return the number of registered datasets."""
        return len(self._datasets)

    def __contains__(self, name: object) -> bool:
        """Return whether a dataset exists."""
        return isinstance(name, str) and name in self._datasets


def build_dataset(
    *,
    name: str,
    data: tuple[Any, ...],
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
    metadata: dict[str, Any] | None = None,
) -> DataSet:
    """Build a validated dataset."""

    return DataSet(
        name=name,
        data=data,
        description=description,
        enabled=enabled,
        metadata={} if metadata is None else metadata,
    )


__all__ = [
    "DataRegistry",
    "DataSet",
    "build_dataset",
]