from abc import ABC, abstractmethod
from flask import Blueprint, Request, Response
from flask import request, make_response, jsonify
from pydantic import BaseModel, ValidationError
from typing import Type, Any

# structural imports
from components.exceptions import ControllerLevelAfterException
from components.exceptions import ControllerLevelBeforeException
from components.exceptions import ControllersException
from components.exceptions import FundamentalException
from components.middlewares import Middlewares


class Controllers(ABC):
    """
    "Controllers" this represents basic functions for handling middleware
    process before continued to "Services" class, generally other controller
    that inherits this class will have function header validation, request
    validation, middleware, next to service.
    """

    def __init__(self, blueprint: Blueprint, path: str, endpoint: str, mw: Type[Middlewares]):
        self.blueprint: Blueprint = blueprint
        self.blueprint.add_url_rule(path, view_func=self.controller, endpoint=endpoint)
        self.res: Response | None = None
        self.req: Request = request
        self.path: str = path
        self.middleware: Middlewares = mw(self.req)
        self.__response_json: Any = None
        self.__response_model: BaseModel | None = None
        self.__response_http_code = 0
        self.__response_type: Type[BaseModel]
        if self.middleware is not None:
            self.middleware.request = self.req
            self.middleware.set_blueprint(self.blueprint)

    def __header_validation(self, header_type: Type[BaseModel]):
        """
        '__header_validation' validating incoming header from request and validate
        the content with pydantic BaseModel class.
        """
        try:
            header_values = dict(self.req.headers)
            return header_type(**header_values)
        except ValidationError as e:
            error_messages = []
            for error in e.errors():
                error_messages.append(f"Header {error['loc'][0]}: {error['msg']}")
            raise ControllerLevelBeforeException(str(",".join(error_messages)))

    def __bind_request_to_dataclass(self, request_type: Type[BaseModel]) -> BaseModel:
        """
        '__bind_request_to_dataclass' validating incoming request and validate
        the content with pydantic BaseModel class.
        """
        try:
            return request_type(**self.req.get_json())
        except ValidationError as e:
            error_messages = []
            for error in e.errors():
                error_messages.append(f"Response body {error['loc'][0]}: {error['msg']}")
            raise ControllerLevelBeforeException(str(",".join(error_messages)))

    def __bind_response_to_dataclass(self, response_type: Type[BaseModel]):
        """
        '__bind_response_to_dataclass' validating out coming response and validate
        the content with pydantic BaseModel class.
        """
        try:
            self.__response_type = response_type
            self.__response_json = response_type(**self.res.get_json())
        except ValidationError as e:
            error_messages = []
            for error in e.errors():
                error_messages.append(f"Response body {error['loc'][0]}: {error['msg']}")
            raise ControllerLevelAfterException(str(",".join(error_messages)))

    def __make_response(self):
        """
        '__make_response' making response to be passed through middleware and controller
        and construct retrieve json response from response model and http code too,
        attaching response for middleware, TODO need to be able adding default response headers
        """
        self.res = make_response(self.__response_model.model_dump_json(), self.__response_http_code)
        if self.middleware is not None:
            self.middleware.response = self.res
        self.res.headers['Content-Type'] = 'application/json'

    def before(self, request_type: Type[BaseModel], header_type: Type[BaseModel]):
        """
        'before' executing binding body and header from incoming request then catch
        the error of validation and will be raised ControllerLevelBeforeException,
        to tells the controller that its happen in before function execution.
        """
        try:
            self.__bind_request_to_dataclass(request_type)
            self.__header_validation(header_type)
        except ControllersException as e:
            raise ControllerLevelBeforeException(str(e))

    def apply(self, response_model: BaseModel, response_http_code: int):
        self.__response_model = response_model
        self.__response_http_code = response_http_code

    def after(self, response_type: Type[BaseModel]):
        """
        'after' executing making response and binding response body then will catch
        the error from making response and binding response body ControllerLevelAfterException,
        to tells the controller that its happen in after function execution.
        """
        try:
            self.__make_response()
            self.__bind_response_to_dataclass(response_type)
        except ControllersException as e:
            raise ControllerLevelAfterException(str(e))

    def done(self):
        """
        'done' returning json data when before apply and after already executed without throwing
        any exception, and it will construct jsonify to returning response to the controller.
        """
        return jsonify(dict(self.__response_json))

    def catcher(self, response_model: BaseModel, e: FundamentalException):
        """
        'catcher' returning jsonify when before apply and after encounter an exception from any other
        source like controller, middleware or business logic.
        """
        self.__response_json = dict(response_model)
        response_data = jsonify(dict(self.__response_json))
        response_data.status_code = e.code
        return response_data

    @abstractmethod
    def controller(self):
        """
        'controller' this represents your controller logic, but you need to call before apply and after to,
        make your process runs smoothly and returns with done when there is no raised exception caught, and
        use catcher to handle raised exception inside the except block.
        """
        raise NotImplemented
