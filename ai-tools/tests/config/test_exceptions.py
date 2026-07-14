import pytest

from ai_tools.config.exceptions import (
    ToolConfigurationError,
)


def test_configuration_error() -> None:
    with pytest.raises(
        ToolConfigurationError,
    ):
        raise ToolConfigurationError()
