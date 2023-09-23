# from enum import Enum
#
#
# class Tagging(Enum): pass
#
#
# class ExceptionLayerTag(Tagging):
#     CONTROLLER = 1
#     MIDDLEWARE = 2
#     SERVICE = 3
#
#
# class ExceptionControllerTag(Tagging):
#     BEFORE = 1
#     APPLY = 2
#     AFTER = 3
#
#
# class ExceptionServiceTag(Tagging):
#     VALIDATE = 1
#     LOGICS = 2
#     RETRIEVE = 3
#
#
# class ExceptionMiddlewareTag(Tagging):
#     BEFORE = 1
#     AFTER = 2
#
#
# class FundamentalException(Exception):
#     def __init__(self, e: Exception, exception_tag: ExceptionLayerTag):
#         super().__init__(e)
#         self.exception_tag = exception_tag
#
#
# """
# asdasdasdjlkasdljksdfjlksadjlkdsfjlksdfjlksdfjlksdjlkdsfjlk
# """
#
#
# class ControllersException(FundamentalException):
#     def __init__(self, e: Exception, error_code=500):
#         super().__init__(e, ExceptionLayerTag.CONTROLLER)
#         self.error_code = error_code
#
#
# class ControllerLevelBeforeException(ControllersException):
#     def __init__(self, e: Exception, error_code=500):
#         super().__init__(e)
#         self.exception_tag = ExceptionControllerTag.BEFORE
#         self.error_code = error_code
#
#
# class ControllerLevelAfterException(ControllersException):
#     def __init__(self, e: Exception, error_code=500):
#         super().__init__(e)
#         self.exception_tag = ExceptionControllerTag.AFTER
#         self.error_code = error_code
#
#
# """
# asdasdasdjlkasdljksdfjlksadjlkdsfjlksdfjlksdfjlksdjlkdsfjlk
# """
#
#
# class ServicesException(FundamentalException):
#     def __init__(self, e: Exception, error_code=500):
#         super().__init__(e, ExceptionLayerTag.SERVICE)
#         self.error_code = error_code
#
#
# class ServicesLevelValidateException(ServicesException):
#     def __init__(self, e: Exception, error_code=500):
#         super().__init__(e)
#         self.exception_tag = ExceptionServiceTag.VALIDATE
#         self.error_code = error_code
#
#
# class ServicesLevelLogicsException(ServicesException):
#     def __init__(self, e: Exception, error_code=500):
#         super().__init__(e)
#         self.exception_tag = ExceptionServiceTag.LOGICS
#         self.error_code = error_code
#
#
# class ServicesLevelRetrieveException(ServicesException):
#     def __init__(self, e: Exception, error_code=500):
#         super().__init__(e)
#         self.exception_tag = ExceptionServiceTag.RETRIEVE
#         self.error_code = error_code
#
#
# """
# asdasdasdjlkasdljksdfjlksadjlkdsfjlksdfjlksdfjlksdjlkdsfjlk
# """
#
#
# class MiddlewaresException(FundamentalException):
#     def __init__(self, e: Exception, error_code=500):
#         super().__init__(e, ExceptionLayerTag.MIDDLEWARE)
#         self.error_code = error_code
#
#
# class MiddlewaresLevelBeforeException(MiddlewaresException):
#     def __init__(self, e: Exception, error_code=500):
#         super().__init__(e)
#         self.exception_tag = ExceptionMiddlewareTag.BEFORE
#         self.error_code = error_code
#
#
# class MiddlewaresLevelAfterException(MiddlewaresException):
#     def __init__(self, e: Exception, error_code=500):
#         super().__init__(e)
#         self.exception_tag = ExceptionMiddlewareTag.AFTER
#         self.error_code = error_code


from enum import Enum


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


class FundamentalException(Exception):
    def __init__(self, message: str, exception_tag: ExceptionLayerTag):
        super().__init__(message)
        self.exception_tag = exception_tag


class ControllersException(FundamentalException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, ExceptionLayerTag.CONTROLLER)
        self.error_code = error_code


class ControllerLevelBeforeException(ControllersException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionControllerTag.BEFORE


class ControllerLevelAfterException(ControllersException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionControllerTag.AFTER


class ServicesException(FundamentalException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, ExceptionLayerTag.SERVICE)
        self.error_code = error_code


class ServicesLevelValidateException(ServicesException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionServiceTag.VALIDATE


class ServicesLevelLogicsException(ServicesException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionServiceTag.LOGICS


class ServicesLevelRetrieveException(ServicesException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionServiceTag.RETRIEVE


class MiddlewaresException(FundamentalException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, ExceptionLayerTag.MIDDLEWARE)
        self.error_code = error_code


class MiddlewaresLevelBeforeException(MiddlewaresException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionMiddlewareTag.BEFORE


class MiddlewaresLevelAfterException(MiddlewaresException):
    def __init__(self, message: str, error_code=500):
        super().__init__(message, error_code)
        self.exception_tag = ExceptionMiddlewareTag.AFTER
