from components.controllers import Controllers


class RoutesManager:

    def __init__(self, routes: []):
        self.routes = routes

    def register_route(self, app):
        for route in self.routes:
            if isinstance(route, Controllers):
                app.register_blueprint(route.blueprint)

    def get_all_routes(self):
        return self.routes
