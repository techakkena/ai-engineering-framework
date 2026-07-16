"""Tests for ai_testing.data.constants."""

from __future__ import annotations

from ai_testing.data import constants


def test_default_dataset_name() -> None:
    assert constants.DEFAULT_DATASET_NAME == "dataset"


def test_default_enabled() -> None:
    assert constants.DEFAULT_ENABLED is True


def test_dataset_name_limits() -> None:
    assert constants.MIN_DATASET_NAME_LENGTH == 1
    assert constants.MAX_DATASET_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.DATA_KEY == "data"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"