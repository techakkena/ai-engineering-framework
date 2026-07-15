"""
Tests for ai_deployment.utils.constants.
"""

from ai_deployment.utils.constants import (
    DEFAULT_ENCODING,
    DEFAULT_HEALTH_ENDPOINT,
    DEFAULT_TIMEOUT_SECONDS,
)


def test_default_encoding() -> None:
    assert DEFAULT_ENCODING == "utf-8"


def test_default_timeout() -> None:
    assert DEFAULT_TIMEOUT_SECONDS == 30


def test_default_health_endpoint() -> None:
    assert DEFAULT_HEALTH_ENDPOINT == "/health"