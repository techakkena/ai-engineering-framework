from __future__ import annotations

from ai_tools.config.constants import (
    DEFAULT_RETRY_COUNT,
    DEFAULT_TIMEOUT,
    DEFAULT_USER_AGENT,
    DEFAULT_VERIFY_SSL,
)


def test_default_timeout() -> None:
    assert DEFAULT_TIMEOUT == 30


def test_default_retry_count() -> None:
    assert DEFAULT_RETRY_COUNT == 3


def test_default_user_agent() -> None:
    assert DEFAULT_USER_AGENT == "ai-tools"


def test_default_verify_ssl() -> None:
    assert DEFAULT_VERIFY_SSL is True
