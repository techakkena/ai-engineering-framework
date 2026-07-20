from __future__ import annotations

"""Configuration operations."""

from __future__ import annotations

from .constants import (
    DEFAULT_PROMPT_DIRECTORY,
    DEFAULT_PROMPT_EXTENSION,
    DEFAULT_TEMPLATE_ENCODING,
)

_CONFIG: dict[str, str] = {
    "prompt_directory": DEFAULT_PROMPT_DIRECTORY,
    "prompt_extension": DEFAULT_PROMPT_EXTENSION,
    "template_encoding": DEFAULT_TEMPLATE_ENCODING,
}


def get_config(key: str) -> str | None:
    """Return a configuration value."""

    return _CONFIG.get(key)


def set_config(
    key: str,
    value: str,
) -> None:
    """Set a configuration value."""

    _CONFIG[key] = value


def reset_config() -> None:
    """Reset configuration to defaults."""

    _CONFIG.clear()

    _CONFIG.update(
        {
            "prompt_directory": DEFAULT_PROMPT_DIRECTORY,
            "prompt_extension": DEFAULT_PROMPT_EXTENSION,
            "template_encoding": DEFAULT_TEMPLATE_ENCODING,
        }
    )


def get_all_config() -> dict[str, str]:
    """Return all configuration."""

    return dict(_CONFIG)


__all__ = [
    "get_config",
    "set_config",
    "reset_config",
    "get_all_config",
]
