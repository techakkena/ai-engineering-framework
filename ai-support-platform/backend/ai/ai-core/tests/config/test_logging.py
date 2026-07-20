from __future__ import annotations

from config.logging_config import LoggingManager


def test_configure():
    LoggingManager.configure()

    assert True


def test_get_logger():
    logger = LoggingManager.get_logger(__name__)

    assert logger is not None


def test_debug():
    logger = LoggingManager.get_logger(__name__)

    logger.debug("Debug message")

    assert True


def test_info():
    logger = LoggingManager.get_logger(__name__)

    logger.info("Framework initialized")

    assert True


def test_warning():
    logger = LoggingManager.get_logger(__name__)

    logger.warning("Warning example")

    assert True


def test_error():
    logger = LoggingManager.get_logger(__name__)

    logger.error("Error example")

    assert True


def test_critical():
    logger = LoggingManager.get_logger(__name__)

    logger.critical("Critical example")

    assert True
