"""
AI Engineering Framework
Configuration Integration Test

Tests:
1. Settings
2. Environment
3. Logging
""" 

from config.settings import settings
from config.environment import environment
from config.logging_config import LoggingManager


def test_settings():
    """Test framework settings."""

    print("\n========== SETTINGS ==========")

    print(f"Framework : {settings.FRAMEWORK_NAME}")
    print(f"Application : {settings.APP_NAME}")
    print(f"Version : {settings.VERSION}")
    print(f"Debug : {settings.DEBUG}")
    print(f"API Host : {settings.API_HOST}")
    print(f"API Port : {settings.API_PORT}")
    print(f"Database : {settings.DATABASE_URL}")
    print(f"AI Model : {settings.OPENAI_MODEL}")
    print(f"Log File : {settings.LOG_FILE}")

    print("✓ Settings Loaded Successfully")


def test_environment():
    """Test environment startup."""

    print("\n========== ENVIRONMENT ==========")

    environment.startup()

    print("✓ Environment Initialized")


def test_logging():
    """Test logging system."""

    print("\n========== LOGGING ==========")

    LoggingManager.configure()

    logger = LoggingManager.get_logger("AI-Core-Test")

    logger.debug("Debug message")

    logger.info("Information message")

    logger.warning("Warning message")

    logger.error("Error message")

    logger.critical("Critical message")

    print("✓ Logging Working Successfully")


def main():

    print("\n")
    print("=" * 70)
    print("AI ENGINEERING FRAMEWORK")
    print("AI CORE CONFIGURATION TEST")
    print("=" * 70)

    test_settings()

    test_environment()

    test_logging()

    print("\n")
    print("=" * 70)
    print("ALL CONFIGURATION TESTS PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()