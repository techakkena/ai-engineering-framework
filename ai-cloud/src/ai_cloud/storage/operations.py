"""Operations for the ai_cloud.storage module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_cloud.storage.constants import (
    DEFAULT_ENABLED,
    DEFAULT_STORAGE_TYPE,
    MAX_STORAGE_NAME_LENGTH,
    MIN_STORAGE_NAME_LENGTH,
    SUPPORTED_STORAGE_TYPES,
)
from ai_cloud.storage.exceptions import (
    DuplicateStorageError,
    StorageNotFoundError,
    StorageValidationError,
    UnsupportedStorageTypeError,
)


@dataclass(slots=True, frozen=True)
class StorageDefinition:
    """Represents a cloud storage configuration."""

    name: str
    capacity: int
    storage_type: str = DEFAULT_STORAGE_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the storage definition."""
        normalized = self.name.strip()

        if not (
            MIN_STORAGE_NAME_LENGTH
            <= len(normalized)
            <= MAX_STORAGE_NAME_LENGTH
        ):
            raise StorageValidationError(
                "Storage name length is outside the allowed range."
            )

        if self.capacity <= 0:
            raise StorageValidationError(
                "Storage capacity must be greater than zero."
            )

        if (
            self.storage_type
            not in SUPPORTED_STORAGE_TYPES
        ):
            raise UnsupportedStorageTypeError(
                f"Unsupported storage type: "
                f"{self.storage_type!r}."
            )

        object.__setattr__(
            self,
            "name",
            normalized,
        )


class StorageRegistry:
    """Registry for storage definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[
            str,
            StorageDefinition,
        ] = {}

    def register(
        self,
        storage: StorageDefinition,
    ) -> None:
        """Register a storage definition."""
        if storage.name in self._definitions:
            raise DuplicateStorageError(
                f"Storage {storage.name!r} "
                "is already registered."
            )

        self._definitions[
            storage.name
        ] = storage

    def unregister(
        self,
        name: str,
    ) -> None:
        """Remove a storage definition."""
        if name not in self._definitions:
            raise StorageNotFoundError(
                f"Storage {name!r} "
                "is not registered."
            )

        del self._definitions[name]

    def get(
        self,
        name: str,
    ) -> StorageDefinition:
        """Return a storage definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise StorageNotFoundError(
                f"Storage {name!r} "
                "is not registered."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        """Return whether a storage exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all registered storage definitions."""
        self._definitions.clear()

    def list(
        self,
    ) -> tuple[
        StorageDefinition,
        ...,
    ]:
        """Return registered storage definitions."""
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
        """Return whether a storage exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_storage(
    *,
    name: str,
    capacity: int,
    storage_type: str = DEFAULT_STORAGE_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> StorageDefinition:
    """Build a validated storage definition."""

    return StorageDefinition(
        name=name,
        capacity=capacity,
        storage_type=storage_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "StorageDefinition",
    "StorageRegistry",
    "build_storage",
]