from __future__ import annotations

from ai_tools.search.constants import (
    DEFAULT_MAX_RESULTS,
)


def test_default_max_results() -> None:
    assert DEFAULT_MAX_RESULTS == 10
