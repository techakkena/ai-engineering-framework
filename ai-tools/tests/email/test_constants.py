from ai_tools.email.constants import (
    DEFAULT_EMAIL_SUBJECT,
)


def test_default_subject() -> None:
    assert DEFAULT_EMAIL_SUBJECT == "No Subject"
