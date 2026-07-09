"""
AI Engineering Framework
Database Constants

Author : TECHAKKENA
"""


class DatabaseEngine:
    SQLITE = "sqlite"
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"
    MSSQL = "mssql"
    ORACLE = "oracle"


class Transaction:
    COMMIT = "COMMIT"
    ROLLBACK = "ROLLBACK"


class SortOrder:
    ASC = "ASC"
    DESC = "DESC"


class DatabaseStatus:
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED" 