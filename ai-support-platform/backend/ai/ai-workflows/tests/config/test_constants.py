from __future__ import annotations

from ai_workflows.config.constants import (
    DEFAULT_FAIL_FAST,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
)


def test_timeout() -> None:
    assert DEFAULT_TIMEOUT == 60


def test_max_retries() -> None:
    assert DEFAULT_MAX_RETRIES == 3


def test_fail_fast() -> None:
    assert DEFAULT_FAIL_FAST is True
