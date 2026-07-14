import pytest

from ai_agents.memory.exceptions import MemoryError


def test_memory_error() -> None:
    with pytest.raises(MemoryError):
        raise MemoryError()
