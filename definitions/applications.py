from abc import ABC, abstractmethod
from flask import Flask, Response
from werkzeug.exceptions import HTTPException
from components.exceptions import FundamentalException
from components import Controllers
from structure import routes_manager


class Applications(ABC):
    """
    'Applications' this represents first entry of the service
    in this class where the merging, initialization, and configs
    are provided and will be distributed between other abstraction.
    """

    # private variables
    __registered_controllers = []
    __config = {
        'port': 5000,
        'debug': 0,
    }

    def __init__(self, flask_app: Flask):
        self.flask_app = flask_app

    @abstractmethod
    def global_handle_http_exception(self, ex: FundamentalException) -> Response:
        """
        'global_handle_http_exception' helps you to define base response for all API
        """
        raise NotImplemented

    @abstractmethod
    def provide_config(self):
        """
        'provide_config' helps you provide configuration using abstract class of Environments
        """
        raise NotImplemented

    def add_controller(self, controller: Controllers):
        self.__registered_controllers.append(controller)

    def log_endpoint(self):
        """
        'log_endpoint' helps you to see registered endpoints to your app
        """
        app = self.flask_app
        blacklist = ['/static', '/favicon.ico']
        for rule in app.url_map.iter_rules():
            if 'GET' in rule.methods and not any(rule.rule.startswith(ignore) for ignore in blacklist):
                print(f"{rule.rule} | {rule.methods}: {rule.endpoint}")

    def start(self):
        """
        'start' start your application service with Flask
        """

        route_extension = routes_manager.RoutesManager(routes=self.__registered_controllers)
        route_extension.register_route(self.flask_app)

        @self.flask_app.errorhandler(HTTPException)
        def handle_http_exception(ex: FundamentalException):
            return self.global_handle_http_exception(ex)

        self.log_endpoint()
        self.flask_app.run(port=5000)
