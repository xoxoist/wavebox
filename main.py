import inspect

from components.exceptions import FundamentalException
from app.routers.routers import RoutesFoo, RoutesBar
from flask import Flask, Response, jsonify
from definitions import Applications
from app.responses import ResponseBase
from werkzeug.exceptions import NotFound


class MyApplication(Applications):

    def __init__(self, flask_app: Flask):
        super().__init__(flask_app)
        self.routes_setup()

    def routes_setup(self):
        RoutesFoo(self).apply()
        RoutesBar(self).apply()

    def provide_config(self):
        pass

    def global_handle_http_exception(self, ex: FundamentalException) -> Response:
        response = ResponseBase()
        if isinstance(ex, NotFound):
            response.response_code = "NFD404"
        else:
            response.response_code = ex.error_code
        response.response_message = str(ex)
        response_data = jsonify(dict(response))
        response_data.status_code = ex.code
        return response_data


def this_is_decorator(params):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if params in kwargs:
                for key, value in kwargs.items():
                    print(key, value)
                return func(*args, **kwargs)

            else:
                raise ValueError(f"Function {func.__name__} must have a '{params}' parameter.")

        return wrapper

    return decorator


def kwargs_decorator(func):
    def wrapper(*args, **kwargs):
        signature = inspect.signature(func)
        arguments = signature.bind(*args, **kwargs)
        arguments.apply_defaults()
        result = func(*args, **kwargs)
        if result is None:
            arg_str = ' '.join([f"{param}={value}" for param, value in arguments.arguments.items()])
            print(f"{func.__name__} {arg_str}")
        else:
            arg_str = ' '.join([f"{param}={value}" for param, value in arguments.arguments.items()])
            print(f"{func.__name__} {arg_str} result={result}")
        return result

    return wrapper


@this_is_decorator("x")
def test(x, y):
    print("HELLO")


@kwargs_decorator
def any_kwargs_attach_to_this_func(t: str, m: str):
    print(t, m)
    return "eek"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    any_kwargs_attach_to_this_func(t="hello", m="world")
    # test(124, x=1, y=2)
    # MyApplication(Flask(__name__)).start()
