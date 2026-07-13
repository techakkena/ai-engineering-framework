from ai_prompts.validation.constants import (
    MAX_TEMPLATE_LENGTH,
    MAX_VARIABLE_COUNT,
    MIN_TEMPLATE_LENGTH,
)


def test_min_template_length():
    assert MIN_TEMPLATE_LENGTH == 1


def test_max_template_length():
    assert MAX_TEMPLATE_LENGTH == 100_000


def test_max_variable_count():
    assert MAX_VARIABLE_COUNT == 100
