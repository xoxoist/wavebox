from structure.controllers import Controllers


class Routes:

    def __init__(self, routes: []):
        self.routes = routes

    def register_route(self, app):
        for route in self.routes:
            if isinstance(route, Controllers):
                app.register_blueprint(route.blueprint)
