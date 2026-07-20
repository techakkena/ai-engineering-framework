from __future__ import annotations

"""Tests for ai_memory.summary.constants."""

from ai_memory.summary.constants import (
    DEFAULT_MAX_SUMMARY_LENGTH,
    DEFAULT_SUMMARY_NAMESPACE,
    SummaryState,
    SummaryStrategy,
    SummaryType,
)


def test_summary_type_values() -> None:
    assert SummaryType.CONVERSATION.value == "conversation"
    assert SummaryType.SESSION.value == "session"
    assert SummaryType.ENTITY.value == "entity"
    assert SummaryType.MEMORY.value == "memory"


def test_summary_strategy_values() -> None:
    assert SummaryStrategy.EXTRACTIVE.value == "extractive"
    assert SummaryStrategy.ABSTRACTIVE.value == "abstractive"
    assert SummaryStrategy.HYBRID.value == "hybrid"


def test_summary_state_values() -> None:
    assert SummaryState.ACTIVE.value == "active"
    assert SummaryState.INACTIVE.value == "inactive"
    assert SummaryState.ARCHIVED.value == "archived"


def test_default_values() -> None:
    assert DEFAULT_MAX_SUMMARY_LENGTH == 1024
    assert DEFAULT_SUMMARY_NAMESPACE == "default"
