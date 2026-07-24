"""Dependency injection providers for the file module."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.files.providers import LocalStorageProvider
from app.files.repository import FileRepository
from app.files.service import FileService


DatabaseSession = Annotated[
    Session,
    Depends(get_db),
]

def get_file_repository(
    session: Annotated[
        Session,
        Depends(get_db),
    ],
) -> FileRepository:
    """Return a file repository instance."""
    return FileRepository(session)


FileRepositoryDep = Annotated[
    FileRepository,
    Depends(get_file_repository),
]


def get_storage_provider() -> LocalStorageProvider:
    """Return the configured storage provider."""
    return LocalStorageProvider()


StorageProviderDep = Annotated[
    LocalStorageProvider,
    Depends(get_storage_provider),
]


def get_file_service(
    session: DatabaseSession,
) -> FileService:
    repository = FileRepository(session)
    storage = LocalStorageProvider()

    return FileService(
        repository=repository,
        storage=storage,
    )


FileServiceDep = Annotated[
    FileService,
    Depends(get_file_service),
]
