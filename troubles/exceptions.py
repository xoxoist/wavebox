from enum import Enum
from werkzeug.exceptions import HTTPException


class Tagging(Enum):
    pass


class ExceptionLayerTag(Tagging):
    CONTROLLER = 1
    MIDDLEWARE = 2
    SERVICE = 3


class ExceptionControllerTag(Tagging):
    BEFORE = 1
    APPLY = 2
    AFTER = 3


class ExceptionServiceTag(Tagging):
    VALIDATE = 1
    LOGICS = 2
    RETRIEVE = 3


class ExceptionMiddlewareTag(Tagging):
    BEFORE = 1
    AFTER = 2


class FundamentalException(HTTPException):
    def __init__(self, message: str, exception_tag: ExceptionLayerTag):
        super().__init__(message)
        self.exception_tag = exception_tag
        self.code = 500


class ControllersException(FundamentalException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, ExceptionLayerTag.CONTROLLER)
        self.code = error_code


class ControllerLevelBeforeException(ControllersException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionControllerTag.BEFORE
        self.code = error_code


class ControllerLevelAfterException(ControllersException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionControllerTag.AFTER
        self.code = error_code


class ServicesException(FundamentalException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, ExceptionLayerTag.SERVICE)
        self.code = error_code


class ServicesLevelValidateException(ServicesException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionServiceTag.VALIDATE
        self.code = error_code


class ServicesLevelLogicsException(ServicesException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionServiceTag.LOGICS
        self.code = error_code


class ServicesLevelRetrieveException(ServicesException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionServiceTag.RETRIEVE
        self.code = error_code


class MiddlewaresException(FundamentalException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, ExceptionLayerTag.MIDDLEWARE)
        self.code = error_code


class MiddlewaresLevelBeforeException(MiddlewaresException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionMiddlewareTag.BEFORE
        self.code = error_code


class MiddlewaresLevelAfterException(MiddlewaresException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionMiddlewareTag.AFTER
        self.code = error_code
