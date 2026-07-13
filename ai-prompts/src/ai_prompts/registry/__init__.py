"""Prompt registry."""

from .constants import (
    DEFAULT_REGISTRY_NAME,
    EMPTY_REGISTRY,
)
from .exceptions import (
    PromptAlreadyRegisteredError,
    PromptNotRegisteredError,
    RegistryError,
)
from .operations import (
    clear_registry,
    get_prompt,
    list_prompts,
    register_prompt,
    unregister_prompt,
)

__all__ = [
    "DEFAULT_REGISTRY_NAME",
    "EMPTY_REGISTRY",
    "RegistryError",
    "PromptAlreadyRegisteredError",
    "PromptNotRegisteredError",
    "register_prompt",
    "unregister_prompt",
    "get_prompt",
    "list_prompts",
    "clear_registry",
]
