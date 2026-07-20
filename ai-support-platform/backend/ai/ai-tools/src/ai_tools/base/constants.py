from __future__ import annotations

"""Constants for ai_tools base."""

from enum import Enum


class ToolCategory(str, Enum):
    """Supported tool categories."""

    FILESYSTEM = "filesystem"
    HTTP = "http"
    DATABASE = "database"
    SEARCH = "search"
    EMAIL = "email"
    CALENDAR = "calendar"
    STORAGE = "storage"
    GITHUB = "github"
