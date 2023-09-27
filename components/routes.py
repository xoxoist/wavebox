# library imports
import typing

from flask import (Blueprint, request)
from components import Middlewares

class Routes(Blueprint):
    incoming_blueprint: Blueprint | None = None

    def __init__(self, name: str, import_name: str, url_prefix: str = "", blueprint: Blueprint | None = None):
        super().__init__(name, import_name, url_prefix=url_prefix)
        if blueprint is not None:
            print("memek", blueprint.url_prefix + url_prefix)
            self.incoming_blueprint = blueprint
            self.url_prefix = blueprint.url_prefix + url_prefix
            self.register_blueprint(blueprint)
        else:
            self.url_prefix = url_prefix

    def use(self, middlewares: typing.Type[Middlewares]):
        if self.incoming_blueprint is None:
            raise Exception("No Blueprint provide")
        else:
            print("kuda terbang", self.incoming_blueprint.url_prefix)
            mw = middlewares(self.incoming_blueprint.url_prefix, request)
            # mw.set_blueprint(self.incoming_blueprint)
            # self.incoming_blueprint.url_prefix += "/v1/foo"
            self.before_request(mw.before)
            self.after_request(mw.after)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
