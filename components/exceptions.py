# library imports
from enum import Enum
from werkzeug.exceptions import HTTPException


class Tagging(Enum):
    pass


# Exception layer tags
class ExceptionLayerTag(Tagging):
    CONTROLLER = 1
    MIDDLEWARE = 2
    SERVICE = 3


# Exception controller tags
class ExceptionControllerTag(Tagging):
    BEFORE = 1
    APPLY = 2
    AFTER = 3


# Exception service tags
class ExceptionServiceTag(Tagging):
    VALIDATE = 1
    LOGICS = 2
    RETRIEVE = 3


# Exception middleware tags
class ExceptionMiddlewareTag(Tagging):
    BEFORE = 1
    AFTER = 2


# Base exception class
class FundamentalException(HTTPException):
    def __init__(self, message: str, exception_tag: ExceptionLayerTag, error_code: str = "APP000"):
        super().__init__(message)
        self.exception_tag = exception_tag
        self.error_code = error_code
        self.code = 500


# Controllers exceptions
class ControllersException(FundamentalException):
    """Exception for controller layer."""

    def __init__(self, message: str, http_code=500, error_code: str = "APP000"):
        super().__init__(message, ExceptionLayerTag.CONTROLLER)
        self.error_code = error_code
        self.code = http_code


class ControllerLevelBeforeException(ControllersException):
    """Exception for controller layer, before execution."""

    def __init__(self, message: str, http_code=500, error_code: str = "APP000"):
        super().__init__(message, http_code)
        self.exception_tag = ExceptionControllerTag.BEFORE
        self.error_code = error_code
        self.code = http_code


class ControllerLevelAfterException(ControllersException):
    """Exception for controller layer, after execution."""

    def __init__(self, message: str, http_code=500, error_code: str = "APP000"):
        super().__init__(message, http_code)
        self.exception_tag = ExceptionControllerTag.AFTER
        self.error_code = error_code
        self.code = http_code


# Services exceptions
class ServicesException(FundamentalException):
    """Exception for service layer."""

    def __init__(self, message: str, http_code=500, error_code: str = "APP000"):
        super().__init__(message, ExceptionLayerTag.SERVICE)
        self.error_code = error_code
        self.code = http_code


class ServicesLevelValidateException(ServicesException):
    """Exception for service layer, validation."""

    def __init__(self, message: str, http_code=500, error_code: str = "APP000"):
        super().__init__(message, http_code)
        self.exception_tag = ExceptionServiceTag.VALIDATE
        self.error_code = error_code
        self.code = http_code


class ServicesLevelLogicsException(ServicesException):
    """Exception for service layer, business logic."""

    def __init__(self, message: str, http_code=500, error_code: str = "APP000"):
        super().__init__(message, http_code)
        self.exception_tag = ExceptionServiceTag.LOGICS
        self.error_code = error_code
        self.code = http_code


class ServicesLevelRetrieveException(ServicesException):
    """Exception for service layer, data retrieval."""

    def __init__(self, message: str, http_code=500, error_code: str = "APP000"):
        super().__init__(message, http_code)
        self.exception_tag = ExceptionServiceTag.RETRIEVE
        self.error_code = error_code
        self.code = http_code


# Middlewares exceptions
class MiddlewaresException(FundamentalException):
    """Exception for middleware layer."""

    def __init__(self, message: str, http_code=500, error_code: str = "APP000"):
        super().__init__(message, ExceptionLayerTag.MIDDLEWARE)
        self.error_code = error_code
        self.code = http_code


class MiddlewaresLevelBeforeException(MiddlewaresException):
    """Exception for middleware layer, before execution."""

    def __init__(self, message: str, http_code=500, error_code: str = "APP000"):
        super().__init__(message, http_code)
        self.exception_tag = ExceptionMiddlewareTag.BEFORE
        self.error_code = error_code
        self.code = http_code


class MiddlewaresLevelAfterException(MiddlewaresException):
    """Exception for middleware layer, after execution."""

    def __init__(self, message: str, http_code=500, error_code: str = "APP000"):
        super().__init__(message, http_code)
        self.exception_tag = ExceptionMiddlewareTag.AFTER
        self.error_code = error_code
        self.code = http_code
