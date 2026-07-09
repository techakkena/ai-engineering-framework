from constants.logging_constants import (
    LogLevel,
    LoggerName,
    LogFormat,
    Rotation,
    OutputType,
)


def test_log_level():
    assert LogLevel.DEBUG == "DEBUG"
    assert LogLevel.INFO == "INFO"
    assert LogLevel.WARNING == "WARNING"
    assert LogLevel.ERROR == "ERROR"
    assert LogLevel.CRITICAL == "CRITICAL"  

def test_logger_name():
    assert LoggerName.FRAMEWORK == "AI-Framework"
    assert LoggerName.CORE == "AI-Core"
    assert LoggerName.AUTH == "AI-Auth"
    assert LoggerName.CHAT == "AI-Chat"
    assert LoggerName.AGENT == "AI-Agent"
    assert LoggerName.RAG == "AI-RAG"
    assert LoggerName.STORAGE == "AI-Storage"
    assert LoggerName.DOCUMENT == "AI-Documents"
    assert LoggerName.EMAIL == "AI-Email"
    assert LoggerName.DASHBOARD == "AI-Dashboard"

def test_log_format():
    assert LogFormat.SIMPLE == "%(levelname)s | %(message)s"
    assert LogFormat.STANDARD == "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    assert LogFormat.DETAILED == (
        "%(asctime)s | %(levelname)-8s | %(name)s | "
        "%(filename)s:%(lineno)d | %(message)s"
    )

def test_rotation():
    assert Rotation.MAX_FILE_SIZE == 10 * 1024 * 1024
    assert Rotation.BACKUP_COUNT == 5

def test_output_type():
    assert OutputType.CONSOLE == "console"
    assert OutputType.FILE == "file"
    assert OutputType.BOTH == "both"