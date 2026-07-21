from __future__ import annotations

"""Tests for ai_memory.conversation.exceptions."""

from ai_memory.conversation.exceptions import (
    ConversationError,
    ConversationNotFoundError,
    ConversationStateError,
    ConversationValidationError,
)


def test_exception_inheritance() -> None:
    """Test exception inheritance."""
    assert issubclass(ConversationNotFoundError, ConversationError)
    assert issubclass(ConversationValidationError, ConversationError)
    assert issubclass(ConversationStateError, ConversationError)


def test_raise_conversation_not_found_error() -> None:
    """Test ConversationNotFoundError."""
    try:
        raise ConversationNotFoundError("not found")
    except ConversationNotFoundError as exc:
        assert str(exc) == "not found"


def test_raise_conversation_validation_error() -> None:
    """Test ConversationValidationError."""
    try:
        raise ConversationValidationError("validation")
    except ConversationValidationError as exc:
        assert str(exc) == "validation"


def test_raise_conversation_state_error() -> None:
    """Test ConversationStateError."""
    try:
        raise ConversationStateError("state")
    except ConversationStateError as exc:
        assert str(exc) == "state"
