from __future__ import annotations

"""Health check endpoints."""

from datetime import UTC, datetime

from app.config.constants import HEALTH_STATUS
from app.config.settings import settings
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/health",
)


class HealthResponse(BaseModel):
    """Health check response model."""

    status: str
    application: str
    version: str
    environment: str
    timestamp: datetime


@router.get(
    "",
    response_model=HealthResponse,
    summary="Health Check",
)
async def health_check() -> HealthResponse:
    """Return the application health status.

    Returns:
        Current application health information.
    """
    return HealthResponse(
        status=HEALTH_STATUS,
        application=settings.APP_NAME,
        version=settings.APP_VERSION,
        environment=settings.APP_ENV,
        timestamp=datetime.now(UTC),
    )
