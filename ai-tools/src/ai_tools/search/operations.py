from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SearchResult:
    """Represents a search result."""

    title: str
    url: str
    snippet: str


class SearchClient:
    """Simple in-memory search client."""

    def __init__(self) -> None:
        self._results: dict[
            str,
            list[SearchResult],
        ] = {}

    def register_results(
        self,
        query: str,
        results: list[SearchResult],
    ) -> None:
        """Register results for a query."""
        self._results[query] = results

    def search(
        self,
        query: str,
    ) -> list[SearchResult]:
        """Search by query."""
        return self._results.get(
            query,
            [],
        )
