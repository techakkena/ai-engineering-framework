from __future__ import annotations

"""Tests for ai_memory.conversation.operations."""

import pytest

from ai_memory.conversation.constants import (
    ConversationRole,
    ConversationState,
    ConversationType,
)

from ai_memory.conversation.exceptions import ConversationValidationError

from ai_memory.conversation.operations import (
    is_valid_conversation_role,
    is_valid_conversation_state,
    is_valid_conversation_type,
    validate_conversation_role,
    validate_conversation_state,
    validate_conversation_type,
)


def test_validate_conversation_type() -> None:
    """Test validate_conversation_type."""
    assert validate_conversation_type("session") is ConversationType.SESSION


def test_validate_conversation_state() -> None:
    """Test validate_conversation_state."""
    assert validate_conversation_state("active") is ConversationState.ACTIVE


def test_validate_conversation_role() -> None:
    """Test validate_conversation_role."""
    assert validate_conversation_role("assistant") is ConversationRole.ASSISTANT


@pytest.mark.parametrize(
    ("value", "validator"),
    [
        ("invalid", validate_conversation_type),
        ("invalid", validate_conversation_state),
        ("invalid", validate_conversation_role),
    ],
)
def test_validation_errors(value: str, validator) -> None:
    """Test validation errors."""
    with pytest.raises(ConversationValidationError):
        validator(value)


def test_is_valid_conversation_type() -> None:
    """Test is_valid_conversation_type."""
    assert is_valid_conversation_type("persistent")
    assert not is_valid_conversation_type("invalid")


def test_is_valid_conversation_state() -> None:
    """Test is_valid_conversation_state."""
    assert is_valid_conversation_state("archived")
    assert not is_valid_conversation_state("invalid")


def test_is_valid_conversation_role() -> None:
    """Test is_valid_conversation_role."""
    assert is_valid_conversation_role("tool")
    assert not is_valid_conversation_role("invalid")
