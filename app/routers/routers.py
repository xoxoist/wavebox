from structure import groups
from flask import request
from app.controllers.foobar_controller import ControllerBar, ControllerFoo
from app.middlewares.foobar_middleware import FooMiddleware
from structure import routes
from structure.application import ApplicationService


class Routers(routes.Routes):
    def __init__(self, application_service: ApplicationService):
        super().__init__()
        self.application_service = application_service
    
    def create_routes(self):
        root = "/foobar/api/v1"

        
        self.application_service.add_controller(
            ControllerFoo(groups.Groups(__name__, "test_blueprint", root),
                          path="/foo", endpoint="foo_endpoint", middleware=FooMiddleware(request)))
        self.application_service.add_controller(
            ControllerBar(groups.Groups(__name__, "test_blueprint", root),
                          path="/bar", endpoint="bar_endpoint"))

    def apply(self) -> ApplicationService:
        self.create_routes()
        return self.application_service