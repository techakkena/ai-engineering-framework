from __future__ import annotations

from ai_prompts.registry.constants import (
    DEFAULT_REGISTRY_NAME,
    EMPTY_REGISTRY,
)


def test_default_registry_name():
    assert DEFAULT_REGISTRY_NAME == "default"


def test_empty_registry():
    assert EMPTY_REGISTRY == {}
