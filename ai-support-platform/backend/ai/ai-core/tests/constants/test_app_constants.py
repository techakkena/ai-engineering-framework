from __future__ import annotations

from constants.app_constants import (
    Application,
    ContentType,
    Environment,
    HTTPStatus,
    LogLevel,
)


def test_application():
    assert Application.NAME is not None
    assert Application.VERSION is not None
    assert Application.DESCRIPTION is not None


def test_environment():
    assert Environment.DEVELOPMENT is not None
    assert Environment.TESTING is not None
    assert Environment.PRODUCTION is not None


def test_http_status():
    assert HTTPStatus.OK == 200
    assert HTTPStatus.CREATED == 201
    assert HTTPStatus.BAD_REQUEST == 400
    assert HTTPStatus.UNAUTHORIZED == 401
    assert HTTPStatus.FORBIDDEN == 403
    assert HTTPStatus.NOT_FOUND == 404
    assert HTTPStatus.INTERNAL_SERVER_ERROR == 500
    assert HTTPStatus.SERVICE_UNAVAILABLE == 503


def test_content_type():
    assert ContentType.JSON == "application/json"
    assert ContentType.PDF == "application/pdf"
    assert ContentType.CSV == "text/csv"
    assert ContentType.TEXT == "text/plain"
    assert ContentType.XML == "application/xml"


def test_log_level():
    assert LogLevel.DEBUG == "DEBUG"
    assert LogLevel.INFO == "INFO"
    assert LogLevel.WARNING == "WARNING"
    assert LogLevel.ERROR == "ERROR"
    assert LogLevel.CRITICAL == "CRITICAL"
