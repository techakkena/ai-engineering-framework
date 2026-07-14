import pytest

from ai_tools.storage.exceptions import (
    StorageToolError,
)


def test_storage_tool_error() -> None:
    with pytest.raises(StorageToolError):
        raise StorageToolError()
