from constants.database_constants import (
    DatabaseEngine,
    DatabaseStatus,
    SortOrder,
    Transaction,
)


def test_database_engine():
    assert DatabaseEngine.SQLITE == "sqlite"
    assert DatabaseEngine.POSTGRESQL == "postgresql"
    assert DatabaseEngine.MYSQL == "mysql"
    assert DatabaseEngine.MSSQL == "mssql"
    assert DatabaseEngine.ORACLE == "oracle"


def test_transaction():
    assert Transaction.COMMIT == "COMMIT"
    assert Transaction.ROLLBACK == "ROLLBACK"


def test_sort_order():
    assert SortOrder.ASC == "ASC"
    assert SortOrder.DESC == "DESC"


def test_database_status():
    assert DatabaseStatus.CONNECTED == "CONNECTED"
    assert DatabaseStatus.DISCONNECTED == "DISCONNECTED"
