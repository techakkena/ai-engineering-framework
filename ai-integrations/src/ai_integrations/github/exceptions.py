"""
Exceptions for the GitHub integration.
"""

from __future__ import annotations


class GitHubError(Exception):
    """Base exception for GitHub operations."""


class GitHubConfigurationError(GitHubError):
    """Raised when GitHub configuration is invalid."""


class GitHubAuthenticationError(GitHubError):
    """Raised when GitHub authentication fails."""


class GitHubRateLimitError(GitHubError):
    """Raised when the GitHub API rate limit is exceeded."""


class GitHubConnectionError(GitHubError):
    """Raised when communication with GitHub fails."""


class GitHubTimeoutError(GitHubError):
    """Raised when a request times out."""


class GitHubRequestError(GitHubError):
    """Raised when a GitHub request is invalid."""


class GitHubResponseError(GitHubError):
    """Raised when GitHub returns an invalid response."""


class GitHubProviderError(GitHubError):
    """Raised for provider-specific runtime failures."""