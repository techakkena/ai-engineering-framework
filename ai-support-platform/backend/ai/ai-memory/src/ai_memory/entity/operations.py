from __future__ import annotations

"""Operations for the ai_memory.entity module."""

from __future__ import annotations

from .constants import EntityState
from .constants import EntityType
from .exceptions import EntityValidationError


def validate_entity_type(entity_type: EntityType | str) -> EntityType:
    """Validate an entity type."""
    try:
        return EntityType(entity_type)
    except ValueError as exc:
        raise EntityValidationError(f"Invalid entity type: {entity_type!r}.") from exc


def validate_entity_state(state: EntityState | str) -> EntityState:
    """Validate an entity state."""
    try:
        return EntityState(state)
    except ValueError as exc:
        raise EntityValidationError(f"Invalid entity state: {state!r}.") from exc


def is_valid_entity_type(entity_type: str) -> bool:
    """Return True if the entity type is valid."""
    try:
        EntityType(entity_type)
        return True
    except ValueError:
        return False


def is_valid_entity_state(state: str) -> bool:
    """Return True if the entity state is valid."""
    try:
        EntityState(state)
        return True
    except ValueError:
        return False
