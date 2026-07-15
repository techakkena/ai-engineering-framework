"""
Tests for ai_integrations.utils.operations.
"""

import pytest

from ai_integrations.utils.constants import (
    DEFAULT_BACKOFF_FACTOR,
    DEFAULT_RETRY_ATTEMPTS,
    DEFAULT_USER_AGENT,
)
from ai_integrations.utils.exceptions import (
    ValidationError,
)
from ai_integrations.utils.operations import (
    RetryPolicy,
    build_user_agent,
    calculate_backoff,
    merge_headers,
    validate_url,
)


def test_retry_policy_defaults() -> None:
    """RetryPolicy should use default values."""
    policy = RetryPolicy()

    assert policy.attempts == DEFAULT_RETRY_ATTEMPTS
    assert (
        policy.backoff_factor
        == DEFAULT_BACKOFF_FACTOR
    )


def test_retry_policy_custom() -> None:
    """RetryPolicy should retain custom values."""
    policy = RetryPolicy(
        attempts=5,
        backoff_factor=3.0,
    )

    assert policy.attempts == 5
    assert policy.backoff_factor == 3.0


def test_calculate_backoff() -> None:
    """Backoff should be exponential."""
    assert calculate_backoff(0) == 1.0
    assert calculate_backoff(1) == 2.0
    assert calculate_backoff(2) == 4.0
    assert calculate_backoff(3) == 8.0


def test_calculate_backoff_custom_factor() -> None:
    """Custom factor should be respected."""
    assert calculate_backoff(3, 3.0) == 27.0


def test_calculate_backoff_negative_attempt() -> None:
    """Negative attempts should fail."""
    with pytest.raises(
        ValidationError,
    ):
        calculate_backoff(-1)


def test_build_user_agent() -> None:
    """User agent should be formatted correctly."""
    agent = build_user_agent(
        "MyApp",
        "1.2.3",
    )

    assert "MyApp/1.2.3" in agent
    assert DEFAULT_USER_AGENT in agent


def test_merge_headers_without_custom() -> None:
    """Headers should be copied."""
    headers = merge_headers(
        {"Accept": "application/json"},
    )

    assert headers == {
        "Accept": "application/json",
    }


def test_merge_headers_with_custom() -> None:
    """Custom headers should override defaults."""
    headers = merge_headers(
        {
            "Accept": "application/json",
            "User-Agent": "Old",
        },
        {
            "User-Agent": "New",
            "Authorization": "Bearer token",
        },
    )

    assert headers["Accept"] == "application/json"
    assert headers["User-Agent"] == "New"
    assert headers["Authorization"] == "Bearer token"


def test_validate_url_https() -> None:
    """HTTPS URLs should be valid."""
    assert validate_url(
        "https://example.com"
    )


def test_validate_url_http() -> None:
    """HTTP URLs should be valid."""
    assert validate_url(
        "http://localhost:8000"
    )


def test_validate_url_invalid_scheme() -> None:
    """Unsupported schemes should fail."""
    with pytest.raises(
        ValidationError,
    ):
        validate_url(
            "ftp://example.com"
        )


def test_validate_url_missing_host() -> None:
    """URLs without hosts should fail."""
    with pytest.raises(
        ValidationError,
    ):
        validate_url(
            "https://"
        )