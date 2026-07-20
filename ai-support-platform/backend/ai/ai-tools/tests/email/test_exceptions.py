from __future__ import annotations

import pytest

from ai_tools.email.exceptions import (
    EmailToolError,
)


def test_email_tool_error() -> None:
    with pytest.raises(EmailToolError):
        raise EmailToolError()
