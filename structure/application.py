from flask import Flask

from .extensions.routes_extension import RoutesExtension
from . import group, controllers

class ApplicationService:
    """
    "ApplicationService" this represents first entry of the service
    in this class where the merging, initialization, and configs
    are provided and will be distributed between other abstraction.
    """

    ctls = []

    def add_controller(self, controller: controllers.Controllers):
        self.ctls.append(controller)
        print(self.ctls)

    def create_app(self):
        routeExtension = RoutesExtension(routes=self.ctls)
        app = Flask(__name__)

        app.config["ERROR_404_HELP"] = False

        root = group.Group(__name__, "foo_or_bar_api", "/foobar/api/v1/")


        routeExtension.register_route(app)

        return app


        
