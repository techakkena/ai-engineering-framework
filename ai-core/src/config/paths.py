"""
AI Engineering Framework
Path Configuration
"""

from pathlib import Path

FRAMEWORK_ROOT = Path(__file__).resolve().parents[3]

STORAGE_ROOT = FRAMEWORK_ROOT / "storage"

UPLOADS_DIR = STORAGE_ROOT / "uploads"
TEMP_DIR = STORAGE_ROOT / "temp"
VECTOR_DB_DIR = STORAGE_ROOT / "vector_db"
LOGS_DIR = STORAGE_ROOT / "logs"
CACHE_DIR = STORAGE_ROOT / "cache"
BACKUPS_DIR = STORAGE_ROOT / "backups"