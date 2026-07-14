from ai_observability.logging.constants import (
    LogLevel,
)
from ai_observability.logging.operations import (
    MemoryLogger,
)


def test_log_entry() -> None:
    logger = MemoryLogger()

    logger.log(
        LogLevel.INFO,
        "Workflow started",
    )

    assert logger.count == 1
    assert logger.entries[0].message == "Workflow started"


def test_log_attributes() -> None:
    logger = MemoryLogger()

    logger.log(
        LogLevel.ERROR,
        "Failure",
        workflow="demo",
    )

    assert logger.entries[0].attributes["workflow"] == "demo"


def test_clear() -> None:
    logger = MemoryLogger()

    logger.log(
        LogLevel.INFO,
        "Test",
    )

    logger.clear()

    assert logger.count == 0
