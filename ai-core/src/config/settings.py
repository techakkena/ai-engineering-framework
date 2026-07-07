from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from .paths import FRAMEWORK_ROOT
# --------------------------------------------------
# Framework Root
# --------------------------------------------------
FRAMEWORK_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):

    FRAMEWORK_NAME: str = "AI Engineering Framework"
    APP_NAME: str = "AI Core"
    VERSION: str = "0.1.0"
    DEBUG: bool = True

    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000
    API_PREFIX: str = "/api/v1"

    DATABASE_URL: str = "sqlite:///framework.db"

    OPENAI_MODEL: str = "gpt-5.5"
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"

    TEMPERATURE: float = 0.2
    MAX_TOKENS: int = 4096

    # ==================================================
# Storage
# ==================================================

    STORAGE_ROOT: str = "storage"

    UPLOAD_FOLDER: str = "storage/uploads"

    TEMP_FOLDER: str = "storage/temp"

    VECTOR_DB_PATH: str = "storage/vector_db"

    CACHE_FOLDER: str = "storage/cache"

    BACKUP_FOLDER: str = "storage/backups"


    # ==================================================
# Logging
# ==================================================

    LOG_LEVEL: str = "INFO"

    LOG_FILE: str = "storage/logs/framework.log"
    

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=FRAMEWORK_ROOT / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()