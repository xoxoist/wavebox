from flask import Request, Response
from structure.middlewares import Middlewares
from troubles.exceptions import MiddlewaresLevelBeforeException


class FooMiddleware(Middlewares):
    def __init__(self, req: Request | None):
        super(FooMiddleware, self).__init__(req)
        self.request = req

    def before(self):
        print("FOO MIDDLEWARE BEFORE", self.request.headers)
        # raise MiddlewaresLevelBeforeException("memeg", 503)
        # abort(401)

    def after(self, response: Response) -> Response:
        print("FOO MIDDLEWARE AFTER", response)
        # response.headers['Content-Type'] = 'application/json'
        # response.headers['Memeg'] = 'Memeg'
        # abort(401)
        return response


class BarMiddleware(Middlewares):
    def __init__(self, req: Request | None):
        super(BarMiddleware, self).__init__(req)
        self.request = req

    def before(self):
        print("BAR MIDDLEWARE BEFORE", self.request.headers)
        raise MiddlewaresLevelBeforeException("memeg", 503)
        # abort(401)

    def after(self, response: Response) -> Response:
        print("BAR MIDDLEWARE AFTER", response)
        # response.headers['Content-Type'] = 'application/json'
        # response.headers['Memeg'] = 'Memeg'
        # abort(401)
        return response
