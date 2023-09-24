from abc import ABC, abstractmethod
from flask import Blueprint, Request, Response, request, make_response, jsonify
from pydantic import BaseModel, ValidationError
from typing import Type, Any
from troubles.exceptions import ControllerLevelAfterException, ControllerLevelBeforeException, ControllersException
from structure.middlewares import Middlewares


class Controllers(ABC):
    """
    "Controllers" this represents basic functions for handling middleware
    process before continued to "Services" class, generally other controller
    that inherits this class will have function header validation, request
    validation, middleware, next to service.
    """

    def __init__(self, blueprint: Blueprint, path: str, endpoint: str, middleware: Middlewares | None):
        self.blueprint: Blueprint = blueprint
        self.blueprint.add_url_rule(path, view_func=self.controller, endpoint=endpoint)
        self.res: Response
        self.req: Request = request
        self.path: str = path
        self.middleware: Middlewares = middleware
        self.__response_json: Any = None
        self.__response_model: BaseModel | None = None
        self.__response_http_code = 0
        self.__response_type: Type[BaseModel]
        if self.middleware is not None:
            self.middleware.request = self.req
            self.middleware.set_blueprint(self.blueprint)

    def __header_validation(self, header_type: Type[BaseModel]):
        try:
            header_values = dict(self.req.headers)
            return header_type(**header_values)
        except ValidationError as e:
            error_messages = []
            for error in e.errors():
                error_messages.append(f"Header {error['loc'][0]}: {error['msg']}")
            raise ControllerLevelBeforeException(str(",".join(error_messages)))

    def __bind_request_to_dataclass(self, request_type: Type[BaseModel]) -> BaseModel:
        try:
            return request_type(**self.req.get_json())
        except ValidationError as e:
            error_messages = []
            for error in e.errors():
                error_messages.append(f"Response body {error['loc'][0]}: {error['msg']}")
            raise ControllerLevelBeforeException(str(",".join(error_messages)))

    def __bind_response_to_dataclass(self, response_type: Type[BaseModel]):
        try:
            self.__response_type = response_type
            self.__response_json = self.__response_type(**self.res.get_json())
        except ValidationError as e:
            error_messages = []
            for error in e.errors():
                error_messages.append(f"Response body {error['loc'][0]}: {error['msg']}")
            raise ControllerLevelAfterException(str(",".join(error_messages)))

    def __make_response(self):
        self.res = make_response(self.__response_model.model_dump_json(), self.__response_http_code)
        # self.middleware.response = self.res
        # self.res.headers['Content-Type'] = 'application/json'

    def __middleware_before(self):
        if self.middleware is not None:
            self.middleware.before()

    def __middleware_after(self):
        if self.middleware is not None:
            self.middleware.after()

    def before(self, request_type: Type[BaseModel], header_type: Type[BaseModel]):
        try:
            self.__bind_request_to_dataclass(request_type)
            self.__header_validation(header_type)
            self.__middleware_before()
        except ControllersException as e:
            raise ControllerLevelBeforeException(str(e))

    def apply(self, response_model: BaseModel, response_http_code: int):
        self.__response_model = response_model
        self.__response_http_code = response_http_code

    def after(self, response_type: Type[BaseModel]):
        try:
            self.__make_response()
            self.__middleware_after()
            self.__bind_response_to_dataclass(response_type)
        except ControllersException as e:
            raise ControllerLevelAfterException(str(e))

    def done(self):
        return jsonify(dict(self.__response_json))

    def catcher(self, response_model: BaseModel):
        self.__response_json = dict(response_model)
        return jsonify(dict(self.__response_json))

    @abstractmethod
    def controller(self):
        raise NotImplemented
