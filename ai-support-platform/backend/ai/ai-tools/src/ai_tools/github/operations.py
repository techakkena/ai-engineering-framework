from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Repository:
    """Represents a GitHub repository."""

    name: str
    owner: str
    private: bool = False


class GitHubClient:
    """Simple in-memory GitHub client."""

    def __init__(self) -> None:
        self._repositories: dict[
            str,
            Repository,
        ] = {}

    def register_repository(
        self,
        repository: Repository,
    ) -> None:
        """Register a repository."""
        self._repositories[repository.name] = repository

    def get_repository(
        self,
        name: str,
    ) -> Repository | None:
        """Return a repository."""
        return self._repositories.get(name)

    @property
    def repository_count(self) -> int:
        """Return number of repositories."""
        return len(self._repositories)
