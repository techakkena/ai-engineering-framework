from constants.api_constants import (
    API,
)


def test_api_prefix():
    assert API.API_PREFIX is not None
    assert API.API_PREFIX != ""


def test_api_version():
    assert API.API_VERSION is not None
    assert API.API_VERSION != ""


def test_default_port():
    assert API.DEFAULT_PORT is not None
    assert isinstance(API.DEFAULT_PORT, int)
