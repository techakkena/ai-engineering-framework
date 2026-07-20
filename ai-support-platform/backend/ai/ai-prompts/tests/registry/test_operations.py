from __future__ import annotations

from ai_prompts.registry.operations import (
    clear_registry,
    get_prompt,
    list_prompts,
    register_prompt,
    unregister_prompt,
)


def setup_function():
    clear_registry()


def test_register_prompt():
    register_prompt(
        "chat",
        "Hello {{name}}",
    )

    assert get_prompt("chat") == "Hello {{name}}"


def test_unregister_prompt():
    register_prompt(
        "chat",
        "Hello",
    )

    unregister_prompt("chat")

    assert get_prompt("chat") is None


def test_list_prompts():
    register_prompt("a", "A")
    register_prompt("b", "B")

    assert list_prompts() == [
        "a",
        "b",
    ]


def test_clear_registry():
    register_prompt(
        "chat",
        "Hello",
    )

    clear_registry()

    assert list_prompts() == []
