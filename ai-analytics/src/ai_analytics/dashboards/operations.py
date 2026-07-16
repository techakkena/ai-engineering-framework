"""Operations for the ai_analytics.dashboards module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_analytics.dashboards.constants import (
    DEFAULT_ENABLED,
    DEFAULT_LAYOUT,
    MAX_DASHBOARD_NAME_LENGTH,
    MIN_DASHBOARD_NAME_LENGTH,
    SUPPORTED_LAYOUTS,
)
from ai_analytics.dashboards.exceptions import (
    DashboardNotFoundError,
    DashboardValidationError,
    DuplicateDashboardError,
    UnsupportedLayoutError,
)


@dataclass(slots=True, frozen=True)
class DashboardDefinition:
    """Represents a dashboard definition."""

    name: str
    title: str
    layout: str = DEFAULT_LAYOUT
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the dashboard definition."""
        normalized = self.name.strip()

        if not (
            MIN_DASHBOARD_NAME_LENGTH
            <= len(normalized)
            <= MAX_DASHBOARD_NAME_LENGTH
        ):
            raise DashboardValidationError(
                "Dashboard name length is outside the allowed range."
            )

        if not self.title.strip():
            raise DashboardValidationError(
                "Dashboard title cannot be empty."
            )

        if self.layout not in SUPPORTED_LAYOUTS:
            raise UnsupportedLayoutError(
                f"Unsupported dashboard layout: {self.layout!r}."
            )

        object.__setattr__(self, "name", normalized)
        object.__setattr__(self, "title", self.title.strip())


class DashboardRegistry:
    """Registry for dashboard definitions."""

    __slots__ = ("_dashboards",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._dashboards: dict[str, DashboardDefinition] = {}

    def register(
        self,
        dashboard: DashboardDefinition,
    ) -> None:
        """Register a dashboard."""
        if dashboard.name in self._dashboards:
            raise DuplicateDashboardError(
                f"Dashboard {dashboard.name!r} is already registered."
            )

        self._dashboards[dashboard.name] = dashboard

    def unregister(self, name: str) -> None:
        """Remove a dashboard."""
        if name not in self._dashboards:
            raise DashboardNotFoundError(
                f"Dashboard {name!r} is not registered."
            )

        del self._dashboards[name]

    def get(
        self,
        name: str,
    ) -> DashboardDefinition:
        """Return a registered dashboard."""
        try:
            return self._dashboards[name]
        except KeyError as exc:
            raise DashboardNotFoundError(
                f"Dashboard {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a dashboard exists."""
        return name in self._dashboards

    def clear(self) -> None:
        """Remove all dashboards."""
        self._dashboards.clear()

    def list(self) -> tuple[
        DashboardDefinition,
        ...,
    ]:
        """Return registered dashboards."""
        return tuple(self._dashboards.values())

    def __len__(self) -> int:
        """Return registry size."""
        return len(self._dashboards)

    def __contains__(self, name: object) -> bool:
        """Return whether a dashboard exists."""
        return (
            isinstance(name, str)
            and name in self._dashboards
        )


def build_dashboard(
    *,
    name: str,
    title: str,
    layout: str = DEFAULT_LAYOUT,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> DashboardDefinition:
    """Build a validated dashboard."""

    return DashboardDefinition(
        name=name,
        title=title,
        layout=layout,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "DashboardDefinition",
    "DashboardRegistry",
    "build_dashboard",
]