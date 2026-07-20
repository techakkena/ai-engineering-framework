from __future__ import annotations

import pytest

from ai_agents.config.exceptions import ConfigurationError


def test_configuration_error() -> None:
    with pytest.raises(ConfigurationError):
        raise ConfigurationError()
