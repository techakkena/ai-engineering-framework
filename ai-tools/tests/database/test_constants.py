from ai_tools.database.constants import (
    DEFAULT_DATABASE_TIMEOUT,
)


def test_default_timeout() -> None:
    assert DEFAULT_DATABASE_TIMEOUT == 30
