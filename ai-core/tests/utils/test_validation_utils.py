"""
AI Engineering Framework
Validation Utils Tests

Author : TECHAKKENA
"""

from utils.validation_utils import ValidationUtils


def test_is_empty():
    assert ValidationUtils.is_empty("") is True
    assert ValidationUtils.is_empty("   ") is True
    assert ValidationUtils.is_empty(None) is True
    assert ValidationUtils.is_empty("AI Framework") is False


def test_is_email():
    assert ValidationUtils.is_email("test@example.com") is True
    assert ValidationUtils.is_email("user.name@test.co.in") is True
    assert ValidationUtils.is_email("invalid-email") is False
    assert ValidationUtils.is_email("test@") is False


def test_is_url():
    assert ValidationUtils.is_url("https://openai.com") is True
    assert ValidationUtils.is_url("http://example.org") is True
    assert ValidationUtils.is_url("not-a-url") is False
    assert ValidationUtils.is_url("example.com") is False


def test_is_uuid():
    assert ValidationUtils.is_uuid(
        "550e8400-e29b-41d4-a716-446655440000"
    ) is True

    assert ValidationUtils.is_uuid(
        "invalid-uuid"
    ) is False


def test_is_json():
    assert ValidationUtils.is_json('{"name":"AI"}') is True
    assert ValidationUtils.is_json("[1,2,3]") is True
    assert ValidationUtils.is_json("invalid json") is False


def test_is_number():
    assert ValidationUtils.is_number("123") is True
    assert ValidationUtils.is_number("123.45") is True
    assert ValidationUtils.is_number("-99") is True
    assert ValidationUtils.is_number("abc") is False


def test_is_ip_address():
    assert ValidationUtils.is_ip_address("192.168.1.1") is True
    assert ValidationUtils.is_ip_address("2001:db8::1") is True
    assert ValidationUtils.is_ip_address("999.999.999.999") is False
    assert ValidationUtils.is_ip_address("invalid-ip") is False


def test_is_filename():
    assert ValidationUtils.is_filename("sample.txt") is True
    assert ValidationUtils.is_filename("image.png") is True
    assert ValidationUtils.is_filename("folder/sample.txt") is False
    assert ValidationUtils.is_filename("C:/temp/file.txt") is False


def test_has_extension():
    assert ValidationUtils.has_extension(
        "sample.pdf",
        ".pdf",
        ".docx",
    ) is True

    assert ValidationUtils.has_extension(
        "image.png",
        ".jpg",
        ".png",
    ) is True

    assert ValidationUtils.has_extension(
        "archive.zip",
        ".pdf",
        ".docx",
    ) is False