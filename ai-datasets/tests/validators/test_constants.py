"""
Unit tests for ai_datasets.validators.constants.
"""

from __future__ import annotations

from ai_datasets.validators import constants


def test_supported_validations() -> None:
    """Supported validations should contain all validation tasks."""
    assert (
        constants.TASK_VALIDATE_DATASET
        in constants.SUPPORTED_VALIDATIONS
    )
    assert (
        constants.TASK_VALIDATE_SCHEMA
        in constants.SUPPORTED_VALIDATIONS
    )
    assert (
        constants.TASK_VALIDATE_INTEGRITY
        in constants.SUPPORTED_VALIDATIONS
    )
    assert (
        constants.TASK_VALIDATE_CONSTRAINTS
        in constants.SUPPORTED_VALIDATIONS
    )
    assert (
        constants.TASK_VALIDATE_METADATA
        in constants.SUPPORTED_VALIDATIONS
    )


def test_supported_severities() -> None:
    """Supported severities should contain all levels."""
    assert constants.SEVERITY_INFO in constants.SUPPORTED_SEVERITIES
    assert constants.SEVERITY_WARNING in constants.SUPPORTED_SEVERITIES
    assert constants.SEVERITY_ERROR in constants.SUPPORTED_SEVERITIES


def test_default_configuration() -> None:
    """Default validator configuration should be valid."""
    assert constants.DEFAULT_STRICT_MODE is True
    assert constants.DEFAULT_FAIL_FAST is False
    assert constants.DEFAULT_MAX_ERRORS > 0


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_VALIDATION_TYPE == "validation_type"
    assert constants.METADATA_ERROR_COUNT == "error_count"
    assert constants.METADATA_WARNING_COUNT == "warning_count"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_STATUS == "status"