from __future__ import annotations

import pytest

from ai_tools.base.exceptions import (
    ToolConfigurationError,
)


def test_configuration_error() -> None:
    with pytest.raises(
        ToolConfigurationError,
    ):
        raise ToolConfigurationError()
