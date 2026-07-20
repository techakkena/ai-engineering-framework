from __future__ import annotations

"""Operations for prompt registry."""

from __future__ import annotations

_REGISTRY: dict[str, str] = {}


def register_prompt(
    name: str,
    template: str,
) -> None:
    """Register a prompt."""

    _REGISTRY[name] = template


def unregister_prompt(
    name: str,
) -> None:
    """Remove a prompt."""

    _REGISTRY.pop(name, None)


def get_prompt(
    name: str,
) -> str | None:
    """Get a prompt."""

    return _REGISTRY.get(name)


def list_prompts() -> list[str]:
    """Return registered prompt names."""

    return sorted(_REGISTRY)


def clear_registry() -> None:
    """Clear registry."""

    _REGISTRY.clear()


__all__ = [
    "register_prompt",
    "unregister_prompt",
    "get_prompt",
    "list_prompts",
    "clear_registry",
]
