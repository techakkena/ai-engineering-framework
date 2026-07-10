"""
AI Engineering Framework
Storage Constants

Author : TECHAKKENA
"""


class StorageDirectory:
    """Framework storage directory names."""

    STORAGE = "storage"

    UPLOADS = "uploads"

    TEMP = "temp"

    LOGS = "logs"

    CACHE = "cache"

    BACKUPS = "backups"

    VECTOR_DB = "vector_db"


class FileExtension:
    """Supported file extensions."""

    PDF = ".pdf"

    DOCX = ".docx"

    TXT = ".txt"

    CSV = ".csv"

    XLSX = ".xlsx"

    JSON = ".json"

    PNG = ".png"

    JPG = ".jpg"

    JPEG = ".jpeg"


class FileSize:
    """Common file size units."""

    KB = 1024

    MB = 1024 * KB

    GB = 1024 * MB


class StorageTypes:
    """
    Supported storage providers.
    """

    LOCAL = "local"

    S3 = "s3"

    AZURE = "azure"

    GCS = "gcs"

    MINIO = "minio"
