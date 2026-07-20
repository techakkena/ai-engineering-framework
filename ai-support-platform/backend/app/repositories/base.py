from __future__ import annotations

"""Generic repository implementation."""

from typing import Any, Generic, TypeVar, cast
from uuid import UUID

from app.database.base import Base
from sqlalchemy import Select, select
from sqlalchemy.orm import Session

ModelT = TypeVar("ModelT", bound=Base)


class BaseRepository(Generic[ModelT]):
    """Generic repository for CRUD operations."""

    def __init__(
        self,
        session: Session,
        model: type[ModelT],
    ) -> None:
        """Initialize the repository.

        Args:
            session: Active database session.
            model: ORM model managed by this repository.
        """
        self.session = session
        self._model = model

    def create(self, entity: ModelT) -> ModelT:
        """Create a new entity."""
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def get(
        self,
        identifier: UUID,
    ) -> ModelT | None:
        """Return an entity by its UUID identifier."""
        entity = self.session.get(
            self._model,
            identifier,
        )

        # Fix: Safely read 'is_deleted' dynamically using getattr
        if entity is None or getattr(entity, "is_deleted", False):
            return None

        return entity

    def get_by_id(
        self,
        identifier: UUID,
    ) -> ModelT | None:
        """Return a model by its identifier."""
        return self.session.get(
            self._model,
            identifier,
        )

    def list(
        self,
        *,
        offset: int = 0,
        limit: int = 100,
    ) -> list[ModelT]:
        """Return non-deleted entities."""
        # Fix: Safely reference the 'is_deleted' attribute on the ORM class level dynamically
        is_deleted_attr = getattr(self._model, "is_deleted", None)
        
        statement: Select[tuple[ModelT]] = select(self._model)
        
        if is_deleted_attr is not None:
            statement = statement.where(is_deleted_attr.is_(False))
            
        statement = statement.offset(offset).limit(limit)

        return list(self.session.scalars(statement))

    def update(self, entity: ModelT) -> ModelT:
        """Persist entity changes."""
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def delete(self, entity: ModelT) -> None:
        """Soft-delete an entity."""
        # Fix: Cast to Any so mypy allows execution of the custom mixin method safely
        cast(Any, entity).soft_delete()
        self.session.commit()

    def exists(self, entity_id: Any) -> bool:
        """Return whether an entity exists."""
        return self.get_by_id(entity_id) is not None