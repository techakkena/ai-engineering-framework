"""Tests for the Knowledge API router."""

from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import MagicMock
from uuid import uuid4

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.auth.dependencies import get_current_user
from app.knowledge.dependencies import get_knowledge_service
from app.knowledge.models import KnowledgeArticle
from app.knowledge.router import router
from app.knowledge.types import KnowledgeStatus
from app.models.user import User

app = FastAPI()
app.include_router(router, prefix="/api/v1")


class TestKnowledgeRouter:
    """Tests for the knowledge router."""

    @pytest.fixture
    def client(self) -> TestClient:
        """Return a FastAPI test client."""
        return TestClient(app)

    @pytest.fixture
    def current_user(self) -> User:
        """Return a mocked authenticated user."""
        user = MagicMock(spec=User)

        user.id = uuid4()
        user.organization_id = uuid4()
        user.is_superuser = False

        return user

    @pytest.fixture
    def knowledge_service(self) -> MagicMock:
        """Return a mocked knowledge service."""
        return MagicMock()

    @pytest.fixture
    def article(self) -> KnowledgeArticle:
        """Return a mocked knowledge article."""
        article = MagicMock(spec=KnowledgeArticle)

        article.id = uuid4()
        article.organization_id = uuid4()
        article.author_id = uuid4()

        article.title = "FastAPI"
        article.slug = "fastapi"

        article.summary = "Knowledge summary"
        article.content = "Knowledge content"

        article.category = "Python"
        article.tags = [
            "python",
            "fastapi",
        ]

        article.status = KnowledgeStatus.DRAFT
        article.version = 1

        article.is_published = False
        article.is_deleted = False

        article.created_at = datetime.now(UTC)
        article.updated_at = datetime.now(UTC)
        article.published_at = None

        return article

    @staticmethod
    def override_dependencies(
        *,
        user: User | None = None,
        service: MagicMock | None = None,
    ) -> None:
        """Override FastAPI dependencies."""
        if user is not None:
            app.dependency_overrides[get_current_user] = lambda: user

        if service is not None:
            app.dependency_overrides[get_knowledge_service] = lambda: service

    @staticmethod
    def clear_dependencies() -> None:
        """Clear dependency overrides."""
        app.dependency_overrides.clear()

    @staticmethod
    def create_payload() -> dict[str, object]:
        """Return a valid create payload."""
        return {
            "title": "FastAPI",
            "summary": "Knowledge summary",
            "content": "Knowledge content",
            "category": "Python",
            "tags": [
                "python",
                "fastapi",
            ],
        }

    @staticmethod
    def update_payload() -> dict[str, object]:
        """Return a valid update payload."""
        return {
            "title": "Updated FastAPI",
            "summary": "Updated summary",
            "content": "Updated content",
            "category": "Backend",
            "tags": [
                "backend",
                "api",
            ],
        }

    @staticmethod
    def publish_payload(
        publish: bool,
    ) -> dict[str, bool]:
        """Return a publish payload."""
        return {
            "publish": publish,
        }

    def test_create_article(
        self,
        client: TestClient,
        current_user: User,
        knowledge_service: MagicMock,
        article: KnowledgeArticle,
    ) -> None:
        """Test creating a knowledge article."""
        knowledge_service.create.return_value = article

        self.override_dependencies(
            user=current_user,
            service=knowledge_service,
        )

        try:
            response = client.post(
                "/api/v1/knowledge",
                json=self.create_payload(),
            )
        finally:
            self.clear_dependencies()

        assert response.status_code == 201

        body = response.json()

        assert body["title"] == article.title
        assert body["slug"] == article.slug
        assert body["version"] == 1

        knowledge_service.create.assert_called_once()

    def test_get_article(
        self,
        client: TestClient,
        knowledge_service: MagicMock,
        article: KnowledgeArticle,
    ) -> None:
        """Test retrieving a knowledge article."""
        knowledge_service.get.return_value = article

        self.override_dependencies(
            service=knowledge_service,
        )

        try:
            response = client.get(
                f"/api/v1/knowledge/{article.id}",
            )
        finally:
            self.clear_dependencies()

        assert response.status_code == 200

        body = response.json()

        assert body["id"] == str(article.id)
        assert body["title"] == article.title
        assert body["slug"] == article.slug

        knowledge_service.get.assert_called_once_with(
            article.id,
        )

    def test_list_articles(
        self,
        client: TestClient,
        knowledge_service: MagicMock,
        article: KnowledgeArticle,
    ) -> None:
        """Test listing knowledge articles."""
        knowledge_service.list_articles.return_value = (
            1,
            [
                article,
            ],
        )

        self.override_dependencies(
            service=knowledge_service,
        )

        try:
            response = client.get(
                "/api/v1/knowledge",
            )
        finally:
            self.clear_dependencies()

        assert response.status_code == 200

        body = response.json()

        assert body["total"] == 1
        assert len(body["items"]) == 1

        assert body["items"][0]["title"] == article.title

        knowledge_service.list_articles.assert_called_once_with(
            offset=0,
            limit=100,
        )

    def test_list_articles_with_pagination(
        self,
        client: TestClient,
        knowledge_service: MagicMock,
        article: KnowledgeArticle,
    ) -> None:
        """Test listing articles with pagination."""
        knowledge_service.list_articles.return_value = (
            1,
            [
                article,
            ],
        )

        self.override_dependencies(
            service=knowledge_service,
        )

        try:
            response = client.get(
                "/api/v1/knowledge",
                params={
                    "offset": 5,
                    "limit": 10,
                },
            )
        finally:
            self.clear_dependencies()

        assert response.status_code == 200

        knowledge_service.list_articles.assert_called_once_with(
            offset=5,
            limit=10,
        )

    def test_search_articles(
        self,
        client: TestClient,
        knowledge_service: MagicMock,
        article: KnowledgeArticle,
    ) -> None:
        """Test searching articles."""
        knowledge_service.search.return_value = [
            article,
        ]

        self.override_dependencies(
            service=knowledge_service,
        )

        try:
            response = client.get(
                "/api/v1/knowledge/search",
                params={
                    "query": "fastapi",
                },
            )
        finally:
            self.clear_dependencies()

        assert response.status_code == 200

        body = response.json()

        assert len(body) == 1
        assert body[0]["title"] == article.title

        knowledge_service.search.assert_called_once()

    def test_search_returns_empty_list(
        self,
        client: TestClient,
        knowledge_service: MagicMock,
    ) -> None:
        """Test empty search results."""
        knowledge_service.search.return_value = []

        self.override_dependencies(
            service=knowledge_service,
        )

        try:
            response = client.get(
                "/api/v1/knowledge/search",
                params={
                    "query": "missing",
                },
            )
        finally:
            self.clear_dependencies()

        assert response.status_code == 200
        assert response.json() == []

        knowledge_service.search.assert_called_once()

    def test_update_article(
        self,
        client: TestClient,
        knowledge_service: MagicMock,
        article: KnowledgeArticle,
    ) -> None:
        """Test updating a knowledge article."""
        knowledge_service.update.return_value = article

        self.override_dependencies(
            service=knowledge_service,
        )

        try:
            response = client.patch(
                f"/api/v1/knowledge/{article.id}",
                json=self.update_payload(),
            )
        finally:
            self.clear_dependencies()

        assert response.status_code == 200

        body = response.json()

        assert body["id"] == str(article.id)
        assert body["title"] == article.title

        knowledge_service.update.assert_called_once()

    def test_update_article_partial(
        self,
        client: TestClient,
        knowledge_service: MagicMock,
        article: KnowledgeArticle,
    ) -> None:
        """Test partially updating a knowledge article."""
        knowledge_service.update.return_value = article

        self.override_dependencies(
            service=knowledge_service,
        )

        try:
            response = client.patch(
                f"/api/v1/knowledge/{article.id}",
                json={
                    "title": "Updated title",
                },
            )
        finally:
            self.clear_dependencies()

        assert response.status_code == 200

        knowledge_service.update.assert_called_once()

    def test_publish_article(
        self,
        client: TestClient,
        knowledge_service: MagicMock,
        article: KnowledgeArticle,
    ) -> None:
        """Test publishing a knowledge article."""
        article.status = KnowledgeStatus.PUBLISHED
        article.is_published = True

        knowledge_service.publish.return_value = article

        self.override_dependencies(
            service=knowledge_service,
        )

        try:
            response = client.post(
                f"/api/v1/knowledge/{article.id}/publish",
                json=self.publish_payload(True),
            )
        finally:
            self.clear_dependencies()

        assert response.status_code == 200

        body = response.json()

        assert body["is_published"] is True
        assert body["status"] == KnowledgeStatus.PUBLISHED.value

        knowledge_service.publish.assert_called_once_with(
            article.id,
        )

        knowledge_service.archive.assert_not_called()

    def test_archive_article(
        self,
        client: TestClient,
        knowledge_service: MagicMock,
        article: KnowledgeArticle,
    ) -> None:
        """Test archiving a knowledge article."""
        article.status = KnowledgeStatus.ARCHIVED
        article.is_published = False

        knowledge_service.archive.return_value = article

        self.override_dependencies(
            service=knowledge_service,
        )

        try:
            response = client.post(
                f"/api/v1/knowledge/{article.id}/publish",
                json=self.publish_payload(False),
            )
        finally:
            self.clear_dependencies()

        assert response.status_code == 200

        body = response.json()

        assert body["status"] == KnowledgeStatus.ARCHIVED.value
        assert body["is_published"] is False

        knowledge_service.archive.assert_called_once_with(
            article.id,
        )

        knowledge_service.publish.assert_not_called()

    def test_delete_article(
        self,
        client: TestClient,
        knowledge_service: MagicMock,
        article: KnowledgeArticle,
    ) -> None:
        """Test deleting a knowledge article."""
        self.override_dependencies(
            service=knowledge_service,
        )

        try:
            response = client.delete(
                f"/api/v1/knowledge/{article.id}",
            )
        finally:
            self.clear_dependencies()

        assert response.status_code == 204
        assert response.content == b""

        knowledge_service.delete.assert_called_once_with(
            article.id,
        )

    def test_delete_article_is_idempotent(
        self,
        client: TestClient,
        knowledge_service: MagicMock,
        article: KnowledgeArticle,
    ) -> None:
        """Test deleting the same article endpoint."""
        self.override_dependencies(
            service=knowledge_service,
        )

        try:
            response = client.delete(
                f"/api/v1/knowledge/{article.id}",
            )
        finally:
            self.clear_dependencies()

        assert response.status_code == 204

        knowledge_service.delete.assert_called_once()

    def test_publish_endpoint_routes_to_publish(
        self,
        client: TestClient,
        knowledge_service: MagicMock,
        article: KnowledgeArticle,
    ) -> None:
        """Test publish endpoint calls publish()."""
        knowledge_service.publish.return_value = article

        self.override_dependencies(
            service=knowledge_service,
        )

        try:
            client.post(
                f"/api/v1/knowledge/{article.id}/publish",
                json={
                    "publish": True,
                },
            )
        finally:
            self.clear_dependencies()

        knowledge_service.publish.assert_called_once_with(
            article.id,
        )

        knowledge_service.archive.assert_not_called()

    def test_publish_endpoint_routes_to_archive(
        self,
        client: TestClient,
        knowledge_service: MagicMock,
        article: KnowledgeArticle,
    ) -> None:
        """Test publish endpoint calls archive()."""
        knowledge_service.archive.return_value = article

        self.override_dependencies(
            service=knowledge_service,
        )

        try:
            client.post(
                f"/api/v1/knowledge/{article.id}/publish",
                json={
                    "publish": False,
                },
            )
        finally:
            self.clear_dependencies()

        knowledge_service.archive.assert_called_once_with(
            article.id,
        )

        knowledge_service.publish.assert_not_called()
