"""
Unit tests for ai_monitoring.utils.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.utils.exceptions import (
    IdentifierValidationError,
)
from ai_monitoring.utils.operations import (
    UtilityResult,
    build_metadata,
    format_duration,
    format_timestamp,
    generate_identifier,
    validate_identifier,
)


def test_generate_identifier_success() -> None:
    """Identifier generation should succeed."""
    result = generate_identifier()

    assert isinstance(result, UtilityResult)
    assert result.success is True
    assert result.task == "generate_identifier"
    assert isinstance(result.data["identifier"], str)
    assert result.data["identifier"]


def test_validate_identifier_success() -> None:
    """Valid identifiers should not raise."""
    validate_identifier("monitor-001")


def test_validate_identifier_empty() -> None:
    """Empty identifiers should raise."""
    with pytest.raises(IdentifierValidationError):
        validate_identifier("")


def test_build_metadata_success() -> None:
    """Metadata creation should succeed."""
    result = build_metadata("monitor-001")

    assert result.success is True
    assert result.task == "build_metadata"
    assert result.data["id"] == "monitor-001"


def test_format_timestamp_success() -> None:
    """Timestamp formatting should succeed."""
    result = format_timestamp()

    assert result.success is True
    assert result.task == "format_timestamp"
    assert isinstance(result.data["timestamp"], str)


def test_format_duration_success() -> None:
    """Duration formatting should succeed."""
    result = format_duration(150)

    assert result.success is True
    assert result.task == "format_duration"
    assert result.data["duration"] == "150 ms"


def test_build_metadata_empty_identifier() -> None:
    """Metadata creation should reject empty identifiers."""
    with pytest.raises(IdentifierValidationError):
        build_metadata("")