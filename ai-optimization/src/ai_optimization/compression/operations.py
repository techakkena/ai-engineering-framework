"""Operations for the ai_optimization.compression module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_optimization.compression.constants import (
    DEFAULT_COMPRESSION_TYPE,
    DEFAULT_ENABLED,
    MAX_COMPRESSION_NAME_LENGTH,
    MIN_COMPRESSION_NAME_LENGTH,
    SUPPORTED_COMPRESSION_TYPES,
)
from ai_optimization.compression.exceptions import (
    CompressionNotFoundError,
    CompressionValidationError,
    DuplicateCompressionError,
    UnsupportedCompressionTypeError,
)


@dataclass(slots=True, frozen=True)
class CompressionDefinition:
    """Represents a compression configuration."""

    name: str
    level: int
    compression_type: str = DEFAULT_COMPRESSION_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the compression definition."""
        normalized = self.name.strip()

        if not (
            MIN_COMPRESSION_NAME_LENGTH
            <= len(normalized)
            <= MAX_COMPRESSION_NAME_LENGTH
        ):
            raise CompressionValidationError(
                "Compression name length is outside the allowed range."
            )

        if not 1 <= self.level <= 9:
            raise CompressionValidationError(
                "Compression level must be between 1 and 9."
            )

        if (
            self.compression_type
            not in SUPPORTED_COMPRESSION_TYPES
        ):
            raise UnsupportedCompressionTypeError(
                f"Unsupported compression type: "
                f"{self.compression_type!r}."
            )

        object.__setattr__(self, "name", normalized)


class CompressionRegistry:
    """Registry for compression definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[
            str,
            CompressionDefinition,
        ] = {}

    def register(
        self,
        compression: CompressionDefinition,
    ) -> None:
        """Register a compression definition."""
        if compression.name in self._definitions:
            raise DuplicateCompressionError(
                f"Compression "
                f"{compression.name!r} "
                "is already registered."
            )

        self._definitions[
            compression.name
        ] = compression

    def unregister(self, name: str) -> None:
        """Remove a compression definition."""
        if name not in self._definitions:
            raise CompressionNotFoundError(
                f"Compression {name!r} "
                "is not registered."
            )

        del self._definitions[name]

    def get(
        self,
        name: str,
    ) -> CompressionDefinition:
        """Return a compression definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise CompressionNotFoundError(
                f"Compression {name!r} "
                "is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a compression exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all compressions."""
        self._definitions.clear()

    def list(
        self,
    ) -> tuple[
        CompressionDefinition,
        ...,
    ]:
        """Return registered compressions."""
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
        """Return whether a compression exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_compression(
    *,
    name: str,
    level: int,
    compression_type: str = DEFAULT_COMPRESSION_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> CompressionDefinition:
    """Build a validated compression."""

    return CompressionDefinition(
        name=name,
        level=level,
        compression_type=compression_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "CompressionDefinition",
    "CompressionRegistry",
    "build_compression",
]