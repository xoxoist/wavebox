import werkzeug.exceptions
from flask import Flask, jsonify

import troubles.exceptions
from structure import controllers
from structure import routes_manager


class ApplicationService:
    """
    "ApplicationService" this represents first entry of the service
    in this class where the merging, initialization, and configs
    are provided and will be distributed between other abstraction.
    """
    __registered_controllers = []

    def add_controller(self, controller: controllers.Controllers):
        self.__registered_controllers.append(controller)

    def list_endpoints(self, app):
        output = []
        for rule in app.url_map.iter_rules():
            # Skip some default routes like /static, /favicon.ico, etc.
            if 'GET' in rule.methods and not any(
                    rule.rule.startswith(ignore) for ignore in ['/static', '/favicon.ico']):
                output.append(f"{rule.rule} | {rule.methods}: {rule.endpoint}")
        return output

    def create_app(self):
        app = Flask(__name__)

        @app.errorhandler(werkzeug.exceptions.HTTPException)
        def handle_http_exception(e):
            response = jsonify({'error': str(e)})
            response.status_code = e.code
            return response

        app.config["ERROR_404_HELP"] = False

        route_extension = routes_manager.RoutesManager(routes=self.__registered_controllers)
        route_extension.register_route(app)

        endpoints = self.list_endpoints(app)
        for endpoint in endpoints:
            print(endpoint)

        return app
