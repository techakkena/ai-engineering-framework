from __future__ import annotations

"""Generic service implementation."""

from typing import Any, Generic, TypeVar

from app.models.base import BaseModel
from app.repositories.base import BaseRepository

ModelT = TypeVar("ModelT", bound=BaseModel)


class BaseService(Generic[ModelT]):
    """Generic service for business operations."""

    def __init__(
        self,
        repository: BaseRepository[ModelT],
    ) -> None:
        """Initialize the service.

        Args:
            repository: Repository instance.
        """
        self._repository = repository

    def create(self, entity: ModelT) -> ModelT:
        """Create a new entity."""
        entity = self._repository.create(entity)
        self._repository.session.commit()
        self._repository.session.refresh(entity)
        return entity

    def get_by_id(self, entity_id: Any) -> ModelT | None:
        """Retrieve an entity by its identifier."""
        return self._repository.get_by_id(entity_id)

    def list(
        self,
        *,
        offset: int = 0,
        limit: int = 100,
    ) -> list[ModelT]:
        """Retrieve entities."""
        return self._repository.list(
            skip=offset,
            limit=limit,
        )

    def update(self, entity: ModelT) -> ModelT:
        """Update an entity."""
        entity = self._repository.update(entity)
        self._repository.session.commit()
        self._repository.session.refresh(entity)
        return entity

    def delete(self, entity: ModelT) -> None:
        """Soft-delete an entity."""
        self._repository.delete(entity)
        self._repository.session.commit()

    def exists(self, entity_id: Any) -> bool:
        """Return whether an entity exists."""
        return self._repository.exists(entity_id)