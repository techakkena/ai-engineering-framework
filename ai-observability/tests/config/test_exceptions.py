import pytest

from ai_observability.config.exceptions import (
    ObservationConfigurationError,
)


def test_configuration_error() -> None:
    with pytest.raises(
        ObservationConfigurationError,
    ):
        raise ObservationConfigurationError()
