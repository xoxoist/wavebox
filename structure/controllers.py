from abc import ABC, abstractmethod
from flask import Blueprint, request, make_response, jsonify
from pydantic import BaseModel
from typing import Type


class Controllers(ABC):
    """
    "Controllers" this represents basic functions for handling middleware
    process before continued to "Services" class, generally other controller
    that inherits this class will have function header validation, request
    validation, middleware, next to service.
    """

    def __init__(self, blueprint: Blueprint, path: str):
        self.blueprint = blueprint
        self.res = None
        self.req = request
        self.path = path
        self.__response_model: BaseModel | None = None
        self.__response_http_code = 0
        self.__response_json = None

    def header_validation(self):
        print(dict(self.req.headers))

    def request_validation(self):
        print(dict(self.req.get_json()))

    def middleware_before(self):
        print("Middleware before", self.req.headers.get("Request-Id"))

    def middleware_after(self):
        print("Middleware after", self.req.headers.get("Request-Id"))

    def bind_request_to_dataclass(self, request_type: Type[BaseModel]) -> BaseModel:
        return request_type(**self.req.get_json())

    def make_response(self):
        self.res = make_response(self.__response_model.model_dump_json(), self.__response_http_code)
        self.res.headers['Content-Type'] = 'application/json'

    def bind_response_to_dataclass(self, response_type: Type[BaseModel]):
        self.__response_json = response_type(**self.res.get_json())

    def before(self, request_type: Type[BaseModel]):
        self.bind_request_to_dataclass(request_type)
        self.header_validation()
        self.request_validation()
        self.middleware_before()

    def apply(self, response_model: BaseModel, response_http_code: int):
        self.__response_model = response_model
        self.__response_http_code = response_http_code

    def after(self, response_type: Type[BaseModel]):
        self.middleware_after()
        self.make_response()
        self.bind_response_to_dataclass(response_type)

    def done(self):
        return jsonify(dict(self.__response_json))

    @abstractmethod
    def controller(self):
        raise NotImplemented
