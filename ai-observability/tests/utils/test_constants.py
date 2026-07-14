from ai_observability.utils.constants import (
    DEFAULT_OBSERVATION_PREFIX,
)


def test_default_observation_prefix() -> None:
    assert DEFAULT_OBSERVATION_PREFIX == "observation"
