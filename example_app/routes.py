from flask import Blueprint
from wavebox.components.routes import Routes
from wavebox.definitions.applications import Applications
from controllers.foo_api import foo_api_service


class ApplicationRouting:
    def __init__(self, application: Applications) -> None:
        self.name = "example_app"
        self.application = application
        self.initialize_routes()

    def foo_api(self, api: Blueprint):
        with Routes('foo', self.name, path="foo", blueprint=api) as foo:
            foo_api_service.FooApiController(foo, endpoint="get-foo", methods=["GET"])
        
        self.application.register_blueprint(foo)


    def initialize_routes(self):
        with Routes('example_api', self.name, path="/api/example/") as api:
            self.foo_api(api)

        self.application.register_blueprint(api)