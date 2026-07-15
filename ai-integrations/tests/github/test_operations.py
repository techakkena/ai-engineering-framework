"""
Tests for ai_integrations.github.operations.
"""

import pytest

from ai_integrations.github.constants import (
    DEFAULT_API_BASE,
    DEFAULT_BRANCH,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
)
from ai_integrations.github.exceptions import (
    GitHubConfigurationError,
)
from ai_integrations.github.operations import (
    GitHubClient,
    PullRequest,
    Repository,
)


def test_repository() -> None:
    """Repository should retain values."""
    repository = Repository(
        owner="openai",
        name="framework",
    )

    assert repository.owner == "openai"
    assert repository.name == "framework"
    assert repository.default_branch == DEFAULT_BRANCH


def test_repository_full_name() -> None:
    """Repository full name should be computed."""
    repository = Repository(
        owner="openai",
        name="framework",
    )

    assert repository.full_name == "openai/framework"


def test_pull_request() -> None:
    """PullRequest should retain values."""
    repository = Repository(
        owner="openai",
        name="framework",
    )

    pull_request = PullRequest(
        repository=repository,
        title="Add GitHub integration",
        source_branch="feature/github",
    )

    assert pull_request.title == "Add GitHub integration"
    assert pull_request.target_branch == DEFAULT_BRANCH


def test_client_defaults() -> None:
    """Client should expose default configuration."""
    client = GitHubClient(
        token="test-token",
    )

    health = client.health_check()

    assert health["provider"] == "github"
    assert health["api_base"] == DEFAULT_API_BASE
    assert health["timeout"] == DEFAULT_TIMEOUT
    assert health["max_retries"] == DEFAULT_MAX_RETRIES
    assert health["configured"] is True


def test_invalid_token() -> None:
    """Empty token should fail."""
    with pytest.raises(
        GitHubConfigurationError,
    ):
        GitHubClient(token="")


def test_create_pull_request() -> None:
    """Pull request creation should succeed."""
    client = GitHubClient(
        token="token",
    )

    repository = Repository(
        owner="openai",
        name="framework",
    )

    pull_request = PullRequest(
        repository=repository,
        title="Initial PR",
        source_branch="feature/test",
    )

    assert client.create_pull_request(
        pull_request,
    )


def test_create_pull_request_invalid_title() -> None:
    """Empty pull request title should fail."""
    client = GitHubClient(
        token="token",
    )

    repository = Repository(
        owner="openai",
        name="framework",
    )

    pull_request = PullRequest(
        repository=repository,
        title="",
        source_branch="feature/test",
    )

    with pytest.raises(
        GitHubConfigurationError,
    ):
        client.create_pull_request(
            pull_request,
        )


def test_list_repositories() -> None:
    """Repository listing should return a list."""
    client = GitHubClient(
        token="token",
    )

    repositories = client.list_repositories()

    assert isinstance(repositories, list)


def test_custom_configuration() -> None:
    """Custom configuration should be retained."""
    client = GitHubClient(
        token="token",
        api_base="https://example.test/api",
        timeout=120.0,
        max_retries=5,
    )

    health = client.health_check()

    assert health["api_base"] == "https://example.test/api"
    assert health["timeout"] == 120.0
    assert health["max_retries"] == 5