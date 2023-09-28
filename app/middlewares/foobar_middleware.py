from flask import Request, Response
from components.middlewares import Middlewares
from components.exceptions import MiddlewaresLevelBeforeException


class AuthMiddleware(Middlewares):
    def __init__(self, path: str, req: Request | None):
        super().__init__(path, req)
        self.path = path
        self.request = req

    def before(self):
        print("AUTH MIDDLEWARE BEFORE", self.request.headers)
        # raise MiddlewaresLevelBeforeException("middleware fault foo", 401)

    def after(self, response: Response) -> Response:
        print("AUTH MIDDLEWARE AFTER", response)
        return response


class FooMiddleware(Middlewares):
    def __init__(self, path: str, req: Request | None):
        super().__init__(path, req)
        self.path = path
        self.request = req

    def before(self):
        print("FOO MIDDLEWARE BEFORE", self.request.headers)
        # raise MiddlewaresLevelBeforeException("middleware fault foo", 401)

    def after(self, response: Response) -> Response:
        print("FOO MIDDLEWARE AFTER", response)
        return response


class BarMiddleware(Middlewares):
    def __init__(self, path: str, req: Request | None):
        super().__init__(path, req)
        self.path = path
        self.request = req

    def before(self):
        print("BAR MIDDLEWARE BEFORE", self.request.headers)
        # raise MiddlewaresLevelBeforeException("middleware fault bar", 401)

    def after(self, response: Response) -> Response:
        print("BAR MIDDLEWARE AFTER", response)
        return response
