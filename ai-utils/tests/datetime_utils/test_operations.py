from __future__ import annotations

from datetime import UTC, datetime

import pytest

from ai_utils.datetime_utils.exceptions import (
    DateTimeParseError,
)
from ai_utils.datetime_utils.operations import (
    format_datetime,
    from_iso,
    from_timestamp,
    local_now,
    parse_datetime,
    to_iso,
    to_timestamp,
    utc_now,
)


def test_utc_now() -> None:
    assert utc_now().tzinfo == UTC


def test_local_now() -> None:
    assert isinstance(local_now(), datetime)


def test_to_iso_and_from_iso() -> None:
    now = utc_now()

    iso = to_iso(now)

    assert from_iso(iso) == now


def test_timestamp_conversion() -> None:
    now = utc_now()

    timestamp = to_timestamp(now)

    restored = from_timestamp(timestamp)

    assert abs(restored.timestamp() - now.timestamp()) < 0.001


def test_format_and_parse_datetime() -> None:
    now = local_now()

    text = format_datetime(now)

    parsed = parse_datetime(text)

    assert parsed.strftime("%Y-%m-%d %H:%M:%S") == text


def test_invalid_iso() -> None:
    with pytest.raises(DateTimeParseError):
        from_iso("invalid")


def test_invalid_datetime_parse() -> None:
    with pytest.raises(DateTimeParseError):
        parse_datetime("invalid")
