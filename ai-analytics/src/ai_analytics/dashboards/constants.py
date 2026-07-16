"""Constants for the ai_analytics.dashboards module."""

from __future__ import annotations

from typing import Final

DEFAULT_DASHBOARD_NAME: Final[str] = "dashboard"
DEFAULT_LAYOUT: Final[str] = "grid"
DEFAULT_ENABLED: Final[bool] = True

GRID_LAYOUT: Final[str] = "grid"
LIST_LAYOUT: Final[str] = "list"
TABS_LAYOUT: Final[str] = "tabs"
FREEFORM_LAYOUT: Final[str] = "freeform"

SUPPORTED_LAYOUTS: Final[frozenset[str]] = frozenset(
    {
        GRID_LAYOUT,
        LIST_LAYOUT,
        TABS_LAYOUT,
        FREEFORM_LAYOUT,
    }
)

MIN_DASHBOARD_NAME_LENGTH: Final[int] = 1
MAX_DASHBOARD_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TITLE_KEY: Final[str] = "title"
LAYOUT_KEY: Final[str] = "layout"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_DASHBOARD_NAME",
    "DEFAULT_ENABLED",
    "DEFAULT_LAYOUT",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "FREEFORM_LAYOUT",
    "GRID_LAYOUT",
    "LAYOUT_KEY",
    "LIST_LAYOUT",
    "MAX_DASHBOARD_NAME_LENGTH",
    "MIN_DASHBOARD_NAME_LENGTH",
    "NAME_KEY",
    "SUPPORTED_LAYOUTS",
    "TABS_LAYOUT",
    "TITLE_KEY",
]