from __future__ import annotations

from ai_tools.github.constants import (
    DEFAULT_GITHUB_API_VERSION,
)


def test_default_api_version() -> None:
    assert DEFAULT_GITHUB_API_VERSION == "2022-11-28"
