from __future__ import annotations

"""Operations for the ai_memory.conversation module."""

from __future__ import annotations

from .constants import ConversationRole
from .constants import ConversationState
from .constants import ConversationType
from .exceptions import ConversationValidationError


def validate_conversation_type(
    conversation_type: ConversationType | str,
) -> ConversationType:
    """Validate a conversation type."""
    try:
        return ConversationType(conversation_type)
    except ValueError as exc:
        raise ConversationValidationError(
            f"Invalid conversation type: {conversation_type!r}."
        ) from exc


def validate_conversation_state(
    state: ConversationState | str,
) -> ConversationState:
    """Validate a conversation state."""
    try:
        return ConversationState(state)
    except ValueError as exc:
        raise ConversationValidationError(
            f"Invalid conversation state: {state!r}."
        ) from exc


def validate_conversation_role(
    role: ConversationRole | str,
) -> ConversationRole:
    """Validate a conversation role."""
    try:
        return ConversationRole(role)
    except ValueError as exc:
        raise ConversationValidationError(
            f"Invalid conversation role: {role!r}."
        ) from exc


def is_valid_conversation_type(conversation_type: str) -> bool:
    """Return True if the conversation type is valid."""
    try:
        ConversationType(conversation_type)
        return True
    except ValueError:
        return False


def is_valid_conversation_state(state: str) -> bool:
    """Return True if the conversation state is valid."""
    try:
        ConversationState(state)
        return True
    except ValueError:
        return False


def is_valid_conversation_role(role: str) -> bool:
    """Return True if the conversation role is valid."""
    try:
        ConversationRole(role)
        return True
    except ValueError:
        return False
