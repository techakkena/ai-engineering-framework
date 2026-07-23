"""FastAPI routes for knowledge management."""

from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, Query, Response, status

from app.auth.dependencies import CurrentActiveUserDependency
from app.knowledge.dependencies import KnowledgeServiceDep
from app.knowledge.schemas import (
    KnowledgeCreate,
    KnowledgeListResponse,
    KnowledgePublishRequest,
    KnowledgeResponse,
    KnowledgeSearchParams,
    KnowledgeUpdate,
)
from app.knowledge.types import KnowledgeStatus

router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge"],
)


@router.post(
    "",
    response_model=KnowledgeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_knowledge(
    request: KnowledgeCreate,
    current_user: CurrentActiveUserDependency,
    service: KnowledgeServiceDep,
) -> KnowledgeResponse:
    """Create a knowledge article."""
    article = service.create(
        organization_id=current_user.organization_id,
        author_id=current_user.id,
        request=request,
    )
    return KnowledgeResponse.model_validate(article)


@router.get(
    "",
    response_model=KnowledgeListResponse,
)
def list_knowledge(
    service: KnowledgeServiceDep,
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
) -> KnowledgeListResponse:
    """List knowledge articles."""
    total, items = service.list_articles(
        offset=offset,
        limit=limit,
    )

    return KnowledgeListResponse(
        total=total,
        items=[KnowledgeResponse.model_validate(article) for article in items],
    )


@router.get(
    "/search",
    response_model=list[KnowledgeResponse],
)
def search_knowledge(
    service: KnowledgeServiceDep,
    query: str | None = None,
    category: str | None = None,
    status: KnowledgeStatus | None = None,
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
) -> list[KnowledgeResponse]:
    """Search knowledge articles."""
    request = KnowledgeSearchParams(
        query=query,
        category=category,
        status=status,
        offset=offset,
        limit=limit,
    )

    articles = service.search(request)

    return [KnowledgeResponse.model_validate(article) for article in articles]


@router.get(
    "/{article_id}",
    response_model=KnowledgeResponse,
)
def get_knowledge(
    article_id: UUID,
    service: KnowledgeServiceDep,
) -> KnowledgeResponse:
    """Retrieve a knowledge article."""
    article = service.get(article_id)
    return KnowledgeResponse.model_validate(article)


@router.patch(
    "/{article_id}",
    response_model=KnowledgeResponse,
)
def update_knowledge(
    article_id: UUID,
    request: KnowledgeUpdate,
    service: KnowledgeServiceDep,
) -> KnowledgeResponse:
    """Update a knowledge article."""
    article = service.update(
        article_id=article_id,
        request=request,
    )

    return KnowledgeResponse.model_validate(article)


@router.post(
    "/{article_id}/publish",
    response_model=KnowledgeResponse,
)
def publish_knowledge(
    article_id: UUID,
    request: KnowledgePublishRequest,
    service: KnowledgeServiceDep,
) -> KnowledgeResponse:
    """Publish or archive a knowledge article."""
    if request.publish:
        article = service.publish(article_id)
    else:
        article = service.archive(article_id)

    return KnowledgeResponse.model_validate(article)


@router.delete(
    "/{article_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_knowledge(
    article_id: UUID,
    service: KnowledgeServiceDep,
) -> Response:
    """Delete a knowledge article."""
    service.delete(article_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
