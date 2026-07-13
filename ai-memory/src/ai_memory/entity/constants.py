"""Constants for the ai_memory.entity module."""

from __future__ import annotations

from enum import Enum


class EntityType(str, Enum):
    """Supported entity types."""

    PERSON = "person"
    ORGANIZATION = "organization"
    LOCATION = "location"
    PRODUCT = "product"
    EVENT = "event"
    CUSTOM = "custom"


class EntityState(str, Enum):
    """Entity lifecycle states."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"


DEFAULT_ENTITY_CONFIDENCE = 1.0
DEFAULT_ENTITY_NAMESPACE = "default"