"""Operations for the ai_memory.base module."""

from __future__ import annotations

from .constants import MemoryFormat
from .constants import MemoryScope
from .constants import MemoryType
from .constants import MessageRole
from .exceptions import MemoryValidationError


def validate_memory_type(memory_type: MemoryType | str) -> MemoryType:
    """
    Validate and normalize a memory type.

    Args:
        memory_type: Memory type value.

    Returns:
        Valid MemoryType.

    Raises:
        MemoryValidationError:
            If the value is invalid.
    """
    try:
        return MemoryType(memory_type)
    except ValueError as exc:
        raise MemoryValidationError(f"Invalid memory type: {memory_type!r}.") from exc


def validate_role(role: MessageRole | str) -> MessageRole:
    """
    Validate and normalize a message role.

    Args:
        role: Message role.

    Returns:
        Valid MessageRole.

    Raises:
        MemoryValidationError:
            If the value is invalid.
    """
    try:
        return MessageRole(role)
    except ValueError as exc:
        raise MemoryValidationError(f"Invalid message role: {role!r}.") from exc


def validate_scope(scope: MemoryScope | str) -> MemoryScope:
    """
    Validate and normalize a memory scope.

    Args:
        scope: Memory scope.

    Returns:
        Valid MemoryScope.

    Raises:
        MemoryValidationError:
            If the value is invalid.
    """
    try:
        return MemoryScope(scope)
    except ValueError as exc:
        raise MemoryValidationError(f"Invalid memory scope: {scope!r}.") from exc


def validate_format(memory_format: MemoryFormat | str) -> MemoryFormat:
    """
    Validate and normalize a memory format.

    Args:
        memory_format: Memory format.

    Returns:
        Valid MemoryFormat.

    Raises:
        MemoryValidationError:
            If the value is invalid.
    """
    try:
        return MemoryFormat(memory_format)
    except ValueError as exc:
        raise MemoryValidationError(
            f"Invalid memory format: {memory_format!r}."
        ) from exc


def is_valid_memory_type(memory_type: str) -> bool:
    """
    Return True if the supplied memory type is valid.

    Args:
        memory_type: Memory type value.

    Returns:
        True if valid, otherwise False.
    """
    try:
        MemoryType(memory_type)
        return True
    except ValueError:
        return False


def is_valid_role(role: str) -> bool:
    """
    Return True if the supplied role is valid.

    Args:
        role: Message role.

    Returns:
        True if valid, otherwise False.
    """
    try:
        MessageRole(role)
        return True
    except ValueError:
        return False


def is_valid_scope(scope: str) -> bool:
    """
    Return True if the supplied scope is valid.

    Args:
        scope: Memory scope.

    Returns:
        True if valid, otherwise False.
    """
    try:
        MemoryScope(scope)
        return True
    except ValueError:
        return False


def is_valid_format(memory_format: str) -> bool:
    """
    Return True if the supplied format is valid.

    Args:
        memory_format: Memory format.

    Returns:
        True if valid, otherwise False.
    """
    try:
        MemoryFormat(memory_format)
        return True
    except ValueError:
        return False
