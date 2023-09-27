from flask import Request, Response
from components.middlewares import Middlewares
from components.interceptors import Interceptors
from components.exceptions import MiddlewaresLevelBeforeException


class MWInterceptor(Interceptors):
    def __init__(self, path):
        super().__init__(path)
        self.path = path

    def show_path(self):
        print(self.path)


class FooMiddleware(Middlewares):
    def __init__(self, path: str, req: Request | None):
        super().__init__(path, req)
        self.path = path
        self.request = req
        self.interceptor = MWInterceptor(self.path)

    def before(self):
        self.interceptor.show_path()
        print("FOO MIDDLEWARE BEFORE", self.request.headers)
        # raise MiddlewaresLevelBeforeException("middleware fault foo", 401)

    def after(self, response: Response) -> Response:
        print("FOO MIDDLEWARE AFTER", response)
        return response


class BarMiddleware(Middlewares):
    def __init__(self, path: str, req: Request | None):
        super().__init__(path, req)
        self.interceptor = MWInterceptor(self.path)
        self.path = path
        self.request = req

    def before(self):
        self.interceptor.show_path()
        print("BAR MIDDLEWARE BEFORE", self.request.headers)
        # raise MiddlewaresLevelBeforeException("middleware fault bar", 401)

    def after(self, response: Response) -> Response:
        print("BAR MIDDLEWARE AFTER", response)
        return response
