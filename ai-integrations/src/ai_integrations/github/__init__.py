"""
GitHub integration for the AI Engineering Framework.

This package provides framework-independent abstractions for interacting
with GitHub repositories, pull requests, issues, releases, workflows,
and webhooks.
"""

from ai_integrations.github.constants import (
    DEFAULT_API_BASE,
    DEFAULT_BRANCH,
    DEFAULT_TIMEOUT,
)
from ai_integrations.github.exceptions import (
    GitHubAuthenticationError,
    GitHubConfigurationError,
    GitHubError,
    GitHubProviderError,
    GitHubRateLimitError,
)
from ai_integrations.github.operations import (
    GitHubClient,
    PullRequest,
    Repository,
)

__all__ = [
    "DEFAULT_API_BASE",
    "DEFAULT_BRANCH",
    "DEFAULT_TIMEOUT",
    "GitHubError",
    "GitHubConfigurationError",
    "GitHubAuthenticationError",
    "GitHubRateLimitError",
    "GitHubProviderError",
    "Repository",
    "PullRequest",
    "GitHubClient",
]