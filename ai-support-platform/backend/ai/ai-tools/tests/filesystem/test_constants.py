from __future__ import annotations

from ai_tools.filesystem.constants import (
    DEFAULT_ENCODING,
)


def test_default_encoding() -> None:
    assert DEFAULT_ENCODING == "utf-8"
