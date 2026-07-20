from __future__ import annotations

from ai_tools.github.operations import (
    GitHubClient,
    Repository,
)


def test_register_repository() -> None:
    client = GitHubClient()

    repository = Repository(
        name="ai-framework",
        owner="openai",
    )

    client.register_repository(
        repository,
    )

    assert client.repository_count == 1


def test_get_repository() -> None:
    client = GitHubClient()

    repository = Repository(
        name="ai-framework",
        owner="openai",
    )

    client.register_repository(
        repository,
    )

    result = client.get_repository(
        "ai-framework",
    )

    assert result is repository


def test_missing_repository() -> None:
    client = GitHubClient()

    assert client.get_repository("missing") is None
