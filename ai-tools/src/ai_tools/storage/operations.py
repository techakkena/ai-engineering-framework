from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class StorageObject:
    """Represents a stored object."""

    key: str
    data: bytes


class StorageClient:
    """Simple in-memory storage client."""

    def __init__(self) -> None:
        self._objects: dict[str, StorageObject] = {}

    def put(
        self,
        obj: StorageObject,
    ) -> None:
        """Store an object."""
        self._objects[obj.key] = obj

    def get(
        self,
        key: str,
    ) -> StorageObject | None:
        """Retrieve an object."""
        return self._objects.get(key)

    def delete(
        self,
        key: str,
    ) -> None:
        """Delete an object."""
        self._objects.pop(key, None)

    def exists(
        self,
        key: str,
    ) -> bool:
        """Return whether an object exists."""
        return key in self._objects

    @property
    def object_count(self) -> int:
        """Return number of stored objects."""
        return len(self._objects)
