"""
Unit tests for ai_multimodal.moderation.constants.
"""

from __future__ import annotations

from ai_multimodal.moderation import constants


def test_supported_tasks() -> None:
    """Supported moderation tasks should contain all task types."""
    assert constants.TASK_TEXT in constants.SUPPORTED_TASKS
    assert constants.TASK_IMAGE in constants.SUPPORTED_TASKS
    assert constants.TASK_AUDIO in constants.SUPPORTED_TASKS
    assert constants.TASK_VIDEO in constants.SUPPORTED_TASKS
    assert constants.TASK_DOCUMENT in constants.SUPPORTED_TASKS
    assert constants.TASK_METADATA in constants.SUPPORTED_TASKS


def test_supported_statuses() -> None:
    """Supported moderation statuses should be available."""
    assert constants.STATUS_SAFE in constants.SUPPORTED_STATUSES
    assert constants.STATUS_REVIEW in constants.SUPPORTED_STATUSES
    assert constants.STATUS_BLOCKED in constants.SUPPORTED_STATUSES


def test_risk_thresholds() -> None:
    """Risk threshold values should be valid."""
    assert constants.MIN_RISK_THRESHOLD == 0.0
    assert constants.DEFAULT_RISK_THRESHOLD == 0.5
    assert constants.MAX_RISK_THRESHOLD == 1.0


def test_supported_categories() -> None:
    """Supported moderation categories should exist."""
    assert constants.CATEGORY_HATE in constants.SUPPORTED_CATEGORIES
    assert constants.CATEGORY_HARASSMENT in constants.SUPPORTED_CATEGORIES
    assert constants.CATEGORY_SELF_HARM in constants.SUPPORTED_CATEGORIES
    assert constants.CATEGORY_SEXUAL in constants.SUPPORTED_CATEGORIES
    assert constants.CATEGORY_VIOLENCE in constants.SUPPORTED_CATEGORIES


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_PROVIDER == "provider"
    assert constants.METADATA_MODEL == "model"
    assert constants.METADATA_POLICY == "policy"
    assert constants.METADATA_RISK_SCORE == "risk_score"
    assert constants.METADATA_LATENCY == "latency_ms"