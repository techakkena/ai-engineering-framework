from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class QueryResult:
    """Represents a database query result."""

    rows: list[dict[str, Any]] = field(default_factory=list)

    @property
    def row_count(self) -> int:
        """Return the number of rows."""
        return len(self.rows)


class DatabaseClient:
    """Simple in-memory database client."""

    def __init__(self) -> None:
        self._results: dict[str, QueryResult] = {}

    def register_result(
        self,
        query: str,
        result: QueryResult,
    ) -> None:
        """Register a result for a query."""
        self._results[query] = result

    def execute(
        self,
        query: str,
    ) -> QueryResult:
        """Execute a query."""

        return self._results.get(
            query,
            QueryResult(),
        )
