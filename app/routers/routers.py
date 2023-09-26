from structure import groups
from app.controllers.foobar_controller import ControllerBar, ControllerFoo
from structure import routes
from definitions.applications import Applications


class RoutesBar(routes.Routes):

    def __init__(self, application_service: Applications):
        self.application_service = application_service

    def create_routes(self):
        root = "/foobar/api/v1"
        self.application_service.add_controller(
            ControllerBar(groups.Groups(__name__, "test_blueprint", root),
                          path="/bar", endpoint="bar_endpoint"))

    def apply(self) -> Applications:
        self.create_routes()
        return self.application_service


class RoutesFoo(routes.Routes):
    def __init__(self, application_service: Applications):
        self.application_service = application_service

    def create_routes(self):
        root = "/foobar/api/v1"
        self.application_service.add_controller(
            ControllerFoo(groups.Groups(__name__, "test_blueprint", root),
                          path="/foo", endpoint="foo_endpoint"))

    def apply(self) -> Applications:
        self.create_routes()
        return self.application_service
