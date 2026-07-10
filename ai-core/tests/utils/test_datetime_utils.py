from datetime import datetime

from utils.datetime_utils import DateTimeUtils


def test_datetime_utils_now():
    assert DateTimeUtils.now() is not None


def test_now():
    assert DateTimeUtils.now() is not None


def test_utc_now():
    assert DateTimeUtils.utc_now() is not None


def test_today():
    assert DateTimeUtils.today() is not None


def test_timestamp():
    assert DateTimeUtils.timestamp() is not None


def test_iso_now():
    assert DateTimeUtils.iso_now() is not None


def test_format():
    dt = DateTimeUtils.now()
    formatted = DateTimeUtils.format(dt)
    assert isinstance(formatted, str)


def test_parse():
    dt = DateTimeUtils.now()
    formatted = DateTimeUtils.format(dt)
    parsed = DateTimeUtils.parse(formatted)
    assert isinstance(parsed, datetime)
