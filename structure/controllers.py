from abc import ABC, abstractmethod
from flask import Blueprint
from flask.wrappers import Request


class Controllers(ABC):
    """
    "Controllers" this represents basic functions for handling middleware
    process before continued to "Services" class, generally other controller
    that inherits this class will have function header validation, request
    validation, middleware, next to service.
    """

    def __init__(self, req: Request, blueprint: Blueprint, path: str):
        self.blueprint = blueprint
        self.req = req
        self.path = path

    def header_validation(self):
        print(dict(self.req.headers))

    def request_validation(self):
        print(dict(self.req.get_json()))

    def middleware_before(self):
        print("Middleware before", self.req.headers.get("Request-Id"))

    def middleware_after(self):
        print("Middleware after", self.req.headers.get("Request-Id"))

    @abstractmethod
    def service(self): raise NotImplemented

    @abstractmethod
    def controller(self): raise NotImplemented
