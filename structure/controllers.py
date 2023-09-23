from abc import ABC, abstractmethod
from flask import Blueprint, request, make_response, jsonify, Request, Response
from pydantic import BaseModel
from typing import Type, Any
import http.client as http_c


class MiddlewaresException(Exception):
    pass


class ServicesException(Exception):
    pass


class ControllersException(Exception):
    def __init__(self, parent_exception: Exception, error_code=None):
        self.error_code = http_c.INTERNAL_SERVER_ERROR
        for s in parent_exception.args:
            print(s)
        # if isinstance(parent_exception.__class__., KeyError):
        #     self.error_code = http_c.BAD_REQUEST
        #
        # if isinstance(parent_exception.__class__, MiddlewaresException):
        #     self.error_code = http_c.BAD_REQUEST
        #
        # if isinstance(parent_exception.__class__, KeyError):
        #     self.error_code = http_c.BAD_REQUEST
        #
        # if isinstance(parent_exception.__class__, KeyError):
        #     self.error_code = http_c.BAD_REQUEST


class Controllers(ABC):
    """
    "Controllers" this represents basic functions for handling middleware
    process before continued to "Services" class, generally other controller
    that inherits this class will have function header validation, request
    validation, middleware, next to service.
    """

    def __init__(self, blueprint: Blueprint, path: str, endpoint: str):
        self.blueprint: Blueprint = blueprint
        self.blueprint.add_url_rule(path, view_func=self.controller, endpoint=endpoint)
        self.res: Response
        self.req: Request = request
        self.path: str = path
        self.__response_json: Any = None
        self.__response_model: BaseModel | None = None
        self.__response_http_code = 0
        self.__response_type: Type[BaseModel]

    def __header_validation(self, header_type: Type[BaseModel]):
        header_values = dict(self.req.headers)
        print(header_values["Request-Id"])
        return header_type(**header_values)

    def __request_validation(self):
        print(dict(self.req.get_json()))

    def __middleware_before(self):
        print("Middleware before", self.req.headers.get("Request-Id"))

    def __middleware_after(self):
        print("Middleware after", self.req.headers.get("Request-Id"))

    def __bind_request_to_dataclass(self, request_type: Type[BaseModel]) -> BaseModel:
        return request_type(**self.req.get_json())

    def __make_response(self):
        self.res = make_response(self.__response_model.model_dump_json(), self.__response_http_code)
        self.res.headers['Content-Type'] = 'application/json'

    def __bind_response_to_dataclass(self, response_type: Type[BaseModel]):
        self.__response_type = response_type
        self.__response_json = response_type(**self.res.get_json())

    def before(self, request_type: Type[BaseModel], header_type: Type[BaseModel]):
        try:
            self.__bind_request_to_dataclass(request_type)
            self.__header_validation(header_type)
            self.__request_validation()
            self.__middleware_before()
        except Exception as e:
            raise ControllersException(e)

    def apply(self, response_model: BaseModel, response_http_code: int):
        self.__response_model = response_model
        self.__response_http_code = response_http_code

    def after(self, response_type: Type[BaseModel]):
        try:
            self.__middleware_after()
            self.__make_response()
            self.__bind_response_to_dataclass(response_type)
        except Exception as e:
            raise ControllersException(e)

    def done(self):
        return jsonify(dict(self.__response_json))

    def catcher(self, e: KeyError):
        return jsonify(dict(self.__response_json))

    @abstractmethod
    def controller(self):
        raise NotImplemented
