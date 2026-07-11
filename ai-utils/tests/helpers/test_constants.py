from __future__ import annotations

from ai_utils.helpers import constants


def test_default_random_length() -> None:
    assert constants.DEFAULT_RANDOM_LENGTH == 16
