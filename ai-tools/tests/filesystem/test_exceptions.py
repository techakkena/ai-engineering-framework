import pytest

from ai_tools.filesystem.exceptions import (
    FileSystemToolError,
)


def test_filesystem_error() -> None:
    with pytest.raises(FileSystemToolError):
        raise FileSystemToolError()
