from exceptions.database_exception import DatabaseException
from exceptions.error_codes import ErrorCode


def test_database_exception():
    message = "Database connection failed."
    details = {"host": "localhost", "port": 5432}

    exception = DatabaseException(message=message, details=details)

    assert exception.message == message
    assert exception.error_code == ErrorCode.DATABASE_ERROR.value
    assert exception.status_code == 500
    assert exception.module == "Database"
    assert exception.details == details
