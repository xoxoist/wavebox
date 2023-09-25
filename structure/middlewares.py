from abc import ABC, abstractmethod
from flask import Blueprint, Request


class Middlewares(ABC):

    def __init__(self, req: Request):
        self.req = req

    def _set_blueprint(self, blueprint: Blueprint):
        blueprint.before_request(self.before)
        blueprint.after_request(self.after)

    @abstractmethod
    def before(self): raise NotImplemented

    @abstractmethod
    def after(self): raise NotImplemented

    