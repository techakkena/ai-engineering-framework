from __future__ import annotations

from utils.string_utils import StringUtils


def test_is_empty():
    assert StringUtils.is_empty("") is True
    assert StringUtils.is_empty("   ") is True
    assert StringUtils.is_empty(None) is True
    assert StringUtils.is_empty("Hello") is False


def test_truncate():
    assert StringUtils.truncate("Hello, World!", 5) == "Hello..."
    assert StringUtils.truncate("Short", 10) == "Short"


def test_remove_extra_spaces():
    assert StringUtils.remove_extra_spaces("Hello   World") == "Hello World"
    assert (
        StringUtils.remove_extra_spaces("   Leading and trailing   ")
        == "Leading and trailing"
    )


def test_title_case():
    assert StringUtils.title_case("hello world") == "Hello World"
    assert StringUtils.title_case("python programming") == "Python Programming"


def test_capitalize_words():
    assert StringUtils.capitalize_words("hello world") == "Hello World"
    assert StringUtils.capitalize_words("python programming") == "Python Programming"


def test_snake_case():
    assert StringUtils.snake_case("HelloWorld") == "hello_world"
    assert StringUtils.snake_case("AIFramework") == "a_i_framework"
    assert StringUtils.snake_case("TestStringUtils") == "test_string_utils"


def test_camel_case():
    assert StringUtils.camel_case("hello_world") == "helloWorld"
    assert StringUtils.camel_case("ai_framework") == "aiFramework"
    assert StringUtils.camel_case("test_string_utils") == "testStringUtils"


def test_slugify():
    assert StringUtils.slugify("Hello World") == "hello-world"
    assert StringUtils.slugify("AI Engineering Framework") == "ai-engineering-framework"
    assert StringUtils.slugify("Python@3.14!") == "python-3-14"
    assert StringUtils.slugify("Hello___World") == "hello-world"
