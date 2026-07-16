"""Operations for the ai_testing.snapshots module."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ai_testing.snapshots.constants import (
    DEFAULT_ENABLED,
    DEFAULT_FORMAT,
    MAX_SNAPSHOT_NAME_LENGTH,
    MIN_SNAPSHOT_NAME_LENGTH,
    SUPPORTED_FORMATS,
)
from ai_testing.snapshots.exceptions import (
    DuplicateSnapshotError,
    SnapshotNotFoundError,
    SnapshotValidationError,
    UnsupportedSnapshotFormatError,
)


@dataclass(slots=True, frozen=True)
class SnapshotDefinition:
    """Represents a snapshot definition."""

    name: str
    content: Any
    format: str = DEFAULT_FORMAT
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the snapshot definition."""
        normalized = self.name.strip()

        if not (
            MIN_SNAPSHOT_NAME_LENGTH
            <= len(normalized)
            <= MAX_SNAPSHOT_NAME_LENGTH
        ):
            raise SnapshotValidationError(
                "Snapshot name length is outside the allowed range."
            )

        if self.format not in SUPPORTED_FORMATS:
            raise UnsupportedSnapshotFormatError(
                f"Unsupported snapshot format: {self.format!r}."
            )

        object.__setattr__(self, "name", normalized)


class SnapshotRegistry:
    """Registry for snapshot definitions."""

    __slots__ = ("_snapshots",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._snapshots: dict[str, SnapshotDefinition] = {}

    def register(self, snapshot: SnapshotDefinition) -> None:
        """Register a snapshot."""
        if snapshot.name in self._snapshots:
            raise DuplicateSnapshotError(
                f"Snapshot {snapshot.name!r} is already registered."
            )

        self._snapshots[snapshot.name] = snapshot

    def unregister(self, name: str) -> None:
        """Remove a snapshot."""
        if name not in self._snapshots:
            raise SnapshotNotFoundError(
                f"Snapshot {name!r} is not registered."
            )

        del self._snapshots[name]

    def get(self, name: str) -> SnapshotDefinition:
        """Return a registered snapshot."""
        try:
            return self._snapshots[name]
        except KeyError as exc:
            raise SnapshotNotFoundError(
                f"Snapshot {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Determine whether a snapshot exists."""
        return name in self._snapshots

    def clear(self) -> None:
        """Remove all snapshots."""
        self._snapshots.clear()

    def list(self) -> tuple[SnapshotDefinition, ...]:
        """Return all registered snapshots."""
        return tuple(self._snapshots.values())

    def __len__(self) -> int:
        """Return the number of registered snapshots."""
        return len(self._snapshots)

    def __contains__(self, name: object) -> bool:
        """Return whether a snapshot exists."""
        return isinstance(name, str) and name in self._snapshots


def build_snapshot(
    *,
    name: str,
    content: Any,
    format: str = DEFAULT_FORMAT,
    enabled: bool = DEFAULT_ENABLED,
) -> SnapshotDefinition:
    """Build and validate a snapshot definition."""
    return SnapshotDefinition(
        name=name,
        content=content,
        format=format,
        enabled=enabled,
    )


__all__ = [
    "SnapshotDefinition",
    "SnapshotRegistry",
    "build_snapshot",
]