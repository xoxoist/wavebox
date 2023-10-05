from .app.middlewares.foobar_middleware import FooMiddleware, MemekMiddleware, BarMiddleware
from .components.exceptions import FundamentalException
from flask import Flask, Response, Request, jsonify, Blueprint
from .definitions import Applications
from .app.models.responses import ResponseBase
from werkzeug.exceptions import NotFound
from .app.controllers.foobar_controller import ControllerBar, ControllerFoo
from .components import Routes


class MyApplication(Applications):
    name: str = __name__

    def __init__(self, flask_app: Flask):
        super().__init__(flask_app, Blueprint('root', self.name, url_prefix="/"))
        self.routes_setup()

    # def before(self):
    #     print("API MIDDLEWARE BEFORE")
    #
    # def after(self, response: Response) -> Response:
    #     print("API MIDDLEWARE AFTER")
    #     return response

    def routes_setup(self):
        with Routes("api", self.name, url_prefix="/api/foobar/v1") as api:
            with Routes("foo", self.name, url_prefix="/foo", blueprint=api) as foo:
                foo.use(MemekMiddleware)
                foo.use(FooMiddleware)
                ControllerFoo(foo, endpoint="foo v1", methods=["POST"])
                self.register_blueprint(foo)
            with Routes("bar", self.name, url_prefix="/bar", blueprint=api) as bar:
                bar.use(MemekMiddleware)
                bar.use(BarMiddleware)
                ControllerBar(bar, endpoint="bar v1", methods=["POST"])
                self.register_blueprint(bar)

                # self.register_blueprint(foobar)

        self.register_blueprint(api)

    def provide_config(self):
        pass

    def global_handle_http_exception(self, ex: FundamentalException) -> Response:
        # response_code = "NFD404" if isinstance(ex, NotFound) else ex.error_code
        response = ResponseBase()
        # response.response_code = response_code
        response.response_message = str(ex)
        response_data = jsonify(dict(response))
        response_data.status_code = ex.code
        return response_data


if __name__ == '__main__':
    MyApplication(Flask(__name__)).start()

# import inspect
# def this_is_decorator(params):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if params in kwargs:
#                 for key, value in kwargs.items():
#                     print(key, value)
#                 return func(*args, **kwargs)
#
#             else:
#                 raise ValueError(f"Function {func.__name__} must have a '{params}' parameter.")
#
#         return wrapper
#
#     return decorator
#
#
# def kwargs_decorator(func):
#     def wrapper(*args, **kwargs):
#         signature = inspect.signature(func)
#         arg_bind = signature.bind(*args, **kwargs)
#         arg_bind.apply_defaults()
#         result = func(*args, **kwargs)
#         if result is None:
#             arg_str = ' '.join([f"{param}={value}" for param, value in arg_bind.arguments.items()])
#             print(f"{func.__name__} {arg_str}")
#         else:
#             arg_str = ' '.join([f"{param}={value}" for param, value in arg_bind.arguments.items()])
#             print(f"{func.__name__} {arg_str} result={result}")
#         return result
#
#     return wrapper
#
#
# @this_is_decorator("x")
# def test(x, y):
#     print("HELLO")
#
#
# @kwargs_decorator
# def any_kwargs_attach_to_this_func(t: str, m: str):
#     print(t, m)

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     MyApplication(Flask(__name__)).start()
# any_kwargs_attach_to_this_func(t="hello", m="world")
# any_kwargs_attach_to_this_func("hello", "world")
# test(124, x=1, y=2)
