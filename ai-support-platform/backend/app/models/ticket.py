from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Status(Base):
    __tablename__ = "statuses"
    
    id: Mapped[UUID] = mapped_column(primary_key=True)
    # Ensure this is defined if statuses are tenant-scoped:
    organization_id: Mapped[UUID] = mapped_column(ForeignKey("organizations.id"), nullable=False)

class Priority(Base):
    __tablename__ = "priorities"
    
    id: Mapped[UUID] = mapped_column(primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(ForeignKey("organizations.id"), nullable=False)

class Category(Base):
    __tablename__ = "categories"
    
    id: Mapped[UUID] = mapped_column(primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(ForeignKey("organizations.id"), nullable=False)

class Ticket(Base):
    __tablename__ = "tickets"
    
    id: Mapped[UUID] = mapped_column(primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(ForeignKey("organizations.id"), nullable=False)