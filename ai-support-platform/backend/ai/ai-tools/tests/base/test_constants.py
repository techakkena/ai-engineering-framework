from __future__ import annotations

from ai_tools.base.constants import ToolCategory


def test_category_count() -> None:
    assert len(ToolCategory) == 8


def test_http_category() -> None:
    assert ToolCategory.HTTP.value == "http"
