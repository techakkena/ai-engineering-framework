"""
Framework-independent GitHub operations.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ai_integrations.github.constants import (
    DEFAULT_API_BASE,
    DEFAULT_BRANCH,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
)
from ai_integrations.github.exceptions import (
    GitHubConfigurationError,
)


@dataclass(slots=True, frozen=True)
class Repository:
    """Represents a GitHub repository."""

    owner: str
    name: str
    default_branch: str = DEFAULT_BRANCH

    @property
    def full_name(self) -> str:
        """Return the repository full name."""
        return f"{self.owner}/{self.name}"


@dataclass(slots=True, frozen=True)
class PullRequest:
    """Represents a pull request."""

    repository: Repository
    title: str
    source_branch: str
    target_branch: str = DEFAULT_BRANCH


class GitHubClient:
    """
    Framework-independent GitHub client.
    """

    def __init__(
        self,
        *,
        token: str,
        api_base: str = DEFAULT_API_BASE,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        if not token.strip():
            raise GitHubConfigurationError(
                "GitHub token cannot be empty."
            )

        self._token = token
        self._api_base = api_base
        self._timeout = timeout
        self._max_retries = max_retries

    def create_pull_request(
        self,
        pull_request: PullRequest,
    ) -> bool:
        """
        Create a pull request.

        Placeholder implementation.
        """
        if not pull_request.title.strip():
            raise GitHubConfigurationError(
                "Pull request title cannot be empty."
            )

        return True

    def list_repositories(self) -> list[Repository]:
        """
        Return repositories.

        Placeholder implementation.
        """
        return []

    def health_check(self) -> dict[str, Any]:
        """Return client configuration."""
        return {
            "provider": "github",
            "api_base": self._api_base,
            "timeout": self._timeout,
            "max_retries": self._max_retries,
            "configured": True,
        }