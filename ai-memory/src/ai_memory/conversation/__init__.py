"""Conversation module."""

from .constants import (
    ConversationRole,
    ConversationState,
    ConversationType,
    DEFAULT_CONVERSATION_NAME,
    DEFAULT_MAX_MESSAGES,
)
from .exceptions import (
    ConversationError,
    ConversationNotFoundError,
    ConversationStateError,
    ConversationValidationError,
)
from .operations import (
    is_valid_conversation_role,
    is_valid_conversation_state,
    is_valid_conversation_type,
    validate_conversation_role,
    validate_conversation_state,
    validate_conversation_type,
)

__all__ = [
    "ConversationType",
    "ConversationState",
    "ConversationRole",
    "DEFAULT_MAX_MESSAGES",
    "DEFAULT_CONVERSATION_NAME",
    "ConversationError",
    "ConversationNotFoundError",
    "ConversationValidationError",
    "ConversationStateError",
    "validate_conversation_type",
    "validate_conversation_state",
    "validate_conversation_role",
    "is_valid_conversation_type",
    "is_valid_conversation_state",
    "is_valid_conversation_role",
]
