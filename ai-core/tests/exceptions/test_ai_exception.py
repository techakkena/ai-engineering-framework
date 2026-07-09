from exceptions.ai_exception import AIException
from exceptions.error_codes import ErrorCode


def test_ai_exception():
    message = "AI model failed to generate a response."
    details = {"model": "gpt-3.5", "input": "Hello, AI!"}

    exception = AIException(message=message, details=details)

    assert exception.message == message
    assert exception.error_code == ErrorCode.AI_ERROR.value
    assert exception.status_code == 500
    assert exception.module == "AI"
    assert exception.details == details