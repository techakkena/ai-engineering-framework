from __future__ import annotations

"""Operations for the ai_memory.store module."""

from __future__ import annotations

from .constants import StoreState
from .constants import StoreType
from .exceptions import StoreValidationError


def validate_store_type(store_type: StoreType | str) -> StoreType:
    """Validate a store type."""
    try:
        return StoreType(store_type)
    except ValueError as exc:
        raise StoreValidationError(
            f"Invalid store type: {store_type!r}."
        ) from exc


def validate_store_state(state: StoreState | str) -> StoreState:
    """Validate a store state."""
    try:
        return StoreState(state)
    except ValueError as exc:
        raise StoreValidationError(
            f"Invalid store state: {state!r}."
        ) from exc


def is_valid_store_type(store_type: str) -> bool:
    """Return True if the store type is valid."""
    try:
        StoreType(store_type)
        return True
    except ValueError:
        return False


def is_valid_store_state(state: str) -> bool:
    """Return True if the store state is valid."""
    try:
        StoreState(state)
        return True
    except ValueError:
        return False
