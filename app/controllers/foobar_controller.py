from flask import Blueprint
from app.requests import RequestCreateBar, RequestCreateFoo
from app.responses import ResponseBase
from app.services.foobar_service import ServiceBar, ServiceFoo
from structure import controllers
from structure.middlewares import Middlewares


"""
The purpose of this class is to be used as Controller file for your flask application,
you need to create a class that needed to be derived from controllers.Controllers and services.Services abstract class.
"""

class ControllerFoo(controllers.Controllers, ServiceFoo):
    def __init__(self, blueprint: Blueprint, path: str, endpoint: str, middleware: Middlewares=None):
        super().__init__(blueprint, path, endpoint, middleware)

    """
    def controller() is a abstract method from Controllers abstract class that can be used for your middleware and http api responses wrapper
    """
    def controller(self):
        super().before(RequestCreateFoo)

        response_model, response_http_code = self.retrieve()
        super().apply(response_model, response_http_code)

        super().after(ResponseBase)
        return super().done()


class ControllerBar(controllers.Controllers, ServiceBar):
    def __init__(self, blueprint: Blueprint, path: str, endpoint: str, middleware: Middlewares=None):
        super().__init__(blueprint, path, endpoint, middleware)

    def controller(self):
        super().prepare_context()
        super().before(RequestCreateBar)

        response_model, response_http_code = self.retrieve()
        super().apply(response_model, response_http_code)

        super().after(ResponseBase)
        return super().done()