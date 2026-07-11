from __future__ import annotations

from ai_utils.datetime_utils import constants


def test_default_datetime_format() -> None:
    assert constants.DEFAULT_DATETIME_FORMAT == "%Y-%m-%d %H:%M:%S"


def test_default_date_format() -> None:
    assert constants.DEFAULT_DATE_FORMAT == "%Y-%m-%d"


def test_default_time_format() -> None:
    assert constants.DEFAULT_TIME_FORMAT == "%H:%M:%S"


def test_utc_timezone() -> None:
    assert constants.UTC_TIMEZONE == "UTC"
