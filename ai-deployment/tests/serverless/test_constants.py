"""
Tests for ai_deployment.serverless.constants.
"""

from ai_deployment.serverless.constants import (
    DEFAULT_MEMORY_MB,
    DEFAULT_RUNTIME,
    DEFAULT_TIMEOUT_SECONDS,
)


def test_default_runtime() -> None:
    assert DEFAULT_RUNTIME == "python3.12"


def test_default_memory() -> None:
    assert DEFAULT_MEMORY_MB == 512


def test_default_timeout() -> None:
    assert DEFAULT_TIMEOUT_SECONDS == 30