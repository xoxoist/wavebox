from flask import Blueprint
from app.requests import RequestCreateBar, RequestCreateFoo
from app.responses import ResponseBase
from app.services.foobar_service import ServiceBar, ServiceFoo
from components import controllers
from structure.tools.request_header import HeaderBase
from app.middlewares.foobar_middleware import FooMiddleware, BarMiddleware
from troubles.exceptions import FundamentalException

"""
The purpose of this class is to be used as Controller file for your flask application,
you need to create a class that needed to be derived from controllers.Controllers and services.Services abstract class.
"""


class ControllerFoo(controllers.Controllers, ServiceFoo):
    def __init__(self, blueprint: Blueprint, path: str, endpoint: str):
        super().__init__(blueprint, path, endpoint, FooMiddleware)

    def controller(self):
        try:
            super().before(RequestCreateFoo, HeaderBase)
            super().apply(*self.retrieve())
            super().after(ResponseBase)
            return super().done()
        except FundamentalException as e:
            err_response = ResponseBase()
            err_response.response_code = "99"
            err_response.response_message = str(e)
            print(e.exception_tag)
            return super().catcher(err_response, e)


class ControllerBar(controllers.Controllers, ServiceBar):
    def __init__(self, blueprint: Blueprint, path: str, endpoint: str):
        super().__init__(blueprint, path, endpoint, BarMiddleware)

    def controller(self):
        try:
            super().before(RequestCreateBar, HeaderBase)
            super().apply(*self.retrieve())
            super().after(ResponseBase)
            return super().done()
        except FundamentalException as e:
            err_response = ResponseBase()
            err_response.response_code = "99"
            err_response.response_message = str(e)
            print(e.exception_tag)
            return super().catcher(err_response, e)
