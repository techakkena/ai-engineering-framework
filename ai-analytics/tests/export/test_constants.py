"""Operations for the ai_analytics.export module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_analytics.export.constants import (
    DEFAULT_ENABLED,
    DEFAULT_EXPORT_FORMAT,
    MAX_EXPORT_NAME_LENGTH,
    MIN_EXPORT_NAME_LENGTH,
    SUPPORTED_EXPORT_FORMATS,
)
from ai_analytics.export.exceptions import (
    DuplicateExportError,
    ExportNotFoundError,
    ExportValidationError,
    UnsupportedExportFormatError,
)


@dataclass(slots=True, frozen=True)
class ExportDefinition:
    """Represents an export definition."""

    name: str
    destination: str
    export_format: str = DEFAULT_EXPORT_FORMAT
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the export definition."""
        normalized = self.name.strip()

        if not (
            MIN_EXPORT_NAME_LENGTH
            <= len(normalized)
            <= MAX_EXPORT_NAME_LENGTH
        ):
            raise ExportValidationError(
                "Export name length is outside the allowed range."
            )

        if not self.destination.strip():
            raise ExportValidationError(
                "Export destination cannot be empty."
            )

        if self.export_format not in SUPPORTED_EXPORT_FORMATS:
            raise UnsupportedExportFormatError(
                f"Unsupported export format: {self.export_format!r}."
            )

        object.__setattr__(self, "name", normalized)
        object.__setattr__(
            self,
            "destination",
            self.destination.strip(),
        )


class ExportRegistry:
    """Registry for export definitions."""

    __slots__ = ("_exports",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._exports: dict[str, ExportDefinition] = {}

    def register(self, export: ExportDefinition) -> None:
        """Register an export."""
        if export.name in self._exports:
            raise DuplicateExportError(
                f"Export {export.name!r} is already registered."
            )

        self._exports[export.name] = export

    def unregister(self, name: str) -> None:
        """Remove an export."""
        if name not in self._exports:
            raise ExportNotFoundError(
                f"Export {name!r} is not registered."
            )

        del self._exports[name]

    def get(self, name: str) -> ExportDefinition:
        """Return a registered export."""
        try:
            return self._exports[name]
        except KeyError as exc:
            raise ExportNotFoundError(
                f"Export {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether an export exists."""
        return name in self._exports

    def clear(self) -> None:
        """Remove all exports."""
        self._exports.clear()

    def list(self) -> tuple[ExportDefinition, ...]:
        """Return all registered exports."""
        return tuple(self._exports.values())

    def __len__(self) -> int:
        """Return registry size."""
        return len(self._exports)

    def __contains__(self, name: object) -> bool:
        """Return whether an export exists."""
        return isinstance(name, str) and name in self._exports


def build_export(
    *,
    name: str,
    destination: str,
    export_format: str = DEFAULT_EXPORT_FORMAT,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> ExportDefinition:
    """Build a validated export definition."""

    return ExportDefinition(
        name=name,
        destination=destination,
        export_format=export_format,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "ExportDefinition",
    "ExportRegistry",
    "build_export",
]