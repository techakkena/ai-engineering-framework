import pytest

from ai_observability.base.exceptions import (
    ObservationConfigurationError,
    ObservationError,
)


def test_observation_error() -> None:
    with pytest.raises(
        ObservationError,
    ):
        raise ObservationError()


def test_configuration_error() -> None:
    with pytest.raises(
        ObservationConfigurationError,
    ):
        raise ObservationConfigurationError()
