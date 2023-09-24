from abc import ABC, abstractmethod
from flask import Blueprint, Request, Response


class Middlewares(ABC):
    request: Request | None
    response: Response | None

    def __init__(self):
        self.request: Request | None
        self.response: Response | None

    def set_blueprint(self, blueprint: Blueprint):
        blueprint.before_request(self.before)
        blueprint.after_request(self.after)

    @abstractmethod
    def before(self): raise NotImplemented

    @abstractmethod
    def after(self): raise NotImplemented
