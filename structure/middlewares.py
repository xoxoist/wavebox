from abc import ABC, abstractmethod
from flask import Request


class Middlewares(ABC):

    def __init__(self, req: Request):
        self.req = req

    @abstractmethod
    def before(self): raise NotImplemented

    @abstractmethod
    def after(self): raise NotImplemented