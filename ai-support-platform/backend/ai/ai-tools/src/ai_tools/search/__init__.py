from __future__ import annotations

"""Search tool."""

from .constants import DEFAULT_MAX_RESULTS
from .exceptions import SearchToolError
from .operations import (
    SearchClient,
    SearchResult,
)

__all__ = [
    "DEFAULT_MAX_RESULTS",
    "SearchToolError",
    "SearchClient",
    "SearchResult",
]
