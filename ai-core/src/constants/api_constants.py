"""
AI Engineering Framework
API Constants

Author : TECHAKKENA
"""


class API:
    """
    API configuration constants.
    """

    DEFAULT_HOST = "127.0.0.1"
    DEFAULT_PORT = 8000
    API_VERSION = "v1"
    API_PREFIX = "/api/v1"


class HTTPMethod:
    """
    Supported HTTP methods.
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"


class Header:
    """
    Standard HTTP headers.
    """

    AUTHORIZATION = "Authorization"
    CONTENT_TYPE = "Content-Type"
    ACCEPT = "Accept"
    USER_AGENT = "User-Agent"


class MimeType:
    """
    Common MIME types.
    """

    JSON = "application/json"
    XML = "application/xml"
    PDF = "application/pdf"
    CSV = "text/csv"
    TEXT = "text/plain"
    HTML = "text/html"


class ResponseMessage:
    """
    Common API response messages.
    """

    SUCCESS = "Success"
    CREATED = "Resource created successfully."
    UPDATED = "Resource updated successfully."
    DELETED = "Resource deleted successfully."
    BAD_REQUEST = "Bad request."
    UNAUTHORIZED = "Unauthorized."
    FORBIDDEN = "Forbidden."
    NOT_FOUND = "Resource not found."
    INTERNAL_SERVER_ERROR = "Internal server error."