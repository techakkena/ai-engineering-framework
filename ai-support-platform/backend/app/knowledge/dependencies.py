"""Dependency injection providers for the knowledge module."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.knowledge.repository import KnowledgeRepository
from app.knowledge.service import KnowledgeService


def get_knowledge_repository(
    session: Annotated[
        Session,
        Depends(get_db),
    ],
) -> KnowledgeRepository:
    """Return a knowledge repository instance."""
    return KnowledgeRepository(session)


KnowledgeRepositoryDep = Annotated[
    KnowledgeRepository,
    Depends(get_knowledge_repository),
]


def get_knowledge_service(
    repository: KnowledgeRepositoryDep,
) -> KnowledgeService:
    """Return a knowledge service instance."""
    return KnowledgeService(repository)


KnowledgeServiceDep = Annotated[
    KnowledgeService,
    Depends(get_knowledge_service),
]
