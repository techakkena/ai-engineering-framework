"""
Tests for ai_integrations.github.constants.
"""

from ai_integrations.github.constants import (
    DEFAULT_API_BASE,
    DEFAULT_BRANCH,
    DEFAULT_MAX_RETRIES,
    DEFAULT_PER_PAGE,
    DEFAULT_TIMEOUT,
    SUPPORTED_PR_STATES,
    SUPPORTED_VISIBILITIES,
)


def test_default_api_base() -> None:
    """Test the default API base."""
    assert DEFAULT_API_BASE == "https://api.github.com"


def test_default_branch() -> None:
    """Test the default branch."""
    assert DEFAULT_BRANCH == "main"


def test_default_timeout() -> None:
    """Test the default timeout."""
    assert DEFAULT_TIMEOUT == 60.0


def test_default_max_retries() -> None:
    """Test the default retry count."""
    assert DEFAULT_MAX_RETRIES == 3


def test_default_per_page() -> None:
    """Test the default page size."""
    assert DEFAULT_PER_PAGE == 100


def test_supported_visibilities() -> None:
    """Test supported repository visibilities."""
    assert "public" in SUPPORTED_VISIBILITIES
    assert "private" in SUPPORTED_VISIBILITIES
    assert "internal" in SUPPORTED_VISIBILITIES


def test_supported_pr_states() -> None:
    """Test supported pull request states."""
    assert "open" in SUPPORTED_PR_STATES
    assert "closed" in SUPPORTED_PR_STATES
    assert "all" in SUPPORTED_PR_STATES