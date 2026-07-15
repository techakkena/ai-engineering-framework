"""
Unit tests for ai_runtime.base.constants.
"""

from __future__ import annotations

from ai_runtime.base.constants import (
    DEFAULT_ENCODING,
    DEFAULT_MAX_WORKERS,
    DEFAULT_RUNTIME_NAME,
    DEFAULT_RUNTIME_STATUS,
    DEFAULT_RUNTIME_VERSION,
    DEFAULT_TIMEOUT,
    FAILED,
    INITIALIZED,
    PAUSED,
    RUNNING,
    STARTING,
    STOPPED,
    STOPPING,
    SUPPORTED_RUNTIME_STATUSES,
)


def test_runtime_defaults() -> None:
    """Test runtime default constants."""
    assert DEFAULT_RUNTIME_NAME == "AI Runtime"
    assert DEFAULT_RUNTIME_VERSION == "1.0.0"
    assert DEFAULT_RUNTIME_STATUS == INITIALIZED


def test_runtime_statuses() -> None:
    """Test supported runtime statuses."""
    expected = {
        INITIALIZED,
        STARTING,
        RUNNING,
        PAUSED,
        STOPPING,
        STOPPED,
        FAILED,
    }

    assert SUPPORTED_RUNTIME_STATUSES == expected


def test_runtime_statuses_are_immutable() -> None:
    """Runtime statuses should be immutable."""
    assert isinstance(
        SUPPORTED_RUNTIME_STATUSES,
        frozenset,
    )


def test_runtime_configuration_defaults() -> None:
    """Test runtime configuration defaults."""
    assert DEFAULT_ENCODING == "utf-8"
    assert DEFAULT_TIMEOUT == 30
    assert DEFAULT_MAX_WORKERS == 4