"""
Unit tests for environment constants.
"""

from __future__ import annotations

from ai_utils.env_utils import constants


def test_default_env_file() -> None:
    assert constants.DEFAULT_ENV_FILE == ".env"
