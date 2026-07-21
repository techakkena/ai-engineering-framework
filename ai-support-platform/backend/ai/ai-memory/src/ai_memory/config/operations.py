from __future__ import annotations

"""Operations for the ai_memory.config module."""

from __future__ import annotations

from .constants import ConfigFormat
from .constants import ConfigScope
from .exceptions import ConfigValidationError


def validate_config_format(
    config_format: ConfigFormat | str,
) -> ConfigFormat:
    """Validate a configuration format."""
    try:
        return ConfigFormat(config_format)
    except ValueError as exc:
        raise ConfigValidationError(
            f"Invalid configuration format: {config_format!r}."
        ) from exc


def validate_config_scope(
    scope: ConfigScope | str,
) -> ConfigScope:
    """Validate a configuration scope."""
    try:
        return ConfigScope(scope)
    except ValueError as exc:
        raise ConfigValidationError(f"Invalid configuration scope: {scope!r}.") from exc


def is_valid_config_format(config_format: str) -> bool:
    """Return True if configuration format is valid."""
    try:
        ConfigFormat(config_format)
        return True
    except ValueError:
        return False


def is_valid_config_scope(scope: str) -> bool:
    """Return True if configuration scope is valid."""
    try:
        ConfigScope(scope)
        return True
    except ValueError:
        return False
