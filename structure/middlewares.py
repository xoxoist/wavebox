from abc import ABC, abstractmethod
from flask import Blueprint, Response, Request, jsonify
import werkzeug.exceptions


class Middlewares(ABC):
    def __init__(self, req: Request | None):
        self.request = req

    def set_blueprint(self, blueprint: Blueprint):
        blueprint.before_request(self.before)
        blueprint.after_request(self.after)

    @abstractmethod
    def before(self): raise NotImplemented

    @abstractmethod
    def after(self, response: Response) -> Response: raise NotImplemented
