from abc import ABC, abstractmethod
from flask import Flask, Blueprint, Response
from werkzeug.exceptions import HTTPException
from components.exceptions import FundamentalException
from typing import List
import time


class Applications(ABC):
    """
    'Applications' this represents first entry of the service
    in this class where the merging, initialization, and configs
    are provided and will be distributed between other abstraction.
    """

    # private variables
    __registered_blueprints: List[Blueprint] = []
    __config = {
        'port': 5000,
        'debug': 1,
    }

    def __init__(self, flask_app: Flask, blueprint: Blueprint):
        self.flask_app = flask_app
        self.blueprint = blueprint

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

    def register_blueprint(self, blueprint: Blueprint):
        self.__registered_blueprints.append(blueprint)

    def log_endpoint(self):
        """
        'log_endpoint' helps you to see registered endpoints to your app
        """
        app = self.flask_app
        ignores = ['/static', '/favicon.ico']
        for rule in app.url_map.iter_rules():
            if not any(rule.rule.startswith(ignore) for ignore in ignores):
                print(f"{rule.rule} | {rule.methods}: {rule.endpoint}")

    def start(self):
        """
        'start' start your application service with Flask
        """
        for blueprint in self.__registered_blueprints:
            self.blueprint.register_blueprint(blueprint)
        self.flask_app.register_blueprint(self.blueprint)

        for name, blueprint in self.flask_app.blueprints.items():
            print(f"{name} : {blueprint.url_prefix}")

        @self.flask_app.errorhandler(HTTPException)
        def handle_http_exception(ex: FundamentalException):
            return self.global_handle_http_exception(ex)

        self.log_endpoint()
        time.sleep(0.2)
        self.flask_app.run(port=5000)
