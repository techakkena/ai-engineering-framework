from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from .paths import FRAMEWORK_ROOT
# --------------------------------------------------
# Framework Root
# --------------------------------------------------
from constants.storage_constants import StorageDirectory

class Settings(BaseSettings):
# ==================================================
# Framework
# ==================================================

    FRAMEWORK_DESCRIPTION: str = "Reusable AI Engineering Framework"
    AUTHOR: str = "TECHAKKENA"
    FRAMEWORK_NAME: str = "AI Engineering Framework"
    APP_NAME: str = "AI Core"
    VERSION: str = "0.1.0"
    DEBUG: bool = True
# ==================================================
# API
# ==================================================
    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000
    API_PREFIX: str = "/api/v1"

    DATABASE_URL: str = "sqlite:///framework.db"
# ==================================================
# AI
# ==================================================

    DEFAULT_CHAT_MODEL: str = "gpt-5.5"

    DEFAULT_EMBEDDING_MODEL: str = "text-embedding-3-small"

    TEMPERATURE: float = 0.2
    MAX_TOKENS: int = 4096

    # ==================================================
# Storage
# ==================================================

    STORAGE_ROOT: Path = FRAMEWORK_ROOT / StorageDirectory.STORAGE

    UPLOAD_FOLDER: Path = STORAGE_ROOT / StorageDirectory.UPLOADS

    TEMP_FOLDER: Path = STORAGE_ROOT / StorageDirectory.TEMP

    VECTOR_DB_PATH: Path = STORAGE_ROOT / StorageDirectory.VECTOR_DB

    CACHE_FOLDER: Path = STORAGE_ROOT / StorageDirectory.CACHE

    BACKUP_FOLDER: Path = STORAGE_ROOT / StorageDirectory.BACKUPS

    LOG_FILE: Path = STORAGE_ROOT / StorageDirectory.LOGS / "framework.log"

# ==================================================
# Logging
# ==================================================

    LOG_LEVEL: str = "INFO"

    LOG_FILE: Path = STORAGE_ROOT / StorageDirectory.LOGS / "framework.log"
# ==================================================
# Security
# ==================================================    
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=FRAMEWORK_ROOT / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()