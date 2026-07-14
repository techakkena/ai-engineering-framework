from ai_agents.memory.operations import (
    InMemoryAgentMemory,
)


def test_set_and_get() -> None:
    memory = InMemoryAgentMemory()

    memory.set(
        "name",
        "Alice",
    )

    assert memory.get("name") == "Alice"


def test_get_missing_key() -> None:
    memory = InMemoryAgentMemory()

    assert memory.get("missing") is None


def test_clear_memory() -> None:
    memory = InMemoryAgentMemory()

    memory.set(
        "key",
        "value",
    )

    memory.clear()

    assert len(memory) == 0


def test_memory_size() -> None:
    memory = InMemoryAgentMemory()

    memory.set("a", 1)
    memory.set("b", 2)

    assert len(memory) == 2
