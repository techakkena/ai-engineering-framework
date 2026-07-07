from .logging_config import LoggingManager

LoggingManager.configure()
logger = LoggingManager.get_logger(__name__)

logger.debug("Debug message")

logger.info("Framework initialized")

logger.warning("Warning example")

logger.error("Error example")

logger.critical("Critical example")