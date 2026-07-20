from __future__ import annotations

import pytest

from ai_tools.database.exceptions import (
    DatabaseToolError,
)


def test_database_error() -> None:
    with pytest.raises(DatabaseToolError):
        raise DatabaseToolError()
