"""Tests for the AI Knowledge router."""

from __future__ import annotations

from uuid import uuid4

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.knowledge.models import KnowledgeArticle
from app.models.organization import Organization
from app.models.user import User


def test_create_knowledge(
    client: TestClient,
    auth_headers: dict[str, str],
    organization: Organization,
    user: User,
    db_session: Session,
) -> None:
    """Test creating a knowledge article."""
    response = client.post(
        "/api/v1/knowledge",
        headers=auth_headers,
        json={
            "title": "Support KB",
            "summary": "Knowledge Base",
            "content": "Knowledge article content.",
            "category": "Support",
            "tags": ["support", "faq"],
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["organization_id"] == str(organization.id)
    assert data["author_id"] == str(user.id)
    assert data["title"] == "Support KB"
    assert data["summary"] == "Knowledge Base"
    assert data["content"] == "Knowledge article content."
    assert data["category"] == "Support"
    assert data["tags"] == ["support", "faq"]
    assert data["version"] == 1
    assert data["status"] == "draft"
    assert data["is_published"] is False
    assert data["is_deleted"] is False


def test_list_knowledge(
    client: TestClient,
    auth_headers: dict[str, str],
    organization: Organization,
    user: User,
    db_session: Session,
) -> None:
    """Test listing knowledge articles."""
    article = KnowledgeArticle(
        organization_id=organization.id,
        author_id=user.id,
        title="KB1",
        slug="kb1",
        summary="Description",
        content="Article content",
        category="Support",
        tags="support",
    )

    db_session.add(article)
    db_session.commit()

    response = client.get(
        "/api/v1/knowledge",
        headers=auth_headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total"] >= 1
    assert len(data["items"]) >= 1


def test_get_knowledge(
    client: TestClient,
    auth_headers: dict[str, str],
    organization: Organization,
    user: User,
    db_session: Session,
) -> None:
    """Test retrieving a knowledge article."""
    article = KnowledgeArticle(
        organization_id=organization.id,
        author_id=user.id,
        title="Support",
        slug="support",
        summary="Description",
        content="Knowledge content",
        category="Support",
        tags="support",
    )

    db_session.add(article)
    db_session.commit()
    db_session.refresh(article)

    response = client.get(
        f"/api/v1/knowledge/{article.id}",
        headers=auth_headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == str(article.id)
    assert data["organization_id"] == str(organization.id)
    assert data["author_id"] == str(user.id)
    assert data["title"] == "Support"
    assert data["summary"] == "Description"
    assert data["content"] == "Knowledge content"


def test_get_knowledge_not_found(
    client: TestClient,
    auth_headers: dict[str, str],
) -> None:
    """Test retrieving a missing knowledge article."""
    response = client.get(
        f"/api/v1/knowledge/{uuid4()}",
        headers=auth_headers,
    )

    assert response.status_code == 404

    data = response.json()

    assert data["success"] is False
    assert data["error_code"] == "KnowledgeNotFoundError"


def test_update_knowledge(
    client: TestClient,
    auth_headers: dict[str, str],
    organization: Organization,
    user: User,
    db_session: Session,
) -> None:
    """Test updating a knowledge article."""
    article = KnowledgeArticle(
        organization_id=organization.id,
        author_id=user.id,
        title="Old Name",
        slug="old-name",
        content="Original content",
    )

    db_session.add(article)
    db_session.commit()
    db_session.refresh(article)

    response = client.patch(
        f"/api/v1/knowledge/{article.id}",
        headers=auth_headers,
        json={
            "title": "New Name",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == str(article.id)
    assert data["title"] == "New Name"
    assert data["version"] == 2


def test_delete_knowledge(
    client: TestClient,
    auth_headers: dict[str, str],
    organization: Organization,
    user: User,
    db_session: Session,
) -> None:
    """Test deleting a knowledge article."""
    article = KnowledgeArticle(
        organization_id=organization.id,
        author_id=user.id,
        title="Delete Me",
        slug="delete-me",
        content="Delete content",
    )

    db_session.add(article)
    db_session.commit()
    db_session.refresh(article)

    article_id = article.id

    response = client.delete(
        f"/api/v1/knowledge/{article_id}",
        headers=auth_headers,
    )

    assert response.status_code == 204

    db_session.expire_all()

    deleted = db_session.get(
        KnowledgeArticle,
        article_id,
    )

    assert deleted is not None
    assert deleted.is_deleted is True


def test_delete_knowledge_not_found(
    client: TestClient,
    auth_headers: dict[str, str],
) -> None:
    """Test deleting a missing knowledge article."""
    response = client.delete(
        f"/api/v1/knowledge/{uuid4()}",
        headers=auth_headers,
    )

    assert response.status_code == 404

    data = response.json()

    assert data["success"] is False
    assert data["error_code"] == "KnowledgeNotFoundError"
