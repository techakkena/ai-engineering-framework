from __future__ import annotations

from constants.storage_constants import (
    FileExtension,
    FileSize,
    StorageDirectory,
    StorageTypes,
)


def test_storage_directory():
    assert StorageDirectory.STORAGE is not None
    assert StorageDirectory.UPLOADS is not None
    assert StorageDirectory.TEMP is not None
    assert StorageDirectory.LOGS is not None
    assert StorageDirectory.CACHE is not None
    assert StorageDirectory.BACKUPS is not None
    assert StorageDirectory.VECTOR_DB is not None


def test_file_extension():
    assert FileExtension.PDF == ".pdf"
    assert FileExtension.DOCX == ".docx"
    assert FileExtension.TXT == ".txt"
    assert FileExtension.CSV == ".csv"
    assert FileExtension.XLSX == ".xlsx"
    assert FileExtension.JSON == ".json"
    assert FileExtension.PNG == ".png"
    assert FileExtension.JPG == ".jpg"
    assert FileExtension.JPEG == ".jpeg"


def test_file_size():
    assert FileSize.KB == 1024
    assert FileSize.MB == 1024 * 1024
    assert FileSize.GB == 1024 * 1024 * 1024


def test_storage_types():
    assert StorageTypes.LOCAL == "local"
    assert StorageTypes.S3 == "s3"
    assert StorageTypes.GCS == "gcs"
    assert StorageTypes.AZURE == "azure"
