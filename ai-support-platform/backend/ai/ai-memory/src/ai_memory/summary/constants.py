from __future__ import annotations

"""Constants for the ai_memory.summary module."""

from __future__ import annotations

from enum import Enum


class SummaryType(str, Enum):
    """Supported summary types."""

    CONVERSATION = "conversation"
    SESSION = "session"
    ENTITY = "entity"
    MEMORY = "memory"


class SummaryStrategy(str, Enum):
    """Supported summary strategies."""

    EXTRACTIVE = "extractive"
    ABSTRACTIVE = "abstractive"
    HYBRID = "hybrid"


class SummaryState(str, Enum):
    """Summary lifecycle states."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"


DEFAULT_MAX_SUMMARY_LENGTH = 1024
DEFAULT_SUMMARY_NAMESPACE = "default"
