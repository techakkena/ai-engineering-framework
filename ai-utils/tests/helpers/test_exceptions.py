from __future__ import annotations

import pytest

from ai_utils.helpers.exceptions import HelpersError


def test_helpers_error_is_exception() -> None:
    assert issubclass(HelpersError, Exception)


def test_exception_can_be_raised() -> None:
    with pytest.raises(HelpersError):
        raise HelpersError("Test")
