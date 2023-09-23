from abc import ABC, abstractmethod
from flask import Blueprint, request, make_response, jsonify, Request, Response
from pydantic import BaseModel
from typing import Type, Any
from structure.middlewares import Middlewares


class Controllers(ABC):
    """
    "Controllers" this represents basic functions for handling middleware
    process before continued to "Services" class, generally other controller
    that inherits this class will have function header validation, request
    validation, middleware, next to service.
    """

    def __init__(self, blueprint: Blueprint, path: str, endpoint: str, middleware: Middlewares | None):
        self.blueprint = blueprint
        self.blueprint.add_url_rule(path, view_func=self.controller, endpoint=endpoint)
        self.res: Response
        self.req: Request = request
        self.path: str = path
        self.middleware: Middlewares = middleware
        self.__response_json: Any = None
        self.__response_model: BaseModel | None = None
        self.__response_http_code = 0

    def __header_validation(self):
        print(dict(self.req.headers))

    def __request_validation(self):
        print(dict(self.req.get_json()))

    def __middleware_before(self):
        if self.middleware is not None:
            self.middleware.before()
        else:
            pass

    def __middleware_after(self):
        if self.middleware is not None:
            self.middleware.after()
        else:
            pass
        # print("Middleware after", self.req.headers.get("Request-Id"))

    def __bind_request_to_dataclass(self, request_type: Type[BaseModel]) -> BaseModel:
        return request_type(**self.req.get_json())

    def __make_response(self):
        self.res = make_response(self.__response_model.model_dump_json(), self.__response_http_code)
        self.res.headers['Content-Type'] = 'application/json'

    def __bind_response_to_dataclass(self, response_type: Type[BaseModel]):
        self.__response_json = response_type(**self.res.get_json())

    def prepare_context(self):
        self.req.test = "MEMEG"

    def before(self, request_type: Type[BaseModel]):
        # print(getattr(self.req, "test"))
        self.__bind_request_to_dataclass(request_type)
        self.__header_validation()
        self.__request_validation()
        self.__middleware_before()

    def apply(self, response_model: BaseModel, response_http_code: int):
        self.__response_model = response_model
        self.__response_http_code = response_http_code

    def after(self, response_type: Type[BaseModel]):
        self.__middleware_after()
        self.__make_response()
        self.__bind_response_to_dataclass(response_type)

    def done(self):
        return jsonify(dict(self.__response_json))

    @abstractmethod
    def controller(self): raise NotImplemented
