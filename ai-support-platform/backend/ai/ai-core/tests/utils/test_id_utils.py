from __future__ import annotations

from utils.id_utils import (
    generate_short_id,
    generate_token,
    generate_uuid,
)


def test_generate_uuid():
    generated_uuid = generate_uuid()

    assert isinstance(generated_uuid, str)
    assert len(generated_uuid) == 36


def test_generate_token():
    token = generate_token(32)

    assert isinstance(token, str)
    assert len(token) == 64


def test_generate_short_id():
    short_id = generate_short_id(8)

    assert isinstance(short_id, str)
    assert len(short_id) == 8
