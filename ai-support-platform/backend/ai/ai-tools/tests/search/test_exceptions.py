from __future__ import annotations

import pytest

from ai_tools.search.exceptions import (
    SearchToolError,
)


def test_search_tool_error() -> None:
    with pytest.raises(SearchToolError):
        raise SearchToolError()
