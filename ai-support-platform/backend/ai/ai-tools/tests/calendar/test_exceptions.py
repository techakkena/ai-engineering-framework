from __future__ import annotations

import pytest

from ai_tools.calendar.exceptions import (
    CalendarToolError,
)


def test_calendar_tool_error() -> None:
    with pytest.raises(CalendarToolError):
        raise CalendarToolError()
